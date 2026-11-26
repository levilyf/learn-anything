# Cybersecurity assessment guide

## Assessment principles

Assess understanding and safe judgment, not tool familiarity or memorized terminology. Use a mix of explanation, application, diagnosis, and transfer tasks. Never infer mastery from a multiple-choice score alone.

## Competency bands

### Foundation
The learner can:
- Explain basic computer, operating-system, and networking concepts.
- Distinguish threat, vulnerability, exploit, control, and risk.
- Describe authentication, authorization, MFA, encryption, hashing, and backups.
- Recognize safe vs. unsafe practice boundaries.

### Applied
The learner can:
- Read a simple network diagram and sanitized log.
- Explain a web request and common trust boundaries.
- Identify basic insecure design patterns in toy examples.
- Recommend proportionate controls and explain trade-offs.
- Complete a scoped lab and document what was and was not tested.

### Independent
The learner can:
- Investigate a supplied scenario using evidence and explicit assumptions.
- Prioritize findings by likelihood, impact, and context.
- Propose remediation and explain how to verify it.
- Communicate a concise incident or assessment report.
- Transfer principles to an unfamiliar but safe scenario.

### Specialization-ready
The learner can:
- Demonstrate the prerequisites for a chosen branch.
- Use the branch's methods in a controlled lab or realistic simulation.
- Explain tool limitations, legal scope, and operational risks.
- Produce a reviewable project with evidence and remediation.

## Evidence types

| Type | Example |
|---|---|
| Explanation | Explain why hashing is not encryption and when each is used. |
| Application | Recommend MFA and recovery controls for a fictional small business. |
| Diagnosis | Interpret a sanitized authentication log and state what cannot be concluded. |
| Transfer | Apply least privilege to a different system or scenario. |
| Practical artifact | Produce a network map, threat model, incident report, or secure design review. |

## Common misconceptions to test

- A vulnerability is not automatically an exploitable incident.
- A scanner finding is not proof of impact.
- HTTPS does not make a malicious site trustworthy.
- Encoding is not encryption.
- Hashing is not reversible encryption.
- Authentication and authorization are different.
- A firewall does not replace patching, identity controls, or secure design.
- A single indicator does not establish attribution.
- Security is risk management, not a promise of zero risk.
- Permission and scope are required before testing.

## Mastery decision

Use the project's shared mastery evaluator and evidence schema. Keep evidence tied to the relevant concept. Require independent performance across more than one task type; for durable mastery, include delayed evidence and a transfer task. If evidence is incomplete, retain the lower state and explain what is missing.

## Remediation

When a learner struggles:
1. Identify the exact misconception or missing prerequisite.
2. Re-explain with a different representation.
3. Model one worked example.
4. Give a smaller, safe practice task.
5. Re-test independently with a different scenario.

When a learner succeeds:
1. Change the context, not just the numbers or names.
2. Ask for trade-offs and limitations.
3. Add a realistic artifact or project.
4. Schedule delayed retrieval.
