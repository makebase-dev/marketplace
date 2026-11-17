#!/usr/bin/env python3
"""Mix and master a short from one JSON cue sheet (see ../templates/sound.json and ../references/mixing.md).

  python mix.py sound.json --out build/sound
  python mix.py sound.json --out build/opt2 --set hit_end=audio/sfx/other.wav
  python mix.py sound.json --out build/sound --picture picture.mp4 --video final.mp4

Writes stems, one WAV per placed cue, cues.json, mix_pre.wav and mix_master.wav into --out, then prints
loudness, each cue's landing time and how clear the voice stays. Paths in the sheet are relative to it.
Needs ffmpeg on PATH and: pip install numpy scipy soundfile
"""
import argparse
import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import butter, lfilter, resample_poly, sosfilt

SR = 48000
TARGET_LUFS = -14.0
PEAK_CEILING = -1.6  # dBTP; the delivery limit is -1.5, and this leaves a little room


def read_json(path):
    with open(path, encoding="utf8") as f:
        return json.load(f)


def ffmpeg(*args):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-y", *args], capture_output=True, text=True, encoding="utf8", errors="replace")
    if p.returncode:
        raise SystemExit(p.stderr[-1500:])
    return p.stderr


def load(path):
    """Any audio or video file as float32 stereo at 48 kHz."""
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-vn", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True)
    if p.returncode:
        raise SystemExit(f"cannot read {path}: {p.stderr.decode(errors='replace')[-300:]}")
    return np.frombuffer(p.stdout, np.float32).reshape(-1, 2).copy()


def measure(path):
    e = ffmpeg("-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-")
    s = e[e.rfind("Summary:"):]
    return {k: float(re.search(k + r":\s+(-?[\d.]+)", s)[1]) for k in ("I", "LRA", "Peak")}


def db_rms(y):
    if len(y) == 0:
        return -240.0
    return 20 * np.log10(np.sqrt(np.mean(np.square(y, dtype=np.float64))) + 1e-12)


def high(f, order=4):
    return butter(order, f, "high", fs=SR, output="sos")


def low(f, order=4):
    return butter(order, f, "low", fs=SR, output="sos")


def bell(f0, gain, q):
    a_ = 10 ** (gain / 40)
    w = 2 * np.pi * f0 / SR
    al = np.sin(w) / (2 * q)
    b = [1 + al * a_, -2 * np.cos(w), 1 - al * a_]
    a = [1 + al / a_, -2 * np.cos(w), 1 - al / a_]
    return np.array(b) / a[0], np.array(a) / a[0]


def low_shelf(f0, gain):
    a_ = 10 ** (gain / 40)
    w = 2 * np.pi * f0 / SR
    c = np.cos(w)
    r = 2 * np.sqrt(a_) * (np.sin(w) / 2 * np.sqrt(2))
    b = [a_ * ((a_ + 1) - (a_ - 1) * c + r), 2 * a_ * ((a_ - 1) - (a_ + 1) * c), a_ * ((a_ + 1) - (a_ - 1) * c - r)]
    a = [(a_ + 1) + (a_ - 1) * c + r, -2 * ((a_ - 1) + (a_ + 1) * c), (a_ + 1) + (a_ - 1) * c - r]
    return np.array(b) / a[0], np.array(a) / a[0]


def ramp(t, a, b):
    """0 before a, 1 after b, a raised cosine between."""
    x = np.clip((t - a) / max(b - a, 1e-6), 0, 1)
    return 0.5 - 0.5 * np.cos(np.pi * x)


def repitch(x, pitch):
    """Resample: pitch 0.8 is lower and slower, 1.2 higher and shorter."""
    if pitch == 1.0:
        return x
    fr = Fraction(1 / pitch).limit_denominator(50)
    return resample_poly(x, fr.numerator, fr.denominator, axis=0).astype(np.float32)


