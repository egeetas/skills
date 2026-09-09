# Skill Catalog

The collection contains 49 skills in six non-overlapping packs. Install a pack with `./scripts/install.sh --pack <name>` or follow [SETUP.md](SETUP.md).

“Boundary” names the closest workflow that should be chosen instead for a neighboring intent.

## Product and architecture

| Skill | Use it for | Boundary |
| --- | --- | --- |
| [`product-strategy-review`](skills/product-strategy-review/) | Challenge an unvalidated idea and find a valuable wedge | Accepted scope → `product-requirements` |
| [`product-requirements`](skills/product-requirements/) | Turn accepted direction into testable scope and criteria | Unvalidated demand → `product-strategy-review` |
| [`codebase-mapping`](skills/codebase-mapping/) | Understand an unfamiliar repository and its flows | Choose a durable design → `architecture-decision` |
| [`architecture-decision`](skills/architecture-decision/) | Compare consequential designs and record an ADR | Simple repository discovery → `codebase-mapping` |
| [`api-design`](skills/api-design/) | Define stable HTTP, RPC, event, or library contracts | Implement an accepted contract → `implementation-standards` |
| [`developer-experience-review`](skills/developer-experience-review/) | Test API, CLI, SDK, or docs onboarding and ergonomics | Customer interface quality → `frontend-quality` |
| [`project-bootstrap`](skills/project-bootstrap/) | Establish a new repository's engineering foundation | Map an existing repository → `codebase-mapping` |

## Core development

| Skill | Use it for | Boundary |
| --- | --- | --- |
| [`implementation-standards`](skills/implementation-standards/) | Implement accepted behavior maintainably | Preserve behavior while restructuring → `refactoring-playbook` |
| [`change-safety`](skills/change-safety/) | Keep a scoped change compatible, reversible, and respectful of user work | Dedicated structural refactor → `refactoring-playbook` |
| [`refactoring-playbook`](skills/refactoring-playbook/) | Improve code structure without behavior change | Add new behavior → `implementation-standards` |
| [`dependency-management`](skills/dependency-management/) | Add, remove, upgrade, or audit dependencies | Whole-system security posture → `security-baseline` |
| [`testing-standards`](skills/testing-standards/) | Design or review deterministic test coverage | Execute and repair checks → `test-and-fix-loop` |
| [`debugging-checklist`](skills/debugging-checklist/) | Diagnose a failure without assuming a fix | Run and fix the repository → `test-and-fix-loop` |
| [`test-and-fix-loop`](skills/test-and-fix-loop/) | Execute checks and repair confirmed failures | Diagnostic-only work → `debugging-checklist` |
| [`code-review`](skills/code-review/) | Review a diff or PR and report defects | Whole-repository audit → `repo-quality-audit` |
| [`repo-quality-audit`](skills/repo-quality-audit/) | Find reproducible repository-wide bugs and security defects | Review only a change set → `code-review` |
| [`issue-triage`](skills/issue-triage/) | Classify and deduplicate a report | Deliver an accepted issue → `issue-to-pr-workflow` |
| [`issue-to-pr-workflow`](skills/issue-to-pr-workflow/) | Carry an accepted issue through a verified PR | Triage-only request → `issue-triage` |
| [`git-workflow`](skills/git-workflow/) | Apply safe branch, commit, rebase, merge, and push conventions | Package finished work for review → `pr-preparation` |
| [`pr-preparation`](skills/pr-preparation/) | Create a review-ready PR and evidence | Review a submitted PR → `code-review` |
| [`release-checklist`](skills/release-checklist/) | Verify readiness before deployment | Observe an already deployed release → `canary-monitoring` |
| [`canary-monitoring`](skills/canary-monitoring/) | Compare a new web release with a baseline | Perform deployment → deployment tooling/workflow |
| [`changelog-generator`](skills/changelog-generator/) | Write notes from a verified change range | General release readiness → `release-checklist` |
| [`software-development-workflow`](skills/software-development-workflow/) | Explicitly orchestrate several lifecycle stages | A single focused task → its specialist skill |

