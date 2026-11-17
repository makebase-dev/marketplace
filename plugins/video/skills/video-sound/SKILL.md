---
name: video-sound
description: "Design, source, mix and master the sound of a short narrated video: real licensed sound effects, ambience, risers and pads, earshot to measure what a sound is, a JSON cue sheet that mixes and masters to -14 LUFS with the voice kept clear, comparison clips, and how to agree the sound with the owner. Use when adding sound effects or ambience to a video, when a mix sounds noisy, cheap or thin, or when sourcing free sounds."
---

# Video sound

Lessons from four rounds of sound on a 60-second narrated short, including two rounds its owner rejected and one that got worse by following an audit too closely. Claude cannot hear: earshot and loudness meters show what a sound is and how loud, never whether it is good. The owner's ears decide.

## Read for the task

| Task | Read |
|---|---|
| Deciding what sounds go where, and timing | `references/design.md` |
| Finding sounds and checking licences | `references/sourcing.md` |
| Measuring sounds with earshot | `references/earshot.md` |
| The cue sheet, mixing, mastering | `references/mixing.md` |
| Showing the owner, taking notes, audits | `references/agreeing.md` |

## Tools

- `scripts/mix.py`: cue sheet to stems, master and optionally the final video. A project has it in `tools/` and runs it with `npm run mix`. `templates/sound.json` is a fuller example sheet.
- `scripts/compare.py`: one clip per decision, the same seconds played once per option, with 1, 2, 3 on screen.

## The flow

1. List the visible events from `timeline.ts`. Give each a role, or decide on silence.
2. Find real recordings for each role, and note the source and licence of every one.
3. Rank candidates with earshot and drop anything that fails `earshot sfx check`.
4. Pick the set yourself. Do not hand the owner a list to choose from.
5. Write `sound.json` and mix. Read the landing times and the voice clearance.
6. Send the video with the mix, and comparison clips for the key moments.
7. Take notes by timestamp, change only what was named, and mix again.
8. After approval, swap previews for full-quality originals, and rebuild at the same levels.

## Rules that held up every time

1. **Real recordings beat invented ones.** Generated and code-made effects were rejected on sight. Generate only long pads, where nothing real fits.
2. **Judge in context.** A list of 27 sounds played alone cannot be judged, by anyone. Put them in the video.
3. **Sound must belong to the picture.** Birds only over real outdoor views, never over maps, graphics or title cards. Air over camera moves. Paper when a photo appears.
4. **Less bed, not more.** A constant layer under everything reads as noise, however quiet. Fill a real hole with a discrete sound first.
5. **Discrete effects give richness; continuous layers give noise.** The best mix was the calm version plus individual hits.
6. **Peaks land on the cut.** The loudest point goes on the event, not the file's start.
7. **The voice wins.** Nothing sits on a word's 1 to 5 kHz. Below 12 dB of clearance on any word, something is wrong.
8. **No dings.** Pure tones and bells read as phone notifications. Use physical hits from the world of the film: stone, wood, paper.
9. **Phones lose the lows.** A low pad or boom needs a small transient at 1 to 3 kHz, or the moment is silent on a phone.
10. **A riser never runs over speech.** Fit it into a pause, or open one in `parts.json`.
11. **An audit's numbers are not the owner's taste.** Measured "too quiet" is not a reason to fill every pause. Silence near a key line is often the point.
