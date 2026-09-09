#!/usr/bin/env python3
"""Discover documented repository checks without executing them."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path


SCRIPT_NAMES = {
    "format": "format",
    "fmt": "format",
    "lint": "lint",
    "typecheck": "type-check",
    "type-check": "type-check",
    "test": "test",
    "test:unit": "unit-test",
    "test:integration": "integration-test",
    "test:e2e": "end-to-end-test",
    "build": "build",
    "check": "check",
}


def add(results: list[dict[str, str]], kind: str, command: str, source: str) -> None:
    item = {"kind": kind, "command": command, "source": source}
    if item not in results:
        results.append(item)


def discover(root: Path) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    package_json = root / "package.json"
    if package_json.exists():
        try:
            scripts = json.loads(package_json.read_text(encoding="utf-8")).get("scripts", {})
        except (OSError, json.JSONDecodeError):
            scripts = {}
        if isinstance(scripts, dict):
            for name in sorted(scripts):
                if name in SCRIPT_NAMES:
                    add(results, SCRIPT_NAMES[name], f"npm run {name}", "package.json")

    pyproject = root / "pyproject.toml"
    if pyproject.exists():
        try:
            data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            data = {}
        if "pytest" in data.get("tool", {}):
            add(results, "test", "python -m pytest", "pyproject.toml [tool.pytest]")
        if "ruff" in data.get("tool", {}):
            add(results, "lint", "ruff check .", "pyproject.toml [tool.ruff]")
        if "mypy" in data.get("tool", {}):
            add(results, "type-check", "mypy .", "pyproject.toml [tool.mypy]")

    makefile = root / "Makefile"
    if makefile.exists():
        text = makefile.read_text(encoding="utf-8", errors="replace")
        for target in re.findall(r"(?m)^([A-Za-z0-9_.-]+):(?:\s|$)", text):
            if target in SCRIPT_NAMES:
                add(results, SCRIPT_NAMES[target], f"make {target}", f"Makefile:{target}")

    if (root / "Cargo.toml").exists():
        add(results, "format", "cargo fmt --check", "Cargo.toml")
        add(results, "lint", "cargo clippy --all-targets --all-features", "Cargo.toml")
        add(results, "test", "cargo test --all-features", "Cargo.toml")
    if (root / "go.mod").exists():
        add(results, "test", "go test ./...", "go.mod")

    for workflow in sorted((root / ".github" / "workflows").glob("*.y*ml")):
        add(results, "ci-reference", f"inspect {workflow.relative_to(root)}", str(workflow.relative_to(root)))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args()
    root = args.repo.resolve()
    if not root.is_dir():
        print(f"error: repository directory not found: {root}", file=sys.stderr)
        return 2
    results = discover(root)
    if args.format == "json":
        json.dump({"repository": str(root), "checks": results}, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        for item in results:
            print(f"{item['kind']}\t{item['command']}\t{item['source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
