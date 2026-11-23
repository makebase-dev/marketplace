# Accessibility audit

The goal is a pass or fail against `wcag22-aa.md` for what is in scope, with
evidence for every finding and an honest list of what was not checked.

## Scope

- A change: the screens, states and stories it touches, and its acceptance
  cases.
- A full site: the pages the user names, or else the home page and one page
  of each template.
- Include the states users reach but demos skip: open menus, errors, empty
  and loading.

## Passes, in order

1. **Automated** (`automated-check.md`): once per state and theme.
2. **Scripted page check** (`page-check.md`): every time, on every state,
   theme and direction.
3. **Conditional checks**: `dark-theme-checks.md`, `rtl-checks.md` and
   `motion-checks.md` when the screen has a dark theme, a right-to-left
   language or animation.
4. **Console**: errors and warnings that appeared with this change.
5. **Design system**: the screen uses the project's tokens and components,
   and matches `architecture-docs/cross-cutting/design-system.md` and the
   feature's `experience.md` when those exist.
6. **Manual** (`manual-checks.md`): every check the tools can perform.
7. **Screenshots**: as "Viewports and themes" says.

Use the tools in `browser.md`. Where a tool cannot produce the evidence, say
so in the report instead of guessing. Leave the user only what tools cannot
do, such as listening with a screen reader or judging visual craft.

## Findings

Each finding states:

- where: view, state, viewport, theme, direction;
- the success criterion it fails;
- what you observed and what the criterion expects;
- the evidence: screenshot path, tree excerpt or measured value;
- the severity: **Critical** (blocks a task for some users), **Serious**
  (task possible only with real difficulty), **Moderate** (friction or
  confusion) or **Minor** (polish).

## Viewports and themes

Screenshots are for new screens, new components, layout changes and full
audits. Skip them for a fix that changes no layout.

Use the first of these that defines viewports and themes:

1. The project's Storybook configuration.
2. `architecture-docs/cross-cutting/design-system.md`.
3. Default: 375, 820, 1280 and 1920 px wide (phone, tablet upright, laptop,
   large desktop), in every theme the app has.

A site offered in both a left-to-right and a right-to-left language gets each
viewport in both directions. Keep screenshots in the session's scratchpad
directory; they never go into the repo.

## Accessibility report

Goes in the pull request description, or in your reply when there is no
pull request.

1. **Verdict.** `Result: pass` or `Result: fail` for the scope checked; which
   engine, its version and rule tags; how many screens, states and stories.
2. **Automated results.** One row per screen or component: states run,
   violations by impact, pass or fail.
3. **Criteria.** Every criterion from `wcag22-aa.md` that failed or that only
   a manual check could decide, and how it was decided.
4. **Findings.** As above, highest severity first, each with its fix.
5. **Left to the user.** Manual checks no tool could perform. They are
   listed, not counted against the verdict.
6. **Fix verification.** After a fix round, each earlier finding marked fixed
   or still open, plus any regression (`review-rounds.md`).
