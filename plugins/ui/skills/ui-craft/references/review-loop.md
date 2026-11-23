# Review loops and taking feedback

## Blind audit rounds

The single most productive habit. Each round:

1. Spawn a **fresh** reviewer agent. Give it the files, the audience and the owner's goals, and tell it to run `ui-audit` (accessibility and UX). Do **not** give it earlier findings: an anchored reviewer confirms your view.
2. Ask for findings ranked by severity with where / observed / criterion / fix, plus what it could not check, under about 900 words.
3. Fix everything that holds up, verify in the browser (both themes, both directions, phone and desktop), commit.
4. Only then start the next round.

What rounds found, in order of discovery (expect the same shape):

| Round | Typical finds |
|---|---|
| 1-2 | Real WCAG failures: broken accessible names, invisible rows (0 px flex children), keyboard-unreachable custom controls, colour-only states, fixes that themselves introduced bugs |
| 3-4 | Consistency: the same thing named five ways, counts that don't add up, the same item with two labels, docs vs prototype drift, too much accent colour |
| 5-7 | Hierarchy and space: crowded bars, cards with no hero, empty desktop space, legibility of documents at real scale, mirroring of controls inside other-direction content |

Five to seven rounds before findings become minor. Then switch to a **component-level** pass (role, hierarchy, information load, icon vs text per component).

## Taking the owner's taste feedback

- When they say "not clear" or "worse", go **simpler**, not more clever: remove a tier, a legend, a decoration. The 22-dots summary was worse than a bar; the bar plus one line was right.
- When they point at a screenshot, fix the whole pattern (all three card types), not only the instance.
- When they approve a direction ("dark is much better"), record the rule and the numbers in the docs so it survives.
- Say what you will not do and why when a request conflicts with evidence (e.g. confetti), and offer the calmer alternative.

## Verification habits

- Re-run a scripted DOM check after every change: broken attributes (`<` or `>` in any attribute), leaked template text (`${`, `undefined`, `NaN`), text contrast of every text node against its effective background, target sizes, `h1` per screen, overflow per scroll container, `<bdi>` count in RTL.
- Screenshot after view transitions finish, not during (cross-fades look like bugs).
- Check at 375, 820, 1280 (and 1920 for side-by-side reading) in dark/light × each language.
