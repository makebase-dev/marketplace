# earshot

[earshot](https://github.com/Leonxlnx/earshot) gives an agent a way to measure sound: what it is, how well it fits a description, when things happen. It runs on the CPU. It is good on single sounds, gives only hints inside a busy mix, and cannot judge taste. Judge source files and stems, not only the final mix.

## Commands in use

| Need | Command |
|---|---|
| Is the install healthy | `earshot doctor` |
| Rank candidates against a description | `earshot rank "a soft warm cinematic impact" sfx/impact/` |
| How well one file fits | `earshot match file.wav "heavy stone scrape"` |
| What does it sound like | `earshot describe file.wav` |
| Best stretch of a long recording | `earshot find long.wav "calm hillside, light wind, distant birds"` |
| Real recording or synthetic | `earshot realness sfx/` |
| Clicks, cut tails, clipping, DC offset | `earshot sfx check sfx/*.wav` |
| Listen through a film | `earshot timeline final.mp4` |
| An annotated picture of a soundtrack | `earshot sheet final.mp4` |
| A scorecard against launch films | `earshot critique final.mp4` |
| Compare two sounds | `earshot ab a.wav b.wav` |

## Reading the numbers

- `rank` z: compare within one role only. Above about +2.5 is a strong match.
- `realness` p_real: above 0.77 reads as a real or professional recording; under 0.17 as synthesised.
- Labels in a mix are hints with weak confidence. Check parts one by one before believing "phone buzz" on a combined window. Then ask the owner to listen there.
- Bird recordings often trigger "children laughing". It usually means chatter, but listen for voices.
- `critique` is built for music-led launch films. Its "no music" finding means nothing for a voice-led short.
- A "cheap" flag on an effect, such as a fast pitch rise at the start, is worth a listen, not an automatic reject.

## Things it cannot do

It will not tell you a mix feels noisy. One round measured better on every audit number and the owner rejected it as noise. Trust the owner over the meter.

Compare versions with numbers anyway, so you can tell what changed: non-voice loudness in pauses, and 2 to 10 kHz energy, which shows added hiss.

## Windows

Run it from PowerShell with ffmpeg on PATH. Models live in `~/.cache/earshot`.