## Frontend and mobile

| Skill | Use it for | Boundary |
| --- | --- | --- |
| [`design-exploration`](skills/design-exploration/) | Compare distinct visual directions before implementation | Chosen direction → `frontend-design` |
| [`frontend-design`](skills/frontend-design/) | Design and build a distinctive chosen interface | Direction still undecided → `design-exploration` |
| [`frontend-quality`](skills/frontend-quality/) | Harden responsive states, resilience, accessibility, and performance | Real browser execution → `webapp-testing` |
| [`webapp-testing`](skills/webapp-testing/) | Exercise rendered flows, console, network, and accessibility | Screenshot baselines → `visual-regression` |
| [`accessibility-review`](skills/accessibility-review/) | Audit semantics, keyboard, focus, names, contrast, and assistive tech | General interface quality → `frontend-quality` |
| [`visual-regression`](skills/visual-regression/) | Maintain deterministic screenshot coverage | Functional browser flow → `webapp-testing` |
| [`platform-guidelines`](skills/platform-guidelines/) | Check native conventions and system integration | Execute device matrix → `device-testing` |
| [`device-testing`](skills/device-testing/) | Test representative devices, OS versions, lifecycle, and networks | Prepare store release → `mobile-release` |
| [`mobile-release`](skills/mobile-release/) | Prepare signed, staged iOS or Android delivery | Compatibility testing → `device-testing` |

## Security and operations

| Skill | Use it for | Boundary |
| --- | --- | --- |
| [`security-baseline`](skills/security-baseline/) | Review practical security controls and defaults | Structured attack-path analysis → `threat-modeling` |
| [`threat-modeling`](skills/threat-modeling/) | Map assets, actors, boundaries, attacks, and mitigations | Implementation security review → `security-baseline` |
| [`database-migrations`](skills/database-migrations/) | Plan compatible, observable, reversible data changes | Ordinary API evolution → `api-design` |
| [`observability-standards`](skills/observability-standards/) | Design logs, metrics, traces, dashboards, and alerts | Investigate a measured regression → `performance-investigation` |
| [`performance-investigation`](skills/performance-investigation/) | Profile latency, throughput, CPU, memory, I/O, or scale | Ongoing telemetry design → `observability-standards` |
| [`incident-response`](skills/incident-response/) | Coordinate a live production incident | Stable incident analysis → `postmortem` |
| [`postmortem`](skills/postmortem/) | Document a stable incident's causal chain and actions | Active mitigation → `incident-response` |

## Project intelligence

| Skill | Use it for | Boundary |
| --- | --- | --- |
| [`project-learnings`](skills/project-learnings/) | Preserve durable, evidence-backed repository knowledge | Resume one unfinished session → `context-handoff` |
| [`context-handoff`](skills/context-handoff/) | Transfer sanitized task state across sessions or worktrees | Long-lived project knowledge → `project-learnings` |
| [`engineering-retrospective`](skills/engineering-retrospective/) | Find systemic improvement from delivery-period evidence | One incident's root cause → `postmortem` |

## AI and documentation

| Skill | Use it for | Boundary |
| --- | --- | --- |
| [`mcp-builder`](skills/mcp-builder/) | Build or review an MCP server | Ordinary application API → `api-design` |
| [`ai-evaluation`](skills/ai-evaluation/) | Measure AI behavior on representative cases | Safety-control review → `model-safety` |
| [`prompt-versioning`](skills/prompt-versioning/) | Version a production prompt with eval evidence and rollback | Whole-feature evaluation → `ai-evaluation` |
| [`model-safety`](skills/model-safety/) | Review misuse, injection, unsafe tools, and data exposure | General model quality → `ai-evaluation` |
| [`documentation-style`](skills/documentation-style/) | Improve routine README, API docs, comments, and changelogs | Substantial decision document → `technical-doc-coauthoring` |
| [`technical-doc-coauthoring`](skills/technical-doc-coauthoring/) | Coauthor and reader-test an RFC, ADR, spec, proposal, or runbook | Small documentation edit → `documentation-style` |
