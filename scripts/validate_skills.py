#!/usr/bin/env python3
"""Validate portable Codex skill structure without third-party packages."""

from __future__ import annotations

import re
import sys
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
    entrypoints = sorted(ROOT.glob("*/SKILL.md"))

    if not entrypoints:
      errors.append("No top-level skill entrypoints found")

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
        if openai_yaml.exists():
            metadata = openai_yaml.read_text(encoding="utf-8")
            default_prompt = scalar(metadata, "default_prompt")
            short_description = scalar(metadata, "short_description")
            if default_prompt and name and f"${name}" not in default_prompt:
                errors.append(f"{openai_yaml.relative_to(ROOT)}: default_prompt must mention ${name}")
            if short_description and not 25 <= len(short_description) <= 64:
                errors.append(f"{openai_yaml.relative_to(ROOT)}: short_description must be 25-64 characters")

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(entrypoints)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
