# Icons: recognition over recall

Recognition over recall means the user sees the meaning; an icon on its own makes them remember it. So:

| Case | Use |
|---|---|
| Default | Icon + word. The icon speeds scanning once learned; the word teaches it |
| Universal controls (back, close, more ⋯, bookmark, pause, clear, zoom, page arrows) | Icon alone, with an `aria-label` from the same dictionary as the visible text |
| Status, scope, navigation tabs, streak or score | Never icon alone |

## Rules

1. **One icon, one meaning** across the product. Write the list down (check-circle = in scope, check = right, cross = wrong, half-circle = partly, circle-slash = out, bookmark = review later, empty circle = not tried, flame = streak, moon = rest day only, clock = time of day, gear = settings, star = mastery). Milestones and decorations get their own icons so they never borrow a status icon (a check on "Honest mark" — the first *wrong* answer — reads as "right").
2. **Reuse learned icons** in new places: the badge icons inside the filter chip that filters by them, the row's progress ring as the legend glyph.
3. **One set, one stroke.** Lucide (ISC licence) at 24 px, rendered 20 px, stroke 1.75, round caps, `currentColor`, inline SVG. Custom glyphs (brand mark, subjects) drawn on the same grid and stroke.
4. **Subject glyphs** sit beside the subject name: leaf Biology, flask Chemistry, atom Physics, sigma Maths, columns History, globe Geography, scales Civics, bulb Philosophy, people Sociology, coins Economics; letter tiles for languages (ع, Fr, En). Test them with real users.
5. **Brand mark states** (e.g. a lamp: unlit, lit with the flame filled, rest) carry meaning; animate only the change of state, never loop.
6. **Directional icons mirror in RTL** (back, chevrons, forward arrows) with `transform: scaleX(-1)` under `[dir="rtl"]`; checks, crosses, clocks, rings, media controls and logos do not. Inside content in another direction (an English PDF in an Arabic UI), page arrows follow the content.
7. Decorative icons get `aria-hidden="true"`; meaningful standalone icons get `role="img"` and a name; never both a name and visible text that disagree.
8. In SVG, `<text>` glyphs (letter tiles) need `fill="currentColor" stroke="none"`; never inject HTML (like `<bdi>`) inside SVG text.

## Before adding an icon, ask

- Would a 15-year-old name it correctly without the word? If not, keep the word.
- Is it already used for something else? Pick another.
- Does it point a direction? Decide mirror or not.
