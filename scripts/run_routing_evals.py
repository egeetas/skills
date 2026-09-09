#!/usr/bin/env python3
"""Evaluate skill description routing with a real Codex model."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---", re.S)


def scalar(block: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", block)
    return match.group(1).strip().strip("'\"") if match else ""


def inventory() -> list[dict[str, object]]:
    items = []
    for entrypoint in sorted(ROOT.glob("skills/*/SKILL.md")):
        match = FRONTMATTER.match(entrypoint.read_text(encoding="utf-8"))
        if match:
            metadata = (entrypoint.parent / "agents/openai.yaml").read_text(encoding="utf-8")
            items.append({
                "name": scalar(match.group(1), "name"),
                "description": scalar(match.group(1), "description"),
                "implicit_invocation": "allow_implicit_invocation: false" not in metadata,
            })
    return items


def cases() -> list[dict[str, object]]:
    payload = json.loads((ROOT / "tests" / "skill-routing-cases.json").read_text(encoding="utf-8"))
    expanded = []
    for item in payload["skills"]:
        for index, prompt in enumerate(item["positive"], start=1):
            expanded.append({"id": f"{item['skill']}-positive-{index}", "prompt": prompt, "expected": [item["skill"]], "excluded": []})
        for index, negative in enumerate(item["negative"], start=1):
            expanded.append({"id": f"{item['skill']}-negative-{index}", "prompt": negative["prompt"], "expected": negative["expected"], "excluded": [item["skill"]]})
    boundaries = json.loads((ROOT / "tests" / "skill-boundary-cases.json").read_text(encoding="utf-8"))
    for item in boundaries["cases"]:
        expanded.append({"id": f"boundary-{item['id']}", "prompt": item["prompt"], "expected": item["expected"], "excluded": item["excluded"]})
    return expanded


def chunks(items: list[dict[str, object]], size: int):
    for index in range(0, len(items), size):
        yield items[index : index + size]


def evaluate(batch: list[dict[str, object]], skills: list[dict[str, object]], model: str | None) -> list[dict[str, object]]:
    schema = {
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "selected": {"type": "array", "items": {"type": "string", "enum": [s["name"] for s in skills]}},
                    },
                    "required": ["id", "selected"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["results"],
        "additionalProperties": False,
    }
    prompt = (
        "You are testing skill description routing. For each user prompt, select only the smallest exact set of skills whose descriptions clearly apply. "
        "Choose zero skills when none apply. A skill with implicit_invocation=false may be selected only when the prompt explicitly requests that skill or workflow. "
        "Do not execute the tasks and do not use tools. Return one result for every case ID.\n\n"
        f"SKILLS:\n{json.dumps(skills, ensure_ascii=False)}\n\n"
        f"CASES:\n{json.dumps([{'id': c['id'], 'prompt': c['prompt']} for c in batch], ensure_ascii=False)}"
    )
    with tempfile.TemporaryDirectory(prefix="skill-routing-eval-") as temp:
        temp_path = Path(temp)
        schema_path = temp_path / "schema.json"
        output_path = temp_path / "result.json"
        schema_path.write_text(json.dumps(schema), encoding="utf-8")
        command = [
            "codex", "exec", "-", "--ephemeral", "--ignore-rules", "--skip-git-repo-check",
            "--sandbox", "read-only", "--cd", str(temp_path), "--output-schema", str(schema_path),
            "--output-last-message", str(output_path), "--color", "never",
        ]
        if model:
            command.extend(["--model", model])
        result = subprocess.run(command, input=prompt, text=True, capture_output=True, check=False, timeout=300)
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "codex exec failed")
        return json.loads(output_path.read_text(encoding="utf-8"))["results"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", help="Codex model override; the configured default is used when omitted")
    parser.add_argument("--case", action="append", default=[], help="Evaluate an exact case ID; repeatable")
    parser.add_argument("--limit", type=int, default=0, help="Evaluate only the first N expanded cases")
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--dry-run", action="store_true", help="Validate and report the plan without model calls")
    parser.add_argument("--output", type=Path, help="Write the full JSON report")
    args = parser.parse_args()

    if args.limit < 0 or args.batch_size < 1:
        parser.error("--limit must be non-negative and --batch-size must be positive")
    if not args.dry_run and shutil.which("codex") is None:
        print("error: codex executable not found", file=sys.stderr)
        return 2

    skill_inventory = inventory()
    selected_cases = cases()
    if args.case:
        requested = set(args.case)
        selected_cases = [case for case in selected_cases if case["id"] in requested]
        missing_ids = sorted(requested - {str(case["id"]) for case in selected_cases})
        if missing_ids:
            print(f"error: unknown case IDs: {', '.join(missing_ids)}", file=sys.stderr)
            return 2
    if args.limit:
        selected_cases = selected_cases[: args.limit]
    print(f"Routing eval plan: {len(skill_inventory)} skills, {len(selected_cases)} cases, batch size {args.batch_size}")
    if args.dry_run:
        return 0

    observed: dict[str, list[str]] = {}
    try:
        for batch in chunks(selected_cases, args.batch_size):
            for result in evaluate(batch, skill_inventory, args.model):
                observed[str(result["id"])] = list(result["selected"])
    except (RuntimeError, subprocess.TimeoutExpired, json.JSONDecodeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    results = []
    for case in selected_cases:
        actual = observed.get(str(case["id"]), [])
        missing = sorted(set(case["expected"]) - set(actual))
        unexpected = sorted(set(actual) - set(case["expected"]))
        forbidden = sorted(set(case["excluded"]) & set(actual))
        duplicate = len(actual) != len(set(actual))
        results.append({
            **case,
            "actual": actual,
            "passed": not missing and not unexpected and not forbidden and not duplicate,
            "missing": missing,
            "unexpected": unexpected,
            "forbidden": forbidden,
            "duplicate": duplicate,
        })

    report = {
        "model": args.model or "configured-default",
        "summary": {"total": len(results), "passed": sum(item["passed"] for item in results), "failed": sum(not item["passed"] for item in results)},
        "results": results,
    }
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    for item in results:
        if not item["passed"]:
            print(f"FAIL {item['id']}: expected={item['expected']} actual={item['actual']} excluded={item['excluded']}")
    return 1 if report["summary"]["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
