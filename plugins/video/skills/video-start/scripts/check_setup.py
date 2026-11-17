#!/usr/bin/env python3
"""Check that this computer can make a video. Prints what is ready and what is missing. Never prints a key."""
import importlib.util
import os
import shutil
import subprocess
import sys


def version(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, shell=os.name == "nt")
        return (out.stdout or out.stderr).splitlines()[0].strip()
    except (OSError, IndexError):
        return None


def line(ok, name, detail):
    print(f"{'ok  ' if ok else 'MISS'} {name:12} {detail}")
    return ok


def main():
    need = True
    for name, cmd, fix in (
        ("node", ["node", "-v"], "install Node 20 or newer"),
        ("ffmpeg", ["ffmpeg", "-version"], "install ffmpeg and put it on PATH (winget install Gyan.FFmpeg, brew install ffmpeg, apt install ffmpeg)"),
        ("ffprobe", ["ffprobe", "-version"], "comes with ffmpeg"),
    ):
        found = shutil.which(cmd[0]) and version(cmd)
        need &= line(bool(found), name, found or fix)
    for mod, pkg in (("numpy", "numpy"), ("scipy", "scipy"), ("soundfile", "soundfile"), ("PIL", "pillow")):
        need &= line(importlib.util.find_spec(mod) is not None, pkg, "" if importlib.util.find_spec(mod) else f"{sys.executable} -m pip install {pkg}")
    print()
    earshot = shutil.which("earshot") or os.environ.get("EARSHOT_BIN")
    line(bool(earshot), "earshot", earshot or "optional but strongly advised; see references/setup.md")
    key = bool(os.environ.get("ELEVENLABS_API_KEY"))
    line(key, "ElevenLabs", "key is set" if key else "optional: only for word timings or generated sounds; set ELEVENLABS_API_KEY")
    print("\nready to edit and mix" if need else "\nfix the MISS lines above first")
    sys.exit(0 if need else 1)


if __name__ == "__main__":
    main()
