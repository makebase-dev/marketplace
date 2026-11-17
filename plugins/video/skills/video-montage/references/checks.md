# Checks and delivery

## Freeze and stutter

```
python scripts/freeze_check.py draft.mp4 --mask 0.62 0.75
```

`--mask` blanks the caption band. Read the result like this:

| Line | Meaning |
|---|---|
| `STUTTER` | A repeated frame inside a moving shot: a defect. Usually a sequence played at the wrong rate or a shared join frame played twice |
| `still for 0.5 s` | Fine for an end card or an intended hold, otherwise a freeze. Eased pushes cause this |
| `jump or cut` | Must match a planned cut. Anything else is a defect |

Deliberate stepped motion looks like stutter to this check: a reveal or hand-drawn mark stepped at 15 a second gave a `STUTTER` line on nearly every step. A line-by-line reveal does not, but its holds show as `still` lines. Compare each line with the storyboard before calling it a defect.

## Look at it

Make a contact sheet and read it. A still from Remotion is faster than a render:

```
npx remotion still MyVideo check.jpg --frame=240 --scale=0.5
ffmpeg -ss 14 -t 20 -i draft.mp4 -vf "fps=0.6,scale=270:480,tile=6x2" -frames:v 1 sheet.jpg
```

After a picture change, render stills of just those frames, show them, then render the whole film.

## Corrupt frames

If a sequence of images was interrupted, the last one may be broken. Open every file with Pillow before rendering.

## Blind audits

An agent who knows your intent will agree with you. Give a fresh agent only the file, the script, the audience and the bar, with no history, and ask for ranked problems with timestamps, evidence and a concrete fix, then the best moments, then a score.

- Run picture and sound as separate audits; `video-sound` covers the sound one.
- Tell it to extract frames every 0.5 seconds and to view some at full size.
- Hand the owner the findings; let them choose. An audit's taste is not the owner's. In one round, applying every sound finding made the film worse.
- Mark which findings need long work, and show stills before starting it.

## Render and deliver

```
npm run draft
npm run mix
npm run share
```

The final audio always comes from the mix, never from Remotion. The picture is copied, so swapping sound needs no new render, as long as the timing stays the same.

Final check: 1080×1920, 30 fps, H.264 and AAC, −14 LUFS, true peak at or below −1.5 dBTP, duration as planned, credits on screen where a licence asks, and one watch on a real phone.
