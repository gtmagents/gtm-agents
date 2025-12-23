#!/usr/bin/env python3
"""
Generate a skills index JSON file from marketplace.json and SKILL.md files.

This script creates a comprehensive skills-index.json that follows the Agent Skills
specification format, making it easy for agents to discover available skills.

Usage:
    python scripts/generate_skills_index.py
    python scripts/generate_skills_index.py --output skills-index.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from SKILL.md content."""
    if not content.startswith("---"):
        return {}
    
    # Find the end of frontmatter
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return {}
    
    frontmatter_text = content[3:end_match.start() + 3].strip()
    
    # Parse frontmatter
    metadata = {}
    lines = frontmatter_text.split("\n")
    i = 0
    in_metadata_block = False
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Handle metadata block
        if stripped == "metadata:":
            in_metadata_block = True
            metadata["metadata"] = {}
            i += 1
            continue
        
        if in_metadata_block:
            if line.startswith("  ") and ":" in stripped:
                key, value = stripped.split(":", 1)
                metadata["metadata"][key.strip()] = value.strip().strip('"\'')
            elif not line.startswith(" "):
                in_metadata_block = False
        
        if not in_metadata_block and ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            
            # Handle multi-line values
            if not value and i + 1 < len(lines) and lines[i + 1].startswith("  "):
                value_lines = []
                i += 1
                while i < len(lines) and lines[i].startswith("  "):
                    value_lines.append(lines[i].strip())
                    i += 1
                value = " ".join(value_lines)
                i -= 1
            
            metadata[key] = value
        i += 1
    
    return metadata


def get_skill_info(skill_path: Path, base_path: Path) -> Optional[dict]:
    """Extract skill information from a SKILL.md file."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return None
    
    try:
        content = skill_md.read_text()
        metadata = parse_frontmatter(content)
    except Exception:
        return None
    
    if not metadata.get("name") or not metadata.get("description"):
        return None
    
    # Determine relative path
    relative_path = skill_path.relative_to(base_path)
    
    # Extract plugin name from path
    parts = relative_path.parts
    plugin_name = None
    if len(parts) >= 2 and parts[0] == "plugins":
        plugin_name = parts[1]
    elif len(parts) >= 2 and parts[0] == "examples":
        plugin_name = "examples"
    
    # Get category from metadata or infer from plugin
    category = None
    if "metadata" in metadata and isinstance(metadata["metadata"], dict):
        category = metadata["metadata"].get("category")
    
    skill_info = {
        "name": metadata["name"],
        "description": metadata["description"],
        "path": str(relative_path),
        "location": str(relative_path / "SKILL.md"),
    }
    
    if plugin_name:
        skill_info["plugin"] = plugin_name
    
    if category:
        skill_info["category"] = category
    
    if metadata.get("license"):
        skill_info["license"] = metadata["license"]
    
    if metadata.get("compatibility"):
        skill_info["compatibility"] = metadata["compatibility"]
    
    # Check for optional directories
    if (skill_path / "assets").exists():
        skill_info["has_assets"] = True
    if (skill_path / "scripts").exists():
        skill_info["has_scripts"] = True
    if (skill_path / "references").exists():
        skill_info["has_references"] = True
    
    return skill_info


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


def generate_skills_index(base_path: Path) -> dict:
    """Generate the complete skills index."""
    skills = find_all_skills(base_path)
    
    skills_list = []
    categories = {}
    plugins = {}
    
    for skill_path in skills:
        skill_info = get_skill_info(skill_path, base_path)
        if skill_info:
            skills_list.append(skill_info)
            
            # Track categories
            category = skill_info.get("category", "uncategorized")
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
            
            # Track plugins
            plugin = skill_info.get("plugin", "unknown")
            if plugin not in plugins:
                plugins[plugin] = 0
            plugins[plugin] += 1
    
    # Sort skills by name
    skills_list.sort(key=lambda x: x["name"])
    
    return {
        "version": "1.0",
        "specification": "https://agentskills.io/specification",
        "generated_from": ".claude-plugin/marketplace.json",
        "total_skills": len(skills_list),
        "categories": dict(sorted(categories.items())),
        "plugins": dict(sorted(plugins.items())),
        "skills": skills_list
    }


def generate_available_skills_xml(skills_index: dict) -> str:
    """Generate the <available_skills> XML format for agent prompts."""
    lines = ["<available_skills>"]
    
    for skill in skills_index["skills"]:
        lines.append("  <skill>")
        lines.append(f"    <name>{skill['name']}</name>")
        lines.append(f"    <description>{skill['description']}</description>")
        lines.append(f"    <location>{skill['location']}</location>")
        lines.append("  </skill>")
    
    lines.append("</available_skills>")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate skills index JSON from SKILL.md files"
    )
    parser.add_argument(
        "--output", "-o",
        default="skills-index.json",
        help="Output file path (default: skills-index.json)"
    )
    parser.add_argument(
        "--xml",
        action="store_true",
        help="Also generate available_skills.xml for agent prompts"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to repository (default: current directory)"
    )
    
    args = parser.parse_args()
    base_path = Path(args.path).resolve()
    
    print(f"Scanning for skills in {base_path}...")
    
    skills_index = generate_skills_index(base_path)
    
    # Write JSON index
    output_path = base_path / args.output
    with open(output_path, "w") as f:
        json.dump(skills_index, f, indent=2)
    
    print(f"✅ Generated {output_path}")
    print(f"   Total skills: {skills_index['total_skills']}")
    print(f"   Categories: {len(skills_index['categories'])}")
    print(f"   Plugins: {len(skills_index['plugins'])}")
    
    # Optionally generate XML
    if args.xml:
        xml_content = generate_available_skills_xml(skills_index)
        xml_path = base_path / "available_skills.xml"
        with open(xml_path, "w") as f:
            f.write(xml_content)
        print(f"✅ Generated {xml_path}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
