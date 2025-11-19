#!/usr/bin/env python3
"""Cross-link validator for Claude GTM Agents marketplace assets.

This script ensures two-way consistency between `.claude-plugin/marketplace.json`
references and the files that live under `plugins/*`. It catches cases where a
plugin references the wrong asset, omits a file from the marketplace catalog, or
stores a component outside its owning plugin directory.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
PLUGINS_DIR = ROOT / "plugins"

COMPONENT_TYPES = ("commands", "agents", "skills")
SKIP_DIR_NAMES = {"templates"}


def fail(message: str) -> None:
    print(f"[cross-link validator] {message}")
    sys.exit(1)


def normalize_marketplace_path(rel_path: str) -> Path:
    abs_path = (MARKETPLACE.parent / rel_path).resolve()
    try:
        return abs_path.relative_to(ROOT)
    except ValueError:
        fail(f"Marketplace path '{rel_path}' resolves outside of repository root")


def collect_actual_components() -> Dict[Tuple[str, str], Set[Path]]:
    """Return {(plugin_name, component_type): {relative_paths}}."""
    results: Dict[Tuple[str, str], Set[Path]] = defaultdict(set)

    for plugin_dir in PLUGINS_DIR.iterdir():
        if not plugin_dir.is_dir() or plugin_dir.name.startswith('.'):
            continue
        plugin_name = plugin_dir.name

        for component_type in COMPONENT_TYPES:
            base_dir = plugin_dir / component_type
            if not base_dir.exists():
                continue

            for path in base_dir.rglob("*.md"):
                if any(part in SKIP_DIR_NAMES for part in path.parts):
                    continue
                if component_type == "skills" and path.name != "SKILL.md":
                    # Skills directories contain SKILL.md plus optional assets; only lint canonical file.
                    continue

                rel = path.relative_to(ROOT)
                results[(plugin_name, component_type)].add(rel)

    return results


def collect_marketplace_components(plugins: List[dict]) -> Dict[Tuple[str, str], Set[Path]]:
    referenced: Dict[Tuple[str, str], Set[Path]] = defaultdict(set)

    for plugin in plugins:
        plugin_name = plugin.get("name")
        if not plugin_name:
            fail("Encountered plugin entry without a name")

        for component_type in COMPONENT_TYPES:
            entries = plugin.get(component_type, [])
            if not isinstance(entries, list):
                fail(f"Plugin '{plugin_name}' field '{component_type}' must be a list")

            for rel_path in entries:
                normalized = normalize_marketplace_path(rel_path)
                referenced[(plugin_name, component_type)].add(normalized)

                try:
                    path_plugin = normalized.parts[1]  # 'plugins/<name>/...'
                except IndexError:  # pragma: no cover - defensive guard
                    fail(f"Marketplace path '{rel_path}' is malformed")

                if path_plugin != plugin_name:
                    fail(
                        f"Plugin '{plugin_name}' lists '{rel_path}' which lives in plugin '{path_plugin}'"
                    )

    return referenced


def main() -> None:
    if not MARKETPLACE.exists():
        fail("marketplace.json not found")

    data = json.loads(MARKETPLACE.read_text())
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("Expected non-empty plugins array in marketplace")

    marketplace_map = collect_marketplace_components(plugins)
    filesystem_map = collect_actual_components()

    errors: List[str] = []

    # Check for missing registrations in marketplace
    for key, actual_paths in filesystem_map.items():
        referenced_paths = marketplace_map.get(key, set())
        missing = sorted(actual_paths - referenced_paths)
        if missing:
            plugin_name, component_type = key
            errors.append(
                f"Plugin '{plugin_name}' is missing {component_type} entries in marketplace: "
                + ", ".join(str(p) for p in missing)
            )

    # Check for marketplace entries pointing to non-existent files (extra guard)
    for key, referenced_paths in marketplace_map.items():
        actual_paths = filesystem_map.get(key, set())
        extras = sorted(referenced_paths - actual_paths)
        if extras:
            plugin_name, component_type = key
            errors.append(
                f"Plugin '{plugin_name}' lists {component_type} not found on disk: "
                + ", ".join(str(p) for p in extras)
            )

    if errors:
        fail("\n".join(errors))

    print("Cross-link validation passed: marketplace references match filesystem")


if __name__ == "__main__":
    main()
