# Visual hierarchy of components

## The three-tier card

For any card whose job is "pick this thing" (a lesson, an exercise, an article, an order):

```
2016 · Ex 2                    ✓ Solved right    tier 1: identity + state, 13 px, muted, one line
A family with albinism                           tier 2: HERO, 18 px semibold (22 px when it is the page's main card), max 2 lines
✓ In program    [leaf] Dihybrid cross            tier 3: context, 13 px, muted
```

- The hero is the item's **own name**. Never prefix it with codes ("Exercise 3 · …", "2016 · Ex 2 · …"); codes go to tier 1.
- Tier 1 holds the short identity at the start and the user's state at the end.
- Tier 3 holds at most two facts. Everything else (section, subject already filtered, page counts, points the user does not decide on) moves to the details view.
- One fill per card at most. Default states are quiet text + icon; only exceptions get a filled badge.
- Make the whole card one link (a stretched title link); never a card that looks clickable plus a separate button doing the same thing.
- A "continue" variant may add one progress line ("Page 3 of 6") and a filled bar whose label says exactly what happens ("Resume at page 3").

Patterns worth copying (Mobbin): Tiimo lesson cards (small chip + status on top, big title below), Uxcel / Alan rows (fixed leading tile, bold title, one muted line), Brink continue card (progress + an action that states what is left).

## Compact rows

Leading fixed-size tile (40 px, subject glyph) so every title starts at the same x; title as hero; one muted line; chevron at the end. Do not lead with variable-width badges: titles stop lining up.

## Rows with details

Put details **under** the name, not at the end of the row. Anything at the end steals width and wraps the details onto three lines. The end holds only a chevron.

## Groups

- One card per group (common region), rows separated by 1 px hairlines inside it.
- The group's heading sits **outside and above** the card, on the page background, one clear size step above the children (e.g. 22 px bold over 15 px names). A heading inside the card at nearly the same size blends with its children.
- 10 px heading-to-card, 28 px between groups. Footer actions of the group ("Not required this year (2)") go inside the same card as its last row.
- Drop numbering that the source data does not own ("Unit 3"): a wrong or ambiguous number confuses more than no number.

## Summary cards ("how far am I?")

One question, one number, one bar, one line:

```
BIOLOGY · REQUIRED FOR 2026-27
14  of 22 topics practised
[██████████████▨▨▨░░░░░]      done solid · started striped · not started empty
3 started · 5 not started yet
```

Rejected after owner review: a four-level colour legend (needs memorising) and one mini glyph per item (22 tiny marks = noise). Finer levels belong on the rows, where they mean something.

## Screen-level

- One primary action per screen, in the thumb zone; the rest secondary or quiet.
- Larger screens show the same content as phones, never more game numbers or extra sections; they use space with master-detail, side panels and wider grids.
- Labels describe practice, not ability ("Practised", not "Weak").
