import unittest

from tools.treasury_sim import decide_work_items, spendable_sats


def policy_fixture():
    return {
        "max_task_sats": 13_000_000,
        "period_remaining_sats": 25_000_000,
        "minimum_confidence": 0.80,
        "minimum_quote_count": 1,
    }


def ledger_fixture():
    return {
        "event_head": "sim:000042",
        "complete": True,
        "verified_settled_inflows_sats": 50_000_000,
        "settled_outflows_sats": 0,
        "outstanding_escrow_sats": 8_000_000,
        "reserved_allocations_sats": 0,
        "authorized_pending_payouts_sats": 2_000_000,
        "committed_network_fees_sats": 1_000_000,
        "protected_reserve_sats": 20_000_000,
        "unconfirmed_inflows_sats": 10_000_000,
    }


def candidates_fixture():
    return [
        {
            "id": "brand-identity",
            "seeded_priority": 0.90,
            "confidence": 0.90,
            "quote_sats": 12_000_000,
            "quote_count": 1,
        },
        {
            "id": "flutter-design-system",
            "seeded_priority": 0.70,
            "confidence": 0.88,
            "quote_sats": 8_000_000,
            "quote_count": 1,
        },
    ]


class TreasurySimulationTests(unittest.TestCase):
    def test_spendable_balance_uses_settled_ledger_and_protects_reserve(self):
        self.assertEqual(spendable_sats(ledger_fixture()), 19_000_000)

    def test_incomplete_or_stale_snapshot_fails_closed(self):
        ledger = ledger_fixture()
        ledger["complete"] = False
        with self.assertRaises(ValueError):
            spendable_sats(ledger)

    def test_unconfirmed_deposit_never_changes_spendable_balance(self):
        ledger = ledger_fixture()
        before = spendable_sats(ledger)
        ledger["unconfirmed_inflows_sats"] = 900_000_000
        self.assertEqual(spendable_sats(ledger), before)

    def test_brain_fixture_funds_first_candidate_and_defers_second(self):
        decisions = decide_work_items(policy_fixture(), ledger_fixture(), candidates_fixture())
        self.assertEqual(
            [(decision["id"], decision["action"]) for decision in decisions],
            [("brand-identity", "fund"), ("flutter-design-system", "defer_insufficient_funds")],
        )
        self.assertEqual(decisions[0]["amount_sats"], 12_000_000)
        self.assertEqual(decisions[1]["spendable_after_sats"], 7_000_000)

    def test_unsupported_price_and_low_confidence_are_deferred(self):
        candidates = candidates_fixture()[:1]
        candidates[0]["quote_count"] = 0
        decisions = decide_work_items(policy_fixture(), ledger_fixture(), candidates)
        self.assertEqual(decisions[0]["action"], "defer_insufficient_pricing_evidence")

        candidates[0]["quote_count"] = 1
        candidates[0]["confidence"] = 0.2
        decisions = decide_work_items(policy_fixture(), ledger_fixture(), candidates)
        self.assertEqual(decisions[0]["action"], "defer_low_confidence")

    def test_duplicate_ids_and_invalid_amounts_are_rejected(self):
        candidates = candidates_fixture()
        candidates.append(dict(candidates[0]))
        with self.assertRaises(ValueError):
            decide_work_items(policy_fixture(), ledger_fixture(), candidates)

        candidates = candidates_fixture()[:1]
        candidates[0]["quote_sats"] = -1
        with self.assertRaises(ValueError):
            decide_work_items(policy_fixture(), ledger_fixture(), candidates)


if __name__ == "__main__":
    unittest.main()
