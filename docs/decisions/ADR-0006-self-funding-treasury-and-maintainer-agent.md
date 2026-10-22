# ADR-0006 - Self-Funding Treasury, Task Bounties with Random Mediation, and the Maintainer Agent

**Status:** Accepted (direction); treasury and release authorization are further specified in ADR-0007 and RFC-0014; settlement and mediation mechanisms remain in RFC-0008 and RFC-0013
**Date:** 2026-10-18
**Decision Type:** Economic, Security and Operations
**Related:** RFC-0003 (§4.2, §4.3, §11), ADR-0003, ADR-0004, ADR-0005, ADR-0007, RFC-0006, RFC-0008, RFC-0013, RFC-0014

> **Implementation boundary:** The mediator lottery, “proof of reading,” bond/slashing, fee proposals, fiat collateral, and mediator-assisted 2-of-3 spend paths below are design proposals from this ADR, not finalized protocol rules. Draft RFC-0013 now supersedes them where it explicitly defers a mechanism. In particular, the first Bitcoin block after claim is not an accepted secure selection algorithm, a signature cannot prove human comprehension, and a mediator verdict is not authority to spend an escrow. Disputed real-funds spending is disabled pending joint RFC-0008/RFC-0013 design and independent Bitcoin script/key review.

---

## Context

The operator wants Alkaest to fund and run its own development from day zero, with as little human intervention as possible, until it runs by itself.

The requirements:

1. **A local AI administers the project.** It works out what the project needs, for example a visual identity, and how much each thing costs. It ranks needs by importance and, when money is available, funds the most important ones.
2. **Anyone can open a paid task, like a Bisq offer.** The task creator chooses the **currency and payment method**.
3. **Proof of work is judged by a randomly drawn mediator.** For code, the proof of work is the patch on the canonical Radicle repository (ADR-0010). Payment is released only after that third party approves.
4. **Fees.** The mediator earns a fee, and a small share goes to Alkaest's maintenance.
5. **Income.** It comes from donations and from network activity, all in crypto. Bisq is used when someone wants fiat.

RFC-0003 already describes donation-first funding and funded work items, and leaves the payout method open (§11.4). ADR-0004 rules out a token and points to Bitcoin settlement. This ADR sets the direction for both.

---

## Decision

### 1. Tasks are open offers, like Bisq

Anyone, including the Alkaest treasury agent, can open a **task** in a space. A task is a `work_item` (RFC-0003) that carries an offer:

* the deliverable and the acceptance criteria;
* the **amount, currency and payment method**, chosen by the creator from the methods the protocol supports (§3);
* the **domain** of the work (code, design, writing, translation, …), which selects the mediator pool;
* a deadline.

Tasks are protocol records, so their whole life is a signed, replayable log. That covers the offer, the claim, the delivery, the mediator's verdict and the payment.

### 2. Payment is held in escrow and released by a random mediator

The model follows Bisq 2: every movement of value is a protocol multisig between **the two parties involved and one mediator**. There is no separate backup-key holder.

When a task is accepted by a worker, the protocol draws a **mediator**. The draw happens at claim time, before funding, because the mediator's key is part of the escrow:

* **Eligible:**
  * the identity runs a **mediator node with a local AI** (§2.1) and advertises the mediator role for that domain;
  * it has posted a **bond**;
  * it meets the domain's validation eligibility policy; any reputation criterion is disabled until RFC-0006's integrity launch gate is met;
  * it has no conflict of interest: it is not the creator or the worker, is not linked to either, and has not mediated the same pair recently.
* **Random, verifiable and not chosen by anyone:**
  * the seed is SHA-256 of the hash of the first Bitcoin block mined after the claim, plus the task id;
  * each candidate's ticket is SHA-256(seed ‖ identityId);
  * the lowest ticket wins under a deterministic eligible-candidate rule; no weighting by reputation is enabled until RFC-0006 defines and validates it;
  * if that mediator does not accept in time, the next ticket is asked.

  Any node can recompute the draw.
For crypto payment methods, the money sits in an escrow **before work starts**, so the worker knows it exists. The escrow is a **2-of-3 multisig: creator, worker, mediator**.

**When both parties agree, the mediator is not needed.** The worker delivers, the creator accepts, and both sign the release. The mediator's AI only checks that both approvals exist, records an automatic confirmation, and needs no human time. In this case, no mediator fee is charged (§4).

**When they disagree, the mediator conciliates.** This happens if the creator does not accept the delivery, or the worker does not accept a refund or a partial payment. The steps:

