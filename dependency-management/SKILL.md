---
name: dependency-management
description: Add, remove, or upgrade software dependencies with necessity, compatibility, maintenance, license, security, and rollback checks.
---

# Dependency Management

Use this skill for dependency changes, lockfile updates, package-manager migrations, and dependency incident remediation.

## Decision Rules

- Confirm the need cannot be met clearly with the standard library or an existing dependency.
- Match the repository's package manager and versioning conventions.
- Check current maintenance, release recency, compatibility, transitive footprint, license, and relevant advisories from authoritative sources.
- Prefer the smallest supported version range consistent with the repository's policy; do not silently introduce floating versions.
- Explain native build, platform, runtime, bundle-size, and operational consequences.

## Changes

Update manifests and lockfiles together using the package manager. Do not hand-edit generated lockfile sections. For upgrades, read migration notes and identify breaking changes before editing code.

Verify installation reproducibility, build, tests, runtime behavior, and the dependency tree. Report why the dependency is needed, version selected, license/security findings, and rollback method.
