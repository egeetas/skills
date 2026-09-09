# Audit report schema

Use one record per independently actionable finding.

## Summary

- Repository and revision audited
- Commands run and their outcomes
- Scope exclusions and environmental limits
- Confirmed finding counts by severity

## Finding

- Title: concise observed defect
- Severity: critical, high, medium, or low
- Confidence: high, medium, or low
- Affected locations: file and tight line range
- Trigger: state or input required
- Observed impact: user, security, data, or operational effect
- Evidence: output, trace, test, or verified code path
- Reproduction: minimal deterministic steps
- Expected behavior: contract or justified expectation
- Suggested direction: bounded fix guidance, not an unverified patch
- Duplicate search: queries and matching issues checked

Keep hypotheses outside confirmed findings. Group symptoms with one root cause into one record.
