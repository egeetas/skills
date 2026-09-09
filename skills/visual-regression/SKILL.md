---
name: visual-regression
description: Create, update, or review deterministic visual regression coverage for meaningful UI states, viewports, themes, and component variants.
---

# Visual Regression

Use when layout, styling, rendering, design-system, or cross-browser changes need image-based regression evidence.

## Stable Capture

- Control viewport, device scale, fonts, locale, timezone, theme, data, animation, network, randomness, and time.
- Capture representative states and boundaries, not every trivial permutation.
- Wait for fonts, images, layout, and intended async content; mask only truly nondeterministic regions.
- Keep baselines tied to a reviewed environment and documented update command.

## Review

Inspect every changed baseline. Classify differences as intended, regression, environment drift, or flakiness. Never approve baselines solely to make CI pass.

Pair visual tests with behavioral and accessibility tests when the UI can look correct but function incorrectly.
