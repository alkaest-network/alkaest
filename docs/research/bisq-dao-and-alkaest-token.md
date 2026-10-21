# Research: Bisq DAO and an Alkaest Token

**Status:** Research baseline; not an issuance proposal  
**Date:** 2026-10-18  
**Related:** ADR-0003, ADR-0004, ADR-0006, ADR-0007, ADR-0008, RFC-0003, RFC-0008, RFC-0014

## Purpose

Alkaest intends to design a native economic and governance asset for a network that may coordinate work across many independent projects. This document studies the Bisq DAO as a reference and records the questions Alkaest must answer before choosing an asset model, implementation, distribution, or launch.

This is protocol research, not legal, investment, tax, or financial advice. It does not authorize token issuance, sale, trading, custody, or a mainnet deployment.

## Bitcoin's long horizon: what the roughly 120-year figure means

The often repeated “120 years” is not a Bitcoin adoption target. Bitcoin's documented long horizon comes from its block-subsidy issuance schedule: the subsidy began at 50 BTC per block, is halved every 210,000 blocks (about four years at the ten-minute target), and is expected to reach zero around 2140. Since the network began in 2009, that is roughly 131 years; “120 years” is an imprecise shorthand, not the protocol's stated duration.

Bitcoin measures this schedule in block heights, not calendar years. Therefore, the 2140 date is an estimate and depends on actual block production. The schedule is meant to make new issuance predictable and finite. It does not say when Bitcoin will achieve “total adoption,” and it does not establish that a protocol needs a 120-year token or governance schedule. As block subsidy declines, transaction fees are expected to become a larger part of miner compensation.

For Alkaest, the useful precedent is a rule that can be checked by independent participants and does not require a founder to keep making discretionary monetary decisions. The duration itself should be used only as a continuity stress-test horizon, not copied as a token emission plan. We should separately model issuance, contributor rewards, governance succession, software maintenance, and service adoption; none can be inferred from Bitcoin's halving schedule.

Primary references:

