---
name: testing-standards
description: Design, implement, or review deterministic unit, integration, contract, and end-to-end tests with risk-based coverage and disciplined doubles.
---

# Testing Standards

Match the repository's framework and conventions. Test observable behavior and contracts rather than private implementation details.

## Test Selection

- Put a test at the lowest layer that can reliably prove the behavior.
- Use integration or contract tests for boundaries that mocks would misrepresent.
- Reserve end-to-end tests for critical user journeys and cross-system behavior.
- Every bug fix should include a regression test when the failure can be reproduced deterministically.

## Quality Rules

- Structure tests with clear setup, action, and assertions; name the behavior and condition.
- Cover success, validation, authorization, error, boundary, state-transition, and concurrency cases in proportion to risk.
- Keep tests deterministic: control time, randomness, network, filesystem, and shared state.
- Mock at stable boundaries, not internal calls. Avoid assertions that merely confirm mock configuration.
- Do not refresh snapshots or golden files without inspecting and explaining the change.
- Treat coverage as a gap-finding signal, not a substitute for meaningful assertions.

Run the focused test first, then the relevant suite. Report commands, results, skipped environments, and flakiness observed.
