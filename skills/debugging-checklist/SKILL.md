---
name: debugging-checklist
description: Diagnose reproducible software failures systematically using evidence, controlled hypotheses, isolation, root-cause analysis, and regression verification.
---

# Debugging Checklist

Diagnose before changing code. A request to investigate does not by itself authorize a fix.

## Workflow

1. Record expected behavior, actual behavior, environment, version, inputs, and exact reproduction steps.
2. Reproduce the failure with the smallest safe command or test. Preserve the first useful error, stack trace, and timestamps.
3. Check recent relevant changes, configuration, dependencies, logs, and boundary conditions.
4. Reduce the problem to the smallest failing component or input.
5. Form a small set of falsifiable hypotheses ranked by evidence.
6. Change one variable at a time and record what each experiment proves or disproves.
7. Identify the root cause, not only the failing symptom.
8. If a fix is authorized, implement the narrow correction and add a regression test that fails before and passes after.
9. Re-run the reproduction and proportional broader checks.

Never hide uncertainty. Distinguish confirmed facts, strong inferences, and open hypotheses in the final report.
