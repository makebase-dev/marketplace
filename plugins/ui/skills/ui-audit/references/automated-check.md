# Automated check

A rule engine catches the mechanical failures quickly, so it runs before the
manual work. It never proves conformance on its own.

## Pick the engine

1. The project already has one (axe in Playwright or Storybook, Lighthouse in
   CI, pa11y): use it.
2. It has none: ask the user, with your recommendation, whether to add
   `@axe-core/playwright` as a dev dependency.
3. They say no, or there is no package setup: the scripted check in
   `page-check.md` is the automated pass. Call it "scripted page check" in the
   report, never axe or Lighthouse.
4. No browser tools at all (`browser.md`): write "automated check: not run"
   and go straight to the manual checks you can do from the screenshot or code.

Do not load a checker from a CDN or any other remote URL into the page.

## Configure it

- **axe-core:** pass the tags `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` and
  `wcag22aa` together, so the run covers every A and AA rule from 2.0 to 2.2.
  The untagged default set mixes in best-practice rules; do not use it.
- **Lighthouse:** run the accessibility category unchanged. Do not enable
  extra or experimental audits.
- Any other engine: limit it to WCAG 2.x A and AA rules.

## Run it

- Load the state with believable data, not an empty shell, and let
  animations settle.
- One run per state per theme, at a single viewport from `auditing.md`
  "Viewports and themes". Running every viewport repeats the same DOM.
- Resize to 320 px wide, and to 256 px tall, and look at reflow there; rule
  engines do not judge it.
- Do not re-run a screen that has not changed since the last run.

## Read the results

| Engine says | Treat as | Action |
|---|---|---|
| axe `violations`, Lighthouse failed audit | Fail | A finding, with the criterion the rule maps to |
| axe `incomplete` ("needs review") | Unknown | Move it to the manual checks; it becomes a finding only if that check fails |
| axe `passes` | Pass | None |
| axe `inapplicable` | Not present | None |

- Drop any result that maps to no WCAG success criterion (best-practice,
  experimental). Every finding in the report cites a criterion.
- Start from the engine's impact (critical, serious, moderate, minor) as the
  severity. Raise or lower it only when this app's context makes it wrong, and
  give the reason in the finding.

## What it cannot tell you

- A clean run means "no detectable failures", not "meets WCAG". Never write
  it up as conformance.
- It misses states it never saw (open menus, errors, empty lists), whole
  journeys, focus order, keyboard behaviour and most of reading order. Those
  are in `manual-checks.md`.
