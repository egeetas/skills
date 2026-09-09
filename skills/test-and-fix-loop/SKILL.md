---
name: test-and-fix-loop
description: Run a repository's relevant formatter, lint, type-check, unit, integration, end-to-end, and build checks; diagnose confirmed failures; and implement fixes when requested. Do not use when the user asks only for a diagnostic report without changes.
---

# Test and Fix Loop

Close the feedback loop between repository checks and verified corrections without hiding failures or rewriting unrelated code.

## Establish the Baseline

Read repository instructions and discover documented package, format, lint, type-check, test, coverage, and build commands. Inspect the working tree first. Start with the narrowest command that reproduces the reported or likely failure, then expand in proportion to risk.

Classify every failure before editing:

- product-code defect;
- incorrect or obsolete test;
- environment, dependency, credential, service, or fixture problem;
- flaky or timing-sensitive behavior;
- unrelated pre-existing failure.

Preserve logs and the minimal reproduction. Do not edit product code merely to satisfy a mistaken assertion, and do not weaken or delete a meaningful test to make the suite green.

## Fix

Trace the failing path to a root cause and make the smallest coherent correction. Add or strengthen a regression test for confirmed defects when deterministic. Preserve public behavior unless the task explicitly changes it.

After two unsuccessful edits for the same symptom, stop patch-chaining: restore the hypothesis table, gather new evidence, and reassess the root cause before another change. Do not mask flakiness with arbitrary sleeps, retries, broad exception handling, or snapshots accepted without inspection.

## Verify

1. Re-run the exact failing check.
2. Run adjacent tests for the affected component or boundary.
3. Run broader lint, type-check, test, coverage, E2E, and build checks proportional to the change.
4. Inspect the final diff for accidental edits and test-only accommodations.

Report commands and results, fixes made, pre-existing or environment-blocked failures, skipped checks, observed flakiness, and residual risk. Never report the repository as clean when required checks were unavailable or still failing.
