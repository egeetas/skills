---
name: engineering-retrospective
description: Produce an evidence-based engineering retrospective for a repository or delivery period using git, pull-request, test, incident, and workflow signals to identify trends and concrete improvements. Do not use for incident root-cause analysis or individual productivity ranking.
---

# Engineering Retrospective

Review how the engineering system worked over a defined period. This is distinct from `postmortem`: it looks for recurring delivery and quality patterns even when no incident occurred. Keep the analysis blameless and resist turning activity volume into a productivity score.

## Establish the Window and Evidence

- Resolve the repository, base branch, local timezone, and explicit period; default to the most recent seven complete days only when the user gave no window.
- Prefer a freshness-verified remote base when network access and authorization allow a fetch. Otherwise disclose the exact local ref and latest commit date.
- Collect available git history, merged pull requests, review cycles, test changes, CI outcomes, incidents, backlog movement, and release evidence. State which sources were unavailable.
- Normalize author aliases only when evidence supports the mapping. Do not infer performance, effort, or working hours from commit timestamps or line counts.

## Analyze the System

Look for evidence-backed patterns in:

- delivered outcomes and work that remained unfinished;
- regressions, repeated fixes, revert frequency, and change hotspots;
- test health, missing regression coverage, flaky checks, and CI reliability;
- review latency, repeated review themes, oversized changes, and rework;
- operational load, incidents, dependency or release friction;
- documentation, onboarding, and recurring manual steps;
- decisions or shortcuts that accumulated follow-up cost.

Counts and code volume may provide context but are not success metrics by themselves. Inspect representative changes before explaining a trend. Label causal explanations as hypotheses unless direct evidence confirms them.

## Compare

When comparison is requested or a compatible prior snapshot exists, compare equal-length periods with the same source definitions. Show absolute values and deltas, and call out changes in data availability. Do not claim improvement from small or noisy samples.

For team retrospectives, discuss ownership distribution, review coverage, and system bottlenecks without ranking individuals. Mention a person only to credit a concrete outcome or route an action when ownership is already known.

## Report

Return:

1. scope, refs, dates, and evidence limitations;
2. outcomes shipped and meaningful wins;
3. quality and delivery signals with supporting examples;
4. trends versus the comparable period, when available;
5. what helped, what created friction, and open hypotheses;
6. at most five actions with expected benefit, measurable completion condition, and owner only when known;
7. experiments to run before the next retrospective.

Write a snapshot or publish the report only when requested. Do not open issues, assign people, or change project state without separate authorization.
