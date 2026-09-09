---
name: accessibility-review
description: Review web or app accessibility across semantics, keyboard use, focus, names, contrast, motion, forms, and assistive technology behavior.
---

# Accessibility Review

Use for UI implementation, accessibility audits, component libraries, and user-flow verification.

## Review

- Prefer native semantic controls and document structure before adding ARIA.
- Verify accessible names, roles, states, descriptions, labels, errors, and live updates.
- Complete critical flows with keyboard only; check logical order, visible focus, traps, restoration, skip mechanisms, and modal behavior.
- Check text and non-text contrast, zoom/reflow, touch targets, orientation, reduced motion, captions/transcripts, and non-color cues as applicable.
- Verify forms preserve input, associate errors, and explain required formats.

Use automated tools for broad detection, then manually verify important interactions. Report the affected user, standard/criterion when known, reproduction, impact, and remediation. Do not claim full compliance from automation alone.
