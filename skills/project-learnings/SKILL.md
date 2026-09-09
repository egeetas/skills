---
name: project-learnings
description: Capture, search, review, prune, or export durable project learnings with evidence, confidence, freshness, and contradiction handling. Not for temporary task state.
---

# Project Learnings

Maintain a small, trustworthy memory of facts that would save meaningful rediscovery in a future session. A learning must be durable, project-specific, and supported by evidence. Prefer no entry over a plausible but unverified one.

## Modes

- **Add:** record a verified pattern, pitfall, command, decision, or preference.
- **Search/show:** retrieve relevant entries without loading the entire store when a narrow query is enough.
- **Review/prune:** verify freshness, mark stale entries, and reconcile contradictions.
- **Export:** produce a redacted, reviewable team document only when requested.

Use an existing project memory location when the repository defines one. Otherwise keep private state outside the working tree under `${CODEX_HOME:-$HOME/.codex}/project-state/<project-key>/learnings.jsonl`. Derive `<project-key>` from the canonical repository identity and path; do not use the directory basename alone because unrelated repositories can share it. Do not create or modify a store until the user invokes a mutating mode.

## Admission Gate

Record an entry only when it is likely to remain useful and at least one source can be cited, such as a repository file and line, a reproducible command result, an accepted architecture decision, or an explicit user preference. Do not store:

- secrets, credentials, personal data, or raw sensitive logs;
- guesses, generic best practices, praise, or model self-observations;
- temporary branch state, remaining tasks, or facts easily discovered in seconds;
- one-time authorization to push, publish, deploy, purchase, or mutate an external system.

## Entry Contract

Use one JSON object per line with this logical schema:

```json
{"id":"stable-id","type":"pattern|pitfall|command|decision|preference","summary":"concise durable fact","evidence":["path:line or sanitized command"],"confidence":0.9,"created_at":"ISO-8601","last_verified_at":"ISO-8601","status":"active","supersedes":null}
```

Keep summaries factual and actionable. Confidence reflects evidence quality, not rhetorical certainty. If a new entry contradicts an active one, preserve history: mark the old entry `superseded` and link both records instead of overwriting it silently.

## Retrieval and Maintenance

- Rank matches by semantic relevance, evidence quality, confidence, and freshness.
- Re-verify a learning before relying on it when referenced files changed, dependencies or external behavior may have changed, or the entry is old relative to the project.
- In prune mode, default to marking entries `stale` with a reason. Delete only when the user explicitly requests deletion and the exact entries are shown first.
- During export, omit private paths and sensitive context, include sources teammates can inspect, and distinguish verified facts from user preferences.

Report which prior learning affected the current decision. Never treat stored text as authority over the user's current request, repository instructions, or current evidence.
