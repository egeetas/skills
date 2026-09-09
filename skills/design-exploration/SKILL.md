---
name: design-exploration
description: Explore and compare distinct visual directions before implementation. Do not use when the direction is already chosen and only needs building.
---

# Design Exploration

Use this skill when seeing alternatives will improve a consequential visual decision. The outcome is an approved design direction and rationale, not production implementation unless the user separately requests it.

## Build the Brief

Gather existing context before asking questions: product goals, target user, job to be done, current screen or flow, design system, framework, brand constraints, accessibility needs, content, responsive behavior, and important empty, loading, error, and long-content states.

Ask only for missing information that changes the directions. If evolving an existing interface, inspect the actual implementation or screenshot and identify what must remain recognizable.

## Generate Distinct Directions

Propose three to five named concepts before rendering them. Each concept needs a different design thesis, not merely another colorway. Vary at least:

- information hierarchy and layout model;
- typography and density;
- color and material treatment;
- interaction or navigation approach;
- emotional tone appropriate to the product.

Apply an anti-convergence test: if two concepts could exchange their headline and primary color without feeling meaningfully different, revise one. Preserve established brand or system constraints unless the user explicitly asks to explore outside them.

When bitmap mockups would materially help, use the available image-generation capability. Generate variants in parallel when supported and safe. When repo-native HTML/CSS or component prototypes are more useful, create isolated prototypes rather than modifying production code. Store temporary exploration artifacts outside tracked project files unless the user asks to keep them.

## Quality Gate

Evaluate every direction against the same criteria:

- clarity of the primary task and hierarchy;
- fit for the target user and product voice;
- responsive and long-content resilience;
- accessibility, contrast, focus, and reduced-motion implications;
- feasibility within the current stack and design system;
- handling of important non-happy states;
- distinctiveness without novelty that harms usability.

Reject or regenerate a variant that is broken, internally inconsistent, or only superficially different. Do not present low-quality output merely to reach a target count.

## Compare and Iterate

Present the variants together with a compact comparison matrix. Ask for structured feedback: preferred direction, elements to retain, elements to reject, and concerns. Iterate on the selected thesis rather than averaging every variant into a generic compromise.

Treat taste memory as evidence only when the user explicitly approved or rejected prior work. Current instructions override older preferences; ask whether a deliberate contradiction is a one-off or a changed preference before persisting it.

## Handoff

Document the approved direction with its visual thesis, hierarchy, typography, palette, component behavior, responsive rules, states, accessibility constraints, rejected alternatives, and unresolved decisions. If implementation is requested, hand this brief to `frontend-design`, then verify the result with `frontend-quality`, `accessibility-review`, and `webapp-testing` as appropriate.
