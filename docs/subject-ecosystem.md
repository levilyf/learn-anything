# Subject ecosystem blueprint

## Purpose

Learn Anything should become a broad library of coherent, high-quality learning paths. The catalogue describes the intended breadth; the modules provide the actual teaching material; the core skill provides a consistent adaptive teaching process.

The goal is not to publish the largest list of subjects. The goal is to help a learner move from a real starting point to demonstrated capability.

## Evidence-informed prioritization

Demand changes. Treat rankings as hypotheses to review, not permanent truth. Current signals include the World Economic Forum's Future of Jobs 2025 report, which identifies AI and big data, networks and cybersecurity, and technological literacy among the fastest-growing skills, alongside analytical and creative thinking ([WEF skills outlook](https://www.weforum.org/publications/the-future-of-jobs-report-2025/3-skills-outlook)). Coursera's 2026 reports point to strong growth in GenAI learning, critical thinking, AI agents, security, personalization, and applied technical skills ([Global Skills Report 2026](https://www.coursera.org/skills-reports/global), [Job Skills Report 2026](https://www.coursera.org/skills-reports/job-skills)).

These reports are useful signals, not a complete measure of what every learner needs. Platform enrollment data is not the same as job openings, local demand, educational importance, or learner outcomes.

### Demand score

Score each candidate from 1–5 on each dimension. Record the evidence, date, confidence, and reviewer. Use a weighted score to help compare candidates:

| Dimension | Weight | What to measure |
|---|---:|---|
| Learner demand | 25% | Direct requests, search interest, community questions, repeat demand. |
| Growth and relevance | 20% | Workforce, education, technology, and societal trend evidence. |
| Transferable usefulness | 20% | Value across careers, education, business, and everyday life. |
| Coverage gap | 15% | Whether accessible, coherent, adaptive learning paths are missing. |
| Feasibility and quality | 20% | Ability to create, validate, maintain, and safely teach the material. |

Formula: `score = sum((dimension_score / 5) * weight)`. Maximum = 100. Do not treat small score differences as meaningful. A safety or accuracy concern can block publication regardless of score.

### Review cadence

- Revisit the top priorities quarterly.
- Reassess sooner when a major technology, regulation, curriculum, or safety change affects a module.
- Track request volume and learner completion/retention separately from demonstrated learning outcomes.
- Preserve a short decision log when priorities change.

## Subject structure

Use this hierarchy:

`Subject → Domain → Skill area → Concept → Lesson → Practice → Assessment → Project`

A subject may contain multiple tracks. A track is a goal-oriented route through shared concepts, not a separate copy of the whole subject. Examples: AI for everyday work vs. AI application development; cybersecurity for personal safety vs. SOC analysis.

Each concept should declare prerequisites and learning outcomes. Model dependencies explicitly. Avoid both a single rigid path and an unordered topic dump.

## Module contract

Every subject module must include:

1. **Identity and scope:** stable ID, title, version, status, audience, scope, exclusions, maintenance/review date.
2. **Learner entry:** prerequisites, diagnostic questions, assumed knowledge, accessible entry points.
3. **Outcome map:** observable outcomes using explain, distinguish, apply, analyze, evaluate, or create.
4. **Curriculum graph:** stages, skill areas, concepts, prerequisite links, and optional branches.
5. **Teaching guidance:** explanations, worked examples, analogies, visual opportunities, misconceptions, and alternate explanations.
6. **Practice:** retrieval, guided practice, independent tasks, transfer tasks, and realistic projects.
7. **Assessment:** rubrics, answer guidance for the tutor, common errors, evidence requirements, and mastery criteria.
8. **Adaptation:** what to do when a learner is stuck, partly correct, advanced, disengaged, or returning after a gap.
9. **Resources:** authoritative, accessible, maintained resources with a clear purpose and date checked.
10. **Safety and inclusion:** legal/ethical/physical boundaries, privacy, accessibility, localization, and domain-specific risks.

A subject may add domain-specific files and formats. Do not force every discipline into identical exercises; a language conversation, a math proof, a business case, and a network lab require different evidence.

## Completeness levels

Use these levels honestly:

- **Listed:** appears in the catalogue only.
- **Outlined:** scope, outcomes, and a dependency-aware roadmap exist.
- **Authored:** core lessons, examples, practice, assessments, and adaptation notes exist.
- **Reviewed:** subject-matter and safety review completed; sources checked.
- **Validated:** test sessions with representative learners show that instructions, assessments, and adaptations work; known gaps are documented.

Do not mark a whole subject complete because its introductory stage exists. State coverage by skill area and level.

## Quality gates

A module cannot be called Validated until it passes all applicable gates:

- **Coverage:** foundations, intermediate applications, advanced branches, and explicit scope boundaries are mapped.
- **Prerequisites:** dependencies are sensible; diagnostic routes can skip known material without skipping essential foundations.
- **Teaching:** each core concept has an explanation, example, practice, misconception handling, and a check for understanding.
- **Assessment:** tasks measure the stated outcomes; answer keys/rubrics exist; independent performance is distinguished from assisted performance.
- **Transfer:** at least one task requires applying knowledge in a new context; projects are assessed against explicit criteria.
- **Adaptation:** the module specifies a response to common failure patterns and supports alternate explanations.
- **Safety and accuracy:** risks are reviewed; changing claims cite maintained sources; practical work has clear boundaries.
- **Accessibility:** language, pacing, device, connectivity, and visual alternatives are considered.
- **Maintenance:** version, reviewer, last-reviewed date, and known limitations are recorded.

## Personalization model

Personalize from evidence, not simplistic learner labels.

### Intake signals
- Goal: curiosity, school/exam, career, project, business, certification, or practical need.
- Starting point: self-report plus a short diagnostic.
- Constraints: available time, device, internet, language, budget, accessibility needs, and learning environment.
- Preference: examples, visuals, discussion, practice-first, theory-first, or mixed.
- Target: what the learner wants to be able to do and by when.

Ask only for details that materially change the route. Allow the learner to begin with incomplete intake and refine the plan as evidence appears.

### Adaptation signals
- Correctness and reasoning quality.
- Independence and hint usage.
- Ability to explain the idea in their own words.
- Performance on a different example or context.
- Error patterns and recurring misconceptions.
- Delayed recall and retention.
- Learner feedback about pace, relevance, and cognitive load.

### Adaptation actions
- Re-explain with a different model or analogy.
- Break a concept into smaller prerequisites.
- Add a worked example or visual.
- Reduce task difficulty, then rebuild it.
- Increase challenge when evidence is strong.
- Revisit prerequisites when errors point backward.
- Schedule retrieval practice after a delay.
- Offer a goal-specific branch without losing core prerequisites.

Never infer a fixed learning style from one preference answer. Preferences can guide presentation; observed performance guides instruction.

## Mastery and progress

Keep the existing mastery states: `not_started`, `introduced`, `practicing`, `proficient`, `mastered`.

- Lesson completion is not mastery.
- A correct answer after a full solution is not independent evidence.
- Use varied tasks: explanation, application, diagnosis, and transfer where appropriate.
- Record concept IDs, timestamps, task type, correctness, independence, hints, and evidence notes.
- Require delayed evidence for durable mastery where the domain allows it.
- Keep uncertainty visible. A tutor must be allowed to say that evidence is insufficient.

## First module portfolio

Build these deeply before broad expansion:

1. **AI and generative AI:** literacy, capabilities/limits, prompting, verification, privacy, responsible use, workflows, agents, and technical development branches.
2. **Programming and computer science:** computational thinking, programming foundations, debugging, data structures, algorithms, software design, testing, and projects.
3. **Mathematics:** diagnostic, arithmetic through algebra and geometry, functions, probability/statistics, and goal-specific advanced branches.
4. **Business and entrepreneurship:** customer discovery, value proposition, business models, pricing, marketing, sales, operations, bookkeeping, cash flow, and validation projects.
5. **English communication:** level-aware grammar, vocabulary, reading, listening, speaking, writing, pronunciation, and real-world communication.
6. **Cybersecurity:** strengthen the existing module into a comprehensive, safe, multi-track pathway.

Shared foundations should be reused rather than copied. For example, programming and mathematics support data science, AI development, and security engineering.

## Expansion sequence

### Phase 1 — Standards and map
Publish this blueprint, catalogue, module contract, and authoring template. Add validation for stable IDs and required metadata.

### Phase 2 — Strengthen the first portfolio
Upgrade cybersecurity and author one complete foundational path at a time. Run learner tests before starting several new modules in parallel.

### Phase 3 — Personalization and evaluation
Add diagnostic fixtures, misconception cases, delayed review examples, transfer tasks, and evaluation reports. Test across different goals and starting levels.

### Phase 4 — Community expansion
Accept proposals against the module contract. Require peer review and safety review for high-risk domains. Publish status and known gaps transparently.

### Phase 5 — Maintain and localize
Review sources and technical claims, support translations, improve accessibility, and retire or revise stale material.

## What not to build yet

Do not build a giant course dump, a custom LLM, a mandatory backend, a credential marketplace, social feeds, or a dashboard before the learning method works reliably. Optional platform features can come later, without making them prerequisites for learning.

## References

- [World Economic Forum — Future of Jobs Report 2025: Skills Outlook](https://www.weforum.org/publications/the-future-of-jobs-report-2025/3-skills-outlook)
- [Coursera — Global Skills Report 2026](https://www.coursera.org/skills-reports/global)
- [Coursera — Job Skills Report 2026](https://www.coursera.org/skills-reports/job-skills)
