#!/usr/bin/env python3
"""
Upgrade all skills to full Agent Skills specification compliance.

This script adds optional fields (license, compatibility, metadata) to all
SKILL.md files that don't already have them.

Usage:
    python scripts/upgrade_skills.py --dry-run  # Preview changes
    python scripts/upgrade_skills.py            # Apply changes
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


def get_plugin_category(skill_path: Path) -> str:
    """Determine category based on plugin location."""
    path_str = str(skill_path)
    
    # Map plugins to categories
    category_map = {
        "sales-prospecting": "sales",
        "sales-pipeline": "sales",
        "sales-enablement": "sales",
        "sales-coaching": "sales",
        "sales-calls": "sales",
        "sales-operations": "sales",
        "sales-handoff": "sales",
        "enterprise-sales": "sales",
        "account-management": "sales",
        "content-marketing": "marketing",
        "email-marketing": "marketing",
        "social-media": "marketing",
        "seo": "marketing",
        "paid-media": "marketing",
        "pr-communications": "marketing",
        "product-marketing": "marketing",
        "event-marketing": "marketing",
        "webinar-automation": "marketing",
        "video-marketing": "marketing",
        "copywriting": "marketing",
        "customer-marketing": "marketing",
        "design-creative": "marketing",
        "brand-strategy": "marketing",
        "marketing-automation": "marketing",
        "marketing-analytics": "marketing",
        "social-media-marketing": "marketing",
        "technical-writing": "marketing",
        "community-building": "marketing",
        "abm-orchestration": "orchestration",
        "lead-nurture-orchestration": "orchestration",
        "product-launch-orchestration": "orchestration",
        "content-pipeline-orchestration": "orchestration",
        "analytics-pipeline-orchestration": "orchestration",
        "email-sequence-orchestration": "orchestration",
        "campaign-orchestration": "orchestration",
        "customer-journey-orchestration": "orchestration",
        "customer-advocacy-orchestration": "orchestration",
        "customer-feedback-orchestration": "orchestration",
        "intent-signal-orchestration": "orchestration",
        "loyalty-lifecycle-orchestration": "orchestration",
        "partner-co-marketing-orchestration": "orchestration",
        "referral-program-orchestration": "orchestration",
        "renewal-orchestration": "orchestration",
        "revenue-forecasting-pipeline": "orchestration",
        "seo-workflow-orchestration": "orchestration",
        "social-scheduler-orchestration": "orchestration",
        "community-orchestration": "orchestration",
        "growth-experiments": "growth",
        "product-led-growth": "growth",
        "pricing-strategy": "growth",
        "customer-analytics": "analytics",
        "revenue-analytics": "analytics",
        "business-intelligence": "analytics",
        "data-enrichment-master": "data",
        "data-signal-enrichment": "data",
        "competitive-intelligence": "research",
        "market-research": "research",
        "voice-of-customer": "research",
        "customer-success": "customer-success",
        "partnership-development": "partnerships",
        "personalization-engine": "personalization",
        "b2b-saas": "industry",
        "e-commerce": "industry",
        "healthcare-marketing": "industry",
        "financial-services": "industry",
        "edtech-growth": "industry",
        "manufacturing-sales": "industry",
    }
    
    # Find plugin name from path
    for plugin_name, category in category_map.items():
        if f"plugins/{plugin_name}/" in path_str:
            return category
    
    # Default for examples
    if "examples/" in path_str:
        return "examples"
    
    return "general"


def parse_frontmatter(content: str) -> tuple[dict, str, str]:
    """Parse YAML frontmatter, returning metadata dict, body, and raw frontmatter."""
    if not content.startswith("---"):
        raise ValueError("Missing YAML frontmatter delimiter")
    
    # Find the end of frontmatter
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        raise ValueError("Invalid frontmatter format - missing closing ---")
    
    frontmatter_end = end_match.start() + 3
    frontmatter_text = content[3:frontmatter_end].strip()
    body = content[frontmatter_end + end_match.end() - end_match.start():]
    
    # Parse frontmatter
    metadata = {}
    lines = frontmatter_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            
            # Handle multi-line values
            if not value and i + 1 < len(lines) and lines[i + 1].startswith("  "):
                # Multi-line value
                value_lines = []
                i += 1
                while i < len(lines) and lines[i].startswith("  "):
                    value_lines.append(lines[i].strip())
                    i += 1
                value = " ".join(value_lines)
                i -= 1  # Back up one since the loop will increment
            
            metadata[key] = value.strip('"\'')
        i += 1
    
    return metadata, body, frontmatter_text


def build_new_frontmatter(metadata: dict, skill_path: Path) -> str:
    """Build new frontmatter with all required and optional fields."""
    name = metadata.get("name", skill_path.name)
    description = metadata.get("description", "")
    
    # Get category
    category = get_plugin_category(skill_path)
    
    # Build new frontmatter
    lines = [
        "---",
        f"name: {name}",
        f"description: {description}",
    ]
    
    # Add license if not present
    if "license" not in metadata:
        lines.append("license: Apache-2.0")
    else:
        lines.append(f"license: {metadata['license']}")
    
    # Add compatibility if not present
    if "compatibility" not in metadata:
        lines.append("compatibility: Claude Code (or similar products)")
    else:
        lines.append(f"compatibility: {metadata['compatibility']}")
    
    # Add metadata block if not present
    if "metadata" not in metadata:
        lines.extend([
            "metadata:",
            "  author: gtm-agents",
            '  version: "1.0"',
            f"  category: {category}",
        ])
    
    lines.append("---")
    
    return "\n".join(lines)


def upgrade_skill(skill_path: Path, dry_run: bool = False) -> tuple[bool, str]:
    """Upgrade a single skill to full compliance."""
    skill_md = skill_path / "SKILL.md"
    
    if not skill_md.exists():
        return False, "SKILL.md not found"
    
    content = skill_md.read_text()
    
    try:
        metadata, body, raw_frontmatter = parse_frontmatter(content)
    except Exception as e:
        return False, f"Failed to parse: {e}"
    
    # Check if already has all optional fields
    has_license = "license" in metadata
    has_compatibility = "compatibility" in metadata
    has_metadata = "metadata:" in raw_frontmatter
    
    if has_license and has_compatibility and has_metadata:
        return True, "Already compliant"
    
    # Build new content
    new_frontmatter = build_new_frontmatter(metadata, skill_path)
    new_content = new_frontmatter + "\n" + body.lstrip()
    
    if dry_run:
        changes = []
        if not has_license:
            changes.append("+ license")
        if not has_compatibility:
            changes.append("+ compatibility")
        if not has_metadata:
            changes.append("+ metadata")
        return True, f"Would add: {', '.join(changes)}"
    
    # Write updated content
    skill_md.write_text(new_content)
    
    changes = []
    if not has_license:
        changes.append("license")
    if not has_compatibility:
        changes.append("compatibility")
    if not has_metadata:
        changes.append("metadata")
    
    return True, f"Added: {', '.join(changes)}"


def find_all_skills(base_path: Path) -> list[Path]:
    """Find all skill directories."""
    skills = []
    
    for skill_md in base_path.glob("plugins/*/skills/*/SKILL.md"):
        skills.append(skill_md.parent)
    
    for skill_md in base_path.glob("examples/skills/*/SKILL.md"):
        skills.append(skill_md.parent)
    
    for skill_md in base_path.glob("examples/skills/*/*/SKILL.md"):
        skills.append(skill_md.parent)
    
    return sorted(skills)


def main():
    parser = argparse.ArgumentParser(
        description="Upgrade skills to full Agent Skills compliance"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Preview changes without modifying files"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to repository or specific skill directory"
    )
    
    args = parser.parse_args()
    base_path = Path(args.path).resolve()
    
    if (base_path / "SKILL.md").exists():
        skills = [base_path]
    else:
        skills = find_all_skills(base_path)
    
    if not skills:
        print("No skills found")
        sys.exit(1)
    
    print(f"{'[DRY RUN] ' if args.dry_run else ''}Processing {len(skills)} skills...\n")
    
    upgraded = 0
    already_compliant = 0
    failed = 0
    
    for skill_path in skills:
        relative_path = skill_path.relative_to(base_path)
        success, message = upgrade_skill(skill_path, dry_run=args.dry_run)
        
        if success:
            if "Already compliant" in message:
                already_compliant += 1
                print(f"✓ {relative_path} - {message}")
            else:
                upgraded += 1
                print(f"✅ {relative_path} - {message}")
        else:
            failed += 1
            print(f"❌ {relative_path} - {message}")
    
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Summary:")
    print(f"  Upgraded: {upgraded}")
    print(f"  Already compliant: {already_compliant}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(skills)}")


if __name__ == "__main__":
    main()
