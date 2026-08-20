---
name: prompt-versioning
description: Change and version production prompts with clear contracts, fixtures, evaluation evidence, compatibility checks, rollout controls, and rollback.
---

# Prompt Versioning

Treat prompts that affect production behavior as code and configuration, not untracked prose.

## Workflow

- Identify the prompt's inputs, expected output contract, model/tool dependencies, safety constraints, and downstream parsers.
- Make one purposeful change at a time and record its rationale.
- Keep prompts in version control with stable identifiers and avoid duplicating conflicting instructions across layers.
- Evaluate against representative, adversarial, and regression cases; check output validity, quality, safety, latency, and cost.
- Preserve compatibility with schemas and tool contracts or version them together.
- Define staged rollout, monitoring, comparison, and rollback to the previous prompt/model configuration.

Do not silently change the model while evaluating a prompt change. Report both prompt and model versions with results.
