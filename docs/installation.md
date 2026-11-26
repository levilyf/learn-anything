# Installation

## Agent Skills-compatible agents

The project includes an Agent Skills-compatible package at `skills/learn-anything/`. Copy that directory into the agent's supported skills directory. Exact paths and reload behavior vary by agent; consult current agent documentation.

## Pi

Copy the skill folder into:

```text
~/.pi/agent/skills/learn-anything/
```

Restart or reload Pi if needed, then invoke:

```text
/skill:learn-anything
```

Example request: "Teach me cybersecurity from absolute zero. Diagnose my level, build a roadmap, and start lesson one. Use short lessons, exercises, and checkpoints."

## Other agents

Do not assume every agent supports the same discovery mechanism. Use its documented skill-loading mechanism, or adapt the `SKILL.md` instructions into its supported custom-instruction format.

Installing a skill does not automatically grant browsing, filesystem access, persistent memory, code execution, or access to training labs.
