from __future__ import annotations

from pathlib import Path
import json
import re
from filelock import FileLock

BASE_DIR = Path(__file__).resolve().parent

CUSTOMER_DIR = BASE_DIR / "database" / "customer_data"
CUSTOMER_DIR.mkdir(parents=True, exist_ok=True)

EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

PHONE_PATTERN = re.compile(
    r"^\+?[0-9\s\-()]{7,20}$"
)


def _customer_path(session_id: str) -> Path:
    return CUSTOMER_DIR / f"{session_id}.json"


def _customer_lock(session_id: str) -> FileLock:
    # Same rationale as memory.py's session lock: guards a single
    # customer record's file against interleaved concurrent
    # read-modify-write cycles on one machine.
    return FileLock(str(CUSTOMER_DIR / f"{session_id}.json.lock"))


def _clean(value: str) -> str:
    return value.strip()


def load_customer(session_id: str):
    path = _customer_path(session_id)

    if not path.exists():
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_customer(session_id: str, customer: dict):
    path = _customer_path(session_id)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            customer,
            f,
            indent=4,
            ensure_ascii=False
        )


def customer_exists(session_id: str) -> bool:
    return _customer_path(session_id).exists()


def delete_customer(session_id: str):
    path = _customer_path(session_id)

    if path.exists():
        path.unlink()


def registration_complete(customer: dict) -> bool:
    return all([
        customer.get("name"),
        customer.get("email"),
        customer.get("company"),
        customer.get("phone"),
    ])


def is_registered(session_id: str) -> bool:
    customer = load_customer(session_id)

    if customer is None:
        return False

    return registration_complete(customer)


def validate_customer(customer: dict):
    if not customer["name"]:
        raise ValueError("Name is required")

    if not customer["company"]:
        raise ValueError("Company is required")

    if not EMAIL_PATTERN.fullmatch(customer["email"]):
        raise ValueError("Invalid email address")

    if not PHONE_PATTERN.fullmatch(customer["phone"]):
        raise ValueError("Invalid phone number")


def register_customer(
    session_id: str,
    *,
    name: str,
    email: str,
    company: str,
    phone: str
):

    with _customer_lock(session_id):
        customer = load_customer(session_id) or {}

        customer.update({
            "name": _clean(name),
            "email": _clean(email),
            "company": _clean(company),
            "phone": _clean(phone)
        })

        validate_customer(customer)

        save_customer(session_id, customer)

    return customer


# --------------------------------------------------
# Pending Question
# --------------------------------------------------

def save_pending_question(
    session_id: str,
    question: str
):
    with _customer_lock(session_id):
        customer = load_customer(session_id) or {}

        customer["pending_question"] = question

        save_customer(session_id, customer)


def load_pending_question(session_id: str) -> str | None:
    customer = load_customer(session_id)

    if customer is None:
        return None

    return customer.get("pending_question")


def clear_pending_question(session_id: str):
    with _customer_lock(session_id):
        customer = load_customer(session_id)

        if customer is None:
            return

        customer.pop("pending_question", None)

        save_customer(session_id, customer)