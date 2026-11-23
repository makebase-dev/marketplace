# Consistency and content checks

Review rounds repeatedly found these; check them in every UX audit.

## Data shown

- [ ] Every count has its unit ("7 of 12 exercises", not "7 of 12").
- [ ] Breakdowns add up to the total they explain.
- [ ] The same item shows the same labels and status on every screen.
- [ ] Previews reflect their own controls (a toggle that is off is not shown in the preview).
- [ ] Sample data is internally consistent (a streak of 12 matches the calendar it sits on).

## Language

- [ ] One word per concept across the product (not "scope" on one screen and "program" on another).
- [ ] Headings and legends match the controls they label ("How did it go?" in both the heading and the group name).
- [ ] Settings are where users look for them (language reachable in one or two taps from anywhere).

## Docs, tokens and implementation

When the project has design docs or tokens, compare them with what is rendered:

- [ ] Sizes, breakpoints, durations and colours in the docs match the tokens and the page.
- [ ] Components described in the docs exist in the page with the described states, and vice versa.
- [ ] Rules in the docs (e.g. "one accent per screen", "badge only exceptions") hold on every screen.

Report drift as a Minor UX finding, with the file and line to change.

## Persuasive design (products for minors, learners or health)

- [ ] No leaderboards or public ranks, no hearts or lives, no guilt notifications, no countdown to losing a streak.
- [ ] Streaks forgive missed days; progress that drops shows its reason.
- [ ] Rewards tie to learning or real progress, not time on site; no random rewards.
- [ ] Timers and countdowns are optional or calm, and say plainly when a date is unknown or cancelled.
