"""Reference mastery policy for Learn Anything.

This evaluator is deliberately conservative and deterministic. It evaluates
one concept at a time; it does not claim to measure intelligence or guarantee
learning. Subject modules may impose stricter requirements.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

INDEPENDENT_SUPPORT = {"none"}
VALID_TASK_TYPES = {"recall", "explanation", "application", "diagnosis", "transfer"}
MASTERED_TASK_TYPES = {"explanation", "application", "diagnosis", "transfer"}


def _parse_date(value: Any) -> datetime | None:
    """Parse an ISO-8601 instant and normalize it to UTC.

    Naive timestamps are rejected because their timezone cannot be inferred.
    """
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


def evaluate_mastery(
    assessments: Iterable[dict[str, Any]],
    *,
    introduced: bool = False,
    concept_id: str | None = None,
) -> dict[str, Any]:
    """Evaluate evidence for exactly one concept.

    Proficient: two distinct correct tasks, independently completed, across
    at least two task types.

    Mastered: four distinct independent correct tasks covering explanation,
    application, diagnosis and transfer, with timezone-aware timestamps
    spanning at least seven days.

    If records contain multiple concepts, callers must specify concept_id.
    This prevents evidence for unrelated concepts from being combined.
    """
    records = list(assessments)
    concept_ids = {item.get("concept_id") for item in records if item.get("concept_id")}

    if concept_id is None and len(concept_ids) > 1:
        return {
            "state": "practicing" if records else ("introduced" if introduced else "not_started"),
            "qualifying_tasks": [],
            "reasons": ["Evidence contains multiple concepts; evaluate each concept separately by passing concept_id."],
        }

    target = concept_id or (next(iter(concept_ids)) if concept_ids else None)
    if target is not None:
        records = [item for item in records if item.get("concept_id") == target]

    if not records:
        state = "introduced" if introduced else "not_started"
        return {"state": state, "qualifying_tasks": [], "reasons": ["No assessment evidence recorded for this concept."]}

    independent = [
        item for item in records
        if item.get("result") == "correct"
        and item.get("support_level") in INDEPENDENT_SUPPORT
        and isinstance(item.get("task"), str)
        and item["task"].strip()
        and item.get("task_type") in VALID_TASK_TYPES
    ]

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

    reasons = ["Evidence is insufficient for independent proficiency."]
    if any(item.get("support_level") != "none" for item in records):
        reasons.append("Supported attempts do not count as independent demonstrations.")
    if len(qualifying) < 2:
        reasons.append("Need at least two distinct independent correct tasks.")
    elif len(types) < 2:
        reasons.append("Need evidence from at least two different task types.")

    has_attempt = any(item.get("result") in {"partial", "correct"} for item in records)
    state = "practicing" if qualifying or has_attempt else ("introduced" if introduced else "practicing")
    return {
        "state": state,
        "qualifying_tasks": [item["task"] for item in qualifying],
        "reasons": reasons,
    }
