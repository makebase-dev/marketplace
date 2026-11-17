import React from "react";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig } from "remotion";

/** A caption chunk: text, the frame it starts, and each word's frame inside it. */
export type Line = { text: string; at: number; wordAt: number[] };

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

/**
 * One chunk at a time, built word by word, the newest word in the accent colour. Words, not letters,
 * so Arabic stays joined. Words not yet spoken stay hidden with their space kept, so the box holds still.
 * `hidden`: frame ranges with no captions (a title already says the line). `only`: show just inside
 * this range, for a second instance at another height.
 */
export const Captions: React.FC<{
  lines: Line[];
  until: number;
  bottom?: number;
  rtl?: boolean;
  fontFamily?: string;
  textColor?: string;
  accent?: string;
  box?: string;
  hidden?: [number, number][];
  only?: [number, number];
}> = ({ lines, until, bottom = 600, rtl = false, fontFamily = "sans-serif", textColor = "#F4EBDD", accent = "#E0A526", box = "rgb(6 20 46 / 86%)", hidden = [], only }) => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  const u = Math.min(width, height) / 1080;
  if (hidden.some(([a, b]) => frame >= a && frame < b) || (only && (frame < only[0] || frame >= only[1]))) return null;
  const i = lines.findIndex((l, k) => frame >= l.at && frame < (lines[k + 1]?.at ?? until));
  if (i < 0) return null;
  const line = lines[i];
  const end = lines[i + 1]?.at ?? until;
  const local = frame - line.at;
  const words = line.text.split(" ");
  const shown = Math.max(1, words.filter((_, k) => local >= line.wordAt[k]).length);
  const opacity = interpolate(frame, [line.at, line.at + 8, end - 8, end], [0, 1, 1, 0], clamp);

  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: bottom * u, pointerEvents: "none" }}>
      <div
        dir={rtl ? "rtl" : "ltr"}
        style={{ maxWidth: `calc(100% - ${160 * u}px)`, textAlign: "center", fontFamily, fontWeight: 700, fontSize: 62 * u, lineHeight: 1.45, color: textColor, opacity, padding: `${14 * u}px ${30 * u}px`, borderRadius: 18 * u, background: box }}
      >
        {words.map((w, k) => {
          const p = interpolate(local - line.wordAt[k], [0, 8], [0, 1], { ...clamp, easing: Easing.out(Easing.cubic) });
          const newest = k === shown - 1 && local < line.wordAt[words.length - 1] + 14;
          return (
            <React.Fragment key={k}>
              <span style={{ display: "inline-block", opacity: k < shown ? p : 0, translate: `0 ${(1 - p) * 0.25}em`, color: newest ? accent : textColor }}>{w}</span>
              {k < words.length - 1 ? " " : null}
            </React.Fragment>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
