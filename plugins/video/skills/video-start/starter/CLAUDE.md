# Video project

Read `NEXT.md` first. Use the `video` plugin's skills: `video-start` for the order of work, `video-montage` for the edit, `video-sound` for sound.

Activate the Python environment with the tools before running `npm run` commands that use Python.

| Step | Do |
|---|---|
| 1. Voice | Put the approved voice-over at `public/audio/narration.mp3` |
| 2. Timings | `npm run words` writes `src/words.json` (needs `ELEVENLABS_API_KEY`) |
| 3. Edit | Photos in `public/photos/`, then `src/timeline.ts`: `SHOTS`, captions, `RTL`. Holds go in `src/parts.json` |
| 4. Preview | `npm run dev` |
| 5. Draft | `npm run draft`, then `npm run check` |
| 6. Sound | Sources in `sound/sfx/`, cues in `sound/sound.json`. The `video-sound` skill has an example sheet in `templates/sound.json` |
| 7. Final | `npm run mix` writes `out/final.mp4`; `npm run share` writes a small copy |

All times live in `src/timeline.ts`. Never type a time in a scene. Note the source and licence of every sound and photo.
