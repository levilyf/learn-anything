# Content and presentation formats

Learn Anything separates **learning content**, **portable learning data**, and **presentation**.

- Markdown is the canonical human-readable format for lessons, instructions, explanations, and documentation.
- Mermaid is the preferred source format for diagrams that explain relationships, sequences, and decisions.
- JSON is the canonical machine-readable format for learner records, curricula, lessons, and assessment evidence.
- JSON Schema defines the contracts that validate those JSON documents.
- ASCII diagrams are a fallback for small diagrams when Mermaid cannot be rendered.

The host agent decides how to display content. A format choice must never change the learning objective or assessment standard.

## Files in this directory

- [Markdown standard](markdown.md)
- [Mermaid standard](mermaid.md)
- [JSON standard](json.md)
- [Rendering contract](rendering-contract.md)
- [Canonical lesson template](lesson-template.md)

## Separation of concerns

1. **Content:** what is taught and what the learner must do.
2. **Data:** structured outcomes, prerequisites, attempts, evidence, and progress.
3. **Presentation:** how an agent or future application displays that content.

Do not encode essential teaching instructions only in a diagram. Do not put learner-specific progress in shared subject files. Do not make a lesson depend on a particular UI.

## Source of truth

The versioned schemas in `../schemas/` define the machine-readable contracts. The standards here explain how to author and render content. If a format guide conflicts with a schema, update both in the same change and add a regression test.
