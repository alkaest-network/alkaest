# Alkaest Long-Term Continuity Requirements

**Status:** Research baseline; candidate requirements, not protocol rules  
**Date:** 2026-10-19  
**Related:** ADR-0003, ADR-0006, ADR-0007, ADR-0008, RFC-0002, RFC-0014, [token research](bisq-dao-and-alkaest-token.md)

## Purpose

Alkaest should remain understandable, verifiable, maintainable, and recoverable if its founder disappears, loses access, or becomes untrusted. This document turns a multi-generation ambition into failure scenarios and review criteria. It does not promise that the project will exist for a particular number of years, select a token schedule, or authorize treasury operations.

Bitcoin's often-cited century-scale horizon is its approximate subsidy-issuance schedule, not a forecast of adoption. Alkaest uses a century-scale horizon only as a stress-test prompt: could participants continue, safely stop, or fork the system without the founder? See the [Bitcoin schedule note](bisq-dao-and-alkaest-token.md#bitcoins-long-horizon-what-the-roughly-120-year-figure-means).

## Design requirements to carry into ADRs and RFCs

These are candidate requirements for review. They become normative only when adopted by the owning ADR or RFC.

### 1. Founder loss or unavailability

- No single person should be required to sign protocol releases, authorize ordinary treasury activity, recover project records, or nominate every successor.
- Public source, protocol data, build/release instructions, and governance records must remain exportable and independently verifiable.
- Key recovery and role replacement must rely on published thresholds, delays, and evidence rather than private founder discretion.
- Succession must not grant a successor retroactive power to rewrite valid signed history.

### 2. Key loss, theft, or compromise

- Separate keys by purpose: identity/signing, release, treasury, and emergency pause/recovery must not collapse into one all-powerful key.
- Define rotation, revocation, recovery quorum, notice, and time-lock behavior before real funds or production authority are enabled.
- Recovery actions must be publicly auditable and must not silently redirect funds or change ownership claims.
- A compromised key must not be able to enlarge its own authority or bypass independent approval.

### 3. Treasury exhaustion or capture

- Distinguish project funds, protocol reserves, operating allowances, and contributor budgets in both accounting and authorization.
- Publish policy limits for ordinary spend, reserve floors, exposure per recipient, and exceptional transfers; agents may execute only within an independently approved policy.
- Exceptional issuance, treasury-policy changes, and large transfers need separate authorization paths, public notice, delay, and independent review.
- The system must retain a safe no-token path: funded work and ordinary operation should remain possible without a transferable Alkaest asset.

### 4. Governance capture, deadlock, or low participation

- No token balance alone should grant unilateral power to appoint mediators, change issuance, seize a project treasury, or rewrite shared protocol rules.
- Separate project-local authority from shared protocol authority and define how each scope can opt in, leave, or fork.
- Specify quorum failure, abstention, conflict of interest, appeal, emergency pause expiry, and recovery from a captured or non-responsive authority set.
- A deadlock must have a bounded safe outcome: preserve the last valid rules and funds, allow a documented exit/fork, and avoid indefinite emergency powers.

### 5. Maintainer disappearance, disagreement, or malicious release

- Publish how maintainers are nominated, removed, and replaced, and require reproducible builds or independent release verification for critical binaries.
- Keep source, issue/task history, signed decisions, and release artifacts mirrored or exportable across independent operators.
- Define how users can reject an invalid release and continue using a compatible implementation without a central registry or domain.
- Upgrades that change validation or treasury behavior need versioned rules, public review, activation delays, and an explicit migration/rollback plan.

### 6. Protocol abandonment, incompatible evolution, or fork

- Users must be able to export their identities, signed history, project records, and evidence in documented formats.
- Define which records are portable, which require consent, and how privacy or deletion obligations apply when data is replicated.
- A fork must be able to establish independent governance and treasury rules without claiming authority over the original network's assets or history.
- Long-term continuity includes safe shutdown and exit, not only indefinite operation.

## Failure-injection scenarios

Before enabling real-money authority, simulate at least these cases using valueless test data and disposable keys:

