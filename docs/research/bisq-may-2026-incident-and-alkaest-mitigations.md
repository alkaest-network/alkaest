# Research: Bisq May 2026 Incident and Alkaest Mitigations

**Status:** Architecture security review input  
**Date:** 2026-10-19  
**Related:** ADR-0003, ADR-0004, ADR-0007, RFC-0001, RFC-0003, RFC-0004, RFC-0005, RFC-0008, RFC-0014

## Confirmed incident

On May 1, 2026, Bisq v1 suffered an exploit in its trade protocol. Bisq's May 16 post-mortem reports 10 affected users and 11.59104 BTC in losses. Bisq 2, fiat trades, and BTC simply held in wallets were not affected. The attacker used a modified client against active altcoin trades.

The root cause was an insufficiently validated trade-protocol field: the taker supplied a miner-fee value to the maker, and the receiving path did not reject negative values. That invalid number caused the maker to calculate an incorrect multisig output amount. The incident was contained by enforcing a mandatory application version that did not exist, effectively halting new trading while investigation and repair proceeded.

Bisq expanded the response beyond a narrow patch to inspect trade messages, deposit/payout transactions, contract consistency, peer wallet data, DAO/P2P components, dependencies, and the build process. Its 1.10.0 release notes report additional validation, dependency signature checks, toolchain verification, updated dependencies, and Docker-based DAO/end-to-end testing. The post-mortem also describes reducing exposure with lower trade limits and disabling a higher-risk auto-confirmation path pending audit. A later update reports affected users were reimbursed.

This is a protocol-validation and economic-state integrity failure, not a wallet-key theft. The public post-mortem does not disclose every exploit implementation detail; this document relies only on its confirmed summary and published release notes.

Primary sources:

- [Bisq Security Incident Post-Mortem](https://bisq.network/blog/security-incident-post-mortem/)
- [Bisq 1 release notes and security fixes](https://github.com/bisq-network/bisq/releases)
- [Bisq update after the incident](https://bisq.network/blog/where-bisq-stands-after-security-incident/)

## What transfers to Alkaest

Alkaest is not Bisq's trading protocol, so the exact exploit does not transfer. The structural pattern does:

1. A peer-controlled value crosses a protocol boundary.
2. The receiving implementation assumes it is valid.
3. Arithmetic/state derivation uses the value before checking its bounds and relationship to other fields.
4. The bad derived state becomes a payment or authority decision.

Alkaest has comparable trust boundaries in WorkItem budgets, Bitcoin fee/amount metadata, escrow references, contributor-submitted evidence, GitHub/CI adapter attestations, token issuance proposals, voting payloads, and AI-generated decisions. Signatures prove who signed a message; they do not prove that its values are safe or semantically valid.

## Required Alkaest mitigations

### Deterministic validation before state mutation

- Treat every peer, adapter, contributor, model, and external-provider payload as adversarial, including messages signed by valid identities.
- Validate canonical encoding, schema/version, integer ranges, units, required fields, authority, state-transition preconditions, and cross-field invariants before mutating durable state.
- Use bounded integer arithmetic for money and counts; reject negative values, overflow, underflow, unsupported precision, and values outside the frozen WorkItem/policy bounds. Never use floating point for settlement calculations.
- Recompute derived amounts from the frozen protocol terms and locally verified settlement data. Do not trust a peer's claimed fee, balance, output value, approval result, or transaction role.
- Verify actual transaction inputs, outputs, fees, destinations, and escrow state against the signed agreement before accepting a settlement event. Invalid or ambiguous data fails closed and leaves funds/state unchanged.
- Make state application atomic: validation either succeeds completely and commits the event, or has no effect. Persist enough evidence to replay and independently audit the decision.

### Independent evidence and implementation diversity

- Bind approvals, CI results, artifact hashes, and payout decisions to the exact immutable WorkItem revision and policy version.
- Require every verifier to independently derive critical monetary and authorization facts rather than forwarding a peer's conclusion.
- For high-risk payment code, use a second implementation or independent review of the amount/transaction validator; include differential tests against the protocol specification.
- Use property-based, fuzz, boundary, malformed-message, regression, and end-to-end tests for every transition that can reserve, release, mint, or redirect value. Maintain a local reproducer for each security fix.
- Security review must include malicious modified clients and correctly signed but semantically invalid messages; a signature-valid happy-path test is insufficient.

### Bound blast radius and contain incidents

- Cap per-WorkItem, per-period, per-contributor, per-project, and newly introduced token issuance exposure. Caps are defense in depth, not a substitute for validation.
- Keep task escrow, treasury reserve, agent allowance, policy keys, and guardian keys separated. Contributor code and CI jobs never receive funds or signing keys.
- Provide a signed, threshold-controlled pause mechanism for new allocations and routine payouts. A pause must not let one agent seize funds, rewrite history, or cancel already-valid user refunds; define its scope, expiry, recovery, and public audit event.
- When a critical integrity failure is suspected: stop the affected operation class, preserve logs/anchors, notify participants through authenticated channels, reproduce in an isolated environment, audit adjacent transitions, release a signed fix, and resume only after independent verification.
- Design compensation/reserve policy before production value is exposed. A reimbursement process is recovery, not prevention, and must not silently authorize inflation or treasury withdrawal.

## Alkaest launch gates

Before any real-money treasury or token function is enabled:

1. RFC-0008 and RFC-0014 specify exact integer units, transaction validation, atomic state transitions, pause authority, recovery, and treasury segregation.
2. All message and transaction parsers have limits for size, count, nesting, timeout, and resource consumption.
3. The full funding-to-payout workflow is tested on Bitcoin `regtest` with malicious peers, invalid/negative/overflowing values, forged or stale attestations, altered outputs, replayed events, and conflicting event order.
4. Independent nodes reach the same result from the same signed inputs; malformed inputs are rejected without changing state or moving funds.
5. Security review includes a second reviewer/team, threat-model review, dependency/build provenance, key-compromise drills, emergency pause and recovery drills, and a tested upgrade path.
6. Production caps remain deliberately low and can only increase through a separately authorized, delayed, signed policy change.

## Design conclusion

The main lesson is not merely “check for negative fees.” It is: no economic or authority-critical value supplied by a peer may be trusted as an input to settlement until each participant has validated its range, authority, and relationship to the agreed state. Alkaest should make those checks protocol rules, test adversarial messages early, and constrain losses if a rule still fails.
