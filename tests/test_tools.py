from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class ToolTests(unittest.TestCase):
    def test_collect_git_range(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test"], check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.email", "test@example.com"], check=True)
            (repo / "a.txt").write_text("one\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "add", "a.txt"], check=True)
            subprocess.run(["git", "-C", str(repo), "commit", "-qm", "initial"], check=True)
            base = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
            (repo / "a.txt").write_text("one\ntwo\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "commit", "-qam", "add second line"], check=True)
            output = subprocess.check_output(
                ["python3", str(ROOT / "skills/changelog-generator/scripts/collect_git_range.py"), "--repo", str(repo), "--base", base],
                text=True,
            )
            payload = json.loads(output)
            self.assertEqual(payload["commits"][0]["subject"], "add second line")
            self.assertEqual(payload["changes"], [{"status": "M", "paths": ["a.txt"]}])

    def test_discover_repo_checks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            (repo / "package.json").write_text('{"scripts":{"lint":"eslint .","test":"vitest"}}\n', encoding="utf-8")
            (repo / "pyproject.toml").write_text("[tool.pytest.ini_options]\naddopts = '-q'\n", encoding="utf-8")
            output = subprocess.check_output(
                ["python3", str(ROOT / "skills/repo-quality-audit/scripts/discover_repo_checks.py"), str(repo), "--format", "json"],
                text=True,
            )
            commands = {item["command"] for item in json.loads(output)["checks"]}
            self.assertEqual(commands, {"npm run lint", "npm run test", "python -m pytest"})

    def test_routing_eval_dry_run(self) -> None:
        output = subprocess.check_output(["python3", str(ROOT / "scripts/run_routing_evals.py"), "--dry-run"], text=True)
        self.assertIn("49 skills, 161 cases", output)


if __name__ == "__main__":
    unittest.main()
