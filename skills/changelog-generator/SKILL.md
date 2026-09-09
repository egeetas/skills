---
name: changelog-generator
description: Generate factual changelogs or release notes from an explicit git, tag, date, or pull-request range. Requires verifiable source material.
---

# Changelog Generator

Turn verified repository changes into release communication without inventing impact or silently hiding operationally important work.

## Resolve the Range

Determine the repository, base and head revision or exact date range, target version, audience, and desired format. Confirm ambiguous ranges before producing a release artifact. Inspect tags, commits, pull requests when available, and the actual diff for claims that commit subjects alone cannot support.

For a git revision range, prefer `scripts/collect_git_range.py --base <ref> --head <ref>` to collect commit, file, and diff-stat evidence before drafting.

Follow an existing changelog style, release template, and versioning policy. Treat issue and PR text as context to verify against code, not automatically true release notes.

## Classify Changes

Group only categories supported by the range, such as:

- breaking changes and required migrations;
- security fixes with disclosure-safe wording;
- new user-visible capabilities;
- behavior improvements and performance changes;
- bug fixes;
- deprecations and removals;
- operator, configuration, dependency, or platform changes.

Exclude merge noise, formatting-only work, and internal refactors from customer notes unless they materially change behavior, risk, operations, or compatibility. Preserve important internal changes in engineering or operator notes when the chosen format supports them.

## Write and Verify

Use plain language, lead with user or operator impact, and avoid marketing claims unsupported by evidence. Link issues or pull requests consistently when available. State migration steps, minimum versions, flags, configuration changes, and known limitations precisely.

Cross-check every entry against the selected range, deduplicate related commits, and distinguish confirmed behavior from inference. Return the resolved range, output format, omitted categories, and any changes that need human product/security wording.

Writing a local changelog file may be part of an explicit request. Publishing a release, creating a tag, or pushing changes requires explicit authorization.
