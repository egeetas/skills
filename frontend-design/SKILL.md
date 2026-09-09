---
name: frontend-design
description: Design and implement distinctive web interfaces when visual direction, typography, layout, motion, responsive behavior, or UI copy materially affect the result. Do not use for backend-only work or a narrow style fix with an established design system.
license: Apache-2.0; see ../LICENSES/Apache-2.0.txt and ../THIRD_PARTY_NOTICES.md
---

# Frontend Design

Create an interface with a deliberate visual point of view grounded in the product, audience, and primary user task. Preserve an established design system unless the user requests a new direction.

## Establish Direction

Before implementation, resolve enough of the brief to make intentional choices. If key context is missing, propose a concrete subject, audience, and primary job; ask only when the answer would materially change the design.

Define a compact design plan:

- a restrained palette with named roles and accessible contrast;
- one or two type families with an intentional scale, weight, and line length;
- a layout concept and alignment logic, using a small ASCII wireframe when it clarifies structure;
- one memorable visual idea, with supporting elements kept quiet;
- motion rules tied to feedback, state, or hierarchy rather than decoration;
- plain, consistent interface language written from the user's perspective.

Review the plan against the actual brief. Replace choices that could be dropped unchanged into an unrelated product.

## Build

- Use the repository's framework, component system, tokens, and conventions.
- Use real or domain-plausible content so layout decisions reflect the product.
- Let hierarchy and information structure determine borders, cards, labels, and grouping.
- Avoid habitual AI defaults such as uniform rounded cards, decorative gradients, repeated fade-up animations, generic marketing copy, and arbitrary all-caps labels unless the brief supports them.
- Keep CSS specificity predictable and avoid competing utility/component rules.
- Make layouts responsive from narrow mobile widths through large screens.
- Use semantic HTML, visible keyboard focus, sufficient contrast, useful empty/error states, and reduced-motion behavior.

## Critique and Verify

Inspect rendered screenshots at representative mobile and desktop sizes when browser tooling is available. Check hierarchy, density, alignment, type rhythm, overflow, states, and whether the result still feels specific to the brief.

Run the repository's relevant formatter, lint, type-check, tests, and build. Report what was verified and any visual or environment limits.
