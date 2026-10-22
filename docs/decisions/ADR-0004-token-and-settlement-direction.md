# ADR-0004 - Token and Settlement Direction

**Status:** Accepted
**Date:** 2026-10-18
**Decision Type:** Economic and Protocol Direction
**Related:** ADR-0003, ADR-0007, RFC-0008 (escrow, bonds and settlement), RFC-0014 (treasury agent)

---

## Context

The operator wants to think about a token now, prototype it running locally first, and later run it across a global multi-node network. Payments are out of scope for the moment, but the near-term goal is a peer-to-peer network that works outside central systems, in the spirit of Bisq.

Alkaest has three distinct things that are easy to conflate:

1. **Reputation**: evidence that someone delivered (or showed up). Must not be buyable.
2. **Payment and escrow**: moving value between a customer and a provider, with protection against fraud.
3. **Coordination incentives and governance**: rewarding people who run service nodes or build Alkaest itself (the `alkaest-network` funding idea), and deciding protocol changes.

---

## Options

| Option | What it means | Pros | Cons |
|---|---|---|---|
| A. No token | Reputation is non-transferable; payments happen outside the protocol (cash, PIX, card) | Simplest; avoids issuing a protocol token; no token speculation | No native escrow or node incentives; other legal obligations may still apply |
| B. Bitcoin as the settlement layer | Payments and escrow in BTC (Lightning for small amounts, 2-of-3 multisig escrow for disputes), like Bisq | No token to launch or defend; censorship-resistant; proven model (Bisq) | BTC volatility for service prices; Lightning UX on phones |
| C. Asset on Bitcoin for governance (BSQ-like) | A colored asset issued on Bitcoin (Taproot Assets or RGB) to reward contributors and service nodes and to vote | Mirrors Bisq's DAO; stays in the Bitcoin security model | Tooling still maturing; legal analysis needed before any distribution |
| D. Token on a smart-contract chain | ERC-20 on an Ethereum L2 (or Solana SPL) | Rich tooling and liquidity | Pulls the network toward a chain's governance and sequencers; strongest regulatory exposure if sold; speculation |
| E. Own chain | Cosmos SDK, Substrate, or custom consensus | Full control | Months of work, validator set to bootstrap and secure; contradicts ADR-0003 (no blockchain needed for validation) |

---

## Recommendation

1. **Reputation is never a token.** It is derived from signed evidence (ADR-0003) and cannot be transferred, bought or staked away.
   Reputation must also resist self-dealing and collusion before it affects authority, funding, or governance; RFC-0006 is a launch gate (see `docs/research/reputation-integrity-threat-model.md`).
2. **Design before launch; issue only after gated approval.** Token purposes and architecture are researched before implementation hardens assumptions (ADR-0008), while rollout phases 0 to 3 still run without an issued asset.
3. **When value moves, settle on Bitcoin first (option B).** It matches the Bisq model the network wants to follow, avoids launching an asset, and keeps escrow peer-to-peer. Under ADR-0007, Bitcoin is also the required external audit layer for Alkaest treasury deposits, escrow settlements, payouts, and periodic treasury-log commitments after real treasury operation is enabled. Stablecoin rails on Bitcoin (Liquid, Taproot Assets) can be evaluated for price-stable service payments.
4. **Evaluate a governance/incentive asset under ADR-0008**, after multi-project simulations, security analysis, and legal advice. No chain or token mechanics are selected by this ADR. Avoid E; compare existing layers before choosing any asset representation.
5. **Prototype locally with no real money**: the first settlement conformance target is on-chain Bitcoin escrow in `regtest`, using simulated tasks between local nodes. Lightning is deferred until a separate RFC specifies its hold-invoice, timeout, claims, refunds, and liquidity semantics. The global testnet follows only after the applicable RFCs are accepted and reviewed.

---

## Legal Note

Decentralising the network changes who controls data and funds; it does not take a project outside the law. Legal obligations depend on the activity, implementation, parties, and jurisdictions involved. This section is a prompt for review, not a legal classification of Alkaest or any option.

* **Data protection:** local storage and pseudonymous signed facts may reduce some exposure, but do not by themselves determine who is responsible or which data-protection duties apply. Review each product and data flow in every operating jurisdiction.
* **Payments and assets:** token issuance, payments, exchange, custody, escrow, and rewards may raise distinct legal, tax, and consumer-protection questions. Do not treat the absence of a token as a blanket exemption.

Obtain qualified, jurisdiction-specific legal advice before enabling real-money payments, escrow, token or asset distribution, or cross-establishment customer signals.

---

## Decision

Accepted on 2026-10-18: **do not issue a token now; when payments arrive, settle on Bitcoin (option B), while designing the future token architecture under ADR-0008.**

* Reputation is never a token.
* Reputation cannot grant consequential authority until RFC-0006 resolves the self-dealing/Sybil threat model and appeal process.
* The intended initial payment asset for paid contributor WorkItems is BTC through Alkaest's funded-work and settlement flow. Contributors may independently use Bisq to seek a peer-to-peer BTC-to-fiat trade; Bisq is optional and conversion is outside Alkaest. RFC-0008 must still select and specify the actual Bitcoin settlement rail, fee handling, quote denomination, escrow, and refund behavior. No availability, liquidity, rate, or instant fiat conversion is promised. See [Bitcoin payouts and optional Bisq conversion](../research/bitcoin-payouts-and-bisq-conversion.md).
* No asset is issued during rollout phases 0 to 3; token design and valueless simulations may proceed under ADR-0008.
* Payment, escrow, treasury, and audit-anchor prototypes begin with on-chain BTC on `regtest`; Lightning is deferred to a separate specification. `signet` experiments require the relevant RFCs and security review. Real treasury operation is gated by ADR-0007, RFC-0003, RFC-0008, RFC-0013, and RFC-0014.
* No custom Alkaest chain is planned. Bitcoin anchors treasury settlement and audit commitments; Alkaest nodes validate signed protocol event logs independently under ADR-0003.
* The governance/incentive asset remains unresolved; ADR-0008 requires research, simulations, legal review, and a separate launch decision before issuance.
* RFC-0008 (escrow, bonds and settlement) must be written against this decision before real-money settlement.
