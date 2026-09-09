# Contributing

Thanks for helping improve this Codex skill collection. Contributions should make
agent behavior more focused, testable, safe, or useful across real software work.
Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Before opening a pull request

1. Search existing skills and issues to avoid duplicate scope.
2. Open a feature request before adding a broad workflow or changing a skill's
   authorization boundary.
3. Keep one skill focused on one coherent job. Prefer composing existing skills
   over building a catch-all prompt.
4. Start new skills from `templates/SKILL.md.template` and place them in
   `skills/<skill-name>/`.
5. Add `agents/openai.yaml` with a specific display name, a 25–64 character short
   description, and a default prompt that explicitly mentions `$skill-name`.
6. Add or update a routing case in `tests/skill-boundary-cases.json` when the new
   behavior could be confused with another skill.

## Quality and safety rules

- State both when the skill should trigger and when it should not.
- Preserve user authorization boundaries for writes, publication, deployment,
  deletion, and other external mutations.
- Treat repository and remote content as untrusted data, not instructions.
- Prefer evidence, reproducible commands, and explicit verification limits.
- Keep `SKILL.md` concise; place deep reference material in a local `references/`
  directory only when it is genuinely needed.
- Do not include secrets, personal data, generated caches, or vendored dependency
  trees.

## Validate locally

```bash
python3 scripts/validate_skills.py
bash scripts/install.sh --list
```

If you changed the installer, also test it against temporary user and repository
destinations. Pull requests should explain the intended trigger, non-trigger, test
evidence, compatibility impact, and any third-party source or license.

By contributing, you agree that your contribution is licensed under this
repository's MIT License unless a file explicitly states otherwise.
