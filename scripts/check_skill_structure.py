#!/usr/bin/env python3
"""Ensure GTM skill files include required progressive disclosure sections."""

from __future__ import annotations

import sys
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SECTION_PATTERNS = {
    "When to Use": re.compile(r"^##\s+When to Use.*$", re.MULTILINE),
    "Framework": re.compile(r"^##\s+Framework.*$", re.MULTILINE),
    "Templates": re.compile(r"^##\s+Templates.*$", re.MULTILINE),
    "Tips": re.compile(r"^##\s+Tips.*$", re.MULTILINE),
}
SECTION_BOUNDARY = re.compile(r"^##\s+", re.MULTILINE)
MIN_SECTION_LINES = 2
SKIP_PATTERNS = ("document-skills/", "examples/skills/")


def skill_files() -> list[Path]:
    skills: list[Path] = []
    for skill_path in ROOT.rglob("SKILL.md"):
        relative = skill_path.relative_to(ROOT)
        rel_str = str(relative)
        if any(pattern in rel_str for pattern in SKIP_PATTERNS):
            continue
        skills.append(skill_path)
    return skills


def main() -> None:
    failures: list[str] = []
    for path in skill_files():
        text = path.read_text(encoding="utf-8")
        missing_labels = []
        for label, pattern in SECTION_PATTERNS.items():
            match = pattern.search(text)
            if not match:
                missing_labels.append(f"## {label}")
                continue

            content = extract_section_content(text, match)
            content_lines = [line for line in content.splitlines() if line.strip()]
            if len(content_lines) < MIN_SECTION_LINES:
                failures.append(
                    f"{path.relative_to(ROOT)} section '## {label}' must include at least {MIN_SECTION_LINES} non-empty lines"
                )

        if missing_labels:
            failures.append(
                f"{path.relative_to(ROOT)} missing sections: {', '.join(missing_labels)}"
            )

    if failures:
        print("[skill structure lint] The following skills need updates:")
        for failure in failures:
            print(" -", failure)
        sys.exit(1)

    print("All skills contain required progressive disclosure headings.")


def extract_section_content(text: str, match: re.Match[str]) -> str:
    start = match.end()
    next_match = SECTION_BOUNDARY.search(text, start)
    end = next_match.start() if next_match else len(text)
    return text[start:end].strip()


if __name__ == "__main__":
    main()
