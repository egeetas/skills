---
name: project-bootstrap
description: Bootstrap a maintainable software repository with appropriate structure, tooling, CI, documentation, and secure defaults.
---

# Project Bootstrap

Use for new repositories or deliberate adoption of foundational tooling. Preserve the user's chosen language, framework, runtime, package manager, and hosting platform.

## Bootstrap Outcomes

- Minimal source and test structure suited to the architecture, without speculative layers.
- Reproducible dependency installation and pinned runtime/tool versions where appropriate.
- Formatter, linter, type/static checks, tests, build, and one documented verification command.
- Ignore rules, example configuration, secret-safe defaults, license, and concise README.
- CI that installs reproducibly and runs the same checks used locally.
- Ownership, contribution, release, security, or dependency automation only when the project needs it.

Do not add fashionable infrastructure without a current requirement. Verify the clean-clone path and report generated files, commands, assumptions, and intentionally deferred decisions.
