#!/usr/bin/env python3
"""Simple scaffolding helper that copies template stubs into new plugin assets."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path
import sys

TEMPLATES = {
    "agent": Path("templates/agent.md"),
    "command": Path("templates/command.md"),
    "skill": Path("templates/skill.md"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy contributor templates into the desired asset path."
    )
    parser.add_argument(
        "asset_type",
        choices=TEMPLATES.keys(),
        help="Type of asset to scaffold",
    )
    parser.add_argument(
        "destination",
        help="Target file path for the new asset (e.g., plugins/foo/agents/bar.md)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite destination file if it already exists.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    template_path = TEMPLATES[args.asset_type]
    if not template_path.exists():
        print(f"Template not found: {template_path}", file=sys.stderr)
        return 1

    destination = Path(args.destination)
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists() and not args.force:
        print(
            f"Destination {destination} already exists. Use --force to overwrite.",
            file=sys.stderr,
        )
        return 2

    shutil.copy(template_path, destination)
    print(f"Copied {template_path} -> {destination}")
    print("Fill in the placeholders ({{ }}) before running validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