1. **AI pre-analysis.** The mediator node's local AI compares the proof of work (the PR, files or other deliverable) with the acceptance criteria. For code, it also reads the CI results. It writes a signed pre-analysis report that both parties can see.
2. **Conciliation proposal.** Based on that report, the mediator proposes a payout: full, partial or refund. If both parties accept, they sign it themselves and the case closes.
3. **Verdict.** If conciliation fails, the human mediator decides: approve, request changes, or reject. The decision is a signed event, and it comes with **proof of reading** (§2.1). The mediator then signs the release with the side the verdict favors:
   * **Approve:** the mediator and the worker release the money to the worker.
   * **Reject:** the mediator and the creator refund it.
4. **Mediator unavailable.** The creator and the worker can always settle between themselves without the mediator.

#### 2.1 Mediator nodes: local AI first, human sign-off always

To be eligible, a mediator must:

* run a node with a **local AI** that analyses its cases. It does not have to be a cloud service: the same node software and brain (`alkaest-brain`) can run on the mediator's own machine;
* **pre-analyse every case**, and attach the signed AI report to the verdict;
* **approve every disputed verdict manually**, with proof of reading.

**What the protocol can verify, and what it cannot:**

* **Which model ran:** the protocol cannot prove it. What it requires is the signed pre-analysis report attached to every verdict. A mediator whose reports are empty or contradict the verdict loses appeals, bonds and reputation.
* **That a human read the case:** the protocol cannot prove it either. It makes rubber-stamping costly instead:
  * a **comprehension check**: the AI generates questions specific to the case, for example "which acceptance criterion does the second commit address?", and the mediator answers them inside the signed verdict;
  * a **reasoned verdict** that cites the acceptance criteria and the evidence;
  * **appeals** that can overturn the verdict and forfeit the bond.

The AI prepares, the human decides. In the cooperative case, the AI's automatic confirmation is enough because both parties already signed.

For **fiat payment methods** (PIX, bank transfer), the money cannot be escrowed. As in Bisq, both sides post a **security deposit in BTC** into the escrow, and the mediator's verdict decides which deposit is forfeited.

An **appeal** goes to a panel of three mediators drawn the same way. Its verdict is final. RFC-0013 specifies this.

### 3. Payment methods

| Method | Escrow | Phase |
|---|---|---|
| BTC on-chain | 2-of-3 multisig | First |
| BTC Lightning | Hold invoice with timeout (small amounts) | Later, after a separate settlement RFC and timeout/refund review |
| Stablecoin on Bitcoin layers (for example USDt on Liquid) | Liquid multisig | Later |
| Fiat (PIX, bank) | BTC security deposits only | Later |

Converting to fiat outside the protocol is done in Bisq.

### 4. Fees

Every task pays, on top of the bounty:

* the **mediator fee**, a published percentage (proposed default 3%), paid only when there is a dispute. A cooperative close costs nothing beyond the maintenance share. In a dispute, the fee comes out of the escrow and the verdict decides which side bears it;
* the **Alkaest maintenance share**, a small published percentage (proposed default 0.5%), sent to the treasury on every closed task.

Both are outputs of the escrow's release and refund transactions, built by every client. An open protocol cannot force a fee, because a fork can drop it, so the share stays small enough to be worth paying. Bisq makes the same bargain with its trade fees.

### 5. The treasury and the maintainer agent

The Alkaest treasury is one more task creator. A local AI agent, called the **Brain** for planning, proposes and prioritizes candidate work under the signed budget policy. ADR-0007 and RFC-0014 refine this direction: the Brain selects an eligible issue and proposes its exact BTC bounty from permitted evidence and a deterministic verified balance; a separate policy gate authorizes publication and funding. The Brain has no treasury signing keys and cannot treat its estimates as verified funds.

What the agent does from day one:

1. **Plan.** It keeps a **needs board** in the `alkaest-network` space. The founder seeds initial candidate needs and budget boundaries; after that, permitted metrics, reports, feedback, complaints, contributor quotes and verified treasury state inform the Brain's ranking. Examples of needs:
   * a visual identity;
   * an RFC-0007 implementation;
   * a security review;
   * translations;
   * hosting costs.

   Each need has acceptance criteria and evidence references. The Brain records priority, confidence, pricing evidence and its proposed BTC bounty; unsupported estimates are deferred or escalated rather than presented as market prices.
