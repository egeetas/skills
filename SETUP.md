# Setup

[Türkçe](SETUP.tr.md)

The installer requires Bash. Repository validation and helper scripts require Python 3.11 or newer.

## Install as a Codex plugin

The repository contains the portable `plugin.json`, compatibility `.codex-plugin/plugin.json`, and marketplace metadata expected by current Codex plugin tooling.

```bash
codex plugin marketplace add egeetas/skills --ref v1.0.0
codex plugin add codex-engineering-skills@egeetas-skills
```

Restart Codex if the newly installed skills do not appear. Use `/skills` or type `$` to open the skill selector.

## Install with the repository script

Clone into a stable location:

```bash
git clone https://github.com/egeetas/skills.git "$HOME/.local/share/egeetas-skills"
cd "$HOME/.local/share/egeetas-skills"
```

The default command symlinks the 17-skill `core-development` pack into `$HOME/.agents/skills`:

```bash
./scripts/install.sh
```

Discover and choose content:

```bash
./scripts/install.sh --list
./scripts/install.sh --list-packs
./scripts/install.sh --pack frontend-mobile --pack security-operations
./scripts/install.sh product-strategy-review codebase-mapping
./scripts/install.sh --all
```

Add the optional `code-explorer`, `quality-reviewer`, and `test-investigator` presets under `$HOME/.codex/agents`:

```bash
./scripts/install.sh --all --with-agents
```

The installer never overwrites an existing file, directory, or unrelated symlink.

## Repository-scoped installation

Copy selected content into a project's `.agents/skills` directory:

```bash
./scripts/install.sh --scope repo --target /absolute/path/to/project --pack core-development
```

Add `--with-agents` to copy presets into `<project>/.codex/agents`. Repository scope uses copies, so future upstream changes are not automatic; review them as an explicit diff.

## Update and verify

```bash
git -C "$HOME/.local/share/egeetas-skills" pull --ff-only
python3 "$HOME/.local/share/egeetas-skills/scripts/validate_skills.py"
```

User-level symlinks expose the updated checkout immediately. The installer deliberately does not update existing repository copies. Compare the source and destination, move or remove only the reviewed skill directories you intend to replace, then run the same install command again.

## Troubleshooting

- Duplicate skill names are not merged. Remove or disable stale copies.
- A conflict means the installer deliberately preserved an existing destination.
- Start Codex within a repository path that includes its `.agents/skills` directory.
- Run `python3 scripts/validate_skills.py` to distinguish malformed metadata from discovery problems.

Official documentation: [Codex skills](https://developers.openai.com/codex/skills) · [Codex plugins](https://developers.openai.com/codex/plugins/build)
