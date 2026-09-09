---
name: security-baseline
description: Review software changes and designs for practical security risks across trust boundaries, identity, input, secrets, data, dependencies, and deployment defaults.
---

# Security Baseline

Use for security-focused reviews, sensitive features, public endpoints, authentication, data access, file handling, network calls, and deployment hardening. Ordinary code changes do not require a deep audit unless risk warrants it.

## Review Areas

- Assets, actors, trust boundaries, entry points, and abuse cases.
- Authentication, session lifecycle, authorization, tenancy, and least privilege.
- Input validation, output encoding, injection, request forgery, path traversal, unsafe deserialization, and file upload/download.
- Secrets, cryptography, token handling, sensitive logs, privacy, retention, and error disclosure.
- Dependency provenance, vulnerable versions, build pipeline, configuration, and secure defaults.
- Rate limits, replay, idempotency, timeouts, resource exhaustion, and abuse monitoring.

## Findings

Require a credible attack path or violated security invariant. State preconditions, impact, evidence, severity, confidence, and the smallest effective remediation. Avoid destructive exploitation and never expose real secrets. Route plausible undisclosed vulnerabilities through the repository's approved private reporting process.
