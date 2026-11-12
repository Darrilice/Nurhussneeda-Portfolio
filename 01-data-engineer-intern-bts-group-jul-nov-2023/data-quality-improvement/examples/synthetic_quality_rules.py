"""Independent portfolio demonstration using synthetic values only.

This is not the submitted BTS implementation or an organization rulebook.
Run with: python synthetic_quality_rules.py
"""

from decimal import Decimal, InvalidOperation
import re


LABELS = {
    "education": {
        "bachelor degree": "bachelor",
        "bachelor's degree": "bachelor",
        "bachelors": "bachelor",
    },
    "gender": {"f": "female", "female": "female", "m": "male", "male": "male"},
    "marital_status": {"single": "single", "married": "married"},
    "occupation": {"software engineer": "engineer", "engineer": "engineer"},
}

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def normalize_label(value: object, category: str) -> str | None:
    """Normalize a synthetic categorical value; preserve unknown values."""
    if value is None:
        return None
    normalized = " ".join(str(value).strip().casefold().split())
    return LABELS.get(category, {}).get(normalized, normalized)


def email_has_basic_shape(value: object) -> bool:
    """Check format only; this does not verify mailbox existence or ownership."""
    return isinstance(value, str) and bool(EMAIL_PATTERN.fullmatch(value.strip()))


def parse_income_number(value: object) -> Decimal | None:
    """Parse a simple synthetic numeric value; ambiguous ranges need review."""
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    try:
        amount = Decimal(text)
    except InvalidOperation:
        return None
    return amount if amount >= 0 else None


if __name__ == "__main__":
    demo = {
        "education": normalize_label(" Bachelor's Degree ", "education"),
        "gender": normalize_label("F", "gender"),
        "income": str(parse_income_number("52,000")),
        "marital_status": normalize_label("SINGLE", "marital_status"),
        "occupation": normalize_label("Software Engineer", "occupation"),
        "email_format_ok": email_has_basic_shape("portfolio.user@example.com"),
    }
    for category, result in demo.items():
        print(f"{category}: {result}")
