---
name: mobile-release
description: Prepare iOS or Android releases with signing, versioning, store metadata, privacy, staged rollout, device checks, monitoring, and rollback.
---

# Mobile Release

Preparation does not authorize signing, uploading, submitting for review, or releasing to users.

## Checklist

- Confirm version/build numbers, release branch/commit, changelog, supported OS/devices, and backend compatibility.
- Run clean release builds, tests, static analysis, startup/upgrade checks, and representative device flows.
- Verify signing identities, entitlements, capabilities, deep links, notifications, background modes, and environment endpoints without exposing credentials.
- Review permissions, privacy declarations, data-safety forms, tracking, screenshots, localization, accessibility, and store metadata.
- Test install, update, offline, interrupted network, authentication, purchase, and migration behavior as applicable.
- Define phased rollout, crash/ANR and business metrics, abort thresholds, backend flags, and recovery for a release that cannot be instantly rolled back.

Require explicit authorization for each store or distribution mutation and report the exact artifact and target channel.
