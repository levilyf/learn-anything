# Cybersecurity labs and projects

Practical work must be safe, scoped, and legal. The default environment is a local sandbox, a supplied dataset, an intentionally vulnerable training application, or a system the learner owns and is explicitly authorized to test.

## Lab rules

Before any hands-on task, the tutor must establish:
- The target and owner.
- Explicit permission and scope.
- The environment and whether it is isolated.
- The permitted actions and prohibited actions.
- A cleanup and recovery plan.

If scope is unclear, do not proceed with active testing. Switch to a fictional scenario, supplied dataset, or conceptual explanation.

Never provide instructions for unauthorized access, credential theft, stealth, persistence, malware deployment, evasion, or real-world exploitation. Do not use public targets as practice. Do not ask learners to expose secrets, personal data, or live credentials in chat.

## Progressive lab sequence

| Level | Lab | Evidence of learning |
|---|---|---|
| Beginner | Identify account security settings on own device | Explains MFA, updates, recovery, and least privilege. |
| Beginner | Draw a home network | Correctly identifies router, clients, DNS, and internet boundary. |
| Beginner | Read a sanitized sample log | Extracts timestamps, source, event, and uncertainty. |
| Beginner | Classify fictional threats and controls | Distinguishes threat, vulnerability, impact, and mitigation. |
| Intermediate | Parse supplied web server logs with a local script | Produces correct counts and explains assumptions. |
| Intermediate | Configure a deliberately local test environment | Documents isolation, scope, and cleanup. |
| Intermediate | Review a toy web application code sample | Identifies insecure patterns and proposes safer code. |
| Intermediate | Analyze a fictional phishing message | Cites observable indicators without interacting with links. |
| Advanced | Triage a simulated incident timeline | Builds a defensible timeline and prioritizes containment. |
| Advanced | Threat-model a fictional service | Maps assets, trust boundaries, threats, controls, and residual risk. |
| Advanced | Complete a defensive capstone | Produces findings, remediation plan, and verification evidence. |

## Suggested safe learning environments

The tutor should verify current access, terms, and lab instructions before recommending a platform. Prefer official documentation and purpose-built training:
- PortSwigger Web Security Academy for guided web security learning.
- OWASP WebGoat or Juice Shop when run locally in an isolated environment.
- picoCTF for educational challenges within its platform rules.
- CyberDefenders for blue-team and incident-analysis exercises, subject to current platform terms.
- Supplied synthetic logs and toy code for learners with limited devices or connectivity.

Do not require a powerful computer. Offer paper-based threat models, sample logs, browser-only theory, or small local scripts as alternatives.

## Project ladder

1. **Personal security checklist:** review updates, MFA, recovery options, password manager use, backups, and privacy settings.
2. **Home network map:** draw devices and trust boundaries; identify realistic risks and controls.
3. **Log investigation report:** analyze a provided dataset, state findings, separate facts from hypotheses, and recommend next steps.
4. **Secure web design review:** threat-model a fictional application and review a deliberately flawed code sample.
5. **Incident response tabletop:** respond to a fictional compromise with a timeline, decisions, communications, and recovery plan.
6. **Specialization capstone:** choose a blue-team, application-security, cloud-security, forensics, or GRC project with explicit scope and rubric.

## Project assessment rubric

Score each dimension from 0–4:
- Technical correctness.
- Quality of evidence and reasoning.
- Safety, scope, and ethical judgment.
- Practical usefulness of mitigations.
- Clarity and reproducibility of documentation.

A high score requires explaining uncertainty and limitations. Tool output without interpretation is not a successful project.
