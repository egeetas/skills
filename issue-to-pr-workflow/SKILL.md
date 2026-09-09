---
name: issue-to-pr-workflow
description: Carry an accepted software issue from triage through implementation, regression tests, review, and pull-request preparation or publication. Use when the user asks to fix an issue or deliver issue-backed work; do not activate merely to inspect or triage an issue.
---

# Issue to Pull Request Workflow

Deliver one coherent issue-backed change with traceable evidence. Reading an issue does not authorize assignment, comments, branches, commits, pushes, or pull requests; perform only the external mutations the user explicitly requested.

## Resolve the Work

1. Identify the repository, issue number, base branch, and acceptance criteria.
2. Read repository instructions, issue discussion, linked specs, relevant code/tests, and open or closed duplicates.
3. Reproduce a reported bug or establish a concrete failing code path. If evidence is insufficient, return an investigation note instead of inventing a fix.
4. Check the working tree and preserve unrelated user changes. Use a focused branch when branch creation is authorized or part of the explicit request.
5. Route plausible vulnerabilities through the repository's private disclosure process; do not expose exploit details in a public issue or PR.

## Implement

Make the smallest coherent change that satisfies the issue. Follow repository conventions and update contracts, migrations, configuration, observability, and documentation only where the behavior requires it.

Use subagents only when available and when the issue contains independent, bounded lanes such as reproduction, security analysis, or test coverage. Give each lane distinct scope; the primary agent validates and deduplicates their findings.

For a bug, add a deterministic regression test that fails for the original behavior when practical. Run focused checks before broader lint, type-check, test, and build commands.

## Review and Deliver

Review the complete diff against the issue and acceptance criteria. Check correctness, edge cases, security, compatibility, performance, tests, generated files, and accidental changes.

Prepare a pull request with:

- a concise issue-linked title and summary;
- the root cause or motivation and the implemented behavior;
- exact verification commands and results;
- risk, migration/configuration, rollout, and rollback notes where relevant;
- screenshots or traces for material UI changes;
- unresolved decisions or follow-ups.

Commit, push, comment, assign, close, or open the PR only when those actions are explicitly authorized. After publication, report the branch, commit, PR URL, checks, and remaining risk; do not merge unless separately requested.
