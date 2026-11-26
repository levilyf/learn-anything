import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class FormatContractTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_all_format_guides_exist(self):
        for relative in (
            "formats/README.md",
            "formats/markdown.md",
            "formats/mermaid.md",
            "formats/json.md",
            "formats/rendering-contract.md",
            "formats/lesson-template.md",
        ):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_rendering_contract_defines_fallbacks(self):
        content = self.read("formats/rendering-contract.md")
        self.assertIn("Mermaid", content)
        self.assertIn("ASCII", content)
        self.assertIn("textual explanation", content)
        self.assertIn("Never claim", content)

    def test_lesson_template_separates_practice_and_assessment(self):
        content = self.read("formats/lesson-template.md")
        self.assertIn("Your turn", content)
        self.assertIn("Knowledge check", content)
        self.assertIn("Evaluation criteria", content)

    def test_skill_references_format_standards(self):
        content = self.read("skills/learn-anything/SKILL.md")
        self.assertIn("Content and rendering formats", content)
        self.assertIn("rendering-contract.md", content)
        self.assertIn("lesson-template.md", content)

    def test_readme_documents_content_data_presentation_split(self):
        content = self.read("README.md")
        self.assertIn("Content and presentation", content)
        self.assertIn("Mermaid", content)
        self.assertIn("JSON", content)


if __name__ == "__main__":
    unittest.main()
