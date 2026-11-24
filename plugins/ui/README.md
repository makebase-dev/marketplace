# ui

Three Claude skills that work as a set:

| Skill | Use it to | Call it |
|---|---|---|
| **ui-craft** | Design or polish a screen or component: visual hierarchy, comfortable dark themes, colour and contrast, icons (recognition over recall), motion, right-to-left and multilingual UI, light gamification, and the twenty habits that make a page look generated | `/ui:ui-craft` |
| **ui-audit** | Review a page, flow or component against WCAG 2.2 AA and UX laws, including dark-theme, right-to-left, motion, consistency and generated-look checks, and blind repeated review rounds | `/ui:ui-audit` |
| **ui-prototype** | Take an idea to a working, responsive, reviewed prototype and design system, phase by phase | `/ui:ui-prototype` |

A typical flow: `ui-prototype` runs the project, `ui-craft` shapes each screen, `ui-audit` reviews it round after round.

## Works best with

- A browser tool (Claude's built-in browser or Playwright) for rendered audits.
- The Mobbin connector for design references, and a deep-research skill for the research phases of `ui-prototype` (both optional).
