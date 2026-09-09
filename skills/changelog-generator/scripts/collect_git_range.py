#!/usr/bin/env python3
"""Collect deterministic git evidence for changelog generation."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--base", required=True, help="Base commit, tag, or ref")
    parser.add_argument("--head", default="HEAD", help="Head commit, tag, or ref")
    args = parser.parse_args()

    repo = args.repo.resolve()
    try:
        base = git(repo, "rev-parse", "--verify", f"{args.base}^{{commit}}").strip()
        head = git(repo, "rev-parse", "--verify", f"{args.head}^{{commit}}").strip()
        raw_commits = git(
            repo,
            "log",
            "--reverse",
            "--format=%H%x1f%aI%x1f%s%x1f%b%x1e",
            f"{base}..{head}",
        )
        commits = []
        for record in raw_commits.strip("\n").split("\x1e"):
            record = record.strip("\n")
            if not record:
                continue
            fields = record.split("\x1f", 3)
            if len(fields) == 4:
                commits.append(dict(zip(("sha", "authored_at", "subject", "body"), fields)))

        changes = []
        for line in git(repo, "diff", "--name-status", f"{base}..{head}").splitlines():
            parts = line.split("\t")
            if parts:
                changes.append({"status": parts[0], "paths": parts[1:]})

        payload = {
            "repository": str(repo),
            "range": {"base": base, "head": head, "expression": f"{args.base}..{args.head}"},
            "commits": commits,
            "changes": changes,
            "diff_stat": git(repo, "diff", "--stat", f"{base}..{head}").rstrip(),
        }
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
