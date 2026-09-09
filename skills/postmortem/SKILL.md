---
name: postmortem
description: Produce a blameless incident postmortem with verified impact, timeline, root cause, contributing factors, response gaps, and owned actions.
---

# Postmortem

Use after an incident is stable. Base the document on logs, timelines, changes, and participant evidence; label uncertainty.

## Structure

- Executive summary and user/business impact with dates, duration, scope, and severity.
- Detection, response, mitigation, recovery, and verification timeline.
- Technical root cause and causal chain, not only the component that failed.
- Contributing organizational, process, dependency, design, and observability factors.
- What worked, what slowed response, and where defenses failed or were absent.
- Corrective actions across prevention, detection, containment, recovery, documentation, and rehearsal.

Actions must have an owner, priority, measurable completion condition, and target date when the organization provides them. Avoid blame, vague commitments, and unsupported counterfactuals. Use [the postmortem template](assets/postmortem-template.md) when no organizational template exists. Publishing or communicating the postmortem requires explicit authorization.
