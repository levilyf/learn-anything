# Contributing

Thanks for helping improve Learn Anything.

## High-value contributions
- Improve teaching instructions with evidence and concrete examples.
- Add a subject module using `subjects/_template/`.
- Add assessment cases that test reasoning and misconceptions.
- Improve portability across AI agents.
- Report inaccurate, unsafe, inaccessible, or confusing learning experiences.

## Before opening a pull request
1. Open an issue for substantial changes so the approach can be discussed.
2. Keep changes focused and explain the learner problem they solve.
3. Do not include private learner data, credentials, API keys, or copyrighted course material.
4. Run `python scripts/validate_project.py` and `python -m unittest discover -s tests -v`.
5. For subject modules, include learning outcomes, prerequisites, safe practice, and assessment criteria.

## Subject-module quality bar
State the audience and prerequisites, define observable outcomes, order topics by dependency, include practice and assessment criteria, address misconceptions, cite trustworthy resources where needed, and identify legal, safety, and ethical constraints.

## Pull request checklist
- [ ] The change has a clear learner benefit.
- [ ] Documentation is updated.
- [ ] Validation and tests pass.
- [ ] No secrets or personal learner data are included.
- [ ] Safety implications have been considered.
