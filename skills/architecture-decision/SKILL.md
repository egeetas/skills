---
name: architecture-decision
description: Evaluate and document consequential software architecture choices, alternatives, trade-offs, migration paths, and operational consequences.
---

# Architecture Decision

Use this skill for decisions that cross module boundaries, introduce durable infrastructure, change public contracts, or are expensive to reverse. Do not require an ADR for routine implementation choices.

## Workflow

1. State the problem, decision deadline, and why the current state is insufficient.
2. Identify constraints: compatibility, scale, security, latency, cost, team skills, operations, and delivery time.
3. Describe viable alternatives, including retaining the current design when meaningful.
4. Compare alternatives against the same explicit criteria. Separate known facts from assumptions.
5. Recommend one option and explain why its trade-offs fit the constraints.
6. Record consequences, failure modes, observability needs, migration stages, rollback, and unresolved questions.

Prefer the least complex option that satisfies current evidence. Do not invent product or business decisions; surface missing choices.

## ADR Output

Return: context, decision, alternatives considered, rationale, consequences, migration/rollback, and follow-ups. Mark the decision as proposed or accepted based on the user's authority.
