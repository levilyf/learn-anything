import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProjectStructureTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md", "LICENSE", "skills/learn-anything/SKILL.md",
            "subjects/cybersecurity/subject.md", "subjects/_template/subject.md",
            "schemas/learner.schema.json", "schemas/curriculum.schema.json",
            "schemas/lesson.schema.json", "schemas/assessment.schema.json",
        ]
        for relative in required:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_skill_has_required_frontmatter(self):
        content = (ROOT / "skills/learn-anything/SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\n"))
        self.assertIn("name: learn-anything", content)
        self.assertIn("description:", content)

    def test_json_schemas_are_valid_json(self):
        for path in (ROOT / "schemas").glob("*.schema.json"):
            with self.subTest(path=path.name):
                schema = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(schema.get("type"), "object")
                self.assertIn("$schema", schema)
                self.assertIn("properties", schema)

    def test_example_learner_is_valid_json_and_versioned(self):
        example = json.loads((ROOT / "examples/learner-cybersecurity.json").read_text(encoding="utf-8"))
        self.assertEqual(example["schema_version"], "1.0.0")
        self.assertEqual(example["subject"], "cybersecurity")
        self.assertIsInstance(example["mastery"], list)

    def test_cybersecurity_module_has_safety_boundary(self):
        content = (ROOT / "subjects/cybersecurity/subject.md").read_text(encoding="utf-8")
        self.assertIn("Safety boundaries", content)
        self.assertIn("authorized", content.lower())


if __name__ == "__main__":
    unittest.main()
