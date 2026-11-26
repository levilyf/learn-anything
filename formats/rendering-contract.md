# Agent rendering contract

This contract keeps learning content portable across agents and future interfaces.

## Responsibilities

The learning engine defines the objective, explanation, practice task, assessment criteria, and adaptation decision. The host agent or application chooses how to render them using available capabilities.

A renderer must not silently change the task, reveal a solution early, weaken safety boundaries, or change mastery criteria.

## Format selection and fallback

| Content | Preferred format | Fallback |
|---|---|---|
| Explanations and instructions | Markdown | Plain text |
| Prerequisite maps and processes | Mermaid | Markdown outline, then small ASCII diagram if useful |
| Learner state and assessment evidence | JSON | Copyable structured text only when JSON cannot be handled |
| Code or command examples | Fenced Markdown code | Plain text with clear boundaries |
| Interactive labs | Host-supported, authorized lab tool | Safe simulation or written exercise |

## Rendering rules

1. Render Markdown as readable content. If rich Markdown is unavailable, preserve headings, lists, and code boundaries in plain text.
2. Render Mermaid only when the host supports it. If unsupported or invalid, replace it with a concise textual explanation. Use ASCII only when it improves clarity.
3. Keep JSON machine-readable when passing it between tools or storing it. Do not expose raw JSON to learners unless they need to inspect or copy the data.
4. Never claim a diagram, file, lab, quiz interaction, or progress update was rendered, saved, executed, or validated unless the host confirms it.
5. If a requested interaction is unavailable, provide the closest safe text-based exercise and state the limitation.
6. Keep essential content available without color, animation, images, or interactive controls.

## Content/presentation separation

- Subject modules define concepts, outcomes, examples, practice, misconceptions, and safety.
- Schemas define portable data contracts.
- Agent integrations describe installation and host-specific capabilities.
- Renderers decide layout and interaction.

Do not put Pi-specific syntax into universal lesson content. Agent-specific invocation examples belong in `integrations/<agent>/`.

## Safety and permissions

A renderer or integration does not create authorization. For cybersecurity labs, use only owned systems, explicitly authorized targets, or intentionally vulnerable environments. If the host cannot provide a safe lab, use a conceptual simulation or defensive exercise instead.
