#!/usr/bin/env python3
"""Simple scaffolding helper that copies template stubs into new plugin assets.

For skills, this creates an Agent Skills compliant directory structure:
  skill-name/
  ├── SKILL.md
  ├── assets/       (optional)
  ├── scripts/      (optional)
  └── references/   (optional)
"""
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
        help="Target file path for the new asset (e.g., plugins/foo/agents/bar.md or plugins/foo/skills/bar/SKILL.md)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite destination file if it already exists.",
    )
    parser.add_argument(
        "--with-assets",
        action="store_true",
        help="For skills: also create assets/ directory with .gitkeep",
    )
    parser.add_argument(
        "--with-scripts",
        action="store_true",
        help="For skills: also create scripts/ directory with .gitkeep",
    )
    parser.add_argument(
        "--with-references",
        action="store_true",
        help="For skills: also create references/ directory with .gitkeep",
    )
    return parser.parse_args()


def scaffold_skill(template_path: Path, destination: Path, args: argparse.Namespace) -> int:
    """Scaffold a skill with Agent Skills compliant structure."""
    # Ensure destination ends with SKILL.md
    if destination.name != "SKILL.md":
        # Assume destination is the skill directory name
        skill_dir = destination
        destination = destination / "SKILL.md"
    else:
        skill_dir = destination.parent
    
    skill_dir.mkdir(parents=True, exist_ok=True)
    
    if destination.exists() and not args.force:
        print(
            f"Destination {destination} already exists. Use --force to overwrite.",
            file=sys.stderr,
        )
        return 2
    
    # Copy template
    shutil.copy(template_path, destination)
    print(f"Created {destination}")
    
    # Create optional directories
    if args.with_assets:
        assets_dir = skill_dir / "assets"
        assets_dir.mkdir(exist_ok=True)
        (assets_dir / ".gitkeep").touch()
        print(f"Created {assets_dir}/")
    
    if args.with_scripts:
        scripts_dir = skill_dir / "scripts"
        scripts_dir.mkdir(exist_ok=True)
        (scripts_dir / ".gitkeep").touch()
        print(f"Created {scripts_dir}/")
    
    if args.with_references:
        refs_dir = skill_dir / "references"
        refs_dir.mkdir(exist_ok=True)
        (refs_dir / ".gitkeep").touch()
        print(f"Created {refs_dir}/")
    
    print()
    print("Next steps:")
    print("  1. Fill in the placeholders ({{ }}) in SKILL.md")
    print("  2. Ensure 'name' matches the directory name")
    print("  3. Run: python scripts/validate_skills.py " + str(skill_dir))
    return 0


def main() -> int:
    args = parse_args()
    template_path = TEMPLATES[args.asset_type]
    if not template_path.exists():
        print(f"Template not found: {template_path}", file=sys.stderr)
        return 1

    destination = Path(args.destination)
    
    # Special handling for skills (Agent Skills compliant structure)
    if args.asset_type == "skill":
        return scaffold_skill(template_path, destination, args)
    
    # Standard handling for agents and commands
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
