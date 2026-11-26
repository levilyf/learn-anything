#!/usr/bin/env python3
"""Dependency-free structural and JSON smoke validator for Learn Anything."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "SECURITY.md", "ROADMAP.md", "skills/learn-anything/SKILL.md",
    "subjects/cybersecurity/subject.md", "subjects/_template/subject.md",
]

def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    for path in (ROOT / "schemas").glob("*.schema.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("type") != "object" or "$schema" not in data:
                errors.append(f"Schema missing expected top-level fields: {path.relative_to(ROOT)}")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
    for path in (ROOT / "examples").glob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
    skill = ROOT / "skills/learn-anything/SKILL.md"
    if skill.exists():
        content = skill.read_text(encoding="utf-8")
        if not content.startswith("---\n") or "name: learn-anything" not in content:
            errors.append("Skill frontmatter is missing or has the wrong name.")
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Learn Anything validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
