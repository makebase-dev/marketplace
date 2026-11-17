#!/usr/bin/env python3
"""Find what eyes catch and metrics miss: repeated frames inside moving shots, still runs, and jumps.

  python freeze_check.py draft.mp4 [--mask 0.62 0.75]

--mask blanks a horizontal band (fractions of the height), usually the captions, so their changes do not count.
A STUTTER line is a defect. A "still" line is a defect unless the shot is meant to hold. A "jump" must be a planned cut.
Needs ffmpeg on PATH and: pip install numpy
"""
import argparse
import subprocess

import numpy as np

W, H = 108, 192


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--mask", nargs=2, type=float, metavar=("TOP", "BOTTOM"))
    ap.add_argument("--fps", type=float, default=30)
    a = ap.parse_args()
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", a.video, "-vf", f"scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
                         capture_output=True, check=True).stdout
    frames = np.frombuffer(raw, np.uint8).reshape(-1, H, W).astype(np.float32)
    if a.mask:
        frames[:, int(H * a.mask[0]):int(H * a.mask[1]), :] = 0
    d = np.abs(np.diff(frames, axis=0)).mean(axis=(1, 2))
    print(f"frames {len(frames)}, median change {np.median(d):.3f}")
    for i in range(1, len(d) - 1):
        if d[i] < 0.05 and d[i - 1] > 0.4 and d[i + 1] > 0.4:
            print(f"STUTTER repeated frame at {(i + 1) / a.fps:.2f}s ({d[i - 1]:.2f} {d[i]:.2f} {d[i + 1]:.2f})")
    run = 0
    for i, x in enumerate(d):
        run = run + 1 if x < 0.05 else 0
        if run == 15:
            print(f"still for 0.5 s or more from {(i - 14) / a.fps:.2f}s")
    for i in range(1, len(d) - 1):
        if d[i] > 6 * max(d[i - 1], d[i + 1], 0.3) and d[i] > 3:
            print(f"jump or cut at {(i + 1) / a.fps:.2f}s (change {d[i]:.1f})")


if __name__ == "__main__":
    main()
