# Architecture overview

Learn Anything is a framework-neutral learning method with agent-specific adapters.

## Layers

1. **Agent interface:** Presents the tutor skill and exposes host capabilities.
2. **Learning workflows:** Curriculum, teaching, practice, assessment, revision, and progress.
3. **Portable records:** Versioned JSON documents for learner state and learning artifacts.
4. **Subject modules:** Domain-specific prerequisites, outcomes, topic sequences, exercises, and safety notes.

## Runtime boundary

The initial release is instruction-first. The host LLM performs reasoning and dialogue. The skill does not itself provide model inference, web search, a filesystem, a scheduler, or lab execution. Optional integrations must be capability-detected, never assumed.

## Data flow

Learner goal -> diagnostic -> curriculum -> lesson -> practice attempt -> assessment evidence -> mastery update -> revision plan -> next lesson.

## Storage

Learner records are user-owned JSON files. Subject modules are shared project content and must never contain personal learner records.

## Why no backend yet?

The first question is whether the teaching workflow produces better learning behavior. A backend, accounts, and dashboard would add operational complexity before that is established.
