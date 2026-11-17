import React from "react";
import { Audio } from "@remotion/media";
import { AbsoluteFill, Img, interpolate, Sequence, staticFile, useCurrentFrame } from "remotion";
import { Captions } from "./Captions";
import { CAPTION_BOTTOM, CAPTIONS, F, NARRATION, PARTS, RTL, S, SHOTS, W } from "./timeline";

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

/** A photo full-bleed with a slow push. Linear, so it is still moving at the cut. */
const Photo: React.FC<{ src: string; len: number }> = ({ src, len }) => {
  const f = useCurrentFrame();
  return <Img src={staticFile(src)} style={{ position: "absolute", width: "100%", height: "100%", objectFit: "cover", scale: String(interpolate(f, [0, len], [1, 1.1], clamp)) }} />;
};

export const Video: React.FC = () => {
  const total = F(S.total);
  return (
    <AbsoluteFill style={{ backgroundColor: "#10182B" }}>
      {SHOTS.map((s, i) => {
        const from = F(s.at);
        const len = (i + 1 < SHOTS.length ? F(SHOTS[i + 1].at) : total) - from;
        return (
          <Sequence key={s.src + i} from={from} durationInFrames={len}>
            <Photo src={s.src} len={len} />
          </Sequence>
        );
      })}
      <Captions lines={CAPTIONS} until={F(S.end)} rtl={RTL} bottom={CAPTION_BOTTOM} />
      {W.length
        ? PARTS.map((p, k) => (
            <Sequence key={k} from={F(p.from + p.shift)}>
              <Audio name={`Voice ${k + 1}`} src={staticFile(NARRATION)} trimBefore={F(p.from)} trimAfter={p.to < 9000 ? F(p.to) : undefined} />
            </Sequence>
          ))
        : null}
    </AbsoluteFill>
  );
};
