# Dark themes that are comfortable

## The numbers (from Material, Apple, Fluent, APCA, app palettes and human-factors research)

| Element | Target | Why |
|---|---|---|
| Background | OKLCH L 18-22, chroma 0.02 or less (e.g. `#15141D`, `#121212`) | Mainstream dark themes keep neutral chroma at 0-0.03. A brand-tinted night (chroma 0.05) felt uncomfortable to the owner and is 4x Material's violet baseline |
| Surfaces | +2 to +5 L per level (bg 19.7 → card 22.8 → raised 26.3) | Elevation by lightness; shadows barely show on dark |
| Borders | about +13 L over the background for dividers; control edges 3:1 on every surface, sheets included | Dark sheets (raised surface) are where control edges fail first |
| Body text | L 88-91, chroma ≤0.012 (e.g. `#E1E0E9`), about 14:1 | Pure white on dark crosses APCA's Lc 90 halation ceiling; about 40 % of adults and 15 % of children have astigmatism |
| Secondary text | L 66-83 | |
| Accent | Pastel (chroma about 0.10, L about 80) on small elements: one button, rings, icons | Saturated colours vibrate on dark; red is the most tiring text colour, yellow the least |
| Brand "lamp" colour | Only on one or two marks per screen | Colour everywhere means colour nowhere |
| True black | Avoid | Saves about 0.3 % more power than dark grey on OLED and smears when scrolling |

## Rules

1. Every colour is a token; no hex in components. Lint for it.
2. Every foreground/background pair the components use is listed in a contrast script and checked in both themes on every change (4.5:1 text, 3:1 large text, icons, control edges, focus). Add the pair before you use it: rings on their track, borders on raised surfaces, status text on hover surfaces, ink on paper.
3. Keep a separate text token for any colour used as a fill (an amber that passes 3:1 as a flame fails 4.5:1 as "+10").
4. Status colours never change meaning between themes; "out of scope" is neutral grey, never red.
5. Soft fills with strong text for badges (dark tint + pastel text), not bright fills with white text.
6. Selected states need more than a soft fill (accent-soft on surface is about 1.2:1): add a 1.5 px accent edge and bold label.
7. Progress steps that must be told apart differ in lightness, not hue alone.
8. Focus ring in the text colour (not the brand accent or a status colour), 2 px with 2 px offset.
9. `color-scheme` on the root so native controls and scrollbars follow; two `<meta name="theme-color">` entries; an inline script in `<head>` applies the saved theme before first paint.
10. Documents and PDFs stay paper: show white pages dimmed (`filter: brightness(.88)`) on a dark well; inversion is an opt-in "night paper" toggle, never default (it breaks graphs and coloured marks).
11. Let the user choose: follow the OS by default, offer Light / Dark / Same as device. Light text on dark is read less accurately at small sizes and at night (Piepenbrock, Dobres), so keep the light theme first-class. Never claim dark mode improves sleep.
12. Typography on dark: keep regular weights (light text looks bolder), generous size and line height (1.5-1.6); cut glare with text colour, not thinner strokes.

## Retuning an existing palette

1. Convert every neutral to OKLCH; cap background, surface and muted-text chroma at about 0.02-0.025, keep the hue.
2. Keep the lightness ramp if it already steps 2-5 L.
3. Drop primary text to L about 91; secondary to about 78.
4. Re-run the contrast script; fix borders on raised surfaces and fills used as text first.
5. Look at the real screens in both themes and both languages before calling it done.
