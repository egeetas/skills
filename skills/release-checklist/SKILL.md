---
name: release-checklist
description: Prepare and verify general software releases across versioning, artifacts, migrations, security, smoke tests, rollout, and rollback. Use mobile-release for app stores.
---

# Release Checklist

Use this skill to prepare or execute a release. Preparation does not authorize tagging, publishing, deploying, or changing production.

## Pre-release

- Resolve the release scope and versioning policy.
- Confirm the working tree, intended commit, CI status, tests, static checks, and reproducible build.
- Review dependency, secret, license, vulnerability, configuration, and compatibility changes.
- Verify migrations, backups, feature flags, ordering constraints, and rollback.
- Update changelog, version metadata, documentation, and breaking-change notices.
- Build and inspect the actual artifact that will be released.

## Rollout

Define owners, stages, health signals, smoke tests, monitoring window, abort thresholds, and rollback commands before production mutation.

Require explicit authorization immediately before each external action such as tag creation, release publication, deployment, or production migration. After rollout, report artifact/version, verification evidence, observed health, and remaining follow-ups.
