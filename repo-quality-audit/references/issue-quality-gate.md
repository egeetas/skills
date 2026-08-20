# Issue Quality Gate

Create or publish an issue only when all required fields are supported by evidence.

## Required Evidence

- Concise problem statement and severity.
- Affected version, environment, module, and exact locations where available.
- Minimal reproduction steps or a deterministic failing test.
- Expected and actual behavior.
- Logs, stack trace, test output, or code-path evidence with secrets removed.
- User, security, data, or operational impact.
- Duplicate search terms and result.
- Suggested direction clearly labeled as a proposal, not a confirmed fix.

## Publication Rules

- Publication requires explicit user authorization and an authenticated GitHub target.
- Follow repository issue templates and disclosure rules.
- Do not publicly disclose a plausible exploitable vulnerability; prepare a private report or ask for the approved security channel.
- Group symptoms sharing one root cause into one issue.
- If evidence is incomplete, return an investigation note instead of an issue.
