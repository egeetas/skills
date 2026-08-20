---
name: ai-evaluation
description: Build representative, reproducible evaluations for AI features using explicit tasks, datasets, graders, baselines, slices, and release gates.
---

# AI Evaluation

Use for model, prompt, retrieval, agent, or tool-workflow quality decisions. Do not rely on a few hand-picked examples.

## Evaluation Design

- Define the user task, failure costs, quality dimensions, latency/cost constraints, and release decision.
- Build a versioned dataset from representative production-like cases, critical edge cases, adversarial inputs, and known regressions. Remove or protect sensitive data.
- Split data used for iteration from held-out evaluation where overfitting is plausible.
- Use deterministic graders for objective properties and calibrated rubrics or pairwise review for judgment-heavy quality.
- Track aggregate scores and important slices; preserve raw examples for error analysis.
- Compare against a frozen baseline and repeat stochastic runs enough to understand variance.

Report dataset/version, configuration, grader limits, scores, confidence/variance, regressions, cost/latency, and release recommendation. Add confirmed failures to the regression set.
