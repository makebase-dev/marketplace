---
name: video-start
description: "Start editing a short narrated video with Remotion on any computer: check and install the tools, create the project, and follow the order of work from voice-over to final file. Use when setting up a new computer for video work, starting a new video, or when a session has to pick up video work and needs the workflow. Use video-montage for the edit itself and video-sound for sound."
---

# Video start

The way of working behind this plugin, learned by finishing a 60-second narrated short through many review rounds with its owner. Montage and sound only: the script, the voice and any 3D or map shots arrive as files.

## Read for the task

| Task | Read |
|---|---|
| New computer, missing tool, or `check_setup.py` shows MISS | `references/setup.md` |
| Building the edit | The `video-montage` skill |
| Anything about sound | The `video-sound` skill |

## First steps in any session

1. Run `python scripts/check_setup.py` from this skill's folder and fix every MISS line before starting.
   With no project yet, run `python scripts/new_project.py <folder>`, adding `--format 16:9` for YouTube or a product explainer: it creates a complete repo (composition, tools, git, Remotion skills). The new project's `CLAUDE.md` lists the steps from voice-over to final file.
2. Read the project's README or notes file. If it has none, create `NEXT.md`: current version, what is running, what the owner decided. Update it at each stop, so another session or computer can continue.
3. Ask what you cannot find: the platform and shape (9:16 for Reels, TikTok and Shorts), the length, who it is for, the language, and any brand assets.

## The order of work

Each step ends with something the owner can react to. Do not skip ahead: a change late in the order costs everything after it.

1. **Claims check, then voice.** Before any voice is generated, verify every number, date and name in the script at its source. A wrong fact found later costs a new voice and every timing after it.
   The owner hears and approves the voice-over before any render. Every timing below hangs on it.
2. **Word timings.** Produce `words.json` from the approved voice-over.
3. **Storyboard.** One line per shot: time, what is said, what is seen, the source file. Agree it before building.
4. **Rough edit.** Timeline, shots and captions, with the voice only. Send a low-quality draft.
5. **Picture fixes.** Work through notes, then run the freeze check.
6. **Sound.** Mix from a cue sheet. See `video-sound`.
7. **Blind audits.** Agents who know nothing about the intent review picture and sound separately.
8. **Final.** Replace previews with full-quality files, mix on the final picture, check, deliver.

## Project layout

```
my-video/
  NEXT.md               state and decisions
  public/               everything Remotion loads: photos/, video/, audio/
  CLAUDE.md             the steps, read first by any session
  src/timeline.ts       the only place with times
  src/parts.json        the voice-over's holds, shared with the mix
  src/words.json        word timings
  src/Video.tsx         the composition
  sound/sound.json      the cue sheet
  sound/sfx/            sources, each with its licence noted
  tools/                words, freeze check, mix, compare
  build/                mixes and drafts (git-ignored)
  out/                  renders (git-ignored)
```

## Rules that held up every time

1. **Show before the long job.** Before anything that runs for hours, show stills and the settings and wait for a yes. Run long jobs in the day.
2. **Let the owner hear it first.** Audio is a fast render, so send audio or a draft before a final picture render.
3. **Never present an unheard mix as finished.** Measurements prove levels, not taste. Say plainly that nobody has listened yet.
4. **Every change gets a version.** v1, v2, v2.1, with the previous one kept, so "the last one was better" is a one-line fix.
5. **Share light.** Send a small copy (`ffmpeg -i final.mp4 -c:v libx264 -crf 28 -preset fast -c:a copy share.mp4`), keep the full file local.
6. **When the owner says worse, go back.** Start again from the version they liked and add only what they named. See `video-sound` for how this played out.
7. **Check the facts on screen against sources,** and show no people in a photo without permission.
8. **Credit what the licence needs,** on screen where it requires that.
