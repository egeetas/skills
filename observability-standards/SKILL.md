---
name: observability-standards
description: Design and review logs, metrics, traces, health checks, dashboards, and alerts that make software behavior and failures diagnosable.
---

# Observability Standards

Instrument user-visible behavior and operational boundaries, not every line of code.

## Signals

- Logs: structured event names, severity, stable context, request or correlation ID, and actionable failure details without secrets or unnecessary personal data.
- Metrics: rates, errors, duration, saturation, queue depth, retries, and domain success indicators with bounded-cardinality labels.
- Traces: meaningful service and dependency boundaries with propagated context and sampled detail.
- Health: distinguish process liveness, readiness, dependency health, and degraded operation.

## Alerts and Dashboards

Alert on symptoms tied to user or operational impact. Each alert should identify ownership, severity, threshold/window, dashboard, and first diagnostic action. Avoid alerts that are unactionable, duplicate, or based on unbounded cardinality.

Verify instrumentation by exercising the behavior and locating the resulting signal. State retention, privacy, cost, and sampling trade-offs.
