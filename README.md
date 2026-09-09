# Codex Engineering Skills

[![Validate skills](https://github.com/egeetas/skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/egeetas/skills/actions/workflows/validate-skills.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Codex skills](https://img.shields.io/badge/Codex_skills-49-111827.svg)](CATALOG.md)

An opinionated, production-minded library of 49 focused Codex skills for taking software from an uncertain idea through implementation, verification, release, and operations.

[Türkçe](README.tr.md) · [Catalog](CATALOG.md) · [Setup](SETUP.md) · [Authoring guide](docs/skill-authoring.md) · [Changelog](CHANGELOG.md)

## Why this collection

- Complete lifecycle coverage without one giant catch-all prompt.
- Narrow descriptions, 147 per-skill cases, and focused boundary cases for predictable discovery.
- Explicit authorization boundaries around fixes, publishing, deployment, and deletion.
- Portable plugin metadata, standalone installation, validation, CI, and optional subagent presets.
- Reusable scripts, schemas, rubrics, and document templates where they improve repeatability.

## Quick start

Clone the repository, then install the default `core-development` pack:

```bash
git clone https://github.com/egeetas/skills.git "$HOME/.local/share/egeetas-skills"
cd "$HOME/.local/share/egeetas-skills"
./scripts/install.sh
```

Choose packs, individual skills, or the entire library:

```bash
./scripts/install.sh --list-packs
./scripts/install.sh --pack product-architecture --pack frontend-mobile
./scripts/install.sh code-review test-and-fix-loop
./scripts/install.sh --all --with-agents
```

Or ask Codex:

```text
Use $skill-installer to install skills from https://github.com/egeetas/skills
```

See [SETUP.md](SETUP.md) for plugin, user-level, and repository-level installation.

## Skill packs

| Pack | Skills | Purpose |
| --- | ---: | --- |
| `core-development` | 17 | Implementation, testing, review, git, issues, PRs, and releases |
| `product-architecture` | 7 | Product validation, requirements, architecture, APIs, and bootstrap |
| `frontend-mobile` | 9 | Design, browser quality, accessibility, visual checks, and mobile delivery |
| `security-operations` | 7 | Security, migrations, observability, performance, and incidents |
| `project-intelligence` | 3 | Durable learnings, session handoffs, and retrospectives |
| `ai-documentation` | 6 | MCP, AI evaluation and safety, prompts, and technical writing |

Every skill appears in exactly one pack. The full [catalog](CATALOG.md) explains each skill and its closest boundary.

## Usage

Use `/skills` in Codex or invoke a skill explicitly:

```text
$product-strategy-review challenge the demand evidence for this idea
$codebase-mapping map the payment flow before we change it
$test-and-fix-loop run the relevant checks and fix confirmed failures
$issue-to-pr-workflow deliver issue 42 as a verified pull request
```

`software-development-workflow` is intentionally explicit-only: invoke it when you want orchestration across several lifecycle stages. Focused skills may be selected automatically when their descriptions match the task.

## Repository structure

```text
skills/<name>/             Skill instructions and optional resources
packs/                     Curated install selections
agent-presets/             Optional Codex custom subagents
scripts/                   Installer, validator, and routing eval runner
tests/                     Boundary and full routing corpora
templates/                 New-skill template
plugin.json                Portable plugin manifest
.codex-plugin/plugin.json  Compatibility manifest
.agents/plugins/           Marketplace metadata
```

## Development

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/run_routing_evals.py --dry-run
```

Development tools require Python 3.11 or newer; skill use itself does not require Python unless a selected skill runs one of its helper scripts.

The real model-backed routing evaluator uses your configured Codex account and may consume usage:

```bash
python3 scripts/run_routing_evals.py --limit 12 --output routing-report.json
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change. The [authoring guide](docs/skill-authoring.md) explains how `SKILL.md`, `agents/openai.yaml`, scripts, references, assets, packs, and evals work together.

## License and attribution

Original work is licensed under [MIT](LICENSE). Adapted material retains its source license; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [`LICENSES/`](LICENSES/).

Official references: [Codex skills](https://developers.openai.com/codex/skills) · [Codex plugins](https://developers.openai.com/codex/plugins/build)