2. **Publish.** It shows the needs board and the treasury balance publicly, in the repository, the site and the app. The board doubles as the donation pitch.
3. **Fund.** A deterministic ledger computes spendable BTC after reservations, pending payouts, fees, obligations and the protected reserve. If the Brain's selected task and proposed bounty fit the signed policy and balance gates, the agent may publish and fund it; otherwise the decision is deferred or escalated. Candidate backlog entries are not open or funded tasks.
4. **Review first.** It writes a first-pass review on each deliverable, including deterministic gates for code: CI, tests, lint and license. This helps the mediator, but **the agent is never the mediator of its own tasks**, because that is a conflict of interest.
5. **Report.** It publishes monthly what was funded, delivered and paid, all verifiable from the log.

**Custody:**

| Wallet | Holds | Control |
|---|---|---|
| **Reserve** | Most funds | 2-of-3 multisig: maintainer (hardware wallet), agent, and a **mediator drawn for the reserve** (§2), redrawn every budget period by moving funds to a new address. The mediator co-signs only refills that match the published budget policy. Neither the agent nor the maintainer can spend alone |
| **Operating allowance** | One budget period of spending, for example a quarter | Agent alone, within the budget policy |
| **Task escrows** | Each funded task | 2-of-3 creator (agent) / worker / mediator |

Human intervention is reduced to **refilling the operating allowance once per period** and **changing the budget policy**. The worst case of an agent fully compromised is losing one allowance. The reserve cannot move without the maintainer or the reserve's mediator.

For routine Alkaest work, the agent acts as the project requester and may accept a contributor's delivery and authorize an uncontested payout when the funded WorkItem's predeclared evidence gates pass. For code, this includes the exact merged revision, required independent reviews, and required CI/security checks; a PR approval by itself is not sufficient. The agent MUST NOT receive payment for its own task, control the contributor's payout destination, alter the policy, or mediate a dispute on a task it funded. Disputes and exceptions go to an independent mediator under RFC-0013. ADR-0007 and RFC-0014 define this boundary and the Bitcoin audit trail.

### 6. Budget policy

The policy is a signed object in the `alkaest-network` space. The agent reads it and cannot change it.

* **Reserve floor:** at least 6 months of infrastructure costs, never spent on tasks.
* **Allowance:** at most 50% of the spendable balance per quarter goes into the operating allowance.
* **Per-task caps:** by domain and complexity, plus a per-worker monthly cap.
* **Price guidance:** a reference table by domain and complexity. The agent's estimates must fall inside it or be flagged for the maintainer.

### 7. Graduation path

| Phase | What runs | Human role |
|---|---|---|
| **A. Simulation (now)** | Agent planning, needs board, tasks, escrows and mediator draws, on Bitcoin `regtest`/`signet` with test repositories | Watches and tunes the agent |
| **B. Supervised** | Real-money operation only after all launch gates; initial operation is human-supervised | Refills the allowance; approves out-of-policy needs; any mediation follows conflict rules |
| **C. Open mediation** | Eligible participants can be drawn under RFC-0013; any reputation-based eligibility remains gated by RFC-0006 | Refills the allowance; changes the policy |
| **D. Self-running** | Several maintainers co-sign the reserve and govern the policy by quorum (RFC-0012, planned, not yet written) | Governance only |

**Phase A is simulation only.** The agent can plan, price, prioritize and publish a simulated needs board. Real-money operation waits for every launch gate in ADR-0007 and the roadmap, including accepted RFC-0008/0013/0014 behavior, adversarial testing, recovery drills, independent security review, and legal/accounting review.

---

## Security Considerations

* **Prompt injection.** Everything the agent reads can be attacker-controlled: issues, PRs, deliverables and comments. The agent's spending power is capped by policy and the operating allowance. Amounts are fixed when a task is funded. Payout destinations come from the worker's signed claim, never from content. Routine uncontested release follows predeclared gates; disputes require an independent mediator.
* **Sybil mediators.** Bonds, reputation thresholds, random draws, and conflict checks do not prove distinct human control. Related identities may evade protocol-visible checks. RFC-0013 must define candidate caps, conflict handling, panels, appeals, and exposure limits; RFC-0006 must define any reputation-derived eligibility. Until these rules pass review, do not describe the mediator pool as Sybil-resistant or open mediation as launch-ready.
* **Mediator/worker collusion.** Random selection and bonds may raise the cost but do not prevent a colluding group from controlling several identities. High-impact tasks require an independently selected panel and appeal path under RFC-0013; limits and human oversight remain necessary.
* **Collusion between the reserve's mediator and the agent** could move the reserve without the maintainer. Three measures limit it:
  * the reserve's mediator must post a bond proportional to the reserve;
  * it is redrawn every budget period;
  * the maintainer watches the reserve address (the node alerts on any spend).

  Until the mediator pool is large and bonded (phase C), keep the reserve small and refill from donations directly.
