#!/usr/bin/env python3
"""Create a complete local video project: voice-over in, final video out.

  python new_project.py ~/videos/my-video [--format 16:9] [--no-install]

Copies the starter, the plugin's templates and tools (so the project stands on its own), starts a git
repository and installs the packages. Next steps are in the new project's CLAUDE.md.
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[2]


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, shell=sys.platform == "win32").returncode == 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--format", choices=("9:16", "16:9"), default="9:16", help="9:16 for Reels, TikTok and Shorts; 16:9 for YouTube and product explainers")
    ap.add_argument("--no-install", action="store_true")
    a = ap.parse_args()
    dest = Path(a.path).expanduser().resolve()
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"{dest} is not empty")
    shutil.copytree(SKILLS / "video-start" / "starter", dest, dirs_exist_ok=True)
    (dest / "gitignore.txt").rename(dest / ".gitignore")
    for f in ("timeline.ts", "Captions.tsx"):
        shutil.copy(SKILLS / "video-montage" / "templates" / f, dest / "src" / f)
    if a.format == "16:9":
        t = dest / "src" / "timeline.ts"
        s = t.read_text(encoding="utf8")
        for old, new in (("WIDTH = 1080", "WIDTH = 1920"), ("HEIGHT = 1920", "HEIGHT = 1080"), ("CAPTION_BOTTOM = 600", "CAPTION_BOTTOM = 90")):
            assert old in s
            s = s.replace(old, new)
        t.write_text(s, encoding="utf8", newline="\n")
    tools = dest / "tools"
    tools.mkdir()
    for f in ("video-montage/scripts/words.py", "video-montage/scripts/freeze_check.py", "video-sound/scripts/mix.py", "video-sound/scripts/compare.py"):
        shutil.copy(SKILLS / f, tools)
    pkg = dest / "package.json"
    p = json.loads(pkg.read_text(encoding="utf8"))
    p["name"] = dest.name.lower().replace(" ", "-")
    if a.format == "16:9":
        p["scripts"]["check"] = p["scripts"]["check"].replace("--mask 0.62 0.75", "--mask 0.8 0.95")
    pkg.write_text(json.dumps(p, indent=2) + "\n", encoding="utf8")
    run(["git", "init", "-q"], dest)
    if not a.no_install:
        if not run(["npm", "install"], dest):
            sys.exit("npm install failed; fix it and run it again in the project")
        if not run(["npx", "-y", "skills", "add", "remotion-dev/skills", "-y"], dest):
            print("Could not add the Remotion skills. Later, run in the project: npx skills add remotion-dev/skills")
    print(f"\nCreated {dest}\nOpen Claude Code there. Next steps are in CLAUDE.md.")


if __name__ == "__main__":
    main()
