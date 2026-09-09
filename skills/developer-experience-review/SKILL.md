---
name: developer-experience-review
description: Plan or test developer experience for an API, CLI, SDK, library, platform, or technical docs. Do not use for non-developer UX.
---

# Developer Experience Review

Evaluate the path from discovery to repeatable success, not only whether the interface is technically correct. Choose `plan` mode for a proposed experience and `live` mode for an implementation that can be exercised. Use both when comparing intended and actual behavior.

## Establish Scope

- Infer the primary developer persona from the product and documentation, then state the inference and confirm it only if a different persona would change the review.
- Define the first meaningful success. Installing a package is not success if the developer's real goal is receiving an event, completing an API call, or deploying a working example.
- Declare the environment, credentials, network access, accounts, and external writes the review would require. Use disposable local resources by default and obtain authorization before creating accounts, consuming paid services, or changing external systems.

## Plan Mode

Trace the proposed journey:

1. discovery and choosing the correct entry point;
2. prerequisites, installation, authentication, and configuration;
3. first meaningful success and its estimated time;
4. debugging a representative failure;
5. extending the first example into a realistic use case;
6. upgrading, removing, or rolling back the integration.

Inspect actual interfaces and documentation where they exist. Identify every context switch, unexplained prerequisite, irreversible step, hidden default, ambiguous error, and place where the developer must guess. Compare current competitors or platform conventions only when they materially affect expectations, using current primary sources.

## Live Mode

- Start from the public entry point a new developer would see; do not rely on undocumented maintainer knowledge.
- Follow the documented commands exactly in a clean temporary environment when practical.
- Record elapsed time to first meaningful success, commands attempted, decision points, and sanitized evidence for failures.
- Exercise at least one likely error path and judge whether the message explains cause, location, and recovery.
- Check examples for copy-paste correctness, version compatibility, placeholder clarity, secret handling, and cleanup.
- For web documentation or consoles, use real-browser testing when available and capture console, network, accessibility, and responsive problems relevant to the journey.

Never expose credentials or paste secrets into the report. Do not weaken security to improve onboarding.

## Scorecard

Score only dimensions supported by evidence on a 0-10 scale:

- discoverability and prerequisites;
- time to first meaningful success;
- API, CLI, or SDK ergonomics;
- error quality and recovery;
- documentation and examples;
- upgrade, compatibility, and removal path.

For each score, cite the observed step or file, explain the friction and consequence, and describe what a clearly better experience would look like. When a prior plan exists, show predicted versus observed time and friction rather than silently replacing the baseline.

Finish with the top three improvements ordered by user impact and effort, quick wins, unresolved risks, and a reproducible verification path. Report findings only unless the user also asked for fixes or issue creation.
