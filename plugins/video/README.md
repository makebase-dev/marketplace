# video

Three Claude skills for editing short narrated videos on any computer, from a voice-over, photos and clips to a finished, mastered file. Editing is code (Remotion), and sound is a cue sheet that a script mixes. Claude cannot hear or watch, so measuring tools stand in for its ears and eyes, and you make the taste calls.

| Skill | Use it to | Call it |
|---|---|---|
| **video-start** | Set up a new computer, start a project, and follow the order of work | `/video:video-start` |
| **video-montage** | Build the edit: timeline from word timings, captions, photo and clip motion, callouts, freeze checks, blind audits, delivery | `/video:video-montage` |
| **video-sound** | Find real licensed sounds, rank them with earshot, place them, mix, master, and agree the result with you in context | `/video:video-sound` |

This plugin covers montage and sound. Writing the script, recording the voice and 3D or map shots are not in it: bring them as files.

## Start on a new computer

Any session can follow these steps. On Windows use PowerShell; on macOS or Linux use the same commands in a terminal.

**1. Install the programs**

| What | Windows | macOS |
|---|---|---|
| Node 20 or newer | `winget install OpenJS.NodeJS.LTS` | `brew install node` |
| ffmpeg | `winget install Gyan.FFmpeg` | `brew install ffmpeg` |
| Python 3.10 or newer | `winget install Python.Python.3.12` | `brew install python` |

Open a new terminal afterwards so the programs are on PATH.

**Linux and WSL (Ubuntu 24.04).** Run these yourself, in your own terminal: `sudo` asks for your password, and a Claude session cannot type it.

```
sudo apt update
sudo apt install -y ffmpeg python3-venv git curl libnss3 libdbus-1-3 libatk1.0-0 libasound2t64 libxrandr2 libxkbcommon-dev libxfixes3 libxcomposite1 libxdamage1 libgbm-dev libcups2 libcairo2 libpango-1.0-0 libatk-bridge2.0-0
```

The long list is what Remotion's browser needs; other versions differ slightly, so see [Remotion's list](https://www.remotion.dev/docs/miscellaneous/linux-dependencies). It needs glibc 2.35 or newer (Ubuntu 22.04 or later). Alpine and NixOS are not supported. Install Node 20 or newer from [nodejs.org](https://nodejs.org/en/download) or with nvm, because the Ubuntu package can be older. On WSL, keep projects inside the Linux file system (`~/videos`), not under `/mnt/c`.

**2. Install this plugin**

```
claude plugin marketplace add makebase-dev/marketplace
claude plugin install video@makebase
```

**3. Install the Python packages and earshot**

```
python -m venv ~/video-tools
~/video-tools/bin/pip install numpy scipy soundfile pillow git+https://github.com/Leonxlnx/earshot
~/video-tools/bin/earshot doctor
```

On macOS and Linux use `python3` for the first line. On Windows the folder is `~\video-tools\Scripts\` instead of `bin`. earshot downloads its listening models (about 4 GB) the first time they are needed. Run the scripts below with this environment's Python.

**4. Create the local repo**

Activate the environment from step 3 (`source ~/video-tools/bin/activate`, or `~\video-tools\Scripts\Activate.ps1` on Windows), then run the generator from the plugin. Ask Claude Code to do it ("use /video:video-start and create a project called my-video"), or run it yourself:

```
python <plugin folder>/skills/video-start/scripts/new_project.py ~/videos/my-video
```

The default is 9:16 for Reels, TikTok and Shorts. Add `--format 16:9` for YouTube or a product explainer.

It creates a complete project: a git repo, a working 9:16 composition, the tools in `tools/`, the Remotion skills, and a `CLAUDE.md` that any session reads first. Each video gets its own repo.

**From voice-over to final video**

Inside the project, with the environment active:

| Step | Do |
|---|---|
| 1. Voice | Put the approved voice-over at `public/audio/narration.mp3` |
| 2. Timings | `npm run words` writes `src/words.json` |
| 3. Edit | Add photos to `public/photos/`, then list them in `SHOTS` in `src/timeline.ts`. For Arabic set `RTL = true`. Add holds in `src/parts.json` |
| 4. Preview | `npm run dev` opens the editor in the browser |
| 5. Draft | `npm run draft` renders, `npm run check` looks for freezes |
| 6. Sound | Put sounds in `sound/sfx/` and cues in `sound/sound.json` |
| 7. Final | `npm run mix` writes `out/final.mp4` at −14 LUFS, `npm run share` a small copy |

The captions work at once, split automatically every four words. Replace them with hand-written ones before the final. Clips are not in the starter composition yet: use Remotion's `<OffthreadVideo>` in `src/Video.tsx`.

**5. Accounts and keys, only if you need them**

| What | For |
|---|---|
| `ELEVENLABS_API_KEY` in your environment | Word timings from a voice-over (the key needs the `speech_to_text` permission), generated pads. Keep it in a local file that git ignores, never in the repo or a chat |
| A Freesound account | Downloading original sound files. You sign in yourself; Claude never types a password |

Remotion is free for individuals and for companies of up to 3 people. Larger companies need a licence: $25 per seat per month for making videos by hand, with separate pricing for automated rendering. See [Remotion's licensing page](https://www.remotion.pro/license).

## The tools in this plugin

| Script | What it does |
|---|---|
| `video-start/scripts/check_setup.py` | Lists what this computer has and what is missing |
| `video-start/scripts/new_project.py` | Creates a complete local video repo |
| `video-montage/scripts/words.py` | Word timings from a voice-over, with ElevenLabs Scribe |
| `video-montage/scripts/freeze_check.py` | Finds repeated frames, still runs and jumps in a render |
| `video-sound/scripts/mix.py` | Mixes and masters from one JSON cue sheet, keeps the voice clear, and checks loudness |
| `video-sound/scripts/compare.py` | Makes a clip that plays the same seconds once per sound option, with a big 1, 2, 3 on screen |

Also: `video-start/starter/` (the project the generator copies), `video-montage/templates/` (timeline from word timings, word-by-word captions in Arabic or English) and `video-sound/templates/sound.json` (an example cue sheet).

## Update

```
claude plugin marketplace update makebase
claude plugin update video@makebase
```

## Works best with

- The Remotion skills (`remotion-dev/skills`), which hold the framework's own rules.
- earshot, the tool that lets Claude measure what a sound is. It cannot judge taste, so you still listen.
