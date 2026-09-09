#!/usr/bin/env python3
"""Validate portable Codex skill structure without third-party packages."""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)


def scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    if not match:
        return None
    return match.group(1).strip().strip("'\"")


def main() -> int:
    errors: list[str] = []
    names: dict[str, Path] = {}
    case_ids: set[str] = set()
    entrypoints = sorted(ROOT.glob("skills/*/SKILL.md"))

    if not entrypoints:
        errors.append("No skill entrypoints found under skills/")

    legacy_entrypoints = sorted(ROOT.glob("*/SKILL.md"))
    for entrypoint in legacy_entrypoints:
        errors.append(f"{entrypoint.relative_to(ROOT)}: move skill under skills/")

    for entrypoint in entrypoints:
        text = entrypoint.read_text(encoding="utf-8")
        match = FRONTMATTER_PATTERN.match(text)
        if not match:
            errors.append(f"{entrypoint.relative_to(ROOT)}: missing YAML frontmatter")
            continue

        frontmatter = match.group(1)
        name = scalar(frontmatter, "name")
        description = scalar(frontmatter, "description")

        if not name or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{entrypoint.relative_to(ROOT)}: invalid or missing name")
        elif name != entrypoint.parent.name:
            errors.append(f"{entrypoint.relative_to(ROOT)}: name must match directory")
        elif name in names:
            errors.append(f"{entrypoint.relative_to(ROOT)}: duplicate name also in {names[name]}")
        else:
            names[name] = entrypoint.relative_to(ROOT)

        if not description or len(description) < 20:
            errors.append(f"{entrypoint.relative_to(ROOT)}: description is missing or too short")
        elif len(description) > 1024:
            errors.append(f"{entrypoint.relative_to(ROOT)}: description exceeds 1024 characters")

        if "TODO" in text or "[TODO" in text:
            errors.append(f"{entrypoint.relative_to(ROOT)}: unfinished placeholder")

        openai_yaml = entrypoint.parent / "agents" / "openai.yaml"
        if not openai_yaml.exists():
            errors.append(f"{openai_yaml.relative_to(ROOT)}: missing Codex interface metadata")
        else:
            metadata = openai_yaml.read_text(encoding="utf-8")
            display_name = scalar(metadata, "display_name")
            default_prompt = scalar(metadata, "default_prompt")
            short_description = scalar(metadata, "short_description")

            if not display_name:
                errors.append(f"{openai_yaml.relative_to(ROOT)}: missing display_name")
            if not default_prompt:
                errors.append(f"{openai_yaml.relative_to(ROOT)}: missing default_prompt")
            elif name and f"${name}" not in default_prompt:
                errors.append(f"{openai_yaml.relative_to(ROOT)}: default_prompt must mention ${name}")
            if not short_description:
                errors.append(f"{openai_yaml.relative_to(ROOT)}: missing short_description")
            elif not 25 <= len(short_description) <= 64:
                errors.append(f"{openai_yaml.relative_to(ROOT)}: short_description must be 25-64 characters")

    presets = sorted((ROOT / "agent-presets").glob("*.toml"))
    if not presets:
        errors.append("agent-presets/: no Codex subagent presets found")
    for preset in presets:
        try:
            data = tomllib.loads(preset.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"{preset.relative_to(ROOT)}: invalid TOML: {exc}")
            continue

        if data.get("name") != preset.stem:
            errors.append(f"{preset.relative_to(ROOT)}: name must match filename")
        if not isinstance(data.get("description"), str) or len(data["description"].strip()) < 20:
            errors.append(f"{preset.relative_to(ROOT)}: description is missing or too short")
        instructions = data.get("developer_instructions")
        if not isinstance(instructions, str) or len(instructions.strip()) < 80:
            errors.append(f"{preset.relative_to(ROOT)}: developer_instructions are missing or too short")
        if data.get("sandbox_mode") not in {"read-only", "workspace-write"}:
            errors.append(f"{preset.relative_to(ROOT)}: unsupported sandbox_mode")

    template = ROOT / "templates" / "SKILL.md.template"
    if not template.exists():
        errors.append("templates/SKILL.md.template: missing authoring template")
    else:
        template_text = template.read_text(encoding="utf-8")
        template_match = FRONTMATTER_PATTERN.match(template_text)
        if not template_match:
            errors.append("templates/SKILL.md.template: missing YAML frontmatter")
        elif scalar(template_match.group(1), "name") != "skill-name":
            errors.append("templates/SKILL.md.template: placeholder name must be skill-name")

    cases_path = ROOT / "tests" / "skill-boundary-cases.json"
    if not cases_path.exists():
        errors.append("tests/skill-boundary-cases.json: missing routing contract corpus")
    else:
        try:
            payload = json.loads(cases_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"tests/skill-boundary-cases.json: invalid JSON: {exc}")
        else:
            if not isinstance(payload, dict):
                errors.append("tests/skill-boundary-cases.json: root must be an object")
            elif payload.get("schema_version") != 1 or not isinstance(payload.get("cases"), list):
                errors.append("tests/skill-boundary-cases.json: expected schema_version 1 and cases list")
            else:
                for index, case in enumerate(payload["cases"], start=1):
                    prefix = f"tests/skill-boundary-cases.json case {index}"
                    if not isinstance(case, dict):
                        errors.append(f"{prefix}: must be an object")
                        continue
                    case_id = case.get("id")
                    prompt = case.get("prompt")
                    expected = case.get("expected")
                    excluded = case.get("excluded")
                    if not isinstance(case_id, str) or not NAME_PATTERN.fullmatch(case_id):
                        errors.append(f"{prefix}: invalid id")
                    elif case_id in case_ids:
                        errors.append(f"{prefix}: duplicate id {case_id}")
                    else:
                        case_ids.add(case_id)
                    if not isinstance(prompt, str) or len(prompt.strip()) < 20:
                        errors.append(f"{prefix}: prompt is missing or too short")
                    if not isinstance(expected, list) or not expected:
                        errors.append(f"{prefix}: expected must be a non-empty list")
                        expected = []
                    if not isinstance(excluded, list):
                        errors.append(f"{prefix}: excluded must be a list")
                        excluded = []
                    for field, values in (("expected", expected), ("excluded", excluded)):
                        for value in values:
                            if not isinstance(value, str) or value not in names:
                                errors.append(f"{prefix}: unknown {field} skill {value!r}")
                    overlap = set(expected) & set(excluded)
                    if overlap:
                        errors.append(f"{prefix}: skills cannot be both expected and excluded: {sorted(overlap)}")

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(entrypoints)} skills and {len(case_ids)} routing boundary cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
