---
name: database-migrations
description: Design and verify safe schema or data migrations with compatibility, batching, observability, rollback, and zero-downtime considerations.
---

# Database Migrations

Use for schema changes, backfills, data corrections, storage-engine changes, and migration incident analysis.

## Plan

- Identify database/version, table size, traffic, replication, locks, constraints, and deployment order.
- Prefer expand-migrate-contract: add compatible structures, deploy dual-compatible code, backfill, verify, switch reads/writes, then remove legacy structures later.
- Separate schema migration from large data backfills when their operational profiles differ.
- Make long work resumable, idempotent, rate-limited, and observable.
- Define correctness queries, progress metrics, abort thresholds, backup requirements, and rollback or forward-fix strategy.

Do not assume DDL is transactional or non-blocking. Verify behavior for the actual database and version. Production execution requires explicit authorization immediately before the migration.

Test migrations against representative data and both old/new application versions when rolling deployments are possible.
