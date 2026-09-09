---
name: webapp-testing
description: Test a local or preview web app in a real browser for user flows, rendered state, accessibility, console or network errors, and responsive layouts.
license: Apache-2.0; see ../LICENSES/Apache-2.0.txt and ../THIRD_PARTY_NOTICES.md
---

# Web Application Testing

Verify observable browser behavior with the repository's existing browser-test framework when possible. Prefer Playwright for new browser automation unless the project already standardizes on another tool.

## Prepare

1. Read repository instructions and discover documented install, server, seed, and test commands.
2. Identify the smallest user journey that proves the requested behavior and the required test data or authentication state.
3. Reuse an already-running server when safe. If starting one, use the project's command, wait for a deterministic readiness signal, record the process, and stop only the process you started.
4. Never point destructive tests at production or shared data without explicit authorization.

## Reconnaissance

Inspect the rendered accessibility tree or DOM, a screenshot, browser console, and failed network requests before guessing selectors or causes. Wait for a page-specific condition such as a visible heading, URL transition, API response, or loading indicator removal; do not rely on `networkidle` when background traffic can continue indefinitely.

Prefer selectors in this order:

1. accessible role and name;
2. associated label or visible text;
3. stable project-owned test ID;
4. CSS selectors only when no semantic handle exists.

## Test

- Exercise the behavior as a user would, including meaningful success, validation, authorization, loading, empty, and failure states.
- Assert outcomes and state transitions, not implementation details or arbitrary time delays.
- Capture console exceptions, unhandled promise rejections, relevant failed requests, and screenshots or traces for failures.
- Check keyboard access and focus behavior for changed interactive flows.
- Cover representative narrow and wide viewports when layout is material.
- Add a regression test for a confirmed bug when it can run deterministically.

Run the focused test first, then the relevant browser suite and supporting lint/type checks in proportion to the change. Treat flaky behavior as a finding to investigate, not a reason to add sleeps or retries blindly.

## Report

Return the tested URL/environment, commands, scenarios, pass/fail results, evidence paths, fixes made if requested, skipped coverage, and residual risk. Do not claim a flow works if a required service or credential prevented verification.
