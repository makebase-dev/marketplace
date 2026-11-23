# Motion checks

Run when the page animates anything.

| Check | Pass | Criterion |
|---|---|---|
| Reduced motion | With `prefers-reduced-motion: reduce` (and any in-app setting) all movement stops (slides, scales, zooms, parallax, ring sweeps); short fades of about 140 ms or less may stay | 2.3.3 (AAA), vestibular safety |
| Not over-removed | Reduced motion still shows a fade or colour change confirming an action | UX |
| Auto-playing motion | Anything that moves for more than 5 s beside other content can be paused, stopped or hidden; no loops in the reading area | 2.2.2 |
| Flashing | No more than 3 flashes a second | 2.3.1 |
| Durations | Feedback within about 100 ms; transitions about 150-400 ms; nothing at 500 ms+ on frequent actions; exits shorter than entrances | UX (NN/g, design systems) |
| No waiting | The user never waits for an animation before acting | UX (Apple HIG) |
| Purpose | Each animation confirms an action, shows where something came from, or marks a rare earned moment; decoration removed | UX |
| Fair feedback | Equal motion for equal choices (e.g. right and wrong answers); no shake or red flash for mistakes in learning products | UX |
| Celebrations | Proportional and rare; no confetti or full-screen interruptions on routine events | UX |
| Timers | Calm; no ticking seconds, pulsing or red; can be shown as text or hidden | UX, anxiety |
| Loading | No spinner or skeleton for loads under about 400 ms; static placeholders preferred over shimmer | UX |
| Performance | Only `transform` and `opacity` animate (plus small SVG strokes); no animated shadows, blur or `backdrop-filter` | Performance |
| RTL | Straight-line motion mirrors; circular motion does not | 1.3.2 |
