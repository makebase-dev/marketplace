# Setup

`scripts/check_setup.py` shows the state of the computer. The plugin's README has the full steps for a person; this is what a session needs.

## Required

| Tool | Why | Install |
|---|---|---|
| Node 20+ | Remotion | `winget install OpenJS.NodeJS.LTS`, `brew install node`, or nvm |
| ffmpeg and ffprobe | Measuring, mixing, muxing. Must be on PATH | `winget install Gyan.FFmpeg`, `brew install ffmpeg`, `apt install ffmpeg` |
| Python 3.10+ with numpy, scipy, soundfile, pillow | The scripts | `python -m pip install numpy scipy soundfile pillow` |

## Advised

**earshot**, in its own environment because it brings torch:

```
python -m venv ~/video-tools
~/video-tools/bin/pip install git+https://github.com/Leonxlnx/earshot
~/video-tools/bin/earshot doctor
```

- Windows: `~\video-tools\Scripts\earshot.exe`.
- Models download on first use into `~/.cache/earshot`. It runs on the CPU; no GPU is needed.
- It needs ffmpeg on PATH. If the session's shell does not have it, set PATH for that command.
- Set `EARSHOT_BIN` to the path of the program so `check_setup.py` finds it.

**Remotion skills:** `npx skills add remotion-dev/skills` in the project. They hold the framework's rules; this plugin does not repeat them. Claude Code's auto mode may block this command. `new_project.py` carries on if it fails, so run it yourself in a terminal afterwards.

## A new project

```
python scripts/new_project.py ~/videos/my-video
```

Add `--format 16:9` for YouTube or a product explainer. The default is 9:16.

It copies the starter, puts the tools in `tools/` so the project stands alone, runs `git init` and `npm install`, and adds the Remotion skills. Run the Python commands with the environment that holds numpy and scipy active, because `npm run words`, `check` and `mix` call `python`.

Big sources stay out of git if the repo goes online: keep a note of where they live.

If Remotion cannot download its browser, point it at an installed one in `remotion.config.ts`.

## Linux and WSL

The plugin README has the commands. Remotion needs glibc 2.35 or newer, such as Ubuntu 22.04 or later, plus some shared libraries. Alpine and NixOS are not supported.

`sudo` asks for a password, which a session cannot and must not type. Give the owner the command to run in their own terminal.

## Windows notes

- ffmpeg's `-i "*.jpg"` glob does not work. Use a numbered pattern (`%04d.jpg`) or Python.
- Python output with Arabic: run `python -X utf8`. `-I` ignores `PYTHONIOENCODING`.
- Use absolute paths when one tool starts another; relative ones can land in the wrong drive.
- ffmpeg's `drawtext` can crash without a font configuration. `compare.py` draws its digits with Pillow for this reason.

## Keys

- `ELEVENLABS_API_KEY` is the only key in use, and only for word timings or generated pads. Keep it in the shell environment or an ignored `.env`.
- Word timings need the key's `speech_to_text` permission. Give a key only the permissions it needs.
- Never print a key, put it in a URL, or commit it. Check with `git status` before each commit.
- Never type a password for the owner. When a site needs a sign-in, stop and ask them to do it.
