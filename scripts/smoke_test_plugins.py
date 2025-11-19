#!/usr/bin/env python3
"""Lightweight smoke test for Claude GTM plugin assets.

This script loads `.claude-plugin/marketplace.json`, iterates over every plugin,
reads each referenced agent/command/skill file, and reports any missing or empty
content. It is intentionally simple so it can be wired into CI alongside the
existing schema validator.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"


def resolve_component_path(plugin_source: str, rel_path: str) -> Path:
    """Resolve rel_path relative to the plugin root, with legacy support."""

    rel_path = rel_path.strip()
    normalized = rel_path.replace("\\", "/")
    plugin_root = (REPO_ROOT / plugin_source.lstrip("./")).resolve()

    if (
        normalized.startswith("./plugins/")
        or normalized.startswith("plugins/")
        or normalized.startswith("../")
    ):
        return (REPO_ROOT / normalized.lstrip("./")).resolve()

    if normalized.startswith("./"):
        return (plugin_root / normalized[2:]).resolve()

    abs_candidate = Path(normalized)
    if abs_candidate.is_absolute():
        return abs_candidate

    return (plugin_root / normalized).resolve()


def read_markdown(path: Path) -> Tuple[bool, str]:
    """Return (is_valid, message) for the provided markdown file."""
    if not path.exists():
        return False, "missing file"
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return False, "file is empty"
    if not text.startswith("---"):
        return False, "missing YAML frontmatter"
    if "#" not in text:
        return False, "missing markdown headings"
    return True, "ok"


def iter_components(plugin: dict) -> Iterable[Tuple[str, Path]]:
    plugin_source = plugin["source"]
    for collection in ("agents", "commands", "skills"):
        for rel_path in plugin.get(collection, []):
            yield collection[:-1], resolve_component_path(plugin_source, rel_path)


def run_smoke_test(selected_plugins: List[str] | None = None) -> int:
    data = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    failures: list[str] = []

    for plugin in data.get("plugins", []):
        name = plugin["name"]
        if selected_plugins and name not in selected_plugins:
            continue
        for component_type, abs_path in iter_components(plugin):
            ok, msg = read_markdown(abs_path)
            if not ok:
                rel = abs_path.relative_to(REPO_ROOT)
                failures.append(f"[{name}] {component_type}: {rel} -> {msg}")

    if failures:
        print("Smoke test failures detected:\n" + "\n".join(failures), file=sys.stderr)
        return 1

    tested = selected_plugins or [p["name"] for p in data.get("plugins", [])]
    print(f"Smoke test passed for {len(tested)} plugin(s).")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Smoke test GTM plugin assets.")
    parser.add_argument(
        "plugins",
        metavar="PLUGIN",
        nargs="*",
        help="Optional subset of plugin names to test. Default checks all.",
    )
    args = parser.parse_args()
    raise SystemExit(run_smoke_test(args.plugins or None))


if __name__ == "__main__":
    main()
