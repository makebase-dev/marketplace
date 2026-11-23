# Independent and repeated reviews

## Blind rounds

An auditor who knows the earlier findings tends to confirm them. When the user asks for a "blind", "independent" or repeated review:

1. Run each round as a fresh agent. Give it the files, the audience and the owner's goals, a unique local server port, and this skill. Do not give it earlier findings or your conclusions.
2. Ask for findings most severe first, with where, observed, criterion or law, and fix, plus what it could not check, in under about 900 words.
3. Fix what holds up, then verify (next section), then start the next round.

Expect the findings to move from WCAG failures (rounds 1-2) to consistency (3-4) to hierarchy and use of space (5-7). After that, switch to `component-audit.md`.

## Verify fixes and check for regressions

Fixes introduce new bugs (an isolation helper that rewrote attributes; a heading change that collapsed a layout). After applying fixes:

- Re-run `page-check.md` in every theme and direction on the changed screens.
- Re-test each fixed finding in the state where it was found.
- Look at the neighbouring components the fix touched.
- In the report, add a "Fixes verified" section: each finding, fixed or not, and any regression found.
