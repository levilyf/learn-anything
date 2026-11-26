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


class VisualLearningTests(unittest.TestCase):
    def read(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_visual_component_catalogue_and_guides_exist(self):
        for relative in (
            "visual/README.md",
            "visual/components/concept-map.md",
            "visual/components/flow-diagram.md",
            "visual/components/annotated-diagram.md",
            "visual/components/learning-roadmap.md",
            "visual/components/simulation.md",
            "visual/components/revision-card.md",
        ):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_visual_schema_is_valid_json_and_has_component_types(self):
        import json
        schema = json.loads(self.read("visual/schemas/visual-component.schema.json"))
        self.assertEqual(schema["type"], "object")
        self.assertIn("simulation", schema["properties"]["type"]["enum"])
        self.assertIn("concept_map", schema["properties"]["type"]["enum"])

    def test_visual_examples_have_text_fallbacks(self):
        concept = self.read("visual/examples/cybersecurity-concept-map.md")
        process = self.read("visual/examples/website-request-flow.md")
        simulation = self.read("visual/examples/network-simulation.json")
        self.assertIn("Text fallback", concept)
        self.assertIn("Text fallback", process)
        self.assertIn('"fallback"', simulation)
        self.assertIn('"connects_to_real_targets": false', simulation)

    def test_skill_teaches_visual_component_usage(self):
        skill = self.read("skills/learn-anything/SKILL.md")
        self.assertIn("Visual learning components", skill)
        self.assertIn("visual-component.schema.json", skill)
        self.assertIn("text fallback", skill)
