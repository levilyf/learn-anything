# JSON data standard

JSON is the portable machine-readable format for learning state and learning artifacts.

## Contracts

Use the JSON Schema files in `../schemas/` as the source of truth:

- `learner.schema.json`
- `curriculum.schema.json`
- `lesson.schema.json`
- `assessment.schema.json`

Do not duplicate schema definitions in prose or silently invent fields.

## Rules

- Use UTF-8.
- Use valid JSON: double-quoted keys and strings, no comments, and no trailing commas.
- Use stable identifiers for concepts, outcomes, lessons, and assessment tasks.
- Include `schema_version` where the relevant schema requires it.
- Represent dates and timestamps in ISO 8601 format with an explicit timezone when recording an instant.
- Use explicit `null` only when the schema permits it. Omit optional unknown fields otherwise.
- Keep learner-specific records separate from public subject content.
- Do not store passwords, API keys, authentication tokens, or unnecessary sensitive personal data.
- Preserve unknown extension fields only when the schema and consumer explicitly support them; otherwise reject or safely ignore them rather than guessing.

## Example

```json
{
  "schema_version": "1.0.0",
  "subject": "cybersecurity",
  "learner_id": "local-example",
  "mastery": [
    {
      "concept_id": "networking.ip-addresses",
      "state": "practicing"
    }
  ]
}
```

This is an illustrative fragment, not a complete learner record and not guaranteed to validate against the learner schema.

## Validation

Parse JSON before use and validate it against the matching JSON Schema when a schema validator is available. The repository's dependency-free checks currently verify JSON syntax and selected structural expectations; they are not a substitute for full JSON Schema validation.
