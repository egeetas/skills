---
name: performance-investigation
description: Investigate latency, throughput, memory, CPU, I/O, bundle size, or scalability using measurement, profiling, experiments, and benchmarks.
---

# Performance Investigation

Measure before optimizing. A performance suspicion is not evidence of a bottleneck.

## Workflow

1. Define the affected workload, user impact, target metric, percentile, environment, and acceptable threshold.
2. Establish a repeatable baseline with representative data and controlled conditions.
3. Profile the relevant resource: wall time, CPU, allocations, memory growth, queries, network, disk, rendering, or bundle composition.
4. Rank bottlenecks by measured contribution and form falsifiable hypotheses.
5. Change one factor at a time and compare against the same baseline.
6. Check correctness, cold/warm behavior, tail latency, variance, resource trade-offs, and scale characteristics.
7. Add a stable regression benchmark or budget when the project can maintain it.

Report environment, commands, dataset, repetitions, before/after results, uncertainty, trade-offs, and remaining bottlenecks. Do not generalize microbenchmark results beyond their measured workload.
