import unittest

from core.mastery import evaluate_mastery


def attempt(task, task_type="application", *, concept="networking.ip-addresses",
            support="none", result="correct", date="2026-01-01T10:00:00Z"):
    return {
        "schema_version": "1.0.0",
        "concept_id": concept,
        "task": task,
        "task_type": task_type,
        "result": result,
        "support_level": support,
        "response_evidence": "Learner response",
        "assessed_at": date,
    }


class MasteryPolicyTests(unittest.TestCase):
    def test_no_evidence_is_not_started(self):
        self.assertEqual(evaluate_mastery([])["state"], "not_started")

    def test_introduced_without_assessments(self):
        self.assertEqual(evaluate_mastery([], introduced=True)["state"], "introduced")

    def test_one_correct_attempt_is_not_proficient(self):
        result = evaluate_mastery([attempt("Explain an IP address", "explanation")])
        self.assertEqual(result["state"], "practicing")

    def test_supported_correct_attempt_does_not_count_as_independent(self):
        result = evaluate_mastery([
            attempt("Explain an IP address", "explanation", support="hint"),
            attempt("Identify a private IP", "application"),
        ])
        self.assertEqual(result["state"], "practicing")
        self.assertEqual(result["qualifying_tasks"], ["Identify a private IP"])

    def test_duplicate_prompt_does_not_count_twice(self):
        result = evaluate_mastery([
            attempt("Explain an IP address", "explanation"),
            attempt("  explain   an IP address  ", "application", date="2026-01-03T10:00:00Z"),
        ])
        self.assertEqual(result["state"], "practicing")

    def test_two_distinct_independent_task_types_reach_proficient(self):
        result = evaluate_mastery([
            attempt("Explain an IP address", "explanation"),
            attempt("Identify a private IP", "application", date="2026-01-02T10:00:00Z"),
        ])
        self.assertEqual(result["state"], "proficient")

    def test_mastered_requires_all_four_types_and_delayed_evidence(self):
        evidence = [
            attempt("Explain addressing", "explanation", date="2026-01-01T10:00:00Z"),
            attempt("Configure a sample address", "application", date="2026-01-03T10:00:00Z"),
            attempt("Diagnose a subnet mistake", "diagnosis", date="2026-01-06T10:00:00Z"),
            attempt("Transfer the idea to a new network", "transfer", date="2026-01-10T10:00:00Z"),
        ]
        self.assertEqual(evaluate_mastery(evidence)["state"], "mastered")

    def test_missing_delayed_evidence_caps_at_proficient(self):
        evidence = [
            attempt("Explain addressing", "explanation"),
            attempt("Configure a sample address", "application"),
            attempt("Diagnose a subnet mistake", "diagnosis"),
            attempt("Transfer the idea to a new network", "transfer"),
        ]
        self.assertEqual(evaluate_mastery(evidence)["state"], "proficient")

    def test_evidence_from_different_concepts_is_not_combined(self):
        evidence = [
            attempt("Explain an IP address", "explanation"),
            attempt("Identify a private IP", "application", concept="networking.private-addresses"),
        ]
        result = evaluate_mastery(evidence)
        self.assertEqual(result["state"], "practicing")
        self.assertIn("multiple concepts", result["reasons"][0])
        self.assertEqual(evaluate_mastery(evidence, concept_id="networking.ip-addresses")["state"], "practicing")

    def test_timezone_offsets_are_normalized(self):
        evidence = [
            attempt("Explain addressing", "explanation", date="2026-01-01T10:00:00+05:30"),
            attempt("Configure a sample address", "application", date="2026-01-03T04:30:00Z"),
            attempt("Diagnose a subnet mistake", "diagnosis", date="2026-01-06T10:00:00+05:30"),
            attempt("Transfer the idea to a new network", "transfer", date="2026-01-10T04:30:00Z"),
        ]
        self.assertEqual(evaluate_mastery(evidence)["state"], "mastered")

    def test_naive_timestamps_cannot_prove_delayed_mastery(self):
        evidence = [
            attempt("Explain addressing", "explanation", date="2026-01-01T10:00:00"),
            attempt("Configure a sample address", "application", date="2026-01-03T10:00:00"),
            attempt("Diagnose a subnet mistake", "diagnosis", date="2026-01-06T10:00:00"),
            attempt("Transfer the idea to a new network", "transfer", date="2026-01-10T10:00:00"),
        ]
        self.assertEqual(evaluate_mastery(evidence)["state"], "proficient")


if __name__ == "__main__":
    unittest.main()
