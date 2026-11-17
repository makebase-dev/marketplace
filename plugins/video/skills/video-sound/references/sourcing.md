# Finding sounds

Free first. Paying is the last resort.

## Sources

| Source | Use | Credit | Notes |
|---|---|---|---|
| **Freesound CC0** | The main source | None | Filter by licence. Search and 128 kbps previews need no account; originals need a sign-in |
| Freesound CC-BY | Only when no CC0 fits | Credit line needed | Never NC or Sampling+ |
| Sonniss GDC bundles | Very good quality | None | Large downloads, no redistribution |
| Pixabay, Mixkit | Fine by licence | None | Pixabay refuses scripts; a person has to download |
| ElevenLabs sound-effects library | Paid plans cover commercial use | None | Its short samples are 1 to 3 s |
| ElevenLabs Music API, instrumental | Long held pads only | None | Risers came back as orchestral music, so reversed real cymbals beat them |
| Openverse | An index over Freesound and others | Depends on the source | Its API was often slow or down |
| Your own recording | The best ambience of all | None | 2 minutes at the place, on a calm day |

Not usable: BBC Sound Effects on social media, YouTube Audio Library outside YouTube, anything marked non-commercial, and AI models with non-commercial weights. Check the licence on the sound's own page, not in a search result. Treat a non-profit project as commercial use.

## Searching well

- Search by what the sound is ("stone block scrape", "handling paper foley"), not its use ("cinematic").
- Risers: reversed cymbals are the reliable real ones.
- Keep `candidates.json` with URL, author, licence and duration for each download. Keep each role in its own folder.
- Long ambience: let `earshot find` pick the best stretch. Listen for voices and dogs in the part you use.
- Prefer ambience from the region of the film. If none fits, say so to the owner.

## Getting originals from Freesound

Previews are 128 kbps MP3: fine for drafts, not for the final. The owner signs in. Never type a password or create an account for them.

- Download link: `/people/<user>/sounds/<id>/download/<file name>`, shown on each sound's page.
- Chrome blocks a site that downloads many files in a row. Ask the owner to allow automatic downloads for freesound.org.
- Trigger one at a time and wait for each file. Fired together, most are dropped.
- Save as `sfx-originals/<id>.<ext>`.
- Originals can start at a different point from previews. Align by cross-correlation against the preview before swapping, and keep every cue at its approved level. Then compare the new master with the approved one: same loudness, and every cue within 0.5 dB.

## Generated sounds

Use them only for what no recording offers. Keep prompts literal, with no "cinematic" or "braam". Run them through `earshot realness`: a low score means listeners may hear a synthetic sound too.
