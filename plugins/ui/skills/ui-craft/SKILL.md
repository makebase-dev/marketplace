---
name: ui-craft
description: "Design and refine interfaces that feel calm, clear and finished: visual hierarchy of components, dark themes that are comfortable at night, colour and contrast, icons (recognition over recall), motion and animation, right-to-left and multilingual UI, and light gamification for learners. Use when designing or polishing a screen or component, choosing a palette or dark theme, adding icons or animation, building for Arabic or other RTL languages, when a page looks generated or generic, or when a design 'feels off' and needs another pass."
---

# UI craft

Lessons from building a dark-first, trilingual (EN/FR/AR) study product through research, seven blind audit rounds and several taste rounds with its owner. Use with `ui-audit` (which checks a design against WCAG and UX laws); this skill says how to make the design good in the first place.

## Read for the task

| Task | Read |
|---|---|
| A component or card feels busy, flat or unclear | `references/hierarchy.md` |
| Choosing colours, building or fixing a dark theme | `references/dark-theme.md` |
| Adding icons or deciding icon vs text | `references/icons.md` |
| Adding animation, transitions or celebrations | `references/motion.md` |
| Arabic, Hebrew or any mixed-direction or multilingual UI | `references/rtl-i18n.md` |
| Streaks, progress, badges, points, timers | `references/gamification.md` |
| A marketing page, landing page or hero, or a design that looks generated or generic | `references/generated-look.md` |
| Running review rounds, or taking design feedback | `references/review-loop.md` |
| Final check before calling a screen done | `references/defects.md` |

## Rules that held up every time

1. **One hero per component.** The thing the user came for (an exercise's own title, a single number) is the only large text; identity and state sit on one quiet line, context on another.
2. **Show exceptions, not defaults.** If 90 % of rows are "in scope", badge only the 10 % that are not. A badge on every row is noise.
3. **Space groups, line rows.** Space between groups about twice the space inside them; separate siblings with hairlines inside one card; put a group's heading outside and above its card, a size step larger than its children.
4. **The simplest version first.** One number, one bar, one line beats a legend, a grid of dots or four colour-coded levels. When the owner says "worse", go simpler, not cleverer.
5. **Dark themes are nearly neutral.** Background OKLCH L about 18-22 with chroma 0.02 or less; text off-white near L 91, never pure white; elevation by lightness; colour only on small marks.
6. **Fills are not text colours.** A colour that works as a fill or icon (3:1) often fails as text (4.5:1); keep a separate text token.
7. **Never colour alone.** Every state has a shape or word as well: icon + word on statuses, a ring outline for "today", a 2 px edge and bold label for "selected".
8. **Icon + word by default.** Icon alone only for universal controls (back, close, more, bookmark, pause) with an accessible name. One icon, one meaning, everywhere.
9. **Motion has three jobs:** confirm a tap within 100 ms, show where a change came from, mark a rare earned moment. Nothing loops; nothing makes the user wait.
10. **Reduce, not remove.** Under reduced motion drop all movement but keep fades of 140 ms or less, and offer an in-app switch.
11. **Isolate mixed-direction text on text nodes**, never by regex over HTML; Arabic never below 15 px; page arrows follow the content's language.
12. **Encourage, don't add a system.** Every game element is a side effect of the one action users already take; plain words and real units, no currency, no ranks.
13. **Every count says its unit and the numbers add up.** "7 of 12 exercises", and a breakdown that sums to the total.
14. **Blind review rounds find what you can't.** A fresh reviewer each round, given the files but not the earlier findings, fixed before the next round; five to seven rounds before quality plateaus.

## Related skills

- `ui-audit`: WCAG 2.2 AA and UX-law audit of what you built.
- `ui-prototype`: the full path from an idea to a working, reviewed prototype; it uses this skill at each design step.
