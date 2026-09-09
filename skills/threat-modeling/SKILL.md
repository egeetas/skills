---
name: threat-modeling
description: Threat-model a feature or system by mapping assets, actors, trust boundaries, attack paths, mitigations, assumptions, and residual risk.
---

# Threat Modeling

Use before or during design of sensitive, exposed, privileged, multi-tenant, payment, identity, file, or data-processing systems.

## Workflow

1. Define scope, architecture, data flows, assets, actors, dependencies, and deployment environment.
2. Mark trust boundaries, entry points, privilege transitions, storage, and third-party calls.
3. Enumerate credible abuse cases across identity spoofing, tampering, disclosure, denial, privilege escalation, replay, supply chain, and business logic.
4. Rank threats by preconditions, likelihood, impact, detectability, and affected assets.
5. Map preventive, detective, and recovery controls; identify owners and validation methods.
6. Record assumptions, accepted risk, unresolved questions, and triggers for re-review.

Prefer concrete system-specific attack paths over generic checklist output. Do not perform destructive exploitation or expose sensitive findings publicly.
