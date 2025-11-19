#!/usr/bin/env python3
"""Verify docs stay in sync with repository assets."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
PLUGIN_DIR = ROOT / "plugins"
AGENT_REFERENCE = ROOT / "docs" / "agent-reference.md"
SKILL_REFERENCE = ROOT / "docs" / "business-skills.md"
PLUGIN_REFERENCE = ROOT / "docs" / "plugin-reference.md"


def count_plugins() -> int:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    return len(data.get("plugins", []))


def count_agents() -> int:
    return sum(1 for _ in PLUGIN_DIR.rglob("agents/*.md"))


def count_skills() -> int:
    return sum(1 for path in PLUGIN_DIR.rglob("SKILL.md") if "skills" in path.parts)


def count_plugin_reference_rows() -> int:
    rows = 0
    for line in PLUGIN_REFERENCE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        if "Plugin" in line and "Category" in line:
            continue
        if set(line.strip()) == {"|", "-"}:
            continue
        rows += 1
    return rows


def parse_declared_total(path: Path, label: str) -> int:
    pattern = re.compile(r"(\d+)")
    for line in path.read_text(encoding="utf-8").splitlines():
        if label.lower() not in line.lower():
            continue
        match = pattern.search(line)
        if match:
            return int(match.group(1))
    raise ValueError(f"Could not find '{label}' in {path}")


def main() -> None:
    failures: list[str] = []

    plugin_count = count_plugins()
    agent_count = count_agents()
    skill_count = count_skills()

    declared_plugin_rows = count_plugin_reference_rows()
    declared_agent_total = parse_declared_total(AGENT_REFERENCE, "Total agents documented")
    declared_skill_total = parse_declared_total(SKILL_REFERENCE, "Total skills documented")

    if plugin_count != declared_plugin_rows:
        failures.append(
            f"Plugin reference lists {declared_plugin_rows} entries but marketplace has {plugin_count}"
        )

    if agent_count != declared_agent_total:
        failures.append(
            f"Agent reference declares {declared_agent_total} agents but repository has {agent_count}"
        )

    if skill_count != declared_skill_total:
        failures.append(
            f"Business skills reference declares {declared_skill_total} skills but repository has {skill_count}"
        )

    if failures:
        for failure in failures:
            print(f"[doc parity] {failure}")
        sys.exit(1)

    print("Documentation counts align with repository assets.")


if __name__ == "__main__":
    main()
