#!/usr/bin/env python3
"""Validate the skill library, packs, routing corpus, and plugin metadata."""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)
RESOURCE_LINK = re.compile(r"\]\(((?:assets|references|scripts)/[^)#]+)(?:#[^)]+)?\)")
DESCRIPTION_BUDGET = 7000
DESCRIPTION_MAX = 200
PLUGIN_NAME = "codex-engineering-skills"
PLUGIN_VERSION = "1.0.0"


def scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    return match.group(1).strip().strip("'\"") if match else None


def load_json(path: Path, errors: list[str]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None


def validate_skills(errors: list[str]) -> dict[str, Path]:
    names: dict[str, Path] = {}
    descriptions: list[str] = []
    entrypoints = sorted(ROOT.glob("skills/*/SKILL.md"))
    if not entrypoints:
        errors.append("No skill entrypoints found under skills/")
    for entrypoint in sorted(ROOT.glob("*/SKILL.md")):
        errors.append(f"{entrypoint.relative_to(ROOT)}: move skill under skills/")

    for entrypoint in entrypoints:
        relative = entrypoint.relative_to(ROOT)
        text = entrypoint.read_text(encoding="utf-8")
        match = FRONTMATTER_PATTERN.match(text)
        if not match:
            errors.append(f"{relative}: missing YAML frontmatter")
            continue
        frontmatter = match.group(1)
        name = scalar(frontmatter, "name")
        description = scalar(frontmatter, "description")
        if not name or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{relative}: invalid or missing name")
        elif name != entrypoint.parent.name:
            errors.append(f"{relative}: name must match directory")
        elif name in names:
            errors.append(f"{relative}: duplicate name also in {names[name]}")
        else:
            names[name] = relative
        if not description or len(description) < 20:
            errors.append(f"{relative}: description is missing or too short")
        elif len(description) > DESCRIPTION_MAX:
            errors.append(f"{relative}: description exceeds {DESCRIPTION_MAX} characters")
        else:
            descriptions.append(description)
        if "TODO" in text or "[TODO" in text:
            errors.append(f"{relative}: unfinished placeholder")
        for resource in RESOURCE_LINK.findall(text):
            if not (entrypoint.parent / resource).is_file():
                errors.append(f"{relative}: missing linked resource {resource}")

        openai_yaml = entrypoint.parent / "agents" / "openai.yaml"
        if not openai_yaml.exists():
            errors.append(f"{openai_yaml.relative_to(ROOT)}: missing Codex interface metadata")
            continue
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
        if not short_description or not 25 <= len(short_description) <= 64:
            errors.append(f"{openai_yaml.relative_to(ROOT)}: short_description must be 25-64 characters")

    if sum(map(len, descriptions)) > DESCRIPTION_BUDGET:
        errors.append(f"Skill descriptions use {sum(map(len, descriptions))} characters; budget is {DESCRIPTION_BUDGET}")
    workflow_metadata = ROOT / "skills/software-development-workflow/agents/openai.yaml"
    if workflow_metadata.exists() and "allow_implicit_invocation: false" not in workflow_metadata.read_text(encoding="utf-8"):
        errors.append("software-development-workflow must remain explicit-only")
    return names


def validate_packs(names: dict[str, Path], errors: list[str]) -> int:
    occurrences: dict[str, list[str]] = {name: [] for name in names}
    pack_count = 0
    for pack in sorted((ROOT / "packs").glob("*.txt")):
        pack_count += 1
        if not NAME_PATTERN.fullmatch(pack.stem):
            errors.append(f"{pack.relative_to(ROOT)}: invalid pack name")
        seen: set[str] = set()
        for line in pack.read_text(encoding="utf-8").splitlines():
            skill = line.strip()
            if not skill or skill.startswith("#"):
                continue
            if skill not in names:
                errors.append(f"{pack.relative_to(ROOT)}: unknown skill {skill}")
            elif skill in seen:
                errors.append(f"{pack.relative_to(ROOT)}: duplicate skill {skill}")
            else:
                seen.add(skill)
                occurrences[skill].append(pack.stem)
    if not (ROOT / "packs/core-development.txt").exists():
        errors.append("packs/core-development.txt: missing default pack")
    for skill, packs in occurrences.items():
        if len(packs) != 1:
            errors.append(f"packs/: {skill} must appear exactly once, found in {packs}")
    return pack_count


def validate_presets(errors: list[str]) -> int:
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
    return len(presets)


def validate_boundary_cases(names: dict[str, Path], errors: list[str]) -> int:
    path = ROOT / "tests/skill-boundary-cases.json"
    payload = load_json(path, errors)
    if not isinstance(payload, dict) or payload.get("schema_version") != 1 or not isinstance(payload.get("cases"), list):
        errors.append("tests/skill-boundary-cases.json: expected schema_version 1 and cases list")
        return 0
    ids: set[str] = set()
    for index, case in enumerate(payload["cases"], start=1):
        prefix = f"tests/skill-boundary-cases.json case {index}"
        if not isinstance(case, dict):
            errors.append(f"{prefix}: must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not NAME_PATTERN.fullmatch(case_id) or case_id in ids:
            errors.append(f"{prefix}: invalid or duplicate id")
        else:
            ids.add(case_id)
        if not isinstance(case.get("prompt"), str) or len(case["prompt"].strip()) < 20:
            errors.append(f"{prefix}: prompt is missing or too short")
        expected, excluded = case.get("expected"), case.get("excluded")
        if not isinstance(expected, list) or not isinstance(excluded, list) or not (expected or excluded):
            errors.append(f"{prefix}: expected and excluded must be lists and cannot both be empty")
            continue
        for value in expected + excluded:
            if value not in names:
                errors.append(f"{prefix}: unknown skill {value!r}")
        if set(expected) & set(excluded):
            errors.append(f"{prefix}: expected and excluded overlap")
    return len(ids)


def validate_routing_matrix(names: dict[str, Path], errors: list[str]) -> int:
    path = ROOT / "tests/skill-routing-cases.json"
    payload = load_json(path, errors)
    if not isinstance(payload, dict) or payload.get("schema_version") != 1 or not isinstance(payload.get("skills"), list):
        errors.append("tests/skill-routing-cases.json: expected schema_version 1 and skills list")
        return 0
    covered: set[str] = set()
    expanded = 0
    for index, item in enumerate(payload["skills"], start=1):
        prefix = f"tests/skill-routing-cases.json item {index}"
        if not isinstance(item, dict) or item.get("skill") not in names:
            errors.append(f"{prefix}: unknown or missing skill")
            continue
        skill = item["skill"]
        if skill in covered:
            errors.append(f"{prefix}: duplicate skill {skill}")
        covered.add(skill)
        positive, negative = item.get("positive"), item.get("negative")
        if not isinstance(positive, list) or len(positive) < 2:
            errors.append(f"{prefix}: requires at least two positive prompts")
            positive = []
        if not isinstance(negative, list) or len(negative) < 1:
            errors.append(f"{prefix}: requires at least one negative prompt")
            negative = []
        for prompt in positive:
            if not isinstance(prompt, str) or len(prompt.strip()) < 20:
                errors.append(f"{prefix}: invalid positive prompt")
        for case in negative:
            if not isinstance(case, dict) or not isinstance(case.get("prompt"), str) or len(case["prompt"].strip()) < 20:
                errors.append(f"{prefix}: invalid negative prompt")
                continue
            expected = case.get("expected")
            if not isinstance(expected, list) or any(value not in names for value in expected):
                errors.append(f"{prefix}: invalid negative expected skills")
        expanded += len(positive) + len(negative)
    missing = sorted(set(names) - covered)
    extra = sorted(covered - set(names))
    if missing or extra:
        errors.append(f"tests/skill-routing-cases.json: coverage mismatch missing={missing} extra={extra}")
    if expanded < len(names) * 3:
        errors.append(f"tests/skill-routing-cases.json: expected at least {len(names) * 3} expanded cases, found {expanded}")
    return expanded


def validate_plugin(errors: list[str]) -> None:
    portable = load_json(ROOT / "plugin.json", errors)
    compatibility = load_json(ROOT / ".codex-plugin/plugin.json", errors)
    marketplace = load_json(ROOT / ".agents/plugins/marketplace.json", errors)
    for label, payload in (("plugin.json", portable), (".codex-plugin/plugin.json", compatibility)):
        if not isinstance(payload, dict):
            continue
        if payload.get("name") != PLUGIN_NAME or payload.get("version") != PLUGIN_VERSION:
            errors.append(f"{label}: expected {PLUGIN_NAME} version {PLUGIN_VERSION}")
        if payload.get("license") != "MIT" or payload.get("repository") != "https://github.com/egeetas/skills":
            errors.append(f"{label}: license or repository metadata mismatch")
    if isinstance(portable, dict) and portable.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json: portable plugin schema is missing")
    if isinstance(portable, dict):
        extensions = portable.get("extensions")
        openai_extension = extensions.get("com.openai") if isinstance(extensions, dict) else None
        portable_interface = openai_extension.get("interface") if isinstance(openai_extension, dict) else None
        if not isinstance(portable_interface, dict):
            errors.append("plugin.json: extensions.com.openai.interface is missing")
        elif isinstance(compatibility, dict):
            compatibility_interface = compatibility.get("interface")
            if not isinstance(compatibility_interface, dict):
                errors.append(".codex-plugin/plugin.json: interface is missing")
            else:
                for field in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "websiteURL"):
                    if portable_interface.get(field) != compatibility_interface.get(field):
                        errors.append(f"plugin manifests: interface.{field} mismatch")
        prompts = portable_interface.get("defaultPrompt") if isinstance(portable_interface, dict) else None
        if not isinstance(prompts, list) or not prompts or not all(isinstance(prompt, str) and prompt.strip() for prompt in prompts):
            errors.append("plugin.json: interface.defaultPrompt must be a non-empty string list")
    if isinstance(compatibility, dict) and compatibility.get("skills") != "./skills/":
        errors.append(".codex-plugin/plugin.json: skills path must be ./skills/")
    if not isinstance(marketplace, dict) or not isinstance(marketplace.get("plugins"), list) or len(marketplace["plugins"]) != 1:
        errors.append(".agents/plugins/marketplace.json: expected one plugin entry")
    else:
        entry = marketplace["plugins"][0]
        if entry.get("name") != PLUGIN_NAME:
            errors.append(".agents/plugins/marketplace.json: plugin name mismatch")
        source = entry.get("source")
        if not isinstance(source, dict) or source.get("source") != "url" or source.get("url") != "https://github.com/egeetas/skills.git":
            errors.append(".agents/plugins/marketplace.json: remote source mismatch")
        elif source.get("ref") != f"v{PLUGIN_VERSION}":
            errors.append(".agents/plugins/marketplace.json: ref must match plugin version")
        if entry.get("policy") != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
            errors.append(".agents/plugins/marketplace.json: policy mismatch")
        if entry.get("category") != "Developer Tools":
            errors.append(".agents/plugins/marketplace.json: category mismatch")


def main() -> int:
    errors: list[str] = []
    names = validate_skills(errors)
    pack_count = validate_packs(names, errors)
    preset_count = validate_presets(errors)
    boundary_count = validate_boundary_cases(names, errors)
    routing_count = validate_routing_matrix(names, errors)
    validate_plugin(errors)

    template = ROOT / "templates/SKILL.md.template"
    if not template.exists() or not FRONTMATTER_PATTERN.match(template.read_text(encoding="utf-8")):
        errors.append("templates/SKILL.md.template: missing or invalid authoring template")

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"Validated {len(names)} skills, {pack_count} packs, {preset_count} agent presets, "
        f"{boundary_count} boundary cases, and {routing_count} routing eval cases"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
