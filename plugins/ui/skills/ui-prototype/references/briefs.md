# Subagent briefs

Fill the `{…}` parts. Give paths and goals, never your own conclusions.

## Blind audit round (one fresh agent per round)

```
You are an independent reviewer. Audit a design system for accessibility and UX. Report findings only; do not edit any file in the repo.

Context: {product, audience with ages, devices, languages and directions, the main jobs, the gamification}. The owner's goals: {e.g. calm but made for Gen-Z; dark mode flawless; encourage without a system to learn; phone, tablet and desktop}.

Repo worktree: {path} (read-only for you). Read: {prototype file}, {tokens files}, {contrast script}, {docs list}.

To see it rendered: run `python -m http.server {unique port} --directory {folder}` in the background, open it in the built-in browser (mcp__Claude_Browser__*), check dark and light, every language, phone, tablet and desktop widths. Stop the server and reset the viewport when done. Do not run build scripts that rewrite files.

Run the `/ui-audit` skill for both an accessibility audit (WCAG 2.2 AA) and a UX audit. Also judge: one primary action per screen; anything confusing for {audience}; mirroring and mixed-direction text; dark mode consistency; use of space on large screens; docs vs tokens vs prototype consistency.

Return findings most severe first (severity, where, observed, criterion or law, fix), then what you could not check. Concrete, no praise, under 900 words.
```

Use a new port per round. After the report: fix, verify, commit, then the next round.

## Research thread (deep-research coordinator spawns 3-4 in parallel)

Split by angle, mutually exclusive: official guidance (design systems, standards), human-factors evidence, real-world implementations or palettes, and the product category (learning apps etc.). Each prompt: objective, key questions with the exact numbers wanted, suggested primary sources, constraints (current year), the notes path. The report writer gets the project context and must end with concrete recommendations (values, a prioritised list, a do-not list, implementation).

## Design-system builder

```
Build the complete {name} design system as a Design System artifact, from the working prototype and the design docs.
Artifact (created, empty): {url}. Step 1: read SKILL.md and artifact-type/reference/{format,craft,cover,from-code}.md and artifact-type/demo.json on that url, and follow them exactly (project/ files, list-shaped tokens.json, previews with the @dsCard line, bundle.css, the cover last, the index last, one publish call with root).
Step 2: sources (read-only): {tokens.json}, {prototype html/css/js}, {docs}. Put the primary theme first.
Step 3: build README brand book (+ sections), tokens with usage notes, every component (README with guidelines, states, accessibility, RTL; live preview using the tokens and the prototype's CSS), icons as SVG asset uploads with a group README of fixed meanings, the cover.
Write under {scratchpad folder}. Check contrast in both themes. No AI tropes. Report counts, gaps and the link in under 250 words.
```
