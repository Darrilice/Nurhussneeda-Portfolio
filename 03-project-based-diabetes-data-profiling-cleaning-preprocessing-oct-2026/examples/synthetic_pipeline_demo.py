"""Small, independent data-preparation demo using generated records only.

This is not the Rajavithi project code or a medical-data example.
Run with: python synthetic_pipeline_demo.py
"""

from datetime import date
from decimal import Decimal, InvalidOperation
import json


RAW_ROWS = [
    {"record_key": "demo-001", "submitted_on": "2026-10-01", "value": " 12.5 "},
    {"record_key": "demo-002", "submitted_on": "2026-10-02", "value": "8"},
    {"record_key": "demo-003", "submitted_on": "not-a-date", "value": "unknown"},
]

SYNTHETIC_LOOKUP = {
    "demo-001": {"source_group": "generated-a"},
    "demo-002": {"source_group": "generated-b"},
}


def clean(rows: list[dict[str, str]]) -> tuple[list[dict[str, object]], list[dict[str, str]]]:
    accepted: list[dict[str, object]] = []
    rejected: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["record_key"].strip()
        if key in seen:
            rejected.append({"record_key": key, "reason": "duplicate key"})
            continue
        seen.add(key)
        try:
            submitted_on = date.fromisoformat(row["submitted_on"].strip())
            value = Decimal(row["value"].strip())
        except (ValueError, InvalidOperation):
            rejected.append({"record_key": key, "reason": "invalid date or numeric value"})
            continue
        accepted.append({"record_key": key, "submitted_on": submitted_on.isoformat(), "value": str(value)})
    return accepted, rejected


def validate(rows: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for row in rows:
        if not row.get("record_key") or not row.get("submitted_on") or row.get("value") is None:
            issues.append("record missing a required value")
    return issues


def join_sources(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [{**row, **SYNTHETIC_LOOKUP.get(str(row["record_key"]), {})} for row in rows]


def preprocess(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [
        {**row, "submission_month": str(row["submitted_on"])[:7]}
        for row in rows
    ]


if __name__ == "__main__":
    cleaned, rejected = clean(RAW_ROWS)
    joined = join_sources(cleaned)
    prepared = preprocess(joined)
    summary = {
        "accepted_count": len(prepared),
        "rejected_count": len(rejected),
        "validation_issues": validate(prepared),
        "prepared_rows": prepared,
        "rejected_summary": rejected,
    }
    print(json.dumps(summary, indent=2))
