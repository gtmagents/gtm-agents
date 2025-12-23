#!/usr/bin/env python3
"""
Validate all skills against the Agent Skills specification.

This script validates skills using the skills-ref library or falls back
to manual validation if skills-ref is not installed.

Usage:
    python scripts/validate_skills.py
    python scripts/validate_skills.py --fix  # Auto-fix common issues
    python scripts/validate_skills.py --verbose  # Show all validation details
"""

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Optional

# Constants from Agent Skills spec
MAX_SKILL_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_COMPATIBILITY_LENGTH = 500

ALLOWED_FIELDS = {
    "name",
    "description", 
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from SKILL.md content."""
    if not content.startswith("---"):
        raise ValueError("Missing YAML frontmatter delimiter")
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Invalid frontmatter format")
    
    frontmatter_text = parts[1].strip()
    body = parts[2].strip() if len(parts) > 2 else ""
    
    # Simple YAML parsing (handles basic key: value pairs)
    metadata = {}
    current_key = None
    current_value = []
    in_metadata_block = False
    
    for line in frontmatter_text.split("\n"):
        stripped = line.strip()
        
        # Handle metadata block
        if stripped == "metadata:":
            in_metadata_block = True
            metadata["metadata"] = {}
            continue
        
        if in_metadata_block:
            if line.startswith("  ") and ":" in stripped:
                key, value = stripped.split(":", 1)
                metadata["metadata"][key.strip()] = value.strip().strip('"\'')
            elif not line.startswith(" "):
                in_metadata_block = False
        
        if not in_metadata_block and ":" in line and not line.startswith(" "):
            if current_key:
                metadata[current_key] = " ".join(current_value).strip()
            
            key, value = line.split(":", 1)
            current_key = key.strip()
            value = value.strip().strip('"\'')
            
            # Handle multi-line values
            if value:
                current_value = [value]
            else:
                current_value = []
        elif current_key and line.startswith("  "):
            current_value.append(line.strip())
    
    if current_key and current_key not in metadata:
        metadata[current_key] = " ".join(current_value).strip()
    
    return metadata, body


def validate_name(name: str, skill_dir: Path) -> list[str]:
    """Validate skill name format and directory match."""
    errors = []
    
    if not name or not isinstance(name, str) or not name.strip():
        errors.append("Field 'name' must be a non-empty string")
        return errors
    
    name = unicodedata.normalize("NFKC", name.strip())
    
    if len(name) > MAX_SKILL_NAME_LENGTH:
        errors.append(
            f"Skill name '{name}' exceeds {MAX_SKILL_NAME_LENGTH} character limit "
            f"({len(name)} chars)"
        )
    
    if name != name.lower():
        errors.append(f"Skill name '{name}' must be lowercase")
    
    if name.startswith("-") or name.endswith("-"):
        errors.append("Skill name cannot start or end with a hyphen")
    
    if "--" in name:
        errors.append("Skill name cannot contain consecutive hyphens")
    
    if not all(c.isalnum() or c == "-" for c in name):
        errors.append(
            f"Skill name '{name}' contains invalid characters. "
            "Only letters, digits, and hyphens are allowed."
        )
    
    dir_name = unicodedata.normalize("NFKC", skill_dir.name)
    if dir_name != name:
        errors.append(
            f"Directory name '{skill_dir.name}' must match skill name '{name}'"
        )
    
    return errors


def validate_description(description: str) -> list[str]:
    """Validate description format."""
    errors = []
    
    if not description or not isinstance(description, str) or not description.strip():
        errors.append("Field 'description' must be a non-empty string")
        return errors
    
    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"Description exceeds {MAX_DESCRIPTION_LENGTH} character limit "
            f"({len(description)} chars)"
        )
    
    return errors


def validate_compatibility(compatibility: str) -> list[str]:
    """Validate compatibility format."""
    errors = []
    
    if not isinstance(compatibility, str):
        errors.append("Field 'compatibility' must be a string")
        return errors
    
    if len(compatibility) > MAX_COMPATIBILITY_LENGTH:
        errors.append(
            f"Compatibility exceeds {MAX_COMPATIBILITY_LENGTH} character limit "
            f"({len(compatibility)} chars)"
        )
    
    return errors


def validate_metadata_fields(metadata: dict) -> list[str]:
    """Validate that only allowed fields are present."""
    errors = []
    
    extra_fields = set(metadata.keys()) - ALLOWED_FIELDS
    if extra_fields:
        errors.append(
            f"Unexpected fields in frontmatter: {', '.join(sorted(extra_fields))}. "
            f"Only {sorted(ALLOWED_FIELDS)} are allowed."
        )
    
    return errors


def validate_skill(skill_dir: Path, verbose: bool = False) -> list[str]:
    """Validate a single skill directory."""
    errors = []
    
    if not skill_dir.exists():
        return [f"Path does not exist: {skill_dir}"]
    
    if not skill_dir.is_dir():
        return [f"Not a directory: {skill_dir}"]
    
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["Missing required file: SKILL.md"]
    
    try:
        content = skill_md.read_text()
        metadata, body = parse_frontmatter(content)
    except Exception as e:
        return [f"Failed to parse frontmatter: {e}"]
    
    # Validate fields
    errors.extend(validate_metadata_fields(metadata))
    
    if "name" not in metadata:
        errors.append("Missing required field in frontmatter: name")
    else:
        errors.extend(validate_name(metadata["name"], skill_dir))
    
    if "description" not in metadata:
        errors.append("Missing required field in frontmatter: description")
    else:
        errors.extend(validate_description(metadata["description"]))
    
    if "compatibility" in metadata:
        errors.extend(validate_compatibility(metadata["compatibility"]))
    
    # Check recommended sections in body
    warnings = []
    if verbose:
        if "## When to Use" not in body:
            warnings.append("Recommended section missing: '## When to Use'")
        if "## Framework" not in body:
            warnings.append("Recommended section missing: '## Framework'")
        if "## Tips" not in body:
            warnings.append("Recommended section missing: '## Tips'")
        
        # Check body length
        body_lines = len(body.split("\n"))
        if body_lines > 500:
            warnings.append(f"SKILL.md body has {body_lines} lines (recommended: <500)")
        
        return errors, warnings
    
    return errors


def find_all_skills(base_path: Path) -> list[Path]:
    """Find all skill directories in the repository."""
    skills = []
    
    # Check plugins/*/skills/*/
    for skill_md in base_path.glob("plugins/*/skills/*/SKILL.md"):
        skills.append(skill_md.parent)
    
    # Check examples/skills/*/
    for skill_md in base_path.glob("examples/skills/*/SKILL.md"):
        skills.append(skill_md.parent)
    
    # Check examples/skills/*/* (nested like document-skills)
    for skill_md in base_path.glob("examples/skills/*/*/SKILL.md"):
        skills.append(skill_md.parent)
    
    return sorted(skills)


def main():
    parser = argparse.ArgumentParser(
        description="Validate skills against Agent Skills specification"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed validation output including warnings"
    )
    parser.add_argument(
        "--fix",
        action="store_true", 
        help="Auto-fix common issues (not yet implemented)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to repository or specific skill directory"
    )
    
    args = parser.parse_args()
    base_path = Path(args.path).resolve()
    
    # Check if path is a single skill or repository
    if (base_path / "SKILL.md").exists():
        skills = [base_path]
    else:
        skills = find_all_skills(base_path)
    
    if not skills:
        print("No skills found to validate")
        sys.exit(1)
    
    results = {
        "total": len(skills),
        "valid": 0,
        "invalid": 0,
        "errors": [],
        "warnings": []
    }
    
    for skill_dir in skills:
        if args.verbose:
            validation_result = validate_skill(skill_dir, verbose=True)
            if isinstance(validation_result, tuple):
                errors, warnings = validation_result
            else:
                errors, warnings = validation_result, []
        else:
            errors = validate_skill(skill_dir, verbose=False)
            warnings = []
        
        relative_path = skill_dir.relative_to(base_path) if base_path in skill_dir.parents or base_path == skill_dir else skill_dir
        
        if errors:
            results["invalid"] += 1
            results["errors"].append({
                "skill": str(relative_path),
                "errors": errors
            })
            if not args.json:
                print(f"❌ {relative_path}")
                for error in errors:
                    print(f"   - {error}")
        else:
            results["valid"] += 1
            if args.verbose and not args.json:
                print(f"✅ {relative_path}")
                for warning in warnings:
                    print(f"   ⚠️  {warning}")
        
        if warnings:
            results["warnings"].append({
                "skill": str(relative_path),
                "warnings": warnings
            })
    
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print()
        print(f"Summary: {results['valid']}/{results['total']} skills valid")
        if results["invalid"] > 0:
            print(f"         {results['invalid']} skills have errors")
    
    sys.exit(0 if results["invalid"] == 0 else 1)


if __name__ == "__main__":
    main()
