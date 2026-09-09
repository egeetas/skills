---
name: dependency-management
description: Evaluate, add, remove, upgrade, or audit dependencies for necessity, compatibility, vulnerabilities, licensing, reproducibility, and supply-chain risk.
---

# Dependency Management

Use this skill for dependency changes, lockfile updates, package-manager migrations, dependency incident remediation, and repository-wide dependency audits.

## Decision Rules

- Confirm the need cannot be met clearly with the standard library or an existing dependency.
- Match the repository's package manager and versioning conventions.
- Check current maintenance, release recency, compatibility, transitive footprint, license, and relevant advisories from authoritative sources.
- Prefer the smallest supported version range consistent with the repository's policy; do not silently introduce floating versions.
- Explain native build, platform, runtime, bundle-size, and operational consequences.

## Audit

- Build the dependency inventory from manifests and lockfiles rather than package names mentioned in source alone.
- Use ecosystem-native audit and outdated-package tools when available; record database freshness and tool limitations.
- Identify direct and transitive vulnerabilities, affected versions, reachable usage where determinable, and the minimum safe version.
- Flag incompatible or unknown licenses for human or legal review without making unsupported legal conclusions.
- Find unused, duplicated, abandoned, unpinned, or unexpectedly sourced packages, but verify dynamic and plugin imports before removal.
- Review maintainer or ownership changes, suspiciously similar names, registry/source changes, integrity metadata, and untrusted install hooks where risk warrants it.
- Group findings by root dependency and distinguish confirmed exposure from advisory-only or unreachable risk.

## Changes

Update manifests and lockfiles together using the package manager. Do not hand-edit generated lockfile sections. For upgrades, read migration notes and identify breaking changes before editing code.

Verify installation reproducibility, build, tests, runtime behavior, and the dependency tree. Report why the dependency is needed, version selected, vulnerability and license findings, transitive effects, residual risk, and rollback method. Never upgrade, remove, or publish dependency changes when the user requested only an audit.
