# Software Engineering Skills

A collection of reusable Codex skills for planning, building, testing, reviewing, shipping, and operating software. Each directory is a self-contained skill with a required `SKILL.md` entrypoint.

## Core Development

- `product-requirements` — scope, acceptance criteria, non-goals, and edge cases.
- `architecture-decision` — alternatives, trade-offs, ADRs, migration, and rollback.
- `implementation-standards` — maintainable implementation and explicit contracts.
- `change-safety` — minimal diffs, compatibility, user-work preservation, and verification.
- `dependency-management` — necessity, versions, licenses, advisories, and lockfiles.
- `testing-standards` — deterministic unit, integration, contract, and E2E tests.
- `debugging-checklist` — reproduction, hypotheses, isolation, and root cause.
- `code-review` — evidence-backed correctness, security, performance, and regression review.
- `repo-quality-audit` — checks, parallel bug hunting, issue quality gates, and deduplication.
- `security-baseline` — trust boundaries, identity, input, secrets, and secure defaults.
- `documentation-style` — README, API docs, comments, and changelogs.
- `git-workflow` — safe branches, commits, staging, history, and pushes.
- `release-checklist` — versioning, artifacts, rollout, monitoring, and rollback.

## Production and Operations

- `database-migrations`
- `observability-standards`
- `performance-investigation`
- `incident-response`
- `postmortem`

## Front-end and Mobile

- `accessibility-review`
- `frontend-quality`
- `visual-regression`
- `platform-guidelines`
- `device-testing`
- `mobile-release`

## APIs and AI Systems

- `api-design`
- `threat-modeling`
- `ai-evaluation`
- `prompt-versioning`
- `model-safety`

## Supporting Workflows

- `project-bootstrap`
- `refactoring-playbook`
- `issue-triage`
- `pr-preparation`
- `software-development-workflow` — routes substantial work through only the relevant specialized skills.

## Design Principles

The skills prefer evidence over speculation, scoped changes over rewrites, risk-based verification over ritual, and explicit authorization for external mutations such as commits, pushes, issue publication, releases, deployments, or production data changes.

## License

MIT — see [LICENSE](LICENSE).
