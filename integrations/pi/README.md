# Pi integration

Build the self-contained skill package from the repository root:

```bash
python scripts/package_skill.py
mkdir -p ~/.pi/agent/skills
cp -R dist/learn-anything ~/.pi/agent/skills/learn-anything
```

Restart or reload Pi if required, then invoke:

```text
/skill:learn-anything
```

The generated package includes the subject module, schemas, format contracts, and visual guides. Do not install only the source `skills/learn-anything/` directory: its supporting materials live elsewhere in the repository and are bundled by the packaging script.

Pi's available filesystem, browsing, persistence, rendering, and execution capabilities depend on the host configuration. The skill must not claim these capabilities unless they are actually available.
