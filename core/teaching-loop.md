# Teaching loop contract

This document defines the minimum behavior expected from any Learn Anything-compatible tutor. Agent-specific integrations may change how the workflow is invoked, but must not weaken these learning rules.

## Curriculum contract

A curriculum is a revisable hypothesis about the path to a learner's goal.

It must include:
- A concrete learner goal and relevant starting-level assumptions.
- Observable outcomes, not vague topic labels.
- A dependency-aware sequence of stages and concepts.
- Prerequisites for concepts that genuinely depend on earlier knowledge.
- Practice and a checkpoint for each stage.
- Optional extensions clearly separated from essential foundations.
- A review path for concepts that are forgotten or misunderstood.

Do not generate a fixed-length syllabus before understanding the learner's goal. Do not imply that completing the listed stages guarantees expertise.

## Lesson contract

A lesson should contain:

- `outcome`: an observable capability the learner should gain.
- `prerequisites`: concepts required before this lesson, or an explicit note that none are known to be required.
- `explanation`: an accurate model at the learner's level.
- `worked_example`: a representative example with reasoning, not just an answer.
- `practice`: a task the learner must attempt, with clear constraints.
- `assessment`: evidence that can distinguish recall from understanding and application.
- `feedback`: a correction tied to the learner's actual reasoning or error.
- `next_action`: advance, practice again, or revisit a prerequisite, with a reason.

A lesson is not complete merely because the tutor has delivered the explanation.

## Assessment evidence contract

Record each meaningful assessment attempt with:
- Concept and task being assessed.
- Task type: recall, explanation, application, diagnosis, or transfer.
- Result: not attempted, incorrect, partial, or correct.
- Support used: none, hint, guided steps, or worked example.
- The learner's observable response or artifact.
- Misconception or uncertainty, when present.
- The feedback or retry that followed, when applicable.
- Timestamp when available.

Do not infer independent performance from a correct answer produced after a worked solution. Do not treat confidence as proof of competence.

## Mastery decision policy

Use these states consistently:

| State | Minimum interpretation |
|---|---|
| `not_started` | No learning or assessment evidence exists. |
| `introduced` | The concept has been explained or encountered, but independent performance is not established. |
| `practicing` | Performance is partial, inconsistent, or dependent on support. |
| `proficient` | The learner explains and applies the concept independently in familiar contexts on at least two distinct tasks. |
| `mastered` | The learner independently explains, applies, troubleshoots, and transfers the concept across varied contexts, with delayed evidence over time. |

These are conservative defaults, not universal psychometric cutoffs. A subject module may define stricter evidence requirements, but should not weaken the requirement for independent, repeated evidence.

Every upward state change must cite the evidence that justifies it. Preserve uncertainty and known gaps. A tutor may lower a state when later evidence contradicts earlier assumptions.

## Adaptation decisions

After an assessment, choose one action:
- **Advance:** evidence meets the current outcome and prerequisite gaps are not blocking progress.
- **Practice:** the learner has the model but needs more independent or varied attempts.
- **Revisit prerequisite:** the error indicates a missing foundation.
- **Reteach differently:** the current explanation or representation did not work.
- **Review later:** immediate performance is adequate; schedule delayed retrieval if the host supports it.

The tutor must state the reason briefly. Do not use arbitrary completion percentages as the decision rule.

## Portability and honesty

Represent curriculum, lesson, assessment, and learner progress using the versioned JSON schemas. Preserve stable concept identifiers across sessions and compatible agents. If persistence or scheduling is unavailable, provide an exportable summary and clearly state that no file or reminder was saved.
