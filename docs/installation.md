# Installation

Learn Anything is maintained as a repository, but an installed agent skill must be self-contained. Build the distributable folder first so the skill's subject modules, schemas, visual guides, and format contracts travel with it.

## Build the skill package

Requirements: Python 3.10+.

From the repository root:

```bash
python scripts/package_skill.py
```

This creates `dist/learn-anything/` containing `SKILL.md` and all local references it needs. The generated folder is the installable artifact; do not copy only `skills/learn-anything/` from the source tree.

## Pi

```bash
mkdir -p ~/.pi/agent/skills
cp -R dist/learn-anything ~/.pi/agent/skills/learn-anything
```

Restart or reload Pi if required, then invoke:

```text
/skill:learn-anything
```

Example request: "Teach me cybersecurity from absolute zero. Diagnose my level, build a roadmap, and start lesson one. Use short lessons, exercises, and checkpoints."

## Other agents

Install the complete generated `dist/learn-anything/` folder using the agent's documented skills directory and discovery mechanism. Do not assume every agent uses the same path or invocation syntax.

Installing a skill does not automatically grant browsing, filesystem access, persistent memory, code execution, interactive rendering, or access to training labs. The skill must be explicit about which host capabilities are available.

## Updating

After pulling repository updates, rebuild the package and replace the installed skill folder. Keep learner progress files outside the skill installation directory so updating the skill does not overwrite personal data.
