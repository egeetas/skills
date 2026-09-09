---
name: incident-response
description: Coordinate production incident diagnosis, mitigation, communication, recovery verification, timeline capture, and blameless follow-up.
---

# Incident Response

Prioritize safety and service restoration over root-cause completeness during an active incident.

## Active Incident

1. Record start time, reporter, affected users, symptoms, severity, and known scope.
2. Assign or identify incident lead, operations owner, and communication owner when a team is involved.
3. Preserve evidence and establish reliable health signals.
4. Contain impact with the smallest reversible mitigation: disable, rollback, isolate, rate-limit, or fail over as authorized.
5. Verify recovery from user-facing and system signals; continue monitoring through a defined stability window.
6. Maintain a timestamped timeline of decisions, commands, changes, and outcomes.

Production mutations, customer communications, rollbacks, and failovers require explicit authorization unless an established runbook grants it.

## Follow-up

Document impact, root cause, contributing factors, detection gaps, what helped, what delayed recovery, and owned actions with deadlines. Keep the review blameless and focus on system improvements.