- [Bitcoin.org: Halving](https://bitcoin.org/en/halving) — initial 50 BTC subsidy, 210,000-block interval, approximate four-year cadence, and estimated endpoint around 2140.
- [Bitcoin Core: chain parameters](https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp) — consensus parameter for the halving interval.
- [Bitcoin Core: subsidy implementation](https://github.com/bitcoin/bitcoin/blob/master/src/validation.cpp) — subsidy calculation from block height and the halving interval.
- [BIP 42: A finite monetary supply for Bitcoin](https://bitcoin.org/bip/42/) — explains the 210,000-block interval and binary-shift subsidy calculation.

## What the Bisq DAO teaches

Bisq's BSQ is a Bitcoin-denominated colored asset interpreted under DAO rules. The historical Bisq overview describes three central functions: contributor compensation, governance voting, and discounted trading fees. Its technical specification describes compensation proposals, voting periods, issuance validation, burns, and reimbursement mechanisms. Current contributor guidance still describes compensation requests being approved by DAO voting and issuance on Bitcoin.

The useful lesson is the closed economic loop: users fund the system through product activity; contributors propose work compensation; stakeholders authorize issuance; protocol clients validate whether issuance follows the vote. A token participates in operations the product already needs. It is not valuable merely because it exists.

The limitations matter too. Historical Bisq documents describe one product and one DAO, and some publicly indexed technical materials are archived or marked superseded. The model's monthly cycles and compensation-after-work approach should not be copied as Alkaest requirements. In particular, Alkaest has already chosen pre-funded task budgets, explicit acceptance criteria, and a bounded treasury agent (ADR-0007/RFC-0014); these reduce contributor risk and enable auditable automation.

Primary references:

- [Bisq DAO technical specification](https://docs.bisq.network/dao/specification)
- [Bisq DAO technical overview](https://docs.bisq.network/dao-technical-overview)
- [Bisq contributor compensation and voting guide](https://docs.bisq.network/compensation)
- [Bisq historical DAO overview](https://github.com/bisq-network/bisq-docs/blob/master/dao/overview.adoc) (archived; explicitly superseded)

## The broader Alkaest problem

Alkaest may coordinate protocol development, independent projects, service providers, customers, node operators, mediators, and AI agents. A single global treasury and one token-weighted vote for all decisions will not scale safely by default.

The protocol must distinguish at least these domains:

1. **Project economies:** project revenue, grants, budgets, and contributor payments. A project should be able to define its own accounting unit and funding rules.
2. **Protocol funding:** shared work that benefits the network, including core maintenance, security, infrastructure, and public goods.
3. **Governance:** authority to change shared rules, budgets, and protocol parameters. Governance rights need not be identical to payment rights.
4. **Service access and fees:** any future network-level service fee or usage credit. This should exist only if the protocol has a real metered service that needs it.
5. **Reputation and credentials:** evidence of past work, reliability, and roles. These remain non-transferable and cannot be purchased, sold, or delegated as if they were the token.
6. **Settlement:** the asset actually used to pay providers and settle escrow. It may be BTC or another supported asset even if governance uses a separate Alkaest asset.

## Initial design principles

- Design the token system now; defer issuance until utility, legal classification, and governance are reviewable.
- Do not create a custom blockchain for token accounting. Reuse an existing settlement/asset layer only after a comparative technical and legal review.
- Keep reputation separate from transferable assets. Token balance must not stand in for contributor merit or earned trust.
- Make project treasuries and protocol treasury distinct scopes with explicit permissions and auditable transfers between them.
- Prefer pre-funded WorkItems with budgets held under disclosed rules. Record the budget, scope, policy version, acceptance evidence, and payout reference as protocol events.
- The treasury agent may execute bounded, previously authorized decisions; it must not set token policy, mint for itself, change its own spending limits, or decide appeals about its own work.
- Separate everyday operations from constitutional decisions. Routine work acceptance should follow task criteria; token voting should not be a substitute for competent review of each pull request.
- Governance must resist token concentration, vote buying, low-participation parameter changes, Sybil attacks, conflicts of interest, and sudden capture. Consider scoped voting, delegation limits, time locks, quorum rules, and non-token evidence, but do not assume any one mechanism solves these risks.
- Publish supply, issuance authority, allocations, vesting or lockups, treasury balances, and decision records in a way independent nodes can verify.
- Never promise appreciation, revenue share, or returns as a way to market the asset. Economic rights and public communications require legal review.

## Working concept: contribution rewards, mediator bonds, and burns

**This is a design exploration requested on 2026-10-19, not an adopted token proposal.** It must preserve ADR-0008's no-issuance gate and ADR-0004's separation between transferable assets and non-transferable reputation.

The idea contains four independent mechanisms that should not be collapsed into one rule:

1. **Earn / issue:** contributors receive tokens after independently verified work. Issuance creates new units and dilutes existing holders unless it is within a defined cap or offset by burns.
2. **Transfer / sell:** a holder can transfer or sell unlocked units. This creates liquidity, but the buyer receives the asset, not the seller's contribution record or reputation.
3. **Lock / bond:** a holder temporarily makes units unspendable as collateral for a role. Locked units cannot also be sold or burned. A bond is returned when the role ends if no valid slashing decision applies.
4. **Burn:** units are made permanently unspendable. A burned unit cannot later be sold, locked, voted with, or restored to the contributor. Slashing by burning should require a narrowly defined violation, evidence, independent review, notice, and appeal.

Bisq is useful because its mechanisms are distinct: compensation requests approved through DAO governance issue BSQ; product fees paid in BSQ destroy units; and high-trust roles such as mediators require separately approved bonded roles. Contributors can also voluntarily burn BSQ in the Burning Men process for a chance to receive bitcoin trade fees. These are not interchangeable token actions. See [Bisq compensation](https://bisq.wiki/Compensation), [Bisq DAO Phase Zero](https://docs.bisq.network/dao/phase-zero.html), and [Bisq 2 roles](https://bisq.wiki/Bisq_2_Roles). Historical/proposal documents explain the lock, unlock-delay, and confiscation pattern, but the Alkaest design must define its own asset and due-process rules; see the [Bisq bonding proposal](https://github.com/bisq-network/proposals/issues/32).

### Three contributor issuance models

| Model | Rule | Strength | Main weakness |
|---|---|---|---|
| A. Pre-priced task reward | Before work begins, a funded WorkItem declares the token reward and acceptance evidence. After acceptance, issue the declared amount under the frozen policy. | Predictable and auditable; contribution approval does not depend on a post-hoc popularity vote. | Token price can move during work; token rewards cannot replace a secure settlement budget. |
| B. Epoch contribution pool | Each period allocates a capped pool among accepted contributions using scores, review and impact. | Adapts to changing network capacity and lets users compare work in a common period. | Reintroduces score gaming, task splitting, popularity bias, collusion and retroactive policy pressure; depends on mature RFC-0006 and appeal rules. |
| C. Fixed issuance schedule | Contributors split a fixed, predeclared supply or vesting allocation; no new token is issued after the cap. | Predictable maximum supply. | Early contributors may receive outsized governance weight; long-term contributors may have no reward after allocation is exhausted. |

**Conservative starting point:** model A, but make a token reward optional and separate from the pre-funded BTC/accounting-unit bounty. Use a fixed token amount declared before work, an epoch issuance ceiling, independent task review and an appeal path. Do not award tokens solely for number of issues, lines of code, merged PRs, AI approval, or token-holder votes. Until RFC-0006 is accepted, treat this as compensation accounting only; the token is not a proof of merit or eligibility for authority.

### Three mediator qualification models

| Model | Rule | Strength | Main weakness |
|---|---|---|---|
| A. Transferable-token threshold | A holder with at least a minimum amount may apply for mediator role. | Simple; a role bond can make misconduct costly. | Wealth can buy eligibility; token ownership does not prove competence, independence, or fairness. |
| B. Token-weighted election/selection | Holders vote or the largest holders choose mediators. | Uses a legible governance mechanism and can replace role holders. | Concentration, vote buying, apathy and purchased power; creates a single wealthy arbiter risk. |
| C. Qualified panel plus equal minimum bond | Candidates meet published, non-transferable qualifications and conflict checks; each selected mediator locks the same minimum bond; cases are assigned by rotation or a verifiable, precommitted selection rule. | Stake does not scale influence; combines accountable collateral with competence and role separation. | Requires a fair qualification/appeal process; identity clustering and panel capture still need safeguards. |

**Recommended design direction for debate:** C, if Alkaest adopts a transferable token at all. Token holders may apply to serve and lock a common minimum bond; owning more than the minimum gives no extra voting weight, case priority, or authority. A mediator recommends or attests to a decision; a separate policy/panel decides any appeal or bond slashing. The mediator does not control treasury keys. If role qualification is based on purchased token alone, call it capital-backed eligibility, not reputation.

### Burn options and the supply loop

- **Fee burn:** burn a disclosed protocol fee when a real service is consumed. This creates token demand only if the service itself is useful; otherwise it is artificial demand and may exclude users.
- **Voluntary burn:** let holders irreversibly burn tokens without promising a return. It is simple but should not be marketed as a route to appreciation or governance influence.
- **Bond slashing:** burn only a bounded part of a mediator bond after a narrowly defined, appealable finding. For reimbursement or victim recovery, burning may be the wrong destination; a separate compensation reserve is needed.
- **Burn-to-qualify:** permanently destroy tokens to obtain a role. This is not a bond: it cannot be returned after service and may privilege wealthy candidates. Avoid for the initial mediator role.
- **Lock-to-qualify:** temporarily lock tokens and return them after a release delay. This preserves collateral and has a recoverable path; it still imposes a capital barrier and requires fair slashing rules.

If all contributor tokens are burned when used, contributors cannot later sell or lock those same units. If fees burn all tokens while contributor work continually issues new units, net supply and funding still depend on issuance policy, fee demand and the timing of both flows. The protocol needs a transparent issuance cap, budget source and reconciliation rule; “everything gets burned” is not itself a sustainable treasury model.

### Founder-independent continuity

A token or DAO does not guarantee that Alkaest survives its founder. Continuity needs protocol rules and operational succession:

1. No founder-only signing key, domain, repository, release pipeline, or treasury key can halt or capture the project. Use threshold custody with independent key holders and rotation/recovery procedures.
2. Publish a signed succession/maintenance policy that defines how maintainers are nominated, removed, and replaced, how protocol changes become active, and how emergency pauses expire.
3. Separate project-local budgets from the shared protocol treasury. Token-weighted holders must not unilaterally change payment policy, appoint themselves mediators, mint for themselves, or redirect funds.
4. Put policy changes behind public notice, a delay, independent review, and a defined challenge/rollback window. Keep emergency pause authority narrow and time-bounded.
5. Preserve open-source reproducible releases, exportable signed history, multiple bootstrap nodes, and a documented right to fork. Token governance cannot replace independent node validation or access to the protocol data.
6. Test founder/key-loss scenarios before mainnet funds or issuance. A safe shutdown, recovery, or fork should be possible without rewriting valid history.

### Questions before any token RFC

- Is the token an optional contributor bonus, a governance asset, a service-fee asset, a mediator bond, or some explicitly bounded combination?
- Does a contributor receive a fixed pre-announced amount per task, a share of a capped epoch pool, or a finite allocation? Who funds the economic value of that reward?
- Can tokens be freely transferred? Does transfer change only ownership, or also governance power? What prevents purchased tokens from dominating protocol decisions?
- Does mediator eligibility require a returned bond or permanent burn? What is the common minimum, unlock delay, maximum slashing amount, decision threshold, and appeal route?
- Can anyone burn tokens voluntarily? Are any service fees burned, paid to a treasury, or used to reimburse contributors? What is the issuance/burn equation per epoch?
- Which roles and key holders take over if the founder disappears, loses keys, or becomes malicious, and how can they be removed without making one group sovereign?
- Can the protocol continue with BTC-funded work and non-transferable credentials if no transferable token survives the legal/security review?

No ticker, supply, distribution, market, price, listing, rights, or launch date is selected by this exploration.

## Architecture questions to answer

### Purpose and rights

- What concrete protocol action requires an Alkaest asset that BTC or project-specific assets cannot already provide?
- Is the asset for governance, protocol fees, incentives, bonding, or some subset? Why should those rights be coupled?
- Does holding it create any claim on treasury assets, revenue, redemption, or services?
- Which decisions are global, which belong to each Space/project, and which should be handled by specialists or delegated councils?

### Supply and funding

- Is supply fixed, capped per epoch, or issued only against approved work? What prevents an emergency from being used to bypass caps?
- How are recurring protocol costs funded when there is little network usage?
- How do grants, donations, product revenue, and service fees enter a project treasury and the protocol treasury?
- Are paid issues denominated in a volatile token, BTC, or a stable accounting unit with settlement separately specified?
- How are refunds, failed work, disputed payouts, security incidents, and reimbursements handled?

### Governance and scale

- Can projects opt into local governance without granting their members control over the protocol treasury?
- What limits whale influence, borrowed voting power, vote buying, voter apathy, and governance capture?
- How can a decision be challenged, appealed, or rolled back without allowing an agent or maintainer to seize funds?
- What independent reviewers, guardians, or threshold controls are required for exceptional transfers and protocol upgrades?
- How do node clients deterministically validate issuance and governance outcomes, including upgrades to those rules?

### Distribution and launch

- What is the genesis distribution and why is each allocation justified?
- Are early contributors compensated at fair market rates, or granted governance power unrelated to future work?
- What prevents insiders from changing rules before broader participation exists?
- What are the testnet, launch, migration, key recovery, incident response, and sunset plans?
- Which jurisdictions are targeted or excluded, and who is responsible for regulatory, consumer, tax, accounting, AML/sanctions, and privacy obligations?

## Regulatory research baseline

The legal treatment follows the asset's rights, distribution, marketing, and surrounding services, not merely the word “utility”, “DAO”, or “token”.

- In the EU, MiCA regulates crypto-asset issuance/offers and service provision, with different regimes and exemptions. For many public offers of crypto-assets other than asset-referenced or e-money tokens, the regulation sets white-paper obligations and specific exemptions; exemptions are conditional and should not be assumed to cover a continuously growing service network. An asset that qualifies as a financial instrument falls outside MiCA's crypto-asset regime and may fall under other financial-services rules. Portugal implementation and competent authority analysis must be confirmed before any offer or service.
- In Brazil, the CVM states that digital representation does not remove securities from CVM oversight; the BCB's virtual-asset service-provider regime and securities regulation cover different activities. Whether Alkaest issues an asset, operates a venue, provides custody, or enables transfers changes the analysis.
- A decentralized software protocol does not by itself eliminate duties for identifiable issuers, offerors, operators, custodians, or service providers.

Primary references:

- [MiCA, Regulation (EU) 2023/1114, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/1114/oj/eng)
- [ESMA guidelines on qualifying crypto-assets as financial instruments](https://www.esma.europa.eu/document/guidelines-conditions-and-criteria-qualification-crypto-assets-financial-instruments)
- [CVM: Decree 11.563/2023 and scope of virtual-asset services](https://www.gov.br/cvm/pt-br/assuntos/noticias/2023/publicado-decreto-sobre-ativos-virtuais)
- [CVM Opinion 40 on crypto-assets and securities](https://www.gov.br/cvm/pt-br/assuntos/noticias/2022/cvm-divulga-parecer-de-orientacao-sobre-criptoativos-e-o-mercado-de-valores-mobiliarios)
- [Brazilian Decree 11.563/2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11563.htm)

This summary is not a legal classification of a hypothetical Alkaest asset. Obtain jurisdiction-specific counsel before distribution, sale, exchange listing, custody, or enabling a regulated service.

## Recommended sequence

1. Specify the economic roles and decision scopes without selecting a chain or ticker.
2. Model at least three token architectures: BSQ-like Bitcoin-colored asset; a separate asset on an established smart-contract network; and no transferable token with BTC settlement plus non-transferable credentials. Compare verification, privacy, UX, fees, governance, migration, custody, and regulatory burden.
3. Simulate multi-project treasury flows, issuance caps, contribution payouts, abuse cases, and governance attacks using fictional data and no real funds.
4. Define the minimum network utility that justifies a token and the conditions under which the protocol should operate without one.
5. Obtain legal, tax, and accounting opinions for Portugal/EU and Brazil, including who is the issuer/offeror/operator and what user-facing services exist.
6. Publish a token design RFC and a revised ADR only after the model and review are complete. Testnet experiments may use valueless assets with explicit no-market/no-redemption rules.
7. Treat any mainnet issuance, public sale, trading, custody, or real treasury authority as a separate gated decision.

## Current conclusion

Alkaest should design for an eventual native token because a multi-project DAO may need a shared way to coordinate protocol-level funding and governance. This does not yet prove that a transferable token is the right solution, nor that one asset should handle every role. No issuance, sale, listing, or real-money governance is authorized by this research. The token's purpose and rights remain open; reputation stays non-transferable; Bitcoin remains the current settlement and audit direction under ADR-0004 and ADR-0007.
