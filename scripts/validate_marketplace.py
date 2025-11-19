#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

REQUIRED_PLUGIN_KEYS = {"name", "source", "description", "category", "version", "commands", "agents", "skills", "keywords"}
REQUIRED_OWNER_KEYS = {"name", "email", "url"}
ALLOWED_AGENT_MODELS = {"haiku", "sonnet"}
FRONTMATTER_NAME_PATTERN = re.compile(r"[a-z0-9-]+")
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
KEYWORD_PATTERN = re.compile(r"^[a-z0-9-]{2,}$")
MIN_KEYWORDS = 3


def fail(message: str):
    print(f"[marketplace validation] {message}")
    sys.exit(1)


def resolve_component_path(plugin_source: str, rel_path: str) -> Path:
    """Return the absolute path for a plugin component reference.

    Modern marketplace entries use paths like "./commands/foo.md" relative to
    the plugin root. Legacy entries may still include "./plugins/..." or
    "../plugins/..." which should resolve from the repo root. This helper
    handles both cases so we can gradually normalize manifests without
    breaking older references.
    """

    rel_path = rel_path.strip()
    normalized = rel_path.replace("\\", "/")
    plugin_root = (ROOT / plugin_source.lstrip("./")).resolve()

    # Legacy references that already include the plugins/ prefix (or traverse
    # upward) should resolve relative to the repo root.
    if (
        normalized.startswith("./plugins/")
        or normalized.startswith("plugins/")
        or normalized.startswith("../")
    ):
        return (ROOT / normalized.lstrip("./")).resolve()

    # Standard case: treat "./foo/bar.md" as relative to the plugin root.
    if normalized.startswith("./"):
        return (plugin_root / normalized[2:]).resolve()

    # Absolute paths (rare) are returned as-is; any missing files will be
    # reported by the downstream validator.
    abs_candidate = Path(normalized)
    if abs_candidate.is_absolute():
        return abs_candidate

    # Fallback to interpreting the entry relative to the plugin root.
    return (plugin_root / normalized).resolve()


def validate_file(path: Path):
    if not path.exists():
        fail(f"Referenced file missing: {path}")
    if path.suffix != ".md" and path.name != "SKILL.md":
        fail(f"Referenced file must be markdown: {path}")


def validate_marketplace():
    if not MARKETPLACE.exists():
        fail("marketplace.json not found")

    data = json.loads(MARKETPLACE.read_text())
    if "owner" not in data:
        fail("Missing owner metadata")

    owner_keys = set(data["owner"].keys())
    missing_owner = REQUIRED_OWNER_KEYS - owner_keys
    if missing_owner:
        fail(f"Owner metadata missing keys: {missing_owner}")

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("Expected non-empty plugins array")

    for plugin in plugins:
        if missing := REQUIRED_PLUGIN_KEYS - set(plugin.keys()):
            fail(f"Plugin '{plugin.get('name')}' missing keys: {missing}")

        version = plugin.get("version", "")
        if not SEMVER_PATTERN.fullmatch(str(version)):
            fail(f"Plugin '{plugin.get('name')}' has invalid semantic version '{version}'")

        keywords = plugin.get("keywords")
        if not isinstance(keywords, list) or len(keywords) < MIN_KEYWORDS:
            fail(
                f"Plugin '{plugin.get('name')}' must include at least {MIN_KEYWORDS} keyword slugs"
            )

        keyword_set = set()
        for keyword in keywords:
            if not isinstance(keyword, str) or not KEYWORD_PATTERN.fullmatch(keyword.strip()):
                fail(
                    f"Plugin '{plugin.get('name')}' contains invalid keyword '{keyword}'. Keywords must be lowercase slugs"
                )
            if keyword in keyword_set:
                fail(f"Plugin '{plugin.get('name')}' contains duplicate keyword '{keyword}'")
            keyword_set.add(keyword)

        plugin_source = plugin["source"]
        for field in ("commands", "agents", "skills"):
            entries = plugin[field]
            if not isinstance(entries, list) or not entries:
                fail(f"Plugin '{plugin['name']}' has empty {field}")
            for rel_path in entries:
                component_path = resolve_component_path(plugin_source, rel_path)
                validate_file(component_path)
                ensure_component_matches_plugin(plugin["name"], field, component_path)

    validate_skill_frontmatter()
    validate_agent_frontmatter()
    validate_command_frontmatter()
    print("marketplace.json validation passed")


