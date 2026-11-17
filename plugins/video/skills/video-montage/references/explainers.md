# Product and UI explainers

From one finished explainer (16:9, under three minutes, approved by its owner). The numbers worked there, so treat them as starting points. For screens rather than photos, these rules replace the photo guidance in `picture.md` where they differ.

Create the project with `--format 16:9`, and see `capture.md` for screens.

## The motion rule

Every motion must do one of three things: follow the voice, show cause and effect, or move the eye to what matters. Anything else goes. A slow push that keeps a photo alive is right in a heritage film and wrong on a screen, where the viewer is trying to read.

## Rebuild or capture

Rebuild what must change state on a spoken word. Capture what serves as proof.

| Rebuild in Remotion, as real text | Show as a capture |
|---|---|
| Terminal sessions, task lists with live status, lists of results, documents and tables, sequence diagrams, chains from one record to the next | Long comments and reports, report tiles, large graphs, and a true screen recording for a live event |

Rebuilding wins for four reasons:

- State changes land exactly on the word.
- Text can be sized to read at 1080p.
- Private data is left out, not blurred.
- Frames of a real terminal played in order read as a slideshow.

## Reveal by line

At 30 fps:

- Give each line a time in `timeline.ts`, set from a word index with `wf(k)`.
- Lines nobody talks about arrive slightly before the first word that needs them, or are on screen at the cut, so a panel is never empty.
- The reveal is an opacity fade with no wipe and no movement: 8 frames for a line, 10 for a card, 12 for a headline, which fades as one whole line.
- Emphasis is separate: a highlight wipes left to right over 12 frames, starting on the spoken word.
- Type character by character only for a person's reply, never for program output.
- When a list passes its visible rows, scroll one row, eased over 12 frames.

Word-by-word headlines and typed program output were the main causes of the owner's "over-animated" note.

## Label replays honestly

Use one small plain line in the bottom-left corner, about 22 px at 1080p, for the whole scene. Say exactly what is real:

| Label | When |
|---|---|
| "Shortened replay of a real session" | Real output, condensed |
| "Built from real project records" | Rebuilt from real data |
| "Real recording" | A true screen recording |
| "Real tasks from story <id>" | Real tasks, with order and overlap arranged for the shot |

The last one claims the tasks are real, not the timing, so it stays accurate. The owner rejected "Illustration". The rule is the same as for a reconstruction in `picture.md`: the viewer must never think they are watching something that did not happen.

## Claims

Every number on screen must match its source on the day of the final render. Run the claims check in `video-start` again if the product changed.

## Captions

Decide per film. A screen full of text may need none. Word-by-word captions are built for phones, and they compete with a screen the viewer is reading.
