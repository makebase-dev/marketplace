# Defects to check before calling a screen done

Each of these shipped at least once and was caught by a review round.

## Layout

- [ ] A horizontally scrolling chip row inside a fixed-height flex column collapses to 0 px: give it `flex: none` and `padding-block` so focus rings are not clipped.
- [ ] Icon buttons shrink in crowded bars: `flex: none`.
- [ ] Titles truncated to an ellipsis next to many icon buttons: move secondary actions into a ⋯ menu, allow two lines.
- [ ] A centred floating pill with `dir="ltr"` plus an RTL `translateX(50%)` rule runs off screen.
- [ ] `aspect-ratio` children with percentage heights collapse: use `min-height` in `em`.
- [ ] A class name reused for two meanings (`.big` for a number and for a large screen) blows up type.
- [ ] Desktop frames with fixed widths make the review page itself overflow on phones.
- [ ] Content not capped (72 rem) on wide screens; empty halves on desktop.

## Semantics and accessibility

- [ ] Custom radio cards are `div role="radio"` without keyboard: use native inputs in a `fieldset`/`legend`.
- [ ] A radio-like toggle group is either native radios or toggle buttons, never `role="radio"` without arrow keys.
- [ ] Chips that open a menu carry `aria-haspopup`, not `aria-pressed`.
- [ ] Every screen has one `h1`; section labels are headings.
- [ ] Dialogs: `aria-modal`, focus moves in, Tab trapped, Esc closes, background `inert`, focus returns.
- [ ] Status messages (`role="status"`) for feedback; timers have `role="timer"` with a full-sentence name.
- [ ] Accessible name starts with the visible label; names localised.
- [ ] Decorative SVG `aria-hidden`; meaningful SVG `role="img"` + name.
- [ ] Disabled primary actions explain why ("Pick your section to start.").
- [ ] Nothing preselected where the default would send a minority user down the wrong path.

## Colour

- [ ] A selected/today marker drawn in the same colour as the fill under it (1:1).
- [ ] A fill colour used as text.
- [ ] Control edges on raised surfaces (sheets) below 3:1.
- [ ] Interactive chips in light mode styled with the card colour (invisible): outline them.
- [ ] Neighbouring progress levels differ by hue only.

## Content

- [ ] Counts without units; breakdowns that don't sum; the same item labelled differently on two screens; previews that ignore their own toggles.
- [ ] Docs, tokens and prototype disagree (sizes, breakpoints, labels): fix the docs in the same change.
- [ ] Two controls for one state (a bookmark and a "Later" button).
