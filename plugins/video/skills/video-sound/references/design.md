# Sound design

Sound in a narrated short works in three tiers. Most of it should be felt, not noticed.

| Tier | What | How much |
|---|---|---|
| Background | Ambience where the picture is a real place | Sparse, 15 to 25 dB under the voice |
| Supporting | One small sound per visible event | 15 to 30 in a minute, 80 to 90% unnoticed |
| Foreground | The featured moments | 1 to 3 in a film: hook, turn, ending |

No music is needed in a calm narrated film with small sounds and real pauses. One effect per transition is usually enough, two is the limit.

## What goes with what

| Picture | Sound | Avoid |
|---|---|---|
| A real outdoor view | Ambience of that kind of place | Ambience over a map, graphic or title card |
| Map or satellite zoom | Continuous wind that rises with the camera's speed, an airy whoosh on the landing | Birds, bright zips |
| Photo appears | Paper handling, kept quiet. Glass set down for an old plate | Projector clatter under the voice |
| Fast camera move or cut | One air pass peaking on the cut | Several stacked whooshes |
| Something heavy lands or settles | A low thump plus a short settle from the right material | Generic cinematic impact on every beat |
| Slow rotation | Nothing, or a soft texture | Whooshes on slow moves |
| Caption | Nothing. At most a soft tick on a key label | A click on every caption |
| The turn of the story | A soft riser ending on the cut, then a warm hit, with the bed pulled down first | Braams, glitches, full sub-drops |
| Key word alone | A held pad with a soft tap on top, in a voice gap | Anything over the word's consonants |
| Recap words | One physical hit per word, well under the voice | Dings, chimes |
| Last word | One heavier hit ringing into the end card | A long fade to nothing |

A drawing stroke with no fitting real sound can stay silent.

## Product and UI explainers

A screen has no world of its own, so the rules shift. From one approved explainer, so treat this as a starting point:

- Music as a very low bed is fine, because there is no ambience to carry the gaps. No melody that competes with the voice.
- Effects must stay audible. A mix with effects 3 to 4 dB under the levels below drew the question "did we include sound effects?".
- More effects fit: about 33 cues a minute, against 15 to 30 for a calm film.
- A riser that ran across the end of a sentence was the one reviewers called noise. Replacing it with a soft air pass fixed it; risers in clear pauses stayed.

Levels in that mix, as `level_db`, with the voice at −16 LUFS before the master:

| Sound | `level_db` |
|---|---|
| Music bed | −41, with `duck_db` −3 |
| Tick | −48 |
| Paper | −47 |
| Tap | −40 to −37 |
| Air pass | −39 to −35 |
| Thump or hit | −33 to −30 |
| Riser | −34 to −33 |

## Timing

Starting points, from a study of eight motion films (earshot's `docs/motion-sfx-study.md`). At 30 fps a frame is 33 ms.

| Cue | File starts | Loudest point | Length |
|---|---|---|---|
| Airy whoosh | 15 to 30 frames early | Within 4 frames of the event | 0.5 to 1.5 s |
| Soft riser | Its own length before the cut | Ends exactly on the cut, then a hit or room tone | About 1 s |
| Gentle impact | 3 to 5 frames early | On the cut | Tail 0.3 to 1 s |
| Tick | About 1 frame after the label | At once | 0.05 to 0.3 s |

`mix.py` aligns by measured peak, so the sheet only needs the event time.

## Moments

- To make something feel loud, make the moment before it quiet: drop the bed 6 to 10 dB for 0.3 to 0.5 seconds.
- Keep the loudest effect off key words. Put it in a gap, and write that gap into the edit.
- Never run a riser over speech. It has to finish in a pause.
- Never use digital silence in the middle of a film; leave a very low room tone. A hole with a visual cut in it needs a sound on the cut.
- Use a sound once. Vary pitch, part and level on any repeat.

## Respect the subject

Use no sacred or ceremonial sounds as mood, such as a call to prayer or singing bowls, and no regional instruments as a shortcut for "the East". Any such sound needs a real reason to be there. Ask the owner when the subject is close to their faith or community.

## The opening and ending

- Start with sound on frame 0: ambience or a low swell, so the first word does not arrive in a vacuum.
- First phrases often read 3 to 5 dB hot. Set `first_phrase_db` to about −2.5.
- End on weight, then let the end card ring out quickly.
