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

## Cross-Model Benchmark Mode

Use this mode when the decision is which model or provider best performs a defined task. It compares models; it does not replace a representative evaluation design.

- Freeze the same prompt, tools, context, dataset, timeouts, and output contract for every candidate. Record unavoidable provider differences.
- Resolve currently available model identifiers from the provider or configured environment; do not rely on remembered names or silently substitute a model.
- Run representative repetitions when stochastic variance could change the ranking. Randomize output order before human or model judging when practical.
- Prefer deterministic graders for factual and structural requirements. For judgment-heavy quality, use a published rubric and blinded pairwise or independent scoring; never let a model grade its own output as the only judge.
- Track task success, important slice failures, latency distribution, token use, estimated cost, tool failures, and variance. A faster or cheaper model is not better when it misses release-critical cases.
- Show expected external cost before a paid benchmark and obtain approval when the run would create material spend. Never expose provider credentials in commands, artifacts, or reports.
- Save the exact configuration and raw sanitized outputs when the user requests a reproducible baseline. Compare future runs only when the task, dataset, grader, and environment remain compatible.

Recommend a model per workload or quality tier when the evidence supports segmentation; do not force a single global winner. State uncertainty and rerun criteria.