def fades(x, fade_in, fade_out):
    ni = min(len(x), max(int(fade_in * SR), int(0.002 * SR)))
    no = min(len(x), max(int(fade_out * SR), int(0.005 * SR)))
    x[:ni] *= (np.sin(np.linspace(0, np.pi / 2, ni)) ** 2)[:, None]
    x[-no:] *= (np.cos(np.linspace(0, np.pi / 2, no)) ** 2)[:, None]
    return x


def merge(spans, gap):
    out = []
    for a, b in spans:
        if out and a - out[-1][1] < gap:
            out[-1][1] = b
        else:
            out.append([a, b])
    return out


class Mix:
    def __init__(self, sheet_path, overrides, picture=None):
        self.root = Path(sheet_path).resolve().parent
        self.c = read_json(sheet_path)
        self.fps = self.c.get("fps", 30)
        if self.c.get("duration", "auto") == "auto":  # the length of the render
            if not picture:
                raise SystemExit('"duration" is "auto": pass --picture, or set it in seconds')
            self.c["duration"] = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", picture], capture_output=True, text=True).stdout)
        self.n = int(round(self.c["duration"] * SR))
        self.t = np.arange(self.n) / SR
        self.overrides = overrides
        v = self.c["voice"]
        parts = v.get("parts")
        if isinstance(parts, str):  # the same file timeline.ts reads
            parts = read_json(self.root / parts)
        self.parts = parts or [{"from": 0, "to": 1e9, "shift": 0}]
        self.offset = v.get("offset", 0.0)
        raw = read_json(self.root / v["words"])
        self.words = [(self.at(w["s"]), self.at(w["s"]) + w["e"] - w["s"]) for w in raw]
        if self.words and self.words[-1][1] > self.c["duration"]:
            raise SystemExit(f"the voice ends at {self.words[-1][1]:.2f} s but the film ends at {self.c['duration']:.2f} s: words would be cut off. Render again, or fix duration or the parts")
        self.voice_band = butter(4, [1000, 5000], "band", fs=SR, output="sos")

    def path(self, p):
        return self.root / p

    def at(self, s):
        """Video time of a narration time."""
        return s + self.offset + next((p["shift"] for p in self.parts if p["from"] <= s < p["to"]), self.parts[-1]["shift"])

    def duck(self, depth, lead=0.2, attack=0.35, hold=0.25, release=0.9, gap=0.6):
        d = np.zeros(self.n)
        for a, b in merge(self.words, gap):
            d = np.minimum(d, depth * (ramp(self.t, a - lead, a - lead + attack) - ramp(self.t, b + hold, b + hold + release)))
        return d

    def voice(self):
        v = self.c["voice"]
        src = load(self.path(v["file"])).mean(1)
        y = np.zeros(self.n, np.float32)
        for p in self.parts:
            seg = src[int(p["from"] * SR):int(min(p["to"], len(src) / SR) * SR)].copy()
            k = min(int(0.005 * SR), len(seg) // 2)
            seg[:k] *= np.linspace(0, 1, k)
            seg[-k:] *= np.linspace(1, 0, k)
            i = int((p["from"] + p["shift"] + self.offset) * SR)
            m = min(len(seg), self.n - i)
            y[i:i + m] += seg[:m]
        eq = v.get("eq", {"high_pass": 90, "shelf_180": -3.0, "presence_3500": 1.0})
        if eq.get("high_pass"):
            y = sosfilt(high(eq["high_pass"], 2), y)
        if eq.get("shelf_180"):
            y = lfilter(*low_shelf(180, eq["shelf_180"]), y)
        if eq.get("presence_3500"):
            y = lfilter(*bell(3500, eq["presence_3500"], 0.8), y)
        if v.get("first_phrase_db"):
            first = merge(self.words, 0.6)[0]
            y = y * 10 ** (v["first_phrase_db"] * (1 - ramp(self.t, first[1] + 0.05, first[1] + 0.5)) / 20)
        return np.stack([y, y], 1).astype(np.float32)

    def bed(self, b):
        src = self.overrides.get(b["id"], b["file"])
        x = load(self.path(src))[int(b.get("skip", 0) * SR):]
        x = repitch(x, b.get("pitch", 1.0))
        if len(x) < self.n:  # loop with a 2 s equal-power crossfade so no seam shows
            k = min(2 * SR, len(x) // 3)
            w = np.linspace(0, np.pi / 2, k)[:, None]
            loop = np.concatenate([x[k:-k], x[-k:] * np.cos(w) + x[:k] * np.sin(w)])
            x = np.concatenate([x[:k], np.tile(loop, (self.n // len(loop) + 2, 1))])
        x = x[:self.n].copy()
        x = sosfilt(high(b.get("hp", 120)), x, axis=0)
        x = sosfilt(low(b.get("lp", 10000)), x, axis=0)
        for f0, g, q in b.get("eq", [[3000, -4, 0.7]]):
            x = lfilter(*bell(f0, g, q), x, axis=0)
        x *= 10 ** ((b.get("level_db", -45) - db_rms(x)) / 20)
        fade = b.get("fade", 0.25)
        mask = np.zeros(self.n)
        for a, e in b.get("windows", [[0, self.c["duration"]]]):
            mask += ramp(self.t, a - fade, a + fade) - ramp(self.t, e - fade, e + fade)
        g = self.duck(b.get("duck_db", -8.0))
        for k in b.get("rise", []):  # [t0, t1, db0, db1]: level follows the picture, such as a camera speeding up
            g = g + k[2] + (k[3] - k[2]) * ramp(self.t, k[0], k[1])
        return x * (np.sqrt(np.clip(mask, 0, 1)) * 10 ** (g / 20))[:, None]

    def cue(self, c):
        x = load(self.path(self.overrides.get(c["id"], c["file"])))[int(c.get("skip", 0) * SR):]
        mid = x.mean(1)
        side = (x[:, 0] - x[:, 1]) / 2
        w = c.get("width", 0.4)
        x = repitch(np.stack([mid + w * side, mid - w * side], 1), c.get("pitch", 1.0))
        x = sosfilt(high(c.get("hp", 120)), x, axis=0)
        x = sosfilt(low(c.get("lp", 8000)), x, axis=0)
        if c.get("dip_db"):
            x = lfilter(*bell(2500, c["dip_db"], 0.6), x, axis=0)
        n = min(len(x), int(c.get("max_len", 3.0) * SR))
        h = max(1, int(c.get("peak_win", 0.005) * SR))
        step = SR // 200

        def env(y):
            m = y.mean(1).astype(np.float64)
            s = np.concatenate([[0], np.cumsum(m ** 2)])
            i = np.arange(0, len(m), step)
            lo = np.clip(i - h // 2, 0, len(m))
            hi = np.clip(i + h // 2 + 1, 0, len(m))
            return np.sqrt((s[hi] - s[lo]) / np.maximum(hi - lo, 1))

        align = c.get("align", "peak")
        if align == "end":
            e = env(x)
            end = min(len(x), (np.where(e > e.max() * 0.25)[0][-1] + 1) * step)
            x = x[max(0, end - n):end]
        elif align == "peak" and c.get("pre") is not None:
            p = int(np.argmax(env(x)) * step)
            s0 = max(0, p - int(c["pre"] * SR))
            x = x[s0:s0 + n]
        else:
            x = x[:n]
        x = fades(x.astype(np.float32).copy(), c.get("fade_in", 0.003), c.get("fade_out", 0.25))
        m = x.mean(1).astype(np.float64)
        k = min(int(0.4 * SR), len(m))
        s = np.concatenate([[0], np.cumsum(m ** 2)])
        x *= 10 ** ((c.get("level_db", -38) - 20 * np.log10(np.sqrt((s[k:] - s[:-k]) / k).max() + 1e-12)) / 20)
        if c.get("pan"):  # constant power, moving from pan[0] to pan[1] across the cue
            th = (np.linspace(c["pan"][0], c["pan"][1], len(x)) + 1) * np.pi / 4
            mono = x.mean(1)
            sd = (x[:, 0] - x[:, 1]) / 2
            x = np.stack([mono * np.cos(th) * np.sqrt(2) + sd, mono * np.sin(th) * np.sqrt(2) - sd], 1).astype(np.float32)
        peak = np.argmax(env(x)) * step / SR
        start = {"peak": c["at"] - peak, "end": c["at"] - len(x) / SR, "start": c["at"]}[align]
        start = max(0.0, start)
        return x, int(round(start * SR)), start + peak

    def clear(self, x, i, vb, c, target):
        """One fixed trim so the cue sits `target` dB under every word it overlaps, in the voice's 1-5 kHz."""
        xb = sosfilt(self.voice_band, x.mean(1))
        worst = None
        for a, e in self.words:
            s0, s1 = max(int(a * SR), i), min(int(e * SR), i + len(x))
            if s1 - s0 > SR // 50:
                d = db_rms(vb[int(a * SR):int(e * SR)]) - db_rms(xb[s0 - i:s1 - i])
                worst = d if worst is None else min(worst, d)
        if worst is None:
            return x, 0.0
        trim = float(np.clip(worst - target, -4.0 if c.get("featured") else -16.0, 0.0))
        return x * 10 ** (trim / 20), trim

    def build(self, out):
        (out / "cues").mkdir(parents=True, exist_ok=True)
        v = self.voice()
        sf.write(out / "stem_voice_raw.wav", v, SR, subtype="FLOAT")
        v = v * 10 ** ((self.c["voice"].get("target_lufs", -16) - measure(out / "stem_voice_raw.wav")["I"]) / 20)
        bed = np.zeros((self.n, 2), np.float32)
        for b in self.c.get("beds", []):
            bed += self.bed(b).astype(np.float32)
        g = np.zeros(self.n)
        for d in self.c.get("dips", []):  # the bed drops so a moment can land
            r = d.get("ramp", 0.3)
            g += d["db"] * (ramp(self.t, d["from"] - r, d["from"]) - ramp(self.t, d["to"], d["to"] + r))
        bed *= (10 ** (g / 20))[:, None].astype(np.float32)
        vb = sosfilt(self.voice_band, v.mean(1))
        target = self.c.get("clearance_db", 16.0)
        placed = []
        for c in self.c.get("cues", []):
            x, i, landed = self.cue(c)
            x = x[:self.n - i]
            x, trim = self.clear(x, i, vb, c, target)
            placed.append({"c": c, "x": x, "i": i, "landed": landed, "trim": trim})
        for a, e in self.words:  # cues stacked on one word: lower the plain ones together until their sum is at most 2 dB less clear than the target
            ia, ie = int(a * SR), int(e * SR)
            on = [p for p in placed if p["i"] < ie and p["i"] + len(p["x"]) > ia]
            if len(on) < 2:
                continue
            total = np.zeros(ie - ia)
            for p in on:
                s0, s1 = max(ia, p["i"]), min(ie, p["i"] + len(p["x"]))
                total[s0 - ia:s1 - ia] += p["x"][s0 - p["i"]:s1 - p["i"]].mean(1)
            short = (target - 2) - (db_rms(vb[ia:ie]) - db_rms(sosfilt(self.voice_band, total)))
            if short > 0:
                for p in on:
                    if not p["c"].get("featured"):
                        p["x"] = p["x"] * 10 ** (-short / 20)
                        p["trim"] -= short
        sfx = np.zeros((self.n, 2), np.float32)
        table = []
        for p in placed:
            c = p["c"]
            sfx[p["i"]:p["i"] + len(p["x"])] += p["x"]
            sf.write(out / "cues" / f"{c['id']}.wav", p["x"], SR, subtype="PCM_24")
            table.append({"id": c["id"], "file": self.overrides.get(c["id"], c["file"]), "event": c["at"], "landed": round(p["landed"], 3),
                          "frame": int(p["i"] / SR * self.fps), "voice_trim_db": round(p["trim"], 1), "note": c.get("note", "")})
        for name, y in (("stem_voice.wav", v), ("stem_bed.wav", bed), ("stem_sfx.wav", sfx), ("mix_pre.wav", v + bed + sfx)):
            sf.write(out / name, y, SR, subtype="FLOAT")
        with open(out / "cues.json", "w", encoding="utf8") as f:
            json.dump(table, f, ensure_ascii=False, indent=1)
        return table, v, bed + sfx

    def clearance(self, v, rest):
        vb = sosfilt(self.voice_band, v.mean(1))
        rb = sosfilt(self.voice_band, rest.mean(1))
        return sorted((round(min(60.0, float(db_rms(vb[int(a * SR):int(e * SR)]) - db_rms(rb[int(a * SR):int(e * SR)]))), 1), round(a, 2)) for a, e in self.words if e - a > 0.03)


def master(out):
    """Brickwall (lowered until the peak fits), then one linear gain to the target: no pumping, no loudnorm guesswork."""
    lim_db = -4.0
    gain = 0.0
    for _ in range(8):
        f = f"alimiter=limit={10 ** (lim_db / 20):.4f}:level=0:attack=5:release=80:asc=1"
        ffmpeg("-i", str(out / "mix_pre.wav"), "-af", f, "-c:a", "pcm_f32le", str(out / "mix_lim.wav"))
        m = measure(out / "mix_lim.wav")
        gain = TARGET_LUFS - m["I"]
        over = m["Peak"] + gain - PEAK_CEILING
        if over <= 0:
            break
        lim_db -= over + 0.05
    ffmpeg("-i", str(out / "mix_lim.wav"), "-af", f"volume={gain:.3f}dB", "-ar", str(SR), "-c:a", "pcm_s24le", str(out / "mix_master.wav"))
    return lim_db, gain


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sheet")
    ap.add_argument("--out", default="build/sound")
    ap.add_argument("--set", action="append", default=[], metavar="ID=FILE", help="swap the file of a cue or bed, to build a comparison option")
    ap.add_argument("--picture", help="a silent or draft render to put this mix on")
    ap.add_argument("--video", help="output video, with --picture")
    a = ap.parse_args()
    out = Path(a.out)
    m = Mix(a.sheet, dict(s.split("=", 1) for s in a.set), a.picture)
    table, v, rest = m.build(out)
    lim_db, gain = master(out)
    r = measure(out / "mix_master.wav")
    print(f"master {r['I']:.1f} LUFS, true peak {r['Peak']:.1f} dBTP, range {r['LRA']:.1f} LU (brickwall {lim_db:.2f} dBFS, gain {gain:+.2f} dB)")
    for row in table:
        print(f"  {row['id']:22} event {row['event']:6.2f}  landed {row['landed']:7.3f} ({1000 * (row['landed'] - row['event']):+5.0f} ms)  voice trim {row['voice_trim_db']:+.1f} dB")
    cl = m.clearance(v, rest)
    print(f"voice clearance in 1-5 kHz: median {np.median([c[0] for c in cl]):.1f} dB; worst words {cl[:3]}")
    if cl[0][0] < 12:
        print("WARNING: a word is under 12 dB clear; lower what sits on it")
    if r["Peak"] > -1.5 or abs(r["I"] - TARGET_LUFS) > 0.5:
        sys.exit("FAIL: outside -14 LUFS +-0.5 or above -1.5 dBTP")
    if a.picture and a.video:
        ffmpeg("-i", a.picture, "-i", str(out / "mix_master.wav"), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-shortest", a.video)
        print("wrote", a.video)


if __name__ == "__main__":
    main()
