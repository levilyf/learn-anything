# Learn Anything

**An open-source, agent-native learning engine for learning any subject.**

Learn Anything helps compatible AI agents teach through structured curricula, interactive lessons, deliberate practice, assessment, revision, and portable learner progress.

> Learn anything. Understand everything.

## Status

**Early development — v0.1.0.** This repository contains the initial teaching workflow, an Agent Skills-compatible entry point, portable data contracts, a beginner cybersecurity module, and validation tests. It is not yet a complete autonomous learning platform.

## What it aims to do

- Diagnose a learner's current knowledge and goals.
- Build a prerequisite-aware curriculum.
- Teach one coherent concept at a time.
- Combine explanations, worked examples, practice, and retrieval.
- Evaluate demonstrated understanding, not just lesson completion.
- Adapt explanations and difficulty when the learner struggles.
- Track mastery and schedule revision.
- Keep learner progress portable across supported agents.

## Quick start

1. Install `skills/learn-anything/` using your agent's skill mechanism.
2. Invoke the skill (for example, in Pi: `/skill:learn-anything`).
3. Ask: `Teach me cybersecurity from absolute zero. Diagnose my level, create a roadmap, and start lesson one.`
4. Export or save your learner record using `schemas/learner.schema.json`.

See [installation](docs/installation.md), [architecture](docs/architecture.md), and [creating subject modules](docs/creating-subject-modules.md).

## Repository layout

- `skills/`: portable Agent Skills entry point and teaching references
- `core/`: framework-neutral teaching-engine specifications
- `schemas/`: versioned JSON contracts for learner and learning data
- `subjects/`: subject-specific roadmaps, outcomes, and safe exercises
- `integrations/`: agent-specific installation and compatibility notes
- `examples/`: example learner data and sessions
- `scripts/` and `tests/`: validation and smoke tests
- `docs/`: architecture, installation, contribution, and roadmap docs

## Design principles

1. **Evidence over completion:** progress reflects what a learner can demonstrate.
2. **Model-agnostic:** the learning method must not depend on one LLM vendor.
3. **Portable by default:** learner data belongs to the learner.
4. **Subject-aware:** the same teaching loop adapts to each discipline.
5. **Safe practice:** hands-on activities respect legal, ethical, and physical safety boundaries.
6. **Honest capabilities:** a skill cannot grant an agent tools, persistent memory, or browsing that the host does not provide.

## Development

Requires Python 3.10+ for validation. Runtime use of the skill does not require Python.

```bash
python scripts/validate_project.py
python -m unittest discover -s tests -v
```

No third-party Python dependencies are required for the initial checks.

## Roadmap

See [ROADMAP.md](ROADMAP.md). The first milestone focuses on validating the teaching loop with real learners before adding a web app, accounts, or a backend.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

Apache-2.0. See [LICENSE](LICENSE).
