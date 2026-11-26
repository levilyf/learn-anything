# Visual Learning System

Visual learning components are reusable teaching representations, not decoration. Each component must make a learning task clearer, help the learner reason, or support recall.

## Component catalogue

| Component | Best for | Canonical representation |
|---|---|---|
| Concept map | Relationships and prerequisite structure | Nodes and labeled edges |
| Process diagram | Ordered mechanisms and decisions | Mermaid flowchart or sequence |
| Annotated diagram | Parts of a system or object | Labeled regions and descriptions |
| Learning roadmap | Stages, dependencies, and progress | Ordered milestones with status |
| Simulation | Experimenting with inputs and observing outcomes | State, controls, rules, and safe scenarios |
| Revision card | Retrieval practice and durable recall | Prompt, response criteria, and visual cue |

## Design principles

1. **Purpose before appearance:** state what the learner should understand or do after viewing it.
2. **One visual, one job:** split diagrams that try to explain too many ideas.
3. **Progressive disclosure:** reveal complexity in stages where possible.
4. **Accessible by default:** labels must be understandable without color; provide text alternatives and descriptions.
5. **Portable definitions:** store meaning and structure independently of any renderer.
6. **Honest capabilities:** a component definition does not guarantee that the host can render or interact with it.

## Component contract

Every component should declare:
- `id`: stable identifier.
- `type`: one of the supported component types.
- `title`: learner-facing title.
- `purpose`: the learning purpose.
- `description`: text alternative or summary.
- `data`: type-specific content.
- `fallback`: a usable text representation.

Use [visual-component.schema.json](schemas/visual-component.schema.json) for the machine-readable contract. The schema is deliberately a common envelope; each component guide defines its type-specific data.

## Guides and examples

- [Concept map](components/concept-map.md)
- [Process diagram](components/flow-diagram.md)
- [Annotated diagram](components/annotated-diagram.md)
- [Learning roadmap](components/learning-roadmap.md)
- [Simulation](components/simulation.md)
- [Revision card](components/revision-card.md)
- [Cybersecurity concept map](examples/cybersecurity-concept-map.md)
- [Website request flow](examples/website-request-flow.md)
- [Network simulation example](examples/network-simulation.json)

## Rendering

Use Mermaid where supported for static diagrams. Use host-native interaction for simulations only when the host explicitly supports it. Otherwise provide a safe written scenario. Follow [the rendering contract](../formats/rendering-contract.md).

Visuals supplement explanations and assessment; they do not replace them. A learner must still demonstrate understanding independently.
