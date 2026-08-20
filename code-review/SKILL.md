---
name: code-review
description: Review pull requests, diffs, or code changes for correctness, regressions, security, performance, maintainability, and missing tests.
---

# Code Review

Review and report by default; do not implement fixes unless requested.

## Review Method

1. Resolve the intended behavior, base revision, and exact changed scope.
2. Read surrounding call sites, contracts, tests, and configuration needed to understand the change.
3. Check correctness, edge cases, error paths, state transitions, concurrency, authorization, data handling, performance, compatibility, and test adequacy.
4. Run focused read-only checks when they materially validate a suspected issue.
5. Report only actionable findings supported by a concrete failure condition.

Do not elevate personal style preferences when the code follows project conventions. Avoid speculative findings without a plausible trigger and impact.

## Findings

Order findings by severity:

- `P0`: immediate catastrophic impact.
- `P1`: likely severe production, security, or data-loss issue.
- `P2`: real functional regression or meaningful operational risk.
- `P3`: limited defect worth correcting.

For each finding include the affected location, triggering conditions, observable impact, evidence, and the smallest reasonable correction. If there are no actionable findings, say so and mention any verification limits.
