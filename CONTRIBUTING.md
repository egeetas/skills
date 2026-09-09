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
4. Read `docs/skill-authoring.md`, start from `templates/SKILL.md.template`, and
   place the skill in `skills/<skill-name>/`.
5. Add `agents/openai.yaml` with a specific display name, a 25–64 character short
   description, and a default prompt that explicitly mentions `$skill-name`.
6. Add two positive and one negative case to `tests/skill-routing-cases.json`.
   Add a focused `tests/skill-boundary-cases.json` case when behavior could be
   confused with another skill.
7. Add the skill to exactly one file under `packs/` and to `CATALOG.md`.

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

Validation and helper scripts require Python 3.11 or newer.

```bash
python3 scripts/validate_skills.py
bash scripts/install.sh --list
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/run_routing_evals.py --dry-run
```

If you changed the installer, also test it against temporary user and repository
destinations. Pull requests should explain the intended trigger, non-trigger, test
evidence, compatibility impact, and any third-party source or license.

By contributing, you agree that your contribution is licensed under this
repository's MIT License unless a file explicitly states otherwise.
