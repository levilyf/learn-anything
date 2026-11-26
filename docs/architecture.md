# Architecture

Learn Anything is an instruction-first, agent-native learning system.

1. **Agent interface:** loads the skill and exposes host capabilities.
2. **Learning workflows:** diagnose, plan, teach, practice, assess, adapt, reinforce.
3. **Portable records:** versioned JSON schemas for learner state and learning artifacts.
4. **Subject modules:** prerequisites, outcomes, topic sequences, practical tasks, assessments, and safety.

The skill does not provide model inference, file access, persistent memory, web search, scheduling, or lab execution. Those capabilities come from the host agent and its tools. The tutor must detect limitations and be honest about them.

The project should not be coupled to Pi or any single model provider. Learner data is private and user-controlled. Store it outside shared subject modules. Do not collect or transmit learner records by default.