def validate_skill_frontmatter():
    for skill_path in ROOT.rglob("SKILL.md"):
        rel = skill_path.relative_to(ROOT)
        if "templates/" in str(rel):
            continue

        text = skill_path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            fail(f"{rel}: missing YAML frontmatter")

        parts = text.split("---", 2)
        if len(parts) < 3:
            fail(f"{rel}: invalid YAML frontmatter structure")

        try:
            data = yaml.safe_load(parts[1])
        except yaml.YAMLError as exc:
            fail(f"{rel}: unable to parse YAML frontmatter ({exc})")

        if not isinstance(data, dict):
            fail(f"{rel}: frontmatter must be a mapping")

        name = data.get("name")
        if not name:
            fail(f"{rel}: missing 'name' in frontmatter")

        if not FRONTMATTER_NAME_PATTERN.fullmatch(name):
            fail(f"{rel}: name '{name}' must be lowercase hyphen-case")

        directory_name = skill_path.parent.name
        if name != directory_name:
            fail(
                f"{rel}: name '{name}' must exactly match containing directory '{directory_name}'"
            )


def validate_agent_frontmatter():
    agent_dir = ROOT / "plugins"
    for agent_path in agent_dir.rglob("agents/*.md"):
        rel = agent_path.relative_to(ROOT)
        if str(rel).startswith("templates/"):
            continue

        data = load_frontmatter(agent_path)
        for key in ("name", "description", "model"):
            if key not in data:
                fail(f"{rel}: missing '{key}' in frontmatter")

        name = data["name"]
        if not FRONTMATTER_NAME_PATTERN.fullmatch(name):
            fail(f"{rel}: name '{name}' must be lowercase hyphen-case")

        filename = agent_path.stem
        if name != filename:
            fail(f"{rel}: name '{name}' must match filename '{filename}'")

        model = str(data["model"]).lower()
        if model not in ALLOWED_AGENT_MODELS:
            fail(
                f"{rel}: model '{data['model']}' must be one of {sorted(ALLOWED_AGENT_MODELS)}"
            )


def validate_command_frontmatter():
    plugins_dir = ROOT / "plugins"
    for command_path in plugins_dir.rglob("commands/*.md"):
        rel = command_path.relative_to(ROOT)
        if str(rel).startswith("templates/"):
            continue

        data = load_frontmatter(command_path)
        for key in ("name", "description", "usage"):
            if key not in data:
                fail(f"{rel}: missing '{key}' in frontmatter")

        name = data["name"]
        if not FRONTMATTER_NAME_PATTERN.fullmatch(name):
            fail(f"{rel}: name '{name}' must be lowercase hyphen-case")

        filename = command_path.stem
        if name != filename:
            fail(f"{rel}: name '{name}' must match filename '{filename}'")

        usage = data["usage"]
        if not isinstance(usage, str) or not usage.strip():
            fail(f"{rel}: 'usage' must be a non-empty string")
        if not usage.strip().startswith("/"):
            fail(f"{rel}: usage '{usage}' must start with '/' to show exact invocation")


def load_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(f"{path.relative_to(ROOT)}: invalid YAML frontmatter structure")

    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        fail(f"{path.relative_to(ROOT)}: unable to parse YAML frontmatter ({exc})")

    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)}: frontmatter must be a mapping")

    return data


def ensure_component_matches_plugin(plugin_name: str, component_type: str, path: Path) -> None:
    try:
        frontmatter = load_frontmatter(path)
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover - defensive
        fail(f"{path}: unable to validate frontmatter ({exc})")

    metadata_name = frontmatter.get("name")
    if metadata_name != path.stem and path.name != "SKILL.md":
        fail(
            f"{path.relative_to(ROOT)}: name '{metadata_name}' must match filename '{path.stem}'"
        )

    plugin_field = frontmatter.get("plugin")
    if plugin_field is None:
        # Not all files specify this yet; skip but enforce directory pattern
        directory_plugin = path.parts[path.parts.index("plugins") + 1]
        if directory_plugin != plugin_name:
            fail(
                f"{path.relative_to(ROOT)}: resides in '{directory_plugin}' but referenced by plugin '{plugin_name}'"
            )
        return

    if plugin_field != plugin_name:
        fail(
            f"{path.relative_to(ROOT)}: plugin field '{plugin_field}' must equal '{plugin_name}'"
        )

if __name__ == "__main__":
    validate_marketplace()
