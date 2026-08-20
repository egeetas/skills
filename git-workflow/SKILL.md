---
name: git-workflow
description: Apply consistent branch, commit, staging, rebase, merge, and push conventions while preserving history and unrelated work.
---

# Git Workflow

Repository-specific rules take precedence. When none exist, use the defaults below.

## Defaults

- Branch names: `<type>/<short-kebab-description>`, such as `feat/session-timeout` or `fix/null-profile`.
- Commits: Conventional Commits, imperative and scoped to one coherent change.
- Keep formatting-only, generated, and functional changes separate when that improves reviewability.
- Prefer rebase for updating a private feature branch and the repository's configured merge policy for integration.

## Safety and Authorization

Inspect status and diffs before staging. Stage only explicitly selected paths; never use broad staging when unrelated work exists. Do not rewrite shared history, force-push, delete branches, or discard changes without explicit authorization.

Staging, committing, pushing, opening a pull request, merging, tagging, and publishing a release are distinct external actions. Perform only the actions explicitly authorized for the current task. Report the branch, staged paths, commit, and remote target before or immediately after the corresponding action as appropriate.
