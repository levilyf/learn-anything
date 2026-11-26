#!/usr/bin/env python3
"""Build a self-contained Agent Skills package for Learn Anything."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIRS = ("schemas", "subjects", "formats", "visual")


def build_skill(destination: Path) -> Path:
    """Build a portable skill folder with every referenced local resource."""
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    source_skill = ROOT / "skills" / "learn-anything"
    skill_text = (source_skill / "SKILL.md").read_text(encoding="utf-8")

    replacements = {
        "../../subjects/": "references/subjects/",
        "../../schemas/": "references/schemas/",
        "../../formats/": "references/formats/",
        "../../visual/": "references/visual/",
    }
    for old, new in replacements.items():
        skill_text = skill_text.replace(old, new)

    (destination / "SKILL.md").write_text(skill_text, encoding="utf-8")
    shutil.copytree(source_skill / "references", destination / "references")

    for directory in PACKAGE_DIRS:
        shutil.copytree(ROOT / directory, destination / "references" / directory)

    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "destination",
        nargs="?",
        type=Path,
        default=ROOT / "dist" / "learn-anything",
        help="Output directory (default: dist/learn-anything)",
    )
    args = parser.parse_args()
    output = build_skill(args.destination.resolve())
    print(f"Built self-contained Learn Anything skill at: {output}")
    print("Install this directory as a single skill folder in your agent's skills directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
