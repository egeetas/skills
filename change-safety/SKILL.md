---
name: change-safety
description: Make scoped code changes while preserving user work, existing behavior, compatibility, and a clear verification and rollback path.
---

# Change Safety

Apply this skill when modifying an existing repository, especially shared, unfamiliar, or production code.

## Before Editing

- Read applicable repository instructions and inspect working-tree status.
- Treat existing uncommitted changes as user-owned. Do not overwrite, revert, reformat, or stage unrelated work.
- Establish the current behavior from code, tests, documentation, or a reproducible command.
- Identify public APIs, persisted data, configuration, and downstream consumers affected by the change.

## During the Change

- Prefer the smallest coherent diff that solves the requested problem.
- Avoid opportunistic refactors and dependency changes unless they are necessary and explained.
- Preserve backward compatibility unless a breaking change is explicitly intended.
- For risky state changes, favor additive migration, feature flags, checkpoints, and reversible steps.
- Stop and request direction when the safe solution materially expands scope.

## Verification

Run the narrowest meaningful checks first, then broader tests in proportion to risk. Report commands, outcomes, skipped checks, residual risk, and rollback considerations.
