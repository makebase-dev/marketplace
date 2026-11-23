# UX audit

## Steps

1. Gather the design: read the code or markup, view the screenshot, or render
   the page. When you can render it, check it at the project's Storybook
   viewports, or at 390 px and 1280 px wide when it has none.
2. Write each screen's primary task in one sentence. Audit against it.
3. Walk the checklist below against the rules in `ux-laws.md`. Note each
   finding with its location.
4. Rate each finding with the severity table below.
5. Write the report, sorted by severity.
6. Apply fixes only when the user asks, highest severity first, within
   the existing design system.

## Severity

| Severity | The finding |
|---|---|
| Critical | Blocks the main task, or misleads users about it |
| Major | Causes noticeable friction, errors or confusion |
| Minor | A polish or consistency problem |

- This scale is for UX findings only. Rate accessibility findings as
  `auditing.md` describes.

## Checklist

- One clear first read and one obvious primary action per view; in each component, one hero (the item's own name or one number), with codes and identifiers kept out of it (`component-audit.md`).
- Default states quiet, exceptions emphasised; a badge on every row is noise.
- Groupings make sense: space inside a group smaller than between groups;
  cards and regions used the same way throughout.
- Same-function elements look the same; different-function ones look
  different.
- A reasonable number of choices at each decision point, with a recommended
  or default option marked.
- Information chunked; nothing makes users memorise values across screens.
- Labels visible and persistent, never placeholder-only. Options shown rather
  than recalled.
- The most important items at the start and end of lists and navigation.
- Advanced options tucked away; nothing needed for the main task hidden.
- Targets large enough and spaced; primary actions within easy reach;
  destructive actions separated.
- Common patterns used for navigation, forms and icons.
- Inputs forgiving of format, whitespace, case and digit script; data filled
  in or inferred where possible.
- No element, field or step that could be removed.
- Fast responses, or loading and progress shown; skeletons for content loads.
- Every state present: hover, focus, active, disabled, loading, empty, error,
  success.
- Errors say what happened and how to fix it, next to the cause.
- Multi-step flows show progress.
- The success state has a clear confirmation and next step.
- Visual polish consistent: spacing scale, alignment, radii, type scale.
- Right-to-left pages mirrored, as `ux-laws.md` describes.
- Counts have units, breakdowns add up, one word per concept, docs match the page (`consistency.md`).
- No pressure patterns in products for minors or learners (`consistency.md`, persuasive design).
- Motion has a purpose and respects reduced motion (`motion-checks.md`).
- Accessibility basics: contrast, visible focus, no colour-only signals,
  keyboard reachable. For pass or fail on these, run the accessibility audit.

## Report

1. A summary of 2 to 3 sentences and the top 3 fixes.
2. The strengths, in a few bullets.
3. Each finding in this format:

```
[Major] Delete sits next to Save
Law: Fitts's law
Where: Product edit form, src/pages/ProductEdit.tsx:88
Issue: Users can delete a product when they mean to save it.
Fix: Move Delete into the overflow menu, and add 24 px between the buttons.
```

4. A short list of actions, in priority order.
