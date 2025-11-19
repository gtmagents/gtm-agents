#!/usr/bin/env python3
"""Audit the number of commands (tools) promised in the README."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_TOOL_COUNT = 48


def load_commands() -> list[str]:
    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
    commands: set[str] = set()
    for plugin in marketplace.get("plugins", []):
        commands.update(plugin.get("commands", []))
    return sorted(commands)


def main() -> None:
    commands = load_commands()
    tool_count = len(commands)

    print("Detected marketplace commands (treated as GTM tools):")
    for rel_path in commands:
        print(" -", rel_path)

    if tool_count < TARGET_TOOL_COUNT:
        deficit = TARGET_TOOL_COUNT - tool_count
        raise SystemExit(
            f"[tool count] Only {tool_count} commands found; need {TARGET_TOOL_COUNT} (missing {deficit})."
        )

    print(f"Tool count OK: {tool_count} >= {TARGET_TOOL_COUNT}")


if __name__ == "__main__":
    main()
