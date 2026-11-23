# UX laws

- When two laws conflict, follow the user's primary task on that screen and
  state the trade-off you made.
- Name a law in a finding or a decision only when it explains it.
- Give concrete values: px, ms, counts. Never "make it clearer".

## Grouping and hierarchy

| Law | Rule |
|---|---|
| Proximity | Make the space between groups about twice the space inside a group. Place each label closer to its own input than to the next field |
| Similarity | Give elements with the same function the same look: one primary button style, links styled as links everywhere. Never style a non-clickable element like a clickable one |
| Common region | Group related content with a card, panel or background. Never nest boxes more than 2 levels deep |
| Visual hierarchy | Give every screen one obvious first read, usually the title or primary task, then a clear second and third. Use size, weight, contrast and position, not colour alone. Use at most about 3 type sizes for body content in one view |
| Isolation (Von Restorff) | Make exactly one element per view stand out: the primary action. Never mark it by colour alone |
| Aesthetic-usability | Keep one spacing scale, aligned edges, and consistent radii and shadows. Audit function as well as looks |

## Choices and memory

| Law | Rule |
|---|---|
| Hick's law | Cut the choices at each decision point. Keep primary navigation to about 5 to 7 items. Mark a recommended option. Split long forms into steps. Set sensible defaults |
| Miller's law | Chunk information: phone and card numbers, settings sections, navigation groups. Never make users hold more than a handful of items in mind |
| Recognition over recall | Show options instead of making users remember them: visible menus, recent items, autocomplete, inline examples. Keep labels visible; never a placeholder as the only label |
| Serial position | Put the most important items first and last in lists and navigation, and the least important in the middle |
| Progressive disclosure | Show what most users need; put advanced options behind "More", an accordion or a secondary screen. Never hide something needed to finish the main task |

## Effort

| Law | Rule |
|---|---|
| Fitts's law | Make important targets large and near where the user's pointer, thumb or attention already is. Make touch targets at least 44 by 44 CSS px with space between them; the WCAG pass or fail check stays at 24 by 24, as `wcag22-aa.md` says. Put destructive actions away from the primary action. Make a whole row or card clickable when it acts as one link |
| Jakob's law | Follow common conventions: logo at the start of the header links home, search at the top, cart at the top end, standard icons and form patterns |
| Tesler's law | Make the system absorb complexity it cannot remove: format input as it is typed, infer what it can, such as country from a phone code, and pre-fill known data |
| Postel's law | Accept input in any reasonable form: phone numbers with or without spaces, extra whitespace, several date formats, Arabic or Latin digits. Normalise it on save. Show errors that help, never ones that blame |
| Occam's razor | Remove every element, step, field and word that does not serve the task. Ask of each field: is it required now? |

## Time, feedback and endings

| Law | Rule |
|---|---|
| Doherty threshold | Respond to an interaction within about 400 ms; under 100 ms feels instant. For slower work, use optimistic updates, skeletons for content, a spinner after a short delay, and a progress bar with cancel for anything over about 10 s |
| Feedback | Give every action a visible response: hover, focus, active and disabled states, inline validation, a toast for background work, and clear empty, loading, error and success states. Make each error say what happened and how to fix it |
| Goal gradient | Show progress toward completion in multi-step flows, such as a stepper or "2 of 4". Pre-fill the first step where the data is known |
| Peak-end rule | Design the success state and the ending: a clear confirmation and a useful next step. Make error and failure moments as gentle as possible |

## Right-to-left interfaces

- Mirror conventions for Arabic and other right-to-left pages: reading order,
  navigation placement and serial-position emphasis start from the right.
- Keep the logo at the start of the header: the right edge.
