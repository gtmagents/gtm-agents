#!/usr/bin/env python3
"""Validate Haiku/Sonnet mix across agent frontmatter."""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / "plugins"
TARGET_HAIKU_SHARE = 0.60
TOLERANCE = 0.05  # ±5%
ALLOWED_MODELS = {"haiku", "sonnet"}


def load_agent_model(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"{path}: missing YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: invalid YAML frontmatter structure")

    data = yaml.safe_load(parts[1]) or {}
    model = str(data.get("model", "")).lower().strip()
    if model not in ALLOWED_MODELS:
        raise ValueError(f"{path}: unexpected model '{data.get('model')}'")
    return model


def gather_models() -> Counter:
    counts: Counter[str] = Counter()
    for agent_path in AGENTS_DIR.rglob("agents/*.md"):
        relative = agent_path.relative_to(ROOT)
        if str(relative).startswith("templates/"):
            continue
        model = load_agent_model(agent_path)
        counts[model] += 1
    return counts


def main() -> None:
    if not AGENTS_DIR.exists():
        print("No plugins directory found", file=sys.stderr)
        sys.exit(1)

    counts = gather_models()
    total = sum(counts.values())
    if not total:
        print("No agents discovered; cannot compute model mix", file=sys.stderr)
        sys.exit(1)

    haiku_share = counts["haiku"] / total
    min_share = TARGET_HAIKU_SHARE - TOLERANCE
    max_share = TARGET_HAIKU_SHARE + TOLERANCE

    print(
        "Model mix summary:\n"
        f"  Total agents: {total}\n"
        f"  Haiku agents: {counts['haiku']} ({haiku_share:.1%})\n"
        f"  Sonnet agents: {counts['sonnet']} ({counts['sonnet'] / total:.1%})\n"
        f"  Target Haiku share: {TARGET_HAIKU_SHARE:.0%} ± {TOLERANCE:.0%}"
    )

    if not (min_share <= haiku_share <= max_share):
        print(
            f"Haiku share {haiku_share:.1%} is outside the allowed range "
            f"[{min_share:.0%}, {max_share:.0%}]",
            file=sys.stderr,
        )
        sys.exit(1)

    print("Model mix is within the allowed tolerance.")


if __name__ == "__main__":
    main()
