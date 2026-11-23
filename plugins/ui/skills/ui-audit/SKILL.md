---
name: ui-audit
description: "Audit web UI for accessibility (WCAG 2.2 AA) and usability (UX laws such as Fitts, Hick, proximity), from a live page, a screenshot or code: pages, flows and single components, dark themes, right-to-left pages, motion, and content consistency, including blind repeated review rounds. Use when reviewing a page, screen, component or flow, or when checking a new screen against the laws."
---

# UI audit

## Read for the task

Several rows usually match; read all of them.

| Task | Read |
|---|---|
| Accessibility audit of a rendered page or component | `references/auditing.md`, `references/automated-check.md`, `references/manual-checks.md` and `references/wcag22-aa.md` |
| UX audit of a screen, page, flow or component | `references/ux-laws.md` and `references/ux-audit.md` |
| Designing a new screen, page, flow or component | `references/ux-laws.md` and `references/designing-screens.md` |
| Opening the page, screenshots, or auditing without a browser | `references/browser.md` |
| Any rendered audit (always, with or without an automated checker) | `references/page-check.md` |
| Auditing components rather than whole pages | `references/component-audit.md` |
| The page has a dark theme | `references/dark-theme-checks.md` |
| The page is offered in a right-to-left language, or mixes languages | `references/rtl-checks.md` |
| The page animates anything | `references/motion-checks.md` |
| Any UX audit (data, wording, docs drift, persuasive design) | `references/consistency.md` |
| The user asks for blind, independent or repeated reviews, or after applying fixes | `references/review-rounds.md` |
| Reviewing UI code, such as a diff, without rendering it | The `web-ui` skill when it is installed: each build reference whose row matches what the code changes. Otherwise `references/wcag22-aa.md` and `references/browser.md` "Without browser tools". Report each rule the code breaks as a finding |

- When asked for "an audit" with no kind named, run both the accessibility
  audit and the UX audit, and report them separately.
- Run `references/page-check.md` on every rendered state, theme and direction; it is the automated pass when the project has no checker.
- After applying fixes, verify them and look for regressions as `references/review-rounds.md` says.
- For page speed and Core Web Vitals, use the `web-testing` skill when it is
  installed. Otherwise say they were not checked.

## Before you start

- When a repo is open, read its CLAUDE.md or README for its run commands,
  design tokens, theme files and component library.
- With no repo and no browser tools, such as in a chat, audit the screenshot
  or code you were given, as `references/browser.md` "Without browser tools"
  says.
- Find the screen's primary task: who uses it and what counts as done.
- Use local, staging or a preview URL. Never submit a form or place an order
  on a production site.

## What wins

1. Accessibility: WCAG 2.2 AA, as `references/wcag22-aa.md` describes. No
   source below lowers it.
2. The user's own words about the design.
3. The project's `architecture-docs/cross-cutting/design-system.md` and the
   feature's `experience.md`, when the repo has them, then its design tokens,
   theme files and component library.
4. The patterns already in the code: layout, naming and styling.
5. The UX laws in `references/ux-laws.md`.

## Always

- Prefer the built-in HTML element (`button`, `select`, `input type="date"`,
  checkbox, `dialog`) over ARIA on a `div` or a hand-built control.
- Fix within the existing design system. Never invent new styles, colours or
  spacing values.
- For a right-to-left page, check the layout mirrored: reading order,
  navigation placement, icons that point a direction, and list emphasis start
  from the right.
- When asked only to audit, report findings and change no code. Apply fixes
  only when the user asks, highest severity first.

## Stop and ask

Ask the user, with your recommendation, when:

- The project has no design tokens or theme and the change needs new ones.
- A fix would change a shared component that other screens use.
- The screen's primary task is unclear.

## Output

| Work | Return |
|---|---|
| Accessibility audit | The accessibility report in `references/auditing.md` |
| UX audit | The report in `references/ux-audit.md` |
| Design | The design and its self-check, as `references/designing-screens.md` describes |

- Name the path of every screenshot you saved.
- List every check marked "not checked" or "not run".

## Related skills

- `ui-craft`: how to design it well (hierarchy, dark themes, icons, motion, RTL, gamification). This skill checks; that one creates.
- `ui-prototype`: the whole path from an idea to a reviewed working prototype; it calls this skill for every review round.
- `web-ui` (when installed): the visual direction and the UI code: components, state, styling, forms, React and Storybook stories. Its build references are the rules a UI code review checks.
