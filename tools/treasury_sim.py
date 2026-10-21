"""Deterministic, offline prototype for the RFC-0014 treasury rehearsal.

This is not the Alkaest Brain, a Bitcoin wallet, or production treasury code.
It accepts already-classified synthetic inputs and models policy gates only.
"""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from typing import Any


MAX_BITCOIN_SATS = 21_000_000 * 100_000_000

_LEDGER_FIELDS = (
    "verified_settled_inflows_sats",
    "settled_outflows_sats",
    "outstanding_escrow_sats",
    "reserved_allocations_sats",
    "authorized_pending_payouts_sats",
    "committed_network_fees_sats",
    "protected_reserve_sats",
)


def _sats(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{field} must be an integer number of satoshis")
    if value < 0 or value > MAX_BITCOIN_SATS:
        raise ValueError(f"{field} is outside the supported satoshi range")
    return value


def _finite_unit_interval(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number from 0 to 1")
    number = float(value)
    if not math.isfinite(number) or not 0 <= number <= 1:
        raise ValueError(f"{field} must be a finite number from 0 to 1")
    return number


def spendable_sats(ledger: Mapping[str, Any]) -> int:
    """Return spendable BTC from one complete synthetic ledger snapshot.

    Unconfirmed inflows are deliberately ignored. A real implementation must
    validate the referenced events and finality through RFC-0008 first.
    """
    if not isinstance(ledger, Mapping):
        raise ValueError("ledger must be a mapping")
    if ledger.get("complete") is not True or not ledger.get("event_head"):
        raise ValueError("ledger snapshot is incomplete or has no event head")

    values = {field: _sats(ledger.get(field), field) for field in _LEDGER_FIELDS}
    deductions = sum(values[field] for field in _LEDGER_FIELDS[1:])
    if deductions > MAX_BITCOIN_SATS:
        raise ValueError("ledger deductions exceed the supported BTC range")
    # A negative result is an inconsistent ledger, not a zero-balance snapshot.
    remaining = values["verified_settled_inflows_sats"] - deductions
    if remaining < 0:
        raise ValueError("ledger obligations exceed verified settled inflows")
    return remaining


def decide_work_items(
    policy: Mapping[str, Any],
    ledger: Mapping[str, Any],
    candidates: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Rank fixture candidates and apply deterministic funding gates.

    Priority is an already-authorized input from the fixture's signed policy;
    this function neither infers priority from complaints nor invokes a model.
    Quotes are all-in amounts, including the fixture's expected fees.
    """
    if not isinstance(policy, Mapping) or not isinstance(candidates, Sequence):
        raise ValueError("policy and candidates have invalid types")
    max_task = _sats(policy.get("max_task_sats"), "max_task_sats")
    period_left = _sats(policy.get("period_remaining_sats"), "period_remaining_sats")
    min_confidence = _finite_unit_interval(
        policy.get("minimum_confidence"), "minimum_confidence"
    )
    min_quotes = policy.get("minimum_quote_count")
    if isinstance(min_quotes, bool) or not isinstance(min_quotes, int) or min_quotes < 1:
        raise ValueError("minimum_quote_count must be a positive integer")

    balance = spendable_sats(ledger)
    normalized: list[tuple[float, str, Mapping[str, Any]]] = []
    seen: set[str] = set()
    for candidate in candidates:
        if not isinstance(candidate, Mapping):
            raise ValueError("each candidate must be a mapping")
        candidate_id = candidate.get("id")
        if not isinstance(candidate_id, str) or not candidate_id:
            raise ValueError("candidate id must be a non-empty string")
        if candidate_id in seen:
            raise ValueError(f"duplicate candidate id: {candidate_id}")
        seen.add(candidate_id)
        priority = _finite_unit_interval(candidate.get("seeded_priority"), "seeded_priority")
        confidence = _finite_unit_interval(candidate.get("confidence"), "confidence")
        amount = _sats(candidate.get("quote_sats"), "quote_sats")
        quote_count = candidate.get("quote_count")
        if isinstance(quote_count, bool) or not isinstance(quote_count, int) or quote_count < 0:
            raise ValueError("quote_count must be a non-negative integer")
        normalized.append((priority, candidate_id, {**candidate, "confidence": confidence,
                                                    "quote_sats": amount,
                                                    "quote_count": quote_count}))

    normalized.sort(key=lambda item: (-item[0], item[1]))
    decisions: list[dict[str, Any]] = []
    for _, candidate_id, candidate in normalized:
        amount = candidate["quote_sats"]
        confidence = candidate["confidence"]
        quote_count = candidate["quote_count"]
        action = "fund"
        if quote_count < min_quotes:
            action = "defer_insufficient_pricing_evidence"
        elif confidence < min_confidence:
            action = "defer_low_confidence"
        elif amount > max_task:
            action = "defer_task_cap"
        elif amount > period_left:
            action = "defer_period_cap"
        elif amount > balance:
            action = "defer_insufficient_funds"

        if action == "fund":
            balance -= amount
            period_left -= amount
        decisions.append({
            "id": candidate_id,
            "action": action,
            "amount_sats": amount,
            "spendable_after_sats": balance,
            "period_remaining_after_sats": period_left,
            "ledger_event_head": ledger["event_head"],
        })
    return decisions
