# Manual checks

These decide the criteria a rule engine cannot. Do as many as the browser
tools in `browser.md` allow; for each one they cannot do, give the user the
steps and the screenshots, and mark it "left to the user".

The accessibility tree is your stand-in for a screen reader: it shows the
name, role, state and value each control announces. It is not a substitute
for listening to one, so screen reader listening always goes on the user's
list.

Do these six every time, even after a clean automated run: keyboard, focus,
reflow, reading order, error and status messages, and widget behaviour.

## Keyboard and widget behaviour

*2.1.1, 2.1.2, 2.4.3*

- For each custom widget, look up its pattern in the WAI-ARIA Authoring
  Practices (menu button, tabs, combobox, disclosure, dialog, listbox) and
  note the keys it promises.
- Drive the widget with those keys, then with `Tab` and `Shift+Tab`. After
  each key, read the tree to see what has focus and what state changed.
- Do each journey the change touches without the mouse, start to finish.
- A finding is any key from the pattern that is missing or does something
  else, any place focus cannot leave, and any jump in tab order that breaks
  the task.
- An ARIA role that promises keys it does not handle is a defect, even when
  the mouse works.
- Dialogs: opening moves focus inside; tabbing cycles within it; `Escape`
  closes it; focus returns to the control that opened it.
- Right-to-left: in horizontal widgets (tabs, sliders, carousels) the arrow
  keys follow the visual direction, so Right arrow moves toward the start.

## Focus

*2.4.7, 2.4.11*

- Tab through the screen and take a screenshot at each stop.
- Each stop needs a visible indicator (2.4.7) and must not be fully covered
  by a sticky header, bottom bar, cookie banner, chat bubble or toast (2.4.11).
- Repeat at the narrowest viewport, where fixed bars cover the most.

## Reflow

*1.4.10*

- Set the viewport to the reflow sizes in `wcag22-aa.md`.
- Fail it when content or a function disappears, or the page scrolls on both
  axes, unless the content is one of the exempt kinds listed there.
- Name the element that overflows (often a long URL, a fixed-width table or
  an image) rather than "the page".

## Target size

*2.5.8*

- Measure the bounding box of each pointer target the change adds or
  touches, using the page's own geometry.
- Grade it with the 24 px rule and its exceptions in `wcag22-aa.md`; ignore
  the figures tools and platform guides print.
- For an undersized target, either name the exception that saves it or
  report it.

## Contrast

*1.4.3, 1.4.11*

- Start from what the browser or checker already flagged.
- Then measure what they skip: placeholder and helper text, input borders,
  focus rings, toggle and checkbox states, icons that carry meaning, chart
  lines. Use the numbers in `wcag22-aa.md`.
- Repeat in every theme the app offers.
- Text over a photo, video or gradient has no single background colour, so a
  computed ratio is unreliable. Screenshot it and list it for review.
- File a contrast failure against the design token that produces the colour,
  so the fix lands everywhere the token is used.

## Forms, errors and status

*3.3.1, 3.3.2, 3.3.7, 4.1.2, 4.1.3*

- Submit each form blank, then with a single bad field. Submit valid data
  only on local, staging or a preview build; on production, list the forms
  and ask before sending anything.
- After each attempt, check in the tree that each field has a name, role,
  value and invalid state, that the error is written in words and tied to its
  field, and that the result is announced without moving focus.
- A placeholder used as the only label fails 3.3.2. An error shown only as
  red or an icon fails 3.3.1.
- Walk the confirmation, retry and failure screens of the journey, and check
  that data entered on an earlier step is not asked for again (3.3.7).

## Reading order

*1.3.2*

- Read the tree top to bottom and compare it with what the screen means
  visually, especially in grids, cards and mixed-direction text.
