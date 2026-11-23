# The working prototype

A real responsive app that the build team copies, kept beside the tokens (e.g. `design/app.html`) so relative paths work locally and when published as a multi-file artifact.

## Files

| File | Holds |
|---|---|
| `app.html` | Shell: meta, theme-color pair, inline pre-paint script (saved theme, language, motion), fonts, `tokens.css`, `base.css`, `app.css`, `<div id="app">`, `<script type="module" src="app.js">` |
| `app-data.js` | Sample data (real-looking, clearly sample), copy per language as functions for plurals and units, the icon set as SVG strings |
| `app.css` | Components and layout from tokens only; responsive tiers by width with real media queries |
| `app.js` | State, routing, screens as template functions, sheets, toasts, timers, events |

## Architecture

- **State** in one object saved to `localStorage` under a versioned key, every access in try/catch; transient per-screen state (`view`) reset on navigation.
- **Routing** as `{name, params}` rendered into `#app`; `go(name, params, dir)` wraps the commit in `document.startViewTransition` (skipped under reduced motion) and toggles `vt-forward` / `vt-back` classes on `<html>`.
- **Root attributes** set on every render: `lang`, `dir`, `data-theme` (absent for "system"), `data-motion="reduce"`, document title per screen.
- **Event delegation** with `data-act` attributes on `#app` and on the open sheet; native inputs fire `change` handlers; focus restored to the control after re-render.
- **Sheets** appended to `body`: scrim + `role="dialog" aria-modal`, `#app.inert = true`, focus into the sheet, Tab trap, Esc closes, closing animation then remove and return focus. Bottom sheet below 600 px, centred dialog above.
- **Toasts** with `role="status"`, one at a time, 4 s.
- **Motion** from tokens: press scale, `@starting-style` entrances, ring `stroke-dashoffset` from the last value seen (stored per ring), once-a-day brand moment flagged in state, milestone card with spring keyframes, a linear CSS timer animation paused with `animation-play-state`.
- **Timers** with `setInterval` once per second updating minute-level text, notices, and auto-finish; a demo "skip ahead" control inside the pause sheet for testing.
- **i18n**: `T()` returns the dictionary for the current language; numbers formatted with `Intl` and Latin digits where the market expects them; mixed-direction runs isolated on text nodes.

## Screens to cover

First visit (language, then a grouped choice with nothing preselected), Home, the main browse screen (grouped cards, master-detail on large screens), search and filters (sheet on phone, side panel on desktop), the core task screen (content, reveal, self-marking, feedback with Undo, next), any timed mode (start, pause once, finish and leave with confirmation), progress and settings (language, section, theme, motion, goal), share.

## Testing it

Serve the folder (`.claude/launch.json` with `python -m http.server`), then drive it with `javascript_tool` clicks and the checks in `checks.md`. Wait for view transitions (or poll for the next screen's element) before asserting; clear `localStorage` to test first visit.
