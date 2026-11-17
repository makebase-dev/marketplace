# Agreeing the sound with the owner

The hardest part of sound is not mixing. It is reaching a decision with someone who hears and a tool that cannot. This is the method that worked, after two that did not.

## What failed

- **Inventing cues.** Rejected at once: the owner could tell, and there was no way to check them.
- **An audition sheet.** 27 sounds, played alone, numbered, one pick per role. The owner called it very hard, and it was: nobody can judge a stone hit without the shot it belongs to.
- **Applying every audit finding.** A blind audit measured thin ambience, so a soft wind went under the whole film. Every number improved. The owner heard noise.

## What worked

1. **Recommend a full set.** Pick for each role yourself, with a reason, and say what you picked.
2. **Put it in the video.** One watch. Ask only for what bothers them, with the second: "27 s, the hit is too much".
3. **Offer comparison clips for the moments that matter.** Five at most: usually the ambience, the turn, the key word, a photo moment and the ending. Each plays the same 6 seconds three times with a big 1, 2, 3 on screen, and 1 is your pick. The reply is "37 s → 2".
4. **Change only what was named.** Notes are specific. Keep the rest.
5. **When they prefer an older version, start from it.** "A middle ground" means: the version they liked as the base, plus only the discrete additions they missed. Check by numbers that the base character returned: pause loudness and high-frequency energy near the old version.

## Comparison clips

```
python mix.py sound/sound.json --out build/opt1
python mix.py sound/sound.json --out build/opt2 --set hit_end=sfx/hit_b.wav
python compare.py --picture out/draft.mp4 --from 34.6 --len 6 --mix build/opt1/mix_master.wav build/opt2/mix_master.wav --out compare/37s-name.mp4
```

## Being honest in each handoff

- Say that nobody has listened to it; you only measured.
- Name the one or two spots to listen to first, and why.
- List what changed from the last version, and what you chose to leave silent.
- Flag doubts: wrong region, a religious association, a sound that may read as a voice.
- Say what is still a preview.

## Blind sound audits

Give a fresh agent the file, the script, the audience and the bar, and let it use ffmpeg and earshot. Its findings on timing, masking, holes and cheap sounds are useful. Treat its loudness targets for ambience as questions for the owner, not as fixes. Show the owner the list, recommend, and let them choose. Keep the version before you apply it.
