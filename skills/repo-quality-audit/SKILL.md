---
name: repo-quality-audit
description: Audit a repository by running checks, finding reproducible correctness or security bugs, coordinating bounded subagents, and drafting authorized issues.
---

# Repository Quality Audit

Audit and report by default. Do not modify code unless the user requests fixes.

## Establish the Baseline

1. Read repository instructions and inspect architecture, status, recent changes, CI, and existing issue conventions.
2. Discover documented install, format, lint, type-check, test, build, and security commands. `scripts/discover_repo_checks.py <repo>` can identify common declared checks without running them. Do not invent expensive or destructive commands.
3. Run checks from narrow to broad and preserve actionable failure evidence.

## Parallel Audit

For a substantial repository, delegate independent bounded lanes to up to three subagents when delegation is available:

- test/build failures and flaky behavior;
- correctness, edge cases, state, and concurrency;
- security boundaries, sensitive data, dependencies, and unsafe defaults.

Give each agent distinct scope and require evidence, reproduction, severity, confidence, and affected locations. The main agent deduplicates and validates results; subagent output is not automatically a finding.

## Finding Gate

Keep a finding only when it has a plausible trigger, observable impact, concrete evidence, and a reproduction or clear code path. Separate confirmed bugs from risks and unverified hypotheses.

Before creating an issue, search open and closed issues for duplicates and follow [the issue quality gate](references/issue-quality-gate.md). Structure results with [the audit report schema](references/audit-report-schema.md). Draft issues unless the user explicitly authorizes publication. Never open multiple speculative issues from one root cause.
