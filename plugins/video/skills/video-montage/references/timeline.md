# Timeline from word timings

## Word timings

`words.json` is a list of `{ "t": word, "s": start, "e": end }` in seconds of the voice-over file.

`npm run words` makes it with ElevenLabs Scribe (`scripts/words.py`). Any speech-to-text with word timestamps also works. It gives a check too: compare the printed transcript with the script to catch misread words.

Timings of a repaired or spliced voice-over must be made again from the final file.

## Parts: opening holds in a continuous take

A take is one continuous read. To give the picture room, cut it at natural pauses and play each part later:

```json
[
  { "from": 0, "to": 16.45, "shift": 0.3 },
  { "from": 16.45, "to": 9999, "shift": 1.1 }
]
```

These live in `src/parts.json`, which `timeline.ts` and `sound.json` both read. The first shift is a beat before the first word, the second a breath after the opening.

- Cut only inside a real pause. Read `words.json` to find one.
- Every shift is a hold the viewer feels. Put the longest before a reveal and after the key line.
- `v(s)` turns narration time into video time; `ws(k)` gives word k's start. Scenes use these, never numbers.
- In Remotion, each part is a `<Sequence>` with an `<Audio>` using `trimBefore` and `trimAfter`.

## Shots

Define each shot boundary as a word plus an offset, and name it:

```ts
const reveal = ws(24) - 0.3; // the cut lands just before the word
```

- Cut slightly before the word it belongs to. The eye should arrive as the word does.
- Let a label land on the word that names the thing.
- Keep cue times for animation in the same file, so sound can read them.

## Reusing a render

If a scene plays frames from a folder, make the join share a frame (the last of A equals the first of B) and start B from its second frame, so nothing repeats.
