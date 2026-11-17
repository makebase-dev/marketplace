/**
 * The only file with times. Everything is built from the voice-over's word timings (words.json:
 * [{ t, s, e }]). The take is one continuous read, cut at natural pauses into parts (parts.json,
 * also read by the sound mix); each part plays later than it was read, which opens the holds.
 */
import words from "./words.json";
import parts from "./parts.json";

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;
export const CAPTION_BOTTOM = 600; // distance from the bottom, at 1080 on the short side
export type Word = { t: string; s: number; e: number };
export const W = words as Word[];
export const NARRATION = "audio/narration.mp3";
export const RTL = false; // true for Arabic
export const PARTS = parts as { from: number; to: number; shift: number }[];

const shiftOf = (s: number) => (PARTS.find((p) => s >= p.from && s < p.to) ?? PARTS[PARTS.length - 1]).shift;
/** Video seconds of a narration second. */
export const v = (s: number) => s + shiftOf(s);
/** Video seconds of word k's start. */
export const ws = (k: number) => v(W[k].s);
export const F = (s: number) => Math.round(s * FPS);
/** Video frame of word k's start. */
export const wf = (k: number) => F(ws(k));

/**
 * Captions: [text, first word, last word]. Replace the automatic chunks with hand-written ones in
 * the script's spelling: 2 to 5 words, never split a noun from its adjective or a number from what it counts.
 */
const auto = (size: number): [string, number, number][] =>
  Array.from({ length: Math.ceil(W.length / size) }, (_, i) => {
    const a = i * size;
    const b = Math.min(W.length, a + size) - 1;
    return [W.slice(a, b + 1).map((w) => w.t).join(" "), a, b];
  });
const CHUNKS: [string, number, number][] = auto(4);

export const CAPTIONS = CHUNKS.map(([text, a, b]) => {
  const at = wf(a);
  const n = text.split(" ").length;
  // Spread the chunk's display words over its spoken words (they rarely differ by more than one).
  const spoken = Array.from({ length: b - a + 1 }, (_, k) => wf(a + k) - at);
  const wordAt = Array.from({ length: n }, (_, k) => spoken[Math.min(spoken.length - 1, Math.round((k * (spoken.length - 1)) / Math.max(1, n - 1)))]);
  return { text, at, wordAt };
});

const lastWord = W.length ? v(W[W.length - 1].e) : 6;
/** End of the voice, and the length of the film. */
export const S = { end: lastWord + 0.6, total: lastWord + 2.0 };

/**
 * Shots: a photo in public/ and when it starts, as a word plus an offset, never a typed time.
 * An empty list shows a plain background.
 */
export const SHOTS: { at: number; src: string }[] = [
  // { at: 0, src: "photos/01.jpg" },
  // { at: ws(12) - 0.2, src: "photos/02.jpg" },
];
