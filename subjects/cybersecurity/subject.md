# Cybersecurity for complete beginners

## Audience and goal
For learners with no assumed technical background. The goal is to build safe foundations and choose a later specialization, not to rush into offensive tools.

## Learning outcomes
The learner should be able to explain basic computer and network concepts, distinguish threats from vulnerabilities and risks, apply core security practices, interpret simple logs, and practice only in authorized environments.

## Curriculum

### Stage 1 — Digital and computer foundations
Files, processes, operating systems, users, permissions, applications, browsers, command-line basics, updates, backups, and safe account practices.
Practice: explain what happens when an application opens a file; identify basic security settings on the learner's own device.

### Stage 2 — Networking foundations
IP and MAC addresses, DNS, ports, TCP and UDP, HTTP and HTTPS, routers, firewalls, TLS, and basic network diagrams.
Practice: draw a home network, inspect the learner's own device configuration, and explain a browser request.

### Stage 3 — Programming and scripting
Variables, conditions, loops, functions, data structures, Python, shell basics, HTTP, JSON, input validation, and safe secret handling.
Practice: parse a supplied sample log and write a simple local file-checking script.

### Stage 4 — Core security concepts
Confidentiality, integrity, availability; authentication and authorization; hashing, encryption and encoding; MFA; sessions; vulnerabilities, threats, risks, attack surface; patching, logging, backups; threat modeling.
Practice: threat-model a fictional small business and recommend proportionate controls.

### Stage 5 — Web and application security
Browser/server/database/API model; cookies and sessions; same-origin policy; CORS; TLS; OWASP Top 10 concepts; access-control failures; injection; misconfiguration; secure coding and remediation.
Practice: use intentionally vulnerable training labs such as PortSwigger Web Security Academy. Explain impact and remediation, not just tool output.

### Stage 6 — Defensive security
Logs, monitoring, alert triage, endpoint and network defenses, SIEM concepts, incident response, recovery, hardening, vulnerability management, and phishing defense.
Practice: analyze supplied sample logs, triage a fictional alert, and write an incident report.

### Stage 7 — Specialization
Possible directions: blue team/SOC, authorized penetration testing, cloud security, digital forensics, malware analysis in isolated labs, application security, governance/risk/compliance. Choose based on learner interest and demonstrated foundations.

## Teaching notes
- Start with concepts before tools.
- For every tool, explain its purpose, limitations, safe use, defender visibility, and remediation.
- Ask the learner to interpret results and explain what they mean.
- Use free resources first and recommend one primary resource at a time.
- Verify changing technical details with official documentation when browsing is available.

## Safety boundaries
Only use owned systems, explicitly authorized targets, or intentionally vulnerable labs. Do not teach unauthorized access, credential theft, stealth, persistence, malware deployment, evasion, or real-world exploitation. Redirect to defensive concepts, safe simulations, detection, remediation, and responsible disclosure.
