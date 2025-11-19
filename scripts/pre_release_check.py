#!/usr/bin/env python3
"""Run the full release precheck suite."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    "python3 scripts/validate_marketplace.py",
    "python3 scripts/check_cross_links.py",
    "python3 scripts/smoke_test_plugins.py",
    "python3 scripts/check_doc_parity.py",
    "python3 scripts/check_model_mix.py",
    "python3 scripts/check_skill_structure.py",
    "python3 scripts/check_tool_count.py",
]


def run(command: str) -> None:
    print(f"\n>>> {command}")
    result = subprocess.run(command, shell=True, cwd=ROOT)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main() -> None:
    for command in COMMANDS:
        run(command)
    print("\nAll release prechecks passed.")


if __name__ == "__main__":
    main()
