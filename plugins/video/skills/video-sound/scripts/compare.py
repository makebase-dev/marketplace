#!/usr/bin/env python3
"""One comparison clip: the same seconds of picture played once per sound option, with a big 1, 2, 3 on screen.

  python compare.py --picture draft.mp4 --from 34.6 --len 6 --mix build/opt1/mix_master.wav build/opt2/mix_master.wav --out compare/37s-name.mp4

Option 1 is always the recommended one. Build the options with mix.py --set, so all share the same master.
"""
import argparse
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw


def run(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def badge(n, path):
    """A big digit drawn as seven segments, so no font is needed (ffmpeg's drawtext fails without fontconfig on Windows)."""
    w, h, t = 150, 240, 26
    seg = {"a": (t, 0, w - t, t), "b": (w - t, t, w, h // 2), "c": (w - t, h // 2, w, h - t), "d": (t, h - t, w - t, h),
           "e": (0, h // 2, t, h - t), "f": (0, t, t, h // 2), "g": (t, h // 2 - t // 2, w - t, h // 2 + t // 2)}
    digits = {1: "bc", 2: "abged", 3: "abgcd", 4: "fgbc", 5: "afgcd", 6: "afgedc", 7: "abc", 8: "abcdefg", 9: "abcfgd"}
    img = Image.new("RGBA", (w + 80, h + 80), (0, 0, 0, 170))
    d = ImageDraw.Draw(img)
    for k in digits[n]:
        x0, y0, x1, y1 = seg[k]
        d.rectangle((x0 + 40, y0 + 40, x1 + 40, y1 + 40), fill=(255, 255, 255, 255))
    img.save(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--picture", required=True)
    ap.add_argument("--from", dest="start", type=float, required=True)
    ap.add_argument("--len", dest="length", type=float, default=6.0)
    ap.add_argument("--mix", nargs="+", required=True, help="one audio file per option")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        segs = []
        for i, mix in enumerate(a.mix, 1):
            seg = tmp / f"seg{i}.mp4"
            png = tmp / f"badge{i}.png"
            badge(i, png)
            run("-ss", str(a.start), "-t", str(a.length), "-i", a.picture, "-ss", str(a.start), "-t", str(a.length), "-i", mix, "-i", str(png),
                "-filter_complex", "[0:v][2:v]overlay=W/14:H/14[v]", "-map", "[v]", "-map", "1:a", "-af", "afade=t=in:d=0.02,areverse,afade=t=in:d=0.05,areverse",
                "-c:v", "libx264", "-crf", "20", "-preset", "fast", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", str(seg))
            segs.append(seg)
        lst = tmp / "list.txt"
        lst.write_text("".join(f"file '{s.as_posix()}'\n" for s in segs), encoding="utf8")
        run("-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", a.out)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
