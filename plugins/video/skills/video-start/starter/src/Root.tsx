import React from "react";
import { Composition } from "remotion";
import { F, FPS, HEIGHT, S, WIDTH } from "./timeline";
import { Video } from "./Video";

export const Root: React.FC = () => <Composition id="Video" component={Video} width={WIDTH} height={HEIGHT} fps={FPS} durationInFrames={F(S.total)} />;
