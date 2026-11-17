#!/usr/bin/env python3
"""Word timings of a voice-over, with ElevenLabs Scribe, as [{ "t", "s", "e" }] for timeline.ts and mix.py.

  python words.py public/audio/narration.mp3 src/words.json [--language ar]

Needs ELEVENLABS_API_KEY in the environment. Standard library only. Prints the transcript: compare it with the script.
"""
import argparse
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio")
    ap.add_argument("out")
    ap.add_argument("--language", help="language code, such as ar or en; detected when left out")
    a = ap.parse_args()
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY is not set")
    audio = Path(a.audio)
    if not audio.exists():
        sys.exit(f"no file at {audio}")
    fields = {"model_id": "scribe_v1", "timestamps_granularity": "word", "tag_audio_events": "false"}
    if a.language:
        fields["language_code"] = a.language
    edge = uuid.uuid4().hex
    body = b"".join(f'--{edge}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k, v in fields.items())
    kind = mimetypes.guess_type(audio.name)[0] or "application/octet-stream"
    body += f'--{edge}\r\nContent-Disposition: form-data; name="file"; filename="{audio.name}"\r\nContent-Type: {kind}\r\n\r\n'.encode()
    body += audio.read_bytes() + f"\r\n--{edge}--\r\n".encode()
    req = urllib.request.Request("https://api.elevenlabs.io/v1/speech-to-text", data=body, method="POST",
                                 headers={"xi-api-key": key, "Content-Type": f"multipart/form-data; boundary={edge}"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"speech-to-text failed: {e.code} {e.read()[:300].decode(errors='replace')}")
    words = [{"t": w["text"], "s": round(w["start"], 3), "e": round(w["end"], 3)} for w in data["words"] if w.get("type", "word") == "word"]
    Path(a.out).write_text(json.dumps(words, ensure_ascii=False, indent=0), encoding="utf8")
    sys.stdout.reconfigure(encoding="utf8")  # Windows consoles default to a code page without Arabic
    print(f"{len(words)} words to {a.out}")
    print(data.get("text", ""))


if __name__ == "__main__":
    main()
