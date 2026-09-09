---
name: software-development-workflow
description: Coordinate a software task from requirements and design through implementation, tests, audit, review, documentation, and release preparation using the relevant specialized skills.
---

# Software Development Workflow

Use this as an orchestrator for substantial end-to-end software work. Do not load or apply every specialized skill automatically; select only the lanes the task actually needs.

## Route the Task

- Unclear feature or product behavior: use `product-requirements`.
- Consequential design choice: use `architecture-decision` and, for sensitive systems, `threat-modeling`.
- Existing-code changes: apply `implementation-standards` and `change-safety`.
- Unfamiliar or consequential change surface: use `codebase-mapping` before planning implementation.
- Dependency or persisted-data changes: use `dependency-management` or `database-migrations`.
- Tests and bug fixes: use `testing-standards`, `debugging-checklist`, and `test-and-fix-loop` as appropriate.
- Broad verification: use `repo-quality-audit`; use subagents only for independent, bounded lanes.
- Review: use `code-review` and `security-baseline` in proportion to risk.
- Frontend implementation or browser verification: use `frontend-design`, `frontend-quality`, `accessibility-review`, `visual-regression`, or `webapp-testing` only for the lanes needed.
- MCP server work: use `mcp-builder`.
- Substantial specs, RFCs, ADRs, or runbooks: use `technical-doc-coauthoring`; apply `documentation-style` to the final form.
- User-facing or operational changes: update documentation and observability where relevant; use `changelog-generator` for release communication.
- Issue-backed delivery: use `issue-to-pr-workflow`; otherwise prepare with `git-workflow`, `pr-preparation`, and `release-checklist`.

## Execution Gates

1. Establish scope, success criteria, constraints, repository instructions, and current state.
2. Make the smallest coherent implementation and keep unrelated user work untouched.
3. Add or update tests that prove the requested behavior.
4. Run focused checks, then broader verification proportional to risk.
5. Review the final diff, update affected documentation, and report residual risk.

Do not infer permission to stage, commit, push, open issues or pull requests, deploy, publish, migrate production data, or communicate externally. Require explicit authorization for each external mutation.
