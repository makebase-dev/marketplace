# Dark theme checks

WCAG 2 contrast ratios overstate contrast near black, so a dark theme can pass 1.4.3 and still be uncomfortable. Run these in every audit of a dark or dark-first interface. Items marked *advisory* are not WCAG failures: report them as UX findings.

| Check | Pass | How |
|---|---|---|
| Body text not pure white | Text near OKLCH L 88-91; APCA no stronger than about Lc 90 for body text (*advisory*, halation for readers with astigmatism) | Read the computed colour; compute APCA if a tool is available |
| Background nearly neutral | OKLCH chroma about 0.03 or less on background and surfaces (*advisory*; mainstream dark themes keep 0-0.03) | Convert the background and surface tokens to OKLCH |
| No true black | Background is dark grey, not `#000` (*advisory*; smearing on OLED) | Computed background |
| Elevation readable | Raised surfaces lighter than the base, 2-5 L per level | Compare surface tokens |
| Control edges on every surface | Inputs, chips, checkboxes 3:1 against the surface they sit on, sheets and dialogs included | Measure border against raised surface |
| Fill colours not used as text | A colour that passes 3:1 as an icon or fill is not used for small text | Search tokens used both ways |
| Selected and current states | Not shown by a soft tint alone (a tint on a surface is often about 1.2:1) | 1.4.1, 1.4.11 |
| Markers on fills | A "today" or "current" outline in the same colour as the fill beneath it (1:1) | Inspect markers on filled cells |
| Saturated colours | Accents and status colours pastel on dark; no saturated red or blue text (*advisory*) | Look at the palette |
| Theme follows the browser | `color-scheme` set; native controls and scrollbars dark; two `theme-color` metas | Inspect `<html>` and `<head>` |
| No flash of the wrong theme | Saved theme applied before first paint | Reload with a saved non-default theme |
| Documents and images | White documents dimmed on a dark well, not left at full white; inversion only on request | Look at embedded pages and images |
| Token pair coverage | The project's contrast script (if any) lists every foreground/background pair the components use, in both themes | Compare the script's pairs with the pairs found on screen |
| Light theme still first-class | The light theme exists, follows the OS, and passes the same checks | Switch themes |
