# Optional Codex subagent presets

These presets complement the skills in this repository. They are deliberately
small and role-focused:

- `code-explorer` maps unfamiliar code without editing it.
- `quality-reviewer` reviews a fixed change scope and reports evidence-backed findings.
- `test-investigator` runs relevant checks and diagnoses failures without changing source code.

Codex discovers custom agents from `$HOME/.codex/agents` or a repository's
`.codex/agents` directory. Install these presets only when you want them:

```bash
./scripts/install.sh --with-agents
```

For a project-scoped installation:

```bash
./scripts/install.sh --scope repo --target /path/to/project --with-agents
```

The installer never overwrites an existing agent definition. Skills can request
bounded subagent work, but Codex remains responsible for deciding whether a
subagent is appropriate and for respecting the user's authorization boundary.

Official documentation: <https://developers.openai.com/codex/subagents>
