# Mixing and mastering

Everything lives in `sound/sound.json`. `scripts/mix.py` turns it into stems, a master and optionally the final video. Paths are relative to the sheet.

```
python mix.py sound/sound.json --out build/sound
python mix.py sound/sound.json --out build/opt2 --set hit_end=sfx/other.wav
python mix.py sound/sound.json --out build/sound --picture out/draft.mp4 --video out/final.mp4
```

It exits with an error when the master misses −14 LUFS ±0.5 or goes above −1.5 dBTP, and when the film ends before the voice does, since words would be cut off. Read the printed table: `landed` shows each cue's loudest point against its event (it only needs to match for `peak` cues), and `voice trim` shows how far it was lowered for the words.

## The sheet

**Top level:** `fps`, `duration` (`"auto"` takes it from `--picture`), `clearance_db` (how far under a word a cue must sit, default 16).

**`voice`**

| Field | Meaning |
|---|---|
| `file`, `words` | The voice-over and its `words.json` |
| `parts` | A path to `src/parts.json`, or the list itself |
| `offset` | Seconds added to everything. Use about 0.025 if an MP3's encoder padding leaves the mix early against the draft |
| `first_phrase_db` | Lowers the opening phrase, usually −2.5 |
| `eq` | Default: `high_pass` 90, `shelf_180` −3, `presence_3500` +1. More presence makes the air around the voice feel noisier |
| `target_lufs` | Voice level before the master, default −16 |

**`beds[]`:** `id`, `file`, `skip` (start point in the file), `level_db` (RMS), `hp`, `lp`, `eq` (`[[freq, gain, q]]`), `windows` (`[[from, to]]`, the times it plays), `fade`, `duck_db` (under speech, default −8), `rise` (`[[t0, t1, db0, db1]]`, so level can follow the picture).

**`dips[]`:** `from`, `to`, `db`, `ramp`: the beds drop so a moment can land.

**`cues[]`**

| Field | Meaning |
|---|---|
| `id`, `file`, `note` | Name, source, and what it is for |
| `at` | Event time in seconds |
| `align` | `peak` (loudest point on `at`), `end` (for risers), `start` |
| `level_db` | Loudest 400 ms, in dBFS RMS. The voice sits near −19 |
| `hp`, `lp`, `dip_db` | High-pass, low-pass, a dip at 2.5 kHz to leave the voice room |
| `pitch` | 0.8 is lower, slower and heavier. Good for making one recording into several |
| `max_len`, `skip`, `pre` | Length, start point, seconds kept before the peak |
| `fade_in`, `fade_out` | Fades. Keep at least 3 ms in and 5 ms out to avoid clicks |
| `width`, `pan` | 0 to 1 stereo width, and `[from, to]` from −1 to 1 for moving with the picture |
| `peak_win` | Peak window; use 0.1 for soft whooshes so one crackle does not count as the peak |
| `featured` | May only be lowered 4 dB for the voice, others up to 16 |

## Starting levels

| Sound | `level_db` | Filters |
|---|---|---|
| Ambience | −45 to −40 | hp 120, lp 10000, −4 dB at 3 kHz |
| Wind over a map | −41 | hp 200, lp 9000 |
| Tick | −46 | hp 600, lp 7000 |
| Paper | −46 | hp 300, lp 7000, dip −6 |
| Air pass | −37 | hp 150, lp 8000, dip −6, width 0.8 |
| Stone or block | −38 | hp 120, lp 6000, dip −9 |
| Low thump | −31 | hp 60, lp 1500, pitch 0.6 |
| Riser | −27 | hp 120, lp 6000, align end |
| Soft impact | −26 | hp 120, lp 4000 |
| Held pad | −27 | hp 120, lp 1200 |
| Final boom | −27 | hp 50, lp 900 |

## How it protects the voice

1. Beds duck under speech with slow ramps (0.35 s attack, 0.9 s release), so they do not pump.
2. Any cue overlapping a word takes one fixed trim until it sits under the word in 1 to 5 kHz. Fixed, not moving, because moving gain sounded busy.
3. Cues stacked on one word drop together.
4. The script reports the median and worst clearance. Aim for 20 dB or more at the median and 12 dB as the floor.

Low filtering is the other way to keep a sound big under speech: below 1.5 kHz it does not compete with the words.

## Mastering

A brickwall limiter, lowered until the peak fits, then one linear gain to −14 LUFS. Never use `loudnorm` in single pass: it pumps. −14 LUFS and −1.5 dBTP is the safe delivery for all platforms, since YouTube turns loud videos down and nobody publishes the others' targets.

## Checks

- `landed` within a frame of the event, for `peak` cues.
- `earshot sfx check` on every source.
- Worst clearance words: go and look at what sits there.
- Compare against the last version the owner liked.
- A last listen on a phone speaker at low volume, by a person.

## Limits

- `mix.py` writes the mix. Remotion's own audio is for drafts only.
- If `--set` swaps a file, the option gets its own master, so options can differ slightly in limiting.
