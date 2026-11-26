# Cybersecurity skill map

This map defines coverage for the cybersecurity subject. It is a curriculum map, not a claim that every lesson or lab is already authored.

## Foundation layer

### Digital literacy and computer systems
- Hardware, CPU, memory, storage, operating systems, filesystems, processes, users, permissions.
- Browsers, applications, extensions, downloads, updates, backups.
- Command-line navigation and safe handling of files.
- Virtualization and isolated lab environments.

### Networking
- Network models and encapsulation.
- IPv4/IPv6, subnet concepts, MAC addresses, ARP, DHCP.
- DNS, routing, NAT, ports, TCP, UDP, ICMP.
- HTTP/HTTPS, TLS, certificates, proxies, VPN concepts.
- Firewalls, segmentation, wireless security, common network devices.
- Packet capture concepts and interpreting provided, sanitized captures.

### Programming and data
- Variables, types, conditions, loops, functions, collections, errors.
- Python fundamentals and shell literacy.
- Text formats, CSV, JSON, regular expressions, timestamps.
- HTTP requests and APIs at a conceptual level.
- Parsing logs, validation, safe file handling, secrets hygiene.
- Git basics and reproducible lab notes.

## Core security layer

### Security principles
- Confidentiality, integrity, availability.
- Identity, authentication, authorization, accounting.
- Least privilege, separation of duties, defense in depth, secure defaults.
- Threat, vulnerability, exploit, exposure, likelihood, impact, risk.
- Attack surface, trust boundaries, security controls.
- Risk acceptance, mitigation, transfer, and avoidance.

### Cryptography and identity
- Encoding vs. hashing vs. encryption.
- Symmetric and asymmetric encryption, key exchange, digital signatures.
- Hash functions, password hashing, salts, key derivation.
- Certificates, PKI, TLS trust model.
- Password managers, MFA, passkeys, recovery codes, session security.
- Key lifecycle, storage, rotation, and compromise response.

### Operating-system and endpoint security
- Users, groups, permissions, services, processes.
- Updates, patching, secure configuration, disk encryption.
- Endpoint protection concepts, application control, backups.
- Linux and Windows security models at a beginner-to-intermediate level.
- Mobile device security and privacy basics.

## Application and cloud layer

### Web and API security
- Browser, server, database, API, and identity flows.
- Cookies, sessions, tokens, same-origin policy, CORS, CSRF.
- Input handling, output encoding, parameterized queries.
- Authentication and authorization failures.
- Access control, injection, insecure design, misconfiguration, vulnerable components.
- File upload risks, SSRF concepts, logging, error handling, rate limiting.
- Secure SDLC, code review, dependency hygiene, threat modeling.
- OWASP Top 10 concepts and remediation-first labs.

### Cloud and infrastructure security
- Shared responsibility model and identity boundaries.
- IAM, roles, policies, secrets, storage permissions.
- Network segmentation, security groups, logging, encryption.
- Containers, images, registries, orchestration concepts.
- Infrastructure as code, configuration drift, supply-chain risks.
- Backup, recovery, resilience, and cost/security trade-offs.

## Defensive operations

### Security monitoring and response
- Log sources, event fields, timestamps, baselines.
- Alert triage, false positives, severity, escalation.
- Indicators of compromise vs. evidence limitations.
- SIEM/EDR concepts and detection logic.
- Incident response lifecycle: prepare, identify, contain, eradicate, recover, learn.
- Evidence preservation, chain of custody, reporting.
- Vulnerability management and remediation prioritization.
- Phishing analysis and user-centered awareness.

### Governance, risk, and privacy
- Asset inventory, policies, standards, procedures.
- Risk registers, control selection, audits, vendor risk.
- Data classification, minimization, retention, consent, privacy by design.
- Security awareness and organizational culture.
- Overview of common frameworks and regulatory concepts; verify jurisdiction-specific details with current official sources.

## Specialization branches

Learners choose a branch after demonstrating core foundations:

1. **Blue team / SOC:** monitoring, alert triage, detection engineering, incident response.
2. **Application security:** secure design, code review, threat modeling, web/API defense.
3. **Cloud security:** cloud IAM, network controls, workload and configuration security.
4. **Authorized security testing:** scope, rules of engagement, lab methodology, reporting, remediation validation. Practice only on owned systems, explicitly authorized targets, or intentionally vulnerable labs.
5. **Digital forensics:** acquisition concepts, integrity, timelines, artifacts, evidence handling, reporting.
6. **Malware analysis:** static/dynamic analysis concepts in isolated, intentionally prepared environments; focus on understanding and defense.
7. **GRC and privacy:** risk, controls, policies, audits, privacy, vendor assessment.
8. **Security engineering:** automation, secure infrastructure, detection pipelines, reliability, and secure architecture.

## Cross-cutting capabilities

- Analytical thinking and evidence-based conclusions.
- Clear technical writing and incident communication.
- Ethical judgment, legal scope, and responsible disclosure.
- Documentation, reproducibility, teamwork, and prioritization.
- Understanding tool limitations and avoiding overclaiming from scanner output.
