# Bitcoin Payouts and Optional Bisq Conversion

**Status:** Informative research and product direction recorded from founder input; settlement details remain subject to RFC-0008 and launch gates.  
**Reviewed:** 2026-10-19

## Direction for Alkaest

The founder's intended model is to pay contributors in **Bitcoin (BTC)** through Alkaest's funded-work flow and make it practical for contributors who want fiat to trade their BTC through Bisq. The initial paid-work asset is Bitcoin specifically; other cryptocurrencies and an Alkaest token are not implied. This aligns with [ADR-0004](../decisions/ADR-0004-token-and-settlement-direction.md), which selects Bitcoin as the first settlement direction and defers any Alkaest token.

For the initial implementation, BTC is the proposed settlement asset, with on-chain Bitcoin in `regtest` as the first conformance target in Draft RFC-0008. Lightning is deferred until a separate settlement specification covers hold-invoice, timeout, claim, refund, and liquidity semantics. The Alkaest network records task terms, funding authority, acceptance, payout authorization, and verifiable settlement references. Bitcoin carries the value transfer/settlement; it does not replace Alkaest's signed event log or validate all protocol events.

## What Bisq provides

Bisq is peer-to-peer trading software, not a fiat conversion counterparty or a universal BTC receiving wallet. Bisq documentation describes trades where the Bitcoin side is managed by the trading software/protocol, while fiat transfers happen directly between the two traders through their chosen external payment method. The protocol helps coordinate the trade; it does not transfer fiat through Bisq or guarantee that a buyer, offer, payment method, or acceptable price is available. [Bisq getting started](https://bisq.network/getting-started/), [Bisq Easy](https://bisq.network/bisq-easy/)

Bisq 2 is designed to support multiple trade protocols and wallet options, and Bisq's documentation distinguishes the Bisq 1 and Bisq 2 applications. Therefore Alkaest should not hard-code a generic destination called “Bisq wallet.” The contributor should supply a BTC destination compatible with the chosen Alkaest settlement rail; the contributor may independently move or receive funds into a wallet and trade through the Bisq version/protocol they choose. Verify any specific wallet and address compatibility with the recipient and the current Bisq release before paying. [Bisq 2 overview](https://bisq.wiki/Bisq_2)

### User-visible promise boundary

Alkaest may say: **“You can receive BTC to a wallet you control and, if you choose, use Bisq to find a peer-to-peer trade for fiat or another supported asset.”**

Alkaest must not promise an instant conversion, guaranteed liquidity, a fixed fiat amount, a specific Bisq wallet feature, or that Bisq handles the contributor's bank transfer. Conversion is a separate user-initiated trade, subject to market offers, fees, timing, limits, payment-method availability, and the user's own tax/legal obligations. This is a product boundary, not legal or tax advice.

## Requirements to resolve before a paid WorkItem

- **Asset and rail:** confirm BTC as the asset for the first real payment and select the supported rail under RFC-0008. Do not advertise generic “crypto” if the first release supports only BTC.
- **Price denomination:** decide whether the task is quoted as a fixed BTC amount or priced in fiat and converted to a fixed BTC amount at a published time/rate source before funding. In either case, freeze the exact BTC amount, fee ownership, and rounding rule before assignment; no post-hoc rate change.
- **Recipient wallet:** bind a contributor-controlled destination using a signed instruction and a small/standard destination-verification process. Do not request seed phrases or private keys. Confirm address/network compatibility and show a human-readable confirmation before funding.
- **Funding and release:** pre-fund the agreed WorkItem or milestone under escrow/refund rules before work starts. Acceptance and payout authorization remain separate from settlement-confirmed `paid`.
- **Bisq optionality:** present Bisq as an optional, independent way to seek a BTC/fiat trade, never as a dependency to receive Alkaest compensation. No automatic transfer to Bisq, trade execution, fiat-account access, or referral/bounty ranking is part of the initial payment flow.
- **Privacy and evidence:** store settlement references and only the data needed to verify amount, destination, and finality. Never publish banking details or personal payment references in the Alkaest replicated log or Bitcoin anchor.
- **Legal/accounting:** review the engagement, tax reporting, and Bitcoin-payment treatment for both the project and contributor jurisdictions before enabling real payments.

## Implications for the first Alkaest tasks

The brand identity and Flutter briefs are candidate needs, not guaranteed first bounties. The Brain should choose their order and exact BTC allocation using the candidate evidence, approved pricing bounds, and verified spendable balance. The contributor may choose a self-custody wallet that they can use with a Bisq workflow, but that preference must not be a mandatory eligibility rule or an Alkaest-managed conversion. Until the treasury is operational and the applicable launch gates pass, all protocol tests use simulated balances or Bitcoin `regtest` and make no real-payment promise.

## Sources

- [Bisq: Getting Started](https://bisq.network/getting-started/) — self-custody and external fiat-payment mechanics.
- [Bisq Easy](https://bisq.network/bisq-easy/) — Bisq Easy as a BTC trade protocol.
- [Bisq 2 overview](https://bisq.wiki/Bisq_2) — multiple protocols/wallet direction and distinction between Bisq applications.
