# Component audit

Use when asked to audit components rather than pages, or after page-level audits stop finding much. Audit each component on its own, in every variant and state, then as it appears on each screen.

## For each component

| Question | Pass |
|---|---|
| Role | One sentence says what it is for; nothing on it serves a different job |
| Hero | Exactly one element is visually dominant, and it is the thing the user came for (an item's own name, a single number), not an identifier or code |
| Tiers | At most three levels: quiet identity and state / hero / quiet context. Codes are not inside the hero |
| Information load | Every fact helps the decision made here; facts the user does not need here (identifiers repeated from the page, internal counts) move to a details view |
| Defaults vs exceptions | Default states are quiet; only exceptions get a filled badge or colour |
| Icon vs text | Icon + word by default; icon alone only for universal controls with an accessible name; no icon reused with two meanings; known icons reused where they help recognition |
| Target | One target per component (the whole card a link), not a card that looks clickable plus a button doing the same |
| States | Default, hover, focus, active/pressed, selected, disabled, loading, empty, error; selected and current not shown by colour alone |
| Grouping | In lists, siblings separated by hairlines inside one container; group headings outside and above, a size step larger |
| Units and numbers | Every count has its unit; breakdowns add up to the total |
| RTL | Mirrors as `rtl-checks.md` says |

## Report

Use the `ux-audit.md` report format, one block per component, and name the laws (visual hierarchy, Von Restorff, recognition over recall, Occam's razor, proximity, common region). When the owner disagrees with a change ("worse"), propose a simpler version, not a more elaborate one.
