#!/usr/bin/env python3
"""Build a self-contained Agent Skills package for Learn Anything."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DESTINATION = ROOT / "dist" / "learn-anything"
PACKAGE_DIRS = ("schemas", "subjects", "formats", "visual")


def build_skill(destination: Path) -> Path:
    """Build a portable skill folder without deleting arbitrary user data."""
    destination = destination.resolve()
    default_destination = DEFAULT_DESTINATION.resolve()

    if destination == ROOT or destination in ROOT.parents:
        raise ValueError("Refusing to use the repository root or one of its parents as output.")
    if destination.is_relative_to(ROOT) and destination != default_destination:
        raise ValueError("Output inside the repository is restricted to dist/learn-anything.")
    if destination.exists():
        if destination != default_destination:
            raise FileExistsError(
                f"Output already exists; refusing to delete arbitrary data: {destination}"
            )
        if destination.is_symlink() or not destination.is_dir():
            raise ValueError("Default output exists but is not a regular directory.")
        shutil.rmtree(destination)

    destination.mkdir(parents=True, exist_ok=True)

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
        default=DEFAULT_DESTINATION,
        help="Output directory (default: dist/learn-anything)",
    )
    args = parser.parse_args()
    output = build_skill(args.destination)
    print(f"Built self-contained Learn Anything skill at: {output}")
    print("Install this directory as a single skill folder in your agent's skills directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
