# WCAG 2.2 AA: what to test

This is the checklist an accessibility audit is graded against. The source is
the W3C recommendation, Web Content Accessibility Guidelines 2.2, levels A
and AA. When this list and the W3C text disagree, the W3C text wins.

## How to use the list

- Go through all four groups below for every screen in scope.
- Mark a row "not present" when the screen has nothing it could apply to (no
  video, no time limit, no drag).
- Content this list leaves out still counts. A screen with captions, audio,
  a timer, flashing or a second language also gets the W3C criteria for that
  content.
- Motion after a user action is AAA (2.3.3 Animation from Interactions). Test
  it with `motion-checks.md` and label those findings AAA so they never fail
  an AA verdict.
- "How" tells you where the evidence comes from: **auto** means the checker
  finds most failures and you confirm in the accessibility tree; **hand** means
  only a manual check (`manual-checks.md`) can decide it.

## Perceivable

| SC | Lvl | Passes when | How |
|---|---|---|---|
| 1.1.1 Non-text Content | A | Meaningful images, icons and image buttons expose a text equivalent; purely decorative ones are hidden from assistive tech | auto |
| 1.3.1 Info and Relationships | A | Headings, lists, tables, groups and label pairings that you can see also exist in the markup | auto |
| 1.3.2 Meaningful Sequence | A | The order a screen reader reads matches the visual meaning, including number ranges, fractions and Latin runs inside right-to-left text | hand |
| 1.4.1 Use of Color | A | Selected, current, error, today and progress states have a cue besides hue (text, icon, shape, underline) | hand |
| 1.4.3 Contrast (Minimum) | AA | Text meets the contrast numbers in "Numbers" | auto, then hand for images and gradients |
| 1.4.4 Resize Text | AA | At 200% browser zoom nothing is cut off and every control still works | hand |
| 1.4.10 Reflow | AA | The screen fits the reflow sizes in "Numbers" without two-way scrolling | hand |
| 1.4.11 Non-text Contrast | AA | Input borders, focus rings, state indicators and meaningful icons meet the non-text number | hand |
| 1.4.12 Text Spacing | AA | Overriding spacing to the values in "Numbers" clips or hides nothing | hand |
| 1.4.13 Content on Hover or Focus | AA | Tooltips and popovers can be closed without moving away (usually `Escape`), can themselves be hovered, and stay until closed or no longer relevant | hand |

## Operable

| SC | Lvl | Passes when | How |
|---|---|---|---|
| 2.1.1 Keyboard | A | Everything a pointer can do, the keyboard can do | hand |
| 2.1.2 No Keyboard Trap | A | Focus never gets stuck; the keys to leave are standard or stated | hand |
| 2.2.1 Timing Adjustable | A | Any time limit can be switched off, lengthened or extended before it ends; a toast that holds an action stays until handled | hand |
| 2.4.2 Page Titled | A | Each page or view sets a `<title>` naming what it is for | auto |
| 2.4.3 Focus Order | A | Tabbing moves through controls in an order that keeps the task making sense | hand |
| 2.4.4 Link Purpose (In Context) | A | A link's text, alone or with its sentence, list item or cell, says where it goes | auto, then hand |
| 2.4.6 Headings and Labels | AA | Headings and labels say what their section or field is; the screen has one `h1`; visual section titles are real headings | auto, then hand |
| 2.4.7 Focus Visible | AA | The focused control shows a visible indicator | hand |
| 2.4.11 Focus Not Obscured (Minimum) | AA | No sticky bar, banner or overlay covers the focused control entirely | hand |
| 2.5.3 Label in Name | A | The accessible name contains the words of the visible label, ideally at the start | hand |
| 2.5.7 Dragging Movements | AA | Each drag has a single-pointer alternative (tap, click, buttons), unless dragging is essential | hand |
| 2.5.8 Target Size (Minimum) | AA | Pointer targets meet the size in "Numbers", or qualify for a listed exception | auto, then hand |

## Understandable

| SC | Lvl | Passes when | How |
|---|---|---|---|
| 3.1.1 Language of Page | A | `<html lang>` matches the page's main language | auto |
| 3.1.2 Language of Parts | AA | A passage in another language (English quoted in an Arabic page, say) carries its own `lang` | hand |
| 3.3.1 Error Identification | A | An input error points at the field and describes the problem in words | hand |
| 3.3.2 Labels or Instructions | A | Each input has a visible label or instructions; a placeholder alone does not count | auto, then hand |
| 3.3.7 Redundant Entry | A | Information the user already gave in this process is pre-filled or offered for selection, unless re-entry is essential | hand |
| 3.3.8 Accessible Authentication (Minimum) | AA | Sign-in needs no recall or puzzle test unless an alternative exists; paste and password managers work | hand |

## Robust

| SC | Lvl | Passes when | How |
|---|---|---|---|
| 4.1.2 Name, Role, Value | A | Custom controls expose their name, role, state and value, and update them as they change | auto |
| 4.1.3 Status Messages | AA | Loading, empty, saved and error messages reach assistive tech through a live region or role, without taking focus | hand |

4.1.1 Parsing is obsolete in WCAG 2.2. Never raise it.

## Numbers

Grade against these values only, not against tool defaults or platform
guidelines.

- **Text contrast (1.4.3):** 4.5:1 for body text; 3:1 for large text (24 px,
  or about 18.7 px bold). Logos, disabled controls and pure decoration have
  no requirement.
- **Non-text contrast (1.4.11):** 3:1 against each adjacent colour.
- **Reflow (1.4.10):** a vertically scrolling page works at 320 CSS px wide
  with no sideways scroll; a horizontally scrolling one works at 256 CSS px
  tall with no vertical scroll. Data tables, maps, diagrams, editors and other
  content that needs both axes are exempt.
- **Text spacing (1.4.12):** line height 1.5 × font size, space after
  paragraphs 2 ×, letter spacing 0.12 ×, word spacing 0.16 ×.
- **Target size (2.5.8):** 24 × 24 CSS px. A smaller target still passes
  under one of five exceptions:
  - *Spacing*: a 24 px diameter circle centred on it intersects no other
    target and no other undersized target's circle;
  - *Equivalent*: the same action is available from a compliant control on the
    same page;
  - *Inline*: it sits in a sentence or block of text;
  - *User agent*: its size is the browser's default and the author did not
    change it;
  - *Essential*: that size or placement is legally required or essential to
    the information.
- 44 × 44 and 48 × 48 are design targets (`ux-laws.md`), not this
  criterion's threshold. Never fail a target for being under 44 px.

## Pairs that get mixed up

- **2.4.7 vs 2.4.11:** 2.4.7 asks whether a focus indicator exists and can be
  seen; 2.4.11 asks whether something else is sitting on top of the focused
  control.
- **1.4.3 vs 1.4.11:** 1.4.3 is about text; 1.4.11 is about everything else a
  user must see to operate the page (borders, rings, icons, chart parts).
