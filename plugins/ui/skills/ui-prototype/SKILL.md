---
name: ui-prototype
description: "Take a product idea to a working, responsive, reviewed prototype and design system: research, personas, theme directions, tokens, a clickable prototype, blind audit rounds, component and dark-theme passes, motion, and a published design system. Use when the user has an idea for an app or site and wants it designed and prototyped properly, or asks to 'go from idea to prototype', 'design this app', or 'make a real prototype'."
---

# UI prototype: from idea to a reviewed prototype

The path that turned a one-paragraph brief into a working trilingual prototype and design system. Each phase ends at a gate: show the result, ask the one decision the user must make (in the format of their CLAUDE.md), and wait. Use `ui-craft` for every design choice and `ui-audit` for every review.

## Phases

| # | Phase | Output | Gate (user decides) |
|---|---|---|---|
| 1 | Frame | One-paragraph brief: audience, devices, languages, the job, constraints, competitors | Brief is right |
| 2 | Research | `docs/design/research.md` with sources: how the audience works today, competitors, what analogous apps do well and badly. Use `deep-research` and Mobbin | none |
| 3 | Personas | `personas.md`: 3-4 personas with goals, frustrations, devices, language, key moments. Mark them as hypotheses | none |
| 4 | Directions | 2-3 theme directions as one visual page (same screen, light and dark, each language): name, voice, palette, type pair, shape, a playful twist, risks | Pick a direction |
| 5 | System v1 | `principles.md`, `tokens.json` → generated `tokens.css`, `base.css`, a contrast script over every pair, `components.md`, `pages.md`, mechanics doc with "data changes to approve" | Approve data changes |
| 6 | Static prototype | Every key screen as phone frames + tablet/desktop frames in one page, with theme and language toggles | none |
| 7 | Blind rounds | 5-7 rounds of fresh `ui-audit` reviewers, each fixed before the next (`references/briefs.md`) | Ask how many rounds |
| 8 | Component pass | Role, hierarchy, info load, icon vs text per component; the owner's screenshots drive it | Owner's taste rounds |
| 9 | Dark and colour | Deep research on comfortable dark themes, retune neutrals and text, re-run contrast | Comfortable now? |
| 10 | Motion and icons | Deep research on motion, a token set and a tiered list; icon set for every category | Approve the plan |
| 11 | Working prototype | A real responsive app (`references/working-prototype.md`): routing, state, flows, motion, all languages and themes, saved state | Where it lives |
| 12 | Design system | A browsable design system artifact from the prototype and docs (a subagent; brief in `references/briefs.md`) | none |
| 13 | Hand-over | Draft PR with everything; notes for the build team; open questions listed | User merges |

## Working rules

- **Research before opinion.** Every big choice (palette, motion, gamification, layout tiers) cites research or real products; keep the reports outside the repo and summarise the rules in the docs.
- **Show, then ask.** Directions, palettes and big component changes are shown as a published page, never only described.
- **One decision per question**, with a recommendation and its consequence; adopt the recommendation for questions left unanswered, and say so.
- **Tokens are the single source.** No hex in components; the contrast script runs on every change and lists every pair a component uses.
- **The simplest version first.** When the user says "worse", go simpler.
- **Verify in the browser after every change** (`references/checks.md`): both themes, both directions, phone/tablet/desktop; screenshots after transitions finish.
- **Commit per phase** on a `feat/` branch with the user's commit prefixes; keep the PR body current with what changed and what is open.
- **Respect parallel sessions**: never edit folders another session owns; leave hand-over notes in the shared notes folder.

## References

- `references/briefs.md`: prompts for research subagents, blind audit rounds and the design-system builder.
- `references/working-prototype.md`: architecture of the working prototype (vanilla JS, no build).
- `references/checks.md`: the scripted checks run after every change.
