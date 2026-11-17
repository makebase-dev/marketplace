---
name: video-montage
description: "Edit a short narrated video in Remotion: build the timeline from the voice-over's word timings, word-by-word captions (Arabic and English), photo and clip motion, callouts, safe zones, transitions, freeze and stutter checks, blind picture audits and delivery. Use when building or fixing the picture of a video, when an edit feels weak or stuttery, or when captions, pacing or framing need work."
---

# Video montage

Lessons from taking a 60-second narrated short from a weak first cut to a finished file, through blind audits and many notes from its owner. Use the Remotion skills for framework rules; this skill says how to make the edit good.

## Read for the task

| Task | Read |
|---|---|
| Timing shots to the voice, splitting and shifting the voice-over | `references/timeline.md` |
| Captions, including Arabic | `references/captions.md` |
| Framing, photo motion, callouts, type, transitions, pacing | `references/picture.md` |
| Freeze checks, blind audits, final render | `references/checks.md` |
| A product or UI explainer, usually 16:9 | `references/explainers.md` |
| Capturing screens from a live product | `references/capture.md` |

## Templates

`new_project.py` copies these into a new project's `src/`:

- `templates/timeline.ts`: helpers from word to frame, caption chunks and shot times.
- `templates/Captions.tsx`: word-by-word captions with hidden ranges.

Word timings: `scripts/words.py`, or `npm run words` in a project.

## Rules that held up every time

1. **One file holds the times.** Every shot, caption and label reads `timeline.ts`, built from word timings. No hand-typed frame in a scene. When the voice changes, the edit follows.
2. **The voice sets the pace.** Cut the take at its natural pauses and shift the parts later to open holds. Never stretch it.
3. **The first two seconds must move.** Text on a still photo for eight seconds reads as a poster. Change something every 2 to 4 seconds, faster at the start.
4. **Keep moves linear.** An eased push slows to nothing and reads as a freeze before the cut. Linear pushes keep moving through it.
   Move images with `translate` or `scale`, never `top` or `left`: those snap to whole pixels, so slow pans stutter.
5. **Never reverse or slow footage to fill time.** Reverse playback and half speed stutter. Render or find the real motion.
6. **Hard cut, or a real match.** A crossfade between similar shots ghosts. Stock transitions look cheap.
7. **Plain beats decorated.** If a photo already shows the thing, remove the ring, the dim and the label. A mark on something obvious is noise.
8. **A mark must be seen.** A thin gold ring on a pale hill disappears. Give marks a dark outline, and add an arrow when the target is small.
9. **Nothing on screen is empty.** A half-frame of black while waiting for the next image looks like a failed render. Show the next image dim until it wipes in.
10. **Check the bottom edge of every photo.** Vertical crops made from wide images often have blurred filler. Crop it out.
11. **Say it once.** Where a title says the line, hide the caption.
12. **Measure, then look.** Run the freeze check on each render and read a contact sheet. Numbers find stutters; only looking finds a weak frame.
