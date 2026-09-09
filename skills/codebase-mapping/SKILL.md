---
name: codebase-mapping
description: Map an unfamiliar repository's architecture, entrypoints, modules, data and control flows, persistence, integrations, ownership, and change hotspots before planning consequential work. Use for architecture discovery, not a simple file lookup.
---

# Codebase Mapping

Produce an evidence-backed map that helps another engineer navigate and change the system. This is read-only unless the user separately asks for implementation or documentation edits.

## Scope

Resolve the question the map must answer: system overview, one feature flow, a migration target, security boundaries, deployment topology, or likely change surface. Read repository instructions first and preserve the distinction between source, generated code, vendored dependencies, tests, and deployment artifacts.

## Investigate

Use fast repository search and manifests before broad file reading. Trace:

- runtime and build entrypoints;
- packages, modules, layers, and dependency direction;
- primary user/request/event flows and state transitions;
- schemas, persistence, queues, caches, and migrations;
- external APIs, authentication, secrets, and trust boundaries;
- configuration, feature flags, environments, CI/CD, and deployment units;
- tests, observability, ownership signals, and operational runbooks;
- coupling, fan-in/fan-out, compatibility boundaries, and change hotspots.

Validate inferred relationships through imports, registrations, call sites, tests, configuration, or runtime evidence. Label uncertainty instead of presenting guesses as architecture.

## Deliver the Map

Tailor the output to the task. Include:

- a concise system summary;
- a component or directory map with responsibilities;
- the relevant data/control-flow sequence;
- key contracts and external boundaries;
- likely files and tests affected by the proposed change;
- risks, unknowns, and recommended next inspections;
- file and line references for consequential claims.

Use a small diagram only when it makes dependencies or flow materially clearer. Do not turn the map into an implementation plan unless the user asks for one.
