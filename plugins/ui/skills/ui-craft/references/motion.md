# Motion and animation

## Three jobs, nothing else

1. **Confirm** a tap within 100 ms (press scale + colour, 80 ms).
2. **Show where a change came from** (content fades up from where it appears; a ring fills from the value the user last saw; a sheet slides from the edge it was summoned from; a shared element moves between views).
3. **Mark a rare earned moment** (a milestone, a topic reaching "strong", the day's first study session). Rare and true: decoration hurts recall (seductive-details meta-analyses), and Duolingo's measured streak gains came from rule changes, not animation.

## Tokens

| Token | Value | Use |
|---|---|---|
| instant | 80 ms | press, hover, focus, colour |
| fast | 140 ms | exits, cross-fades, mark fill, top-level tab fade; the only duration kept under reduced motion |
| base | 220 ms | small entrances: reveal, toast, desktop dialog, drill-in slide |
| slow | 360 ms | bottom sheet, ring fill, glow |
| celebrate | 700 ms | rare blooms only |
| standard / enter / exit | `cubic-bezier(0.2,0,0,1)` / `(0,0,0,1)` / `(0.3,0,1,1)` | Material 3 web values; exits shorter than entrances |
| springs | `linear()` samples of Apple's damped spring (gentle 0.35 s bounce 0.15; pop 0.30 s bounce 0.30; milestone 0.40 s bounce 0.35), bezier fallback in `@supports` | only for things that physically arrive (a flame, a star, a badge); colour and opacity always use beziers |
| distance | 8 px / 16 px, 0 under reduced motion | entrance and drill-in offsets |
| `--dir` | 1, -1 in RTL | multiply every `translateX` |

Five design systems (Material 3, Carbon, Fluent, Atlassian, Polaris) converge on 50-150 ms for interactions and 150-400 ms for transitions; NN/g: 500 ms+ "feels like a drag". The more often something happens, the shorter and subtler it should be.

## Good moments (calm, learning product)

Press feedback; identical fill for every answer choice (different motion for right and wrong biases honest self-marking); content reveal; ring fill from last seen value (drops quiet, with the reason in text); a star popping once at mastery; a brand mark lighting once a day (grey to lit, like Sweatcoin's flame); an inline milestone card (never full-screen), tap to dismiss, once ever; sheets; a linear timer bar driven by one CSS animation with minute-level text; cross-fade between top-level tabs, short slide when drilling in.

## Never

Confetti, full-screen celebrations, mascots; looping or flickering flames (Apple: avoid sustained oscillation); shake or red flash on wrong; celebrating a drop; shimmer skeletons (static placeholder after 400 ms instead); spinners under 400 ms; ticking seconds or red timers; parallax, scroll-jacking, scroll-triggered reveals; sliding between top-level tabs; staggered lists on every visit; animated `box-shadow`, `blur`, `backdrop-filter`; sound by default; Lottie (56-75 kB) or Rive (78 kB WASM) when CSS does it at 0 kB; anything the user must wait for before tapping.

## Reduced motion: reduce, not remove

WCAG 2.3.3 treats colour and opacity changes as non-motion. Under `prefers-reduced-motion: reduce` or an in-app setting (`<html data-motion="reduce">`): distances 0, durations down to 140 ms, keyframe animations off, components skip scale, rotate and ring sweeps, fades kept. A blanket `* { transition-duration: 0.01ms !important }` removes the fade that confirms an action: don't.

## Implementation (web, 2026)

- Animate only `transform` and `opacity` (plus small SVG stroke and colour). `@starting-style` and `transition-behavior: allow-discrete` for entrances from `display: none`.
- Routes: View Transitions API (`document.startViewTransition`; React 19.3 `<ViewTransition>` only inside `startTransition`), direction classes for forward/back, keyframes gated behind `prefers-reduced-motion: no-preference`. Browsers without it just update.
- No animation library unless gestures demand one (Motion: about 5 kB + 24 kB lazy).
- Rings: `stroke-dashoffset` transition; count-ups only with the final value in text and the ticking copy `aria-hidden`.
- Low-end Android: never animate shadows (fade a pre-shadowed pseudo-element), avoid blur, limit simultaneous animations.
- RTL: straight-line motion mirrors (`--dir`, `transform-origin` flips); clockwise rings, clocks and checks do not.
