---
name: pr-preparation
description: Prepare a reviewable pull request with scoped commits, self-review, verification evidence, risks, screenshots, migrations, and rollback guidance.
---

# Pull Request Preparation

Preparation does not authorize staging, committing, pushing, or opening a pull request; each action requires explicit authorization.

## Prepare

1. Resolve the intended base, head, issue/context, and acceptance criteria.
2. Inspect the complete diff and working tree; exclude unrelated or accidental files.
3. Self-review correctness, security, compatibility, data/config changes, generated files, tests, and documentation.
4. Run relevant formatter, static checks, tests, and build. Record exact commands and results.
5. Prepare a concise title and body covering why, what, verification, risk, migrations/config, rollout/rollback, and follow-ups.
6. Add visual evidence only for material UI outcomes and remove sensitive data.
7. Identify reviewer expertise and unresolved decisions without assigning reviewers unless authorized.

Keep the PR focused. Split independent changes when doing so improves review or rollback rather than merely reducing line count.
