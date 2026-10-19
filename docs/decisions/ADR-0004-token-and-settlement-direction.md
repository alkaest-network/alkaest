# ADR-0004 - Token and Settlement Direction

**Status:** Accepted
**Date:** 2026-10-18
**Decision Type:** Economic and Protocol Direction
**Related:** ADR-0003, roadmap RFC-0008 (escrow, bonds and settlement)

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
| A. No token | Reputation is non-transferable; payments happen outside the protocol (cash, PIX, card) | Simplest; no regulatory exposure; no speculation | No native escrow or node incentives |
| B. Bitcoin as the settlement layer | Payments and escrow in BTC (Lightning for small amounts, 2-of-3 multisig escrow for disputes), like Bisq | No token to launch or defend; censorship-resistant; proven model (Bisq) | BTC volatility for service prices; Lightning UX on phones |
| C. Asset on Bitcoin for governance (BSQ-like) | A colored asset issued on Bitcoin (Taproot Assets or RGB) to reward contributors and service nodes and to vote | Mirrors Bisq's DAO; stays in the Bitcoin security model | Tooling still maturing; legal analysis needed before any distribution |
| D. Token on a smart-contract chain | ERC-20 on an Ethereum L2 (or Solana SPL) | Rich tooling and liquidity | Pulls the network toward a chain's governance and sequencers; strongest regulatory exposure if sold; speculation |
| E. Own chain | Cosmos SDK, Substrate, or custom consensus | Full control | Months of work, validator set to bootstrap and secure; contradicts ADR-0003 (no blockchain needed for validation) |

---

## Recommendation

1. **Reputation is never a token.** It is derived from signed evidence (ADR-0003) and cannot be transferred, bought or staked away.
2. **No token until there is real usage.** Phases 0 to 3 of the rollout plan run without one.
3. **When value moves, settle on Bitcoin first (option B).** It matches the Bisq model the network wants to follow, avoids launching an asset, and keeps escrow peer-to-peer. Stablecoin rails on Bitcoin (Liquid, Taproot Assets) can be evaluated for price-stable service payments.
4. **If incentives or governance need an asset, evaluate option C**, after legal advice. Avoid D and E.
5. **Prototype locally with no real money**: Bitcoin `regtest` plus a local Lightning network (for example Polar) and simulated escrow between local nodes. This is the "first running locally" step; the global testnet then uses Bitcoin `signet`.

---

## Legal Note

Decentralising the network changes who controls data and funds; it does not take a project outside the law. Bisq stays operable because it never holds users' data or money, not because laws do not apply to it.

* **Data protection (LGPD in Brazil, GDPR elsewhere):** a network that keeps personal data on the owner's node and carries only pseudonymous, signed facts (ADR-0003) minimises exposure by design. Alkaest Chatbot, as a commercial service for local businesses, remains responsible for the personal data it processes.
* **Tokens:** selling or promising returns on a token can make it a security (CVM in Brazil), and exchanging or custodying crypto-assets is regulated (Law 14.478/2022). Options A and B avoid issuing an asset at all.

Get legal advice before distributing any asset or enabling cross-establishment customer signals.

---

## Decision

Accepted on 2026-10-18: **no token now (option A); when payments arrive, settle on Bitcoin (option B).**

* Reputation is never a token.
* No asset is issued during rollout phases 0 to 3.
* Payment and escrow prototypes run only on Bitcoin `regtest` with a local Lightning network, then `signet` on the global testnet.
* A Bitcoin-native governance or incentive asset (option C) may be reconsidered later, only after legal advice and a new ADR.
* RFC-0008 (escrow, bonds and settlement) is written against this decision.
