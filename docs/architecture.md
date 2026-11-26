# Architecture

Learn Anything is an instruction-first, agent-native learning system.

1. **Agent interface:** loads the skill and exposes host capabilities.
2. **Learning workflows:** diagnose, plan, teach, practice, assess, adapt, reinforce.
3. **Portable records:** versioned JSON schemas for learner state and learning artifacts.
4. **Subject modules:** prerequisites, outcomes, topic sequences, practical tasks, assessments, and safety.
5. **Content formats:** Markdown for human-readable lessons, Mermaid for optional diagrams, and JSON validated against JSON Schema for portable data.
6. **Presentation layer:** the host agent or future application renders content according to the rendering contract. It is not part of the universal teaching content.

## Content, data, and presentation

These are separate concerns:

- **Content** defines what is taught, why it matters, examples, practice, and evaluation criteria.
- **Data** records stable IDs, prerequisites, learner state, attempts, and evidence.
- **Presentation** decides whether a host displays Markdown, renders Mermaid, or provides an interactive interface.

See [the format standards](../formats/README.md) and [agent rendering contract](../formats/rendering-contract.md).

The skill does not provide model inference, file access, persistent memory, web search, scheduling, diagram rendering, or lab execution. Those capabilities come from the host agent and its tools. The tutor must detect limitations and be honest about them. A fallback must preserve the learning objective and safety requirements rather than pretending an unavailable feature exists.

The project should not be coupled to Pi or any single model provider. Learner data is private and user-controlled. Store it outside shared subject modules. Do not collect or transmit learner records by default.