1. Founder unavailable for a year; no response or signing action is possible.
2. Founder key compromised while another critical key is lost.
3. Treasury agent is malicious or its host is compromised, but its operating allowance is bounded.
4. Token holders or a guardian quorum collude to approve a self-serving policy change.
5. No quorum can be reached for routine governance or an appeal.
6. Maintainers disagree about a release; one publishes a malicious or unreproducible binary.
7. The primary repository, domain, hosting provider, and one data mirror are unavailable together.
8. A project exits or forks while a protocol-level dispute and funded WorkItems are unresolved.
9. Token issuance or market liquidity ceases, while users still need to fund maintenance and settle existing obligations.
10. A critical vulnerability requires a temporary pause, but the pause authority becomes unavailable or refuses to expire it.

For every scenario, record: who can act; what evidence is required; what funds or records are at risk; how independent nodes verify the outcome; the maximum time to recovery; and how a participant can exit if recovery fails.

## Review criteria

A design is not ready for production authority until reviewers can answer “yes” to all applicable items:

- Can ordinary operation continue without the founder and without a single privileged operator?
- Can each authority be replaced or recovered without granting it unilateral control over funds or protocol history?
- Can independent participants verify decisions from signed, portable records and a published policy version?
- Are emergency powers narrow, time-bounded, reviewable, and unable to mint or redirect funds by themselves?
- Can a project preserve its own assets and records when it leaves or forks?
- Does the system remain usable if the Alkaest token is never issued, loses liquidity, or is abandoned?
- Is safe shutdown or migration possible without the founder's private cooperation?

## Decisions still open

- What threshold and independent key-holder diversity are appropriate for recovery, release signing, and exceptional treasury actions?
- Which actions require delay and public challenge, and what maximum delays are tolerable?
- Who can activate an emergency pause, what exactly can it pause, and how does it expire if the authority is unavailable?
- What records need redundant publication, and what are the minimum independent operators for each critical artifact?
- How should continuity testing be repeated as governance, implementation, and threat assumptions change?

These questions belong in the owning ADRs/RFCs, particularly ADR-0006/0007 and RFC-0002/0014. This document is a checklist and research aid, not a substitute for those specifications.

## Recovery authority options

Recovery authority should restore or rotate a compromised authority under predeclared rules. It should not be a general-purpose treasury spending role. A person or quorum able to recover keys must not gain new power to choose payout destinations, issue assets, rewrite history, or weaken the recovery policy as part of recovery.

| Model | Example | Benefits | Main risks |
|---|---|---|---|
| Small fixed quorum | 2-of-3 guardians | Low coordination overhead; can recover after one unavailable guardian. | Two compromised or colluding guardians can act; correlated custody or social ties undermine nominal independence. |
| Larger fixed quorum | 3-of-5 guardians | Tolerates two unavailable guardians while requiring multiple approvals; practical for a small independent steward set. | Three colluding/compromised guardians can act; five long-lived key holders still create succession and coordination burden. |
| Higher threshold | 4-of-7 guardians | More approvals are needed for capture; tolerates three unavailable guardians. | Harder to coordinate; widespread loss or inactivity can permanently deadlock recovery. |
| Role-separated recovery | Separate quorums for release keys, policy changes, pause, and recovery | Limits the blast radius of one compromised group and avoids one universal “root” quorum. | More complex; overlapping membership can make separation cosmetic, and each quorum needs its own succession rules. |
| Social recovery | Named people or institutions nominate/recover a replacement after a delay | Can adapt when original key holders disappear. | Identity, coercion, collusion, and contested succession are difficult to resolve objectively; recovery can become governance by informal authority. |

### Candidate direction for Alkaest review

Carry **role-separated authority** into the next ADR review, with a fixed **3-of-5 guardian quorum** as a simulation baseline rather than an adopted threshold. The five guardians should be independent in custody and organizational control; one person or organization should not control multiple nominal seats. The recovery quorum may rotate/revoke keys and nominate replacements only through a public, delayed, challengeable event. It must not itself authorize reserve spending. Treasury transactions remain subject to the treasury's separate spending policy and keys.

For a critical compromise, a separate pause quorum may temporarily stop new allocations and routine payouts. The pause must be narrow, expire automatically, and have a public reason and recovery path. A pause cannot change key ownership or move funds. If a quorum is unavailable, the default is to retain the last valid authority and policy, block only actions that require missing authorization, and keep read/export/fork paths available.

This baseline trades the lower coordination cost of 2-of-3 for additional separation, while avoiding the operational burden of a 4-of-7 default. It is not a claim that five guardians are sufficient for all future network sizes. Before any real-money use, test it against guardian collusion, two unavailable guardians, three lost keys, a contested replacement, and an urgent security incident. Review actual independence and recovery time, not only the numeric threshold.
