# Cybersecurity

## Module identity
- **Subject ID:** `cybersecurity`
- **Version:** 0.2.0
- **Status:** Expanded curriculum outline; lessons and labs are authored progressively.
- **Audience:** Complete beginners through learners preparing for a first specialization.
- **Prerequisites:** None for the foundation track. Basic computer literacy is helpful but not required.
- **Estimated effort:** Variable. Diagnose the learner and agree on a weekly time budget instead of promising a fixed completion date.
- **Primary goal:** Build accurate security mental models, practical defensive capability, safe technical foundations, and a route into a chosen specialization.

## Scope

Cybersecurity is the practice of reducing digital risk across people, devices, software, networks, data, and organizations. This module covers digital foundations, networking, programming literacy, security principles, application/cloud security, defensive operations, governance, and specialization choices.

It is not a shortcut to becoming a penetration tester. Tools are introduced only when the learner understands the system, the question being investigated, and the legal scope.

## Learning outcomes

A learner progressing through the core path should be able to:
1. Explain how computers, operating systems, networks, browsers, and web applications fit together.
2. Distinguish assets, threats, vulnerabilities, exploits, controls, likelihood, impact, and risk.
3. Apply practical personal and small-organization security controls.
4. Explain identity, access control, cryptography, sessions, and secure configuration.
5. Interpret simple sanitized logs and communicate evidence with uncertainty.
6. Identify common web/application security weaknesses in toy examples and recommend remediation.
7. Plan a safe, authorized lab and document its scope, results, and cleanup.
8. Select a specialization based on interest and demonstrated prerequisite knowledge.

## Entry diagnosis and personalization

Start by asking the learner's goal in plain language: personal safety, school, career exploration, SOC/blue team, application security, cloud security, authorized testing, forensics, or governance.

Use a short, low-pressure diagnostic covering:
- Computer and operating-system familiarity.
- Basic networking concepts.
- Any programming experience.
- Security concepts the learner already knows.
- Available device, connectivity, time, and budget.

Do not block learning if the learner cannot answer. Start at the first unknown prerequisite. Offer low-resource routes using diagrams, supplied sample data, browser-based material, and paper exercises. Do not assume the learner has a Linux machine or can run virtual machines.

## Curriculum architecture

The core route is prerequisite-aware, not strictly linear. A learner may skip a concept only when diagnostic and independent evidence support it.

### Phase 1 — Digital foundations
Hardware, CPU, memory, storage, operating systems, files, processes, users, permissions, applications, browsers, updates, backups, command-line basics, virtualization concepts.

**Milestone:** Explain what happens when a user opens a file or visits a website; identify basic security settings on their own device.

### Phase 2 — Networking foundations
Network models, IP/MAC addresses, subnet concepts, DNS, DHCP, routing, NAT, ports, TCP/UDP, HTTP/HTTPS, TLS, certificates, firewalls, wireless networks, VPN concepts.

**Milestone:** Draw a simple home network and explain a browser request from device to server.

### Phase 3 — Programming and data literacy
Computational thinking, variables, conditions, loops, functions, collections, Python basics, shell literacy, files, CSV/JSON, regular expressions, timestamps, HTTP concepts, APIs, Git, safe secret handling.

**Milestone:** Read and transform a supplied log dataset with a small script, explain the code, and handle input safely.

### Phase 4 — Core security principles
Confidentiality, integrity, availability; identity; authentication vs. authorization; least privilege; defense in depth; threat/vulnerability/exploit/risk; attack surface; trust boundaries; controls; risk treatment; security culture.

**Milestone:** Threat-model a fictional small business and justify controls in proportion to risk.

### Phase 5 — Identity, cryptography, and endpoint security
Password managers, MFA, passkeys, sessions, recovery, encoding vs. hashing vs. encryption, symmetric/asymmetric cryptography, signatures, certificates, key management, operating-system permissions, patching, disk encryption, backups, endpoint protection concepts.

**Milestone:** Explain why common security controls work, their limits, and how to recover safely from account compromise.

### Phase 6 — Web and application security
Browser/server/database/API architecture, cookies, sessions, tokens, same-origin policy, CORS, CSRF, access control, injection, input validation, output encoding, file handling, insecure design, misconfiguration, dependencies, logging, rate limits, secure SDLC, threat modeling, OWASP Top 10 concepts.

**Milestone:** Review a deliberately flawed toy application, identify risks, propose safer designs, and explain verification.

