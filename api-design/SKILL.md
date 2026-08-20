---
name: api-design
description: Design and review stable HTTP, RPC, event, or library APIs with explicit contracts, errors, authorization, idempotency, pagination, compatibility, and evolution.
---

# API Design

Start from consumer tasks and domain semantics rather than transport mechanics.

## Contract

- Define resources/actions, inputs, outputs, invariants, ownership, authorization, and side effects.
- Specify validation, error categories, retryability, timeouts, cancellation, and partial failure.
- Use idempotency for retryable mutations and define concurrency/conflict semantics.
- Design pagination, filtering, ordering, field selection, limits, and consistency explicitly.
- Bound payloads and document rate limits, quotas, and abuse controls.
- Use stable names and additive evolution; document deprecation, versioning, and migration for breaking changes.

Provide representative success and failure examples plus contract tests. For event APIs, also define delivery guarantees, ordering, duplication, schema evolution, replay, and dead-letter handling.