* **Rubber-stamping mediators** who approve without reading are deterred by comprehension checks, reasoned verdicts and appeals that forfeit bonds (§2.1). None of these is a proof, which is why appeals exist.
* **Randomness bias.** The seed uses a future Bitcoin block hash. A miner could bias the draw only by throwing away valid blocks, which costs far more than a typical task. For very large tasks, the seed can combine several blocks.
* **Untrusted deliverables.** Code from tasks runs only in isolated CI or throwaway VMs, never on the machine that holds the agent's or the reserve's keys.
* **Least privilege for the agent.** Forge credentials are limited to issues and comments, with no merge rights: its Radicle identity is never a repository delegate, and any GitHub-mirror token is read and comment only. The network reaches only the project's forges and its own Bitcoin and Lightning nodes. Every action is a signed event or a public comment.
* **Bootstrapping the mediator pool.** A small initial pool is a trust assumption, not proof of decentralization. Publish its membership, conflicts, decision history, limits, and appeal path; keep consequential decisions supervised until independent participation and RFC gates justify expansion.

---

## Model and Hardware

Planning, pricing and first-pass reviews need a stronger model than the chatbot's qwen3:4b. The target is a local model in the 30B class with good coding and reasoning, re-evaluated in AI_MODEL_STRATEGY.md.

The target machine has 32 to 64 GB of RAM, or an Apple silicon Mac with 32 GB or more. It is separate from the customer-facing chatbot node.

---

## Legal Note

This is not legal or tax advice, and it does not classify the proposed activities under any jurisdiction's laws. Before phase B, obtain qualified legal and accounting advice for the actual operating model and countries involved.

Items for that review include donation handling, compensation and mediator fees, reporting and tax treatment, third-party escrow, custody and control of treasury funds, consumer obligations, and the legal form that should hold the treasury. Non-custodial multisig does not by itself establish that an activity is outside regulation. Using Bisq does not determine Alkaest's or its users' separate obligations (ADR-0004).

---

## Consequences

### Positive

* Alkaest funds itself in public, and every satoshi is traceable in the protocol log.
* The task market is useful beyond Alkaest: anyone can hire anyone for verifiable work. This is the first real market on the network.
* Human intervention shrinks to refilling an allowance and governing a policy.

### Negative

* This is a large scope: two RFCs (escrow, and validation and mediation), Bitcoin and Lightning integration, the agent, and a mediator bootstrap.
* Mediation quality is the product. Bad early verdicts would hurt trust more than slow growth would.
* The legal exposure grows with fiat payment methods and third-party escrows.

---

## Implementation Order

1. **Specs:**
   * RFC-0013 Validation and Mediation: eligibility, draw, verdicts, appeals, bonds;
   * RFC-0008 Escrow, Bonds and Settlement: 2-of-3 escrows, Lightning hold invoices, security deposits, fee outputs;
   * RFC-0003 updates: task offer fields, payout destination in the claim, needs board, budget policy;
   * RFC-0014 Treasury Agent and Release Authorization: policy-bound issue funding, provider evidence, automated acceptance/payout gates, and Bitcoin audit anchors.
2. **Agent, phase A, planning only:** the needs board with priorities and price estimates, published from the `alkaest-network` space. It needs no money and can run on day zero.
3. **Treasury service in `alkaest-node`** (Rust, BDK): reserve and allowance wallets, escrow creation and release, on `regtest`.
4. **Mediator draw, cooperative close, AI pre-analysis, conciliation and verdict flow** in the node. The mediator node reuses `alkaest-brain` for the pre-analysis. The app gets screens for mediators (review the deliverable, sign the verdict) and for workers (claim, deliver, receive).
5. **Phase B, only after all launch gates:** supervised real-money operation, published policy, key recovery drills, independent security review, and a mediator pool governed by RFC-0013. Legal review alone or RFC-0014 alone is insufficient.

---

## Open Questions

* Confirm the proposed defaults: mediator fee 3% (disputes only), maintenance share 0.5%.
* Bond sizes and the minimum reputation for mediators in each domain, including the reserve's mediator.
* The minimum model and hardware a mediator node must run for its AI pre-analysis.
* Which fiat methods to support first, and whether at all before phase C.
