# Markdown authoring standard

Markdown is the default format for human-readable Learn Anything content.

## Rules

- Use clear headings with a logical hierarchy. Start with one H1 per document.
- Prefer short paragraphs, meaningful lists, and tables only when they improve comparison.
- Explain a concept before introducing dense terminology. Define new terms on first use.
- Use fenced code blocks with a language identifier for code.
- Use inline code for identifiers, commands, paths, and literal values.
- Keep one main learning objective per lesson.
- Separate explanation, worked example, learner practice, and assessment.
- Use links with descriptive labels. Do not rely on color, emoji, or visual position to convey meaning.
- Keep content readable in plain-text environments.
- Never make an essential instruction available only through an image or diagram.

## Canonical lesson structure

Use [lesson-template.md](lesson-template.md) for new lessons. The usual sequence is:

1. Objective and relevance.
2. Prerequisites.
3. Explanation and key terms.
4. Worked example.
5. Diagram, when it adds clarity.
6. Independent practice.
7. Knowledge check and feedback criteria.
8. Next step and review trigger.

Not every lesson needs every optional section. Do not pad a lesson to satisfy a template.

## Accessibility and clarity

- Use descriptive link text.
- Provide a text explanation for every meaningful diagram.
- Avoid giant paragraphs and unexplained abbreviations.
- Keep examples culturally and contextually understandable; explain domain-specific assumptions.
- Prefer concrete language over motivational filler.

## Frontmatter

Agent Skills files may use YAML frontmatter as required by the Agent Skills format. Ordinary lesson Markdown should not invent custom frontmatter fields. Store machine-readable lesson metadata in the corresponding JSON representation when one is needed.
