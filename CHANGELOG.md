# Changelog

All notable changes to this project are documented here. Dates use `YYYY-MM-DD` and releases follow semantic versioning.

## [1.0.0] - 2026-09-09

### Added

- 49 focused Codex skills covering product discovery, architecture, implementation, testing, review, frontend and mobile quality, security, operations, AI systems, and technical documentation.
- Six non-overlapping install packs with `core-development` as the default selection and explicit `--all` support.
- Portable and compatibility plugin manifests plus an installable Codex marketplace definition.
- Three optional subagent presets for repository exploration, quality review, and test investigation.
- Reusable ADR, PRD, RFC, postmortem, AI evaluation, audit, and reader-test resources.
- Deterministic git-range and repository-check discovery tools.
- A 147-case routing corpus, focused boundary cases, and a real Codex model-backed routing evaluator.

### Changed

- Reduced the combined skill discovery descriptions from 8,966 to 6,848 characters and made the broad workflow orchestrator explicit-only.
- Split concise English and Turkish entry documentation from the complete skill catalog and authoring guide.
- Expanded CI to validate packs, plugin metadata, resource links, scripts, installer modes, and tool unit tests.

### Security

- Preserved explicit authorization boundaries for code changes, issues, pull requests, releases, deployments, and destructive actions.
- Kept audit subagents bounded and required coordinating agents to reproduce and deduplicate findings.

[1.0.0]: https://github.com/egeetas/skills/releases/tag/v1.0.0
