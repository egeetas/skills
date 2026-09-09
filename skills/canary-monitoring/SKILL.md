---
name: canary-monitoring
description: Monitor a new web release against a baseline for persistent failures, errors, performance regressions, and visual anomalies. Do not deploy.
---

# Canary Monitoring

Observe a release immediately after deployment and distinguish persistent regressions from transient noise. This skill is read-only: deployment, rollback, feature-flag changes, and production fixes require separate explicit authorization.

## Establish the Contract

Before monitoring, resolve:

- deployment identifier, production or canary URL, and expected version;
- critical pages and user flows;
- monitoring duration and interval;
- a pre-deploy baseline or, when none exists, the limited health-check behavior;
- expected console or network noise, authentication needs, health signals, and abort thresholds;
- owner and exact rollback procedure, without executing it.

If credentials or a logged-in browser are required, use the user's available authenticated surface without exposing session material. Never probe destructive actions, submit real transactions, or create persistent data unless the user explicitly scoped and authorized a safe test account and cleanup plan.

## Capture and Compare

Use a real browser when available. For each critical page or flow, capture comparable evidence:

- navigation success, HTTP failures, and broken critical resources;
- uncaught exceptions and new console errors;
- failed or materially slower network requests;
- load and interaction timings available from the environment;
- screenshot or rendered-state evidence for missing content and visual breakage;
- a lightweight functional assertion tied to the page's purpose.

Compare changes against the baseline rather than generic absolutes. Without a baseline, report observed health but do not label existing errors as deployment regressions.

## Alert Discipline

Classify a finding by user impact and confidence:

- **Critical:** core flow unavailable, widespread page failure, or clear data/security risk.
- **High:** new persistent exception or broken critical interaction.
- **Medium:** material performance or non-core functional regression.
- **Low:** limited visual or secondary-resource issue.

Except for a clear critical failure, require the same symptom in at least two consecutive checks before escalating. Preserve timestamps and screenshots or logs for every alert. If evidence conflicts, say so rather than averaging it away.

When a threshold is reached, promptly report the affected page or flow, first and latest occurrence, baseline versus current signal, confidence, and the prepared rollback or investigation option. Do not silently continue until the window ends when user action is time-sensitive.

## Final Report

Return:

- monitored version, URLs, duration, intervals, and coverage;
- baseline source and any comparability limitations;
- per-page or per-flow status and evidence;
- alerts, including transient findings that did not persist;
- verdict: `healthy`, `degraded`, `broken`, or `inconclusive`;
- recommendation to continue rollout, hold, investigate, or roll back, with explicit thresholds;
- gaps and the next monitoring window.

Update a baseline only after the user accepts a healthy release as the new reference. Saving reports, scheduling recurring monitoring, rollback, deployment changes, and issue creation each require the corresponding authorization.
