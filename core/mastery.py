"""Reference mastery policy for Learn Anything.

This module is deliberately small and deterministic. It evaluates recorded
assessment evidence; it does not claim to measure intelligence or guarantee
learning. Subject modules may impose stricter requirements.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Iterable

STATES = ("not_started", "introduced", "practicing", "proficient", "mastered")
INDEPENDENT_SUPPORT = {"none"}
MASTERED_TASK_TYPES = {"explanation", "application", "diagnosis", "transfer"}


def _parse_date(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def evaluate_mastery(
    assessments: Iterable[dict[str, Any]],
    *,
    introduced: bool = False,
) -> dict[str, Any]:
    """Return a conservative mastery state and an auditable explanation.

    Proficient: two distinct correct tasks, independently completed, across
    at least two task types.

    Mastered: four distinct independent correct tasks covering explanation,
    application, diagnosis and transfer, with valid timestamps spanning at
    least seven days.

    Hints, guided work, worked examples, retries after a worked solution,
    repeated task wording, and confidence are not independent evidence.
    """
    records = list(assessments)
    if not records:
        state = "introduced" if introduced else "not_started"
        return {"state": state, "qualifying_tasks": [], "reasons": ["No assessment evidence recorded."]}

    independent = [
        item for item in records
        if item.get("result") == "correct"
        and item.get("support_level") in INDEPENDENT_SUPPORT
        and isinstance(item.get("task"), str)
        and item["task"].strip()
        and item.get("task_type") in {"recall", "explanation", "application", "diagnosis", "transfer"}
    ]

    # Count each task description once; retain the first record to avoid
    # turning repeated attempts at the same prompt into separate evidence.
    unique: dict[str, dict[str, Any]] = {}
    for item in independent:
        key = " ".join(item["task"].lower().split())
        unique.setdefault(key, item)

    qualifying = list(unique.values())
    types = {item["task_type"] for item in qualifying}
    dates = [_parse_date(item.get("assessed_at")) for item in qualifying]
    valid_dates = [date for date in dates if date is not None]

    if (
        len(qualifying) >= 4
        and MASTERED_TASK_TYPES.issubset(types)
        and len(valid_dates) >= 4
        and (max(valid_dates) - min(valid_dates)).days >= 7
    ):
        return {
            "state": "mastered",
            "qualifying_tasks": [item["task"] for item in qualifying],
            "reasons": ["Four distinct independent task types are demonstrated, including transfer, across at least seven days."],
        }

    if len(qualifying) >= 2 and len(types) >= 2:
        return {
            "state": "proficient",
            "qualifying_tasks": [item["task"] for item in qualifying],
            "reasons": ["At least two distinct tasks across two task types were completed correctly without support."],
        }

    if records:
        reasons = ["Evidence is insufficient for independent proficiency."]
        if any(item.get("support_level") != "none" for item in records):
            reasons.append("Supported attempts do not count as independent demonstrations.")
        if len(qualifying) < 2:
            reasons.append("Need at least two distinct independent correct tasks.")
        elif len(types) < 2:
            reasons.append("Need evidence from at least two different task types.")
        return {
            "state": "practicing" if qualifying or any(item.get("result") in {"partial", "correct"} for item in records) else ("introduced" if introduced else "practicing"),
            "qualifying_tasks": [item["task"] for item in qualifying],
            "reasons": reasons,
        }

    return {"state": "introduced" if introduced else "practicing", "qualifying_tasks": [], "reasons": ["No qualifying independent correct attempts."]}
