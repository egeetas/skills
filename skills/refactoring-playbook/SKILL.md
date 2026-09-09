---
name: refactoring-playbook
description: Refactor existing code through behavior-preserving checkpoints, characterization tests, small transformations, compatibility, and measurable completion.
---

# Refactoring Playbook

Refactoring changes structure, not intended behavior. If behavior must change, separate and describe that change.

## Workflow

1. Define the concrete maintainability problem and completion signal.
2. Establish behavior with existing tests or add characterization tests around risky paths.
3. Identify public contracts, persisted data, callers, generated code, and performance constraints.
4. Plan small reviewable transformations that keep the repository working at each checkpoint.
5. Make one structural move at a time; avoid simultaneous renaming, formatting, dependency, and behavior changes.
6. Run focused checks after each meaningful step and the relevant suite at completion.
7. Remove temporary compatibility code only after consumers have migrated and evidence supports removal.

Report behavior evidence, structural improvement, compatibility impact, verification, and remaining cleanup. Do not use refactoring as permission for unrelated rewrites.