### Phase 7 — Defensive security operations
Asset inventory, hardening, vulnerability management, logs, monitoring, alert triage, SIEM/EDR concepts, detection logic, phishing analysis, incident response, evidence handling, recovery, post-incident learning.

**Milestone:** Analyze a sanitized dataset and fictional incident timeline, produce a concise report, separate facts from hypotheses, and recommend prioritized actions.

### Phase 8 — Cloud, infrastructure, and supply chain
Shared responsibility, IAM, secrets, storage permissions, network controls, containers, images, infrastructure as code, dependency risks, software supply chain, configuration drift, resilience, backup and recovery.

**Milestone:** Review a fictional cloud architecture and identify identity, data, network, and supply-chain risks.

### Phase 9 — Specialization selection
Choose one branch after core milestones. The branch must define its own prerequisites, safe lab scope, competencies, project, and assessment rubric.

## Specialization tracks

- **Blue team / SOC:** alert triage, log analysis, detection, incident response, endpoint/network defense.
- **Application security:** secure design, code review, threat modeling, web/API defense, remediation verification.
- **Cloud security:** cloud IAM, workload protection, configuration, secrets, network boundaries, monitoring.
- **Authorized security testing:** scoping, rules of engagement, controlled lab methodology, validation, reporting, remediation. Never test a real target without explicit authorization.
- **Digital forensics:** evidence integrity, acquisition concepts, timelines, artifacts, analysis limitations, reporting.
- **Malware analysis:** static/dynamic analysis concepts in isolated, intentionally prepared environments, with defensive emphasis.
- **GRC and privacy:** risk registers, controls, policies, audits, vendor risk, privacy by design, regulatory awareness.
- **Security engineering:** secure infrastructure, automation, architecture, detection pipelines, reliability.

## Teaching method

- Explain the system before introducing a tool.
- Teach one coherent concept at a time, then give a task that requires reasoning.
- Use network maps, request-flow diagrams, annotated logs, attack-surface maps, and incident timelines when they clarify the concept.
- For each tool, state its purpose, prerequisites, safe scope, limitations, expected output, and defensive relevance.
- Never equate tool output with truth. Ask what evidence supports a conclusion and what remains unknown.
- Prefer free, maintained resources. Recommend one primary resource at a time and explain exactly what to study.
- Verify changing technical claims against official documentation or authoritative project guidance when browsing is available.

## Assessment and mastery

Use `assessment-guide.md` and the shared project mastery rules. Assess explanation, application, diagnosis, transfer, and practical artifacts. Require independent evidence across multiple task types; use delayed retrieval for durable mastery. Keep mastery attached to individual concept IDs. A completed lab or quiz does not prove subject mastery.

## Labs and projects

Use `labs-and-projects.md`. Start with the learner's own device settings, diagrams, supplied synthetic logs, toy code, and fictional scenarios. Progress to intentionally vulnerable local labs only when the learner can explain isolation and scope.

Suggested capstones:
- Personal security improvement plan.
- Home network diagram and risk review.
- Log investigation report.
- Secure design review of a toy web service.
- Incident response tabletop.
- Specialization project with a documented scope and rubric.

## Accessibility and constraints

Offer a path for:
- Phone-only learners.
- Low bandwidth or intermittent internet.
- No administrator/root access.
- Limited storage or compute.
- Learners who need extra practice with English technical vocabulary.
- Learners who benefit from diagrams, analogies, short tasks, or worked examples.

Do not require paid certifications, paid labs, or expensive hardware for core outcomes.

## Safety and legal boundaries

Only use owned systems, explicitly authorized targets, or intentionally vulnerable training labs. Before practical work, define the target, permission, scope, allowed actions, prohibited actions, isolation, and cleanup.

Do not teach unauthorized access, credential theft, stealth, persistence, malware deployment, evasion, or real-world exploitation. Do not direct learners to test public systems. Redirect unsafe requests to defensive concepts, synthetic scenarios, detection, remediation, secure design, and responsible disclosure. Never ask learners to paste passwords, private keys, tokens, personal records, or sensitive logs into chat.

## Maintenance

Review technical references and platform availability at least every six months, and sooner when major changes affect safety or correctness. Record the date checked, version, reviewer, known gaps, and source links in future lesson/resource records.

## Related material

- [Full skill map](skills-map.md)
- [Beginner-to-specialist roadmap](roadmap.md)
- [Safe labs and projects](labs-and-projects.md)
- [Assessment guide](assessment-guide.md)
- [Subject ecosystem quality standard](../../docs/subject-ecosystem.md)
