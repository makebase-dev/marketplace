# Designing a new screen

1. Write the job in one sentence: who the user is, the single primary task on
   this screen, and what counts as done.
2. List every element the screen needs. Cut each one that does not serve the
   task. Move what most users do not need behind progressive disclosure.
3. Group the elements with proximity and common region. Order them with
   serial position and visual hierarchy. Start from common patterns.
4. Choose the one primary action. Size and place it as Fitts's law in
   `ux-laws.md` says.
5. Reduce effort on every input and choice with the "Choices and memory" and
   "Effort" rules in `ux-laws.md`.
6. Define every state of each component and of the page: default, hover,
   focus, active, disabled, loading, empty, error, success. Meet the Doherty
   threshold or show progress.
7. Design the ending: the success state, the confirmation and the next step.
8. For a right-to-left page, mirror the layout as `ux-laws.md` describes.
9. Use the project's design tokens, theme and components. Ask the user
   before adding a new token or a new shared component.
10. Run the checklist in `ux-audit.md` against your design and fix each
    finding.
11. Check the design against the criteria in `wcag22-aa.md` it can already
    fail, such as contrast, target size, labels and focus.

## Return

- The design: a wireframe or the code, as the user asked.
- The job sentence from the first step.
- The laws that drove the key decisions, one line each.
- The self-check findings you fixed, and any you left, with the reason.
