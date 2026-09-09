---
name: implementation-standards
description: Implement maintainable production code aligned with repository architecture, language idioms, contracts, error handling, and boundaries.
---

# Implementation Standards

Follow existing architecture and conventions unless the request explicitly changes them. Prefer clarity over novelty.

## Standards

- Keep modules cohesive and dependencies directional; separate domain logic from I/O and framework glue.
- Make public contracts, types, nullability, ownership, and side effects explicit.
- Validate untrusted data at boundaries and preserve useful error context without exposing secrets.
- Handle resource cleanup, cancellation, timeouts, retries, and concurrency where the execution model requires them.
- Keep configuration external to code and never embed credentials.
- Log actionable events with stable context; avoid sensitive data and high-volume noise.
- Remove dead branches introduced by the change, but do not perform unrelated cleanup.
- Add tests at the lowest reliable layer for new behavior and regressions.

Before finishing, run the repository's formatter, static checks, tests, and build in proportion to the change. Explain any deliberate deviation from established conventions.
