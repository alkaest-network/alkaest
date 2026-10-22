# ADR-0010 — Decentralized Source and Site Hosting

**Status:** Accepted (2026-10-22): Radicle is the canonical forge; seed operation and private-repository migration remain open
**Date:** 2026-10-22
**Decision Type:** Project Infrastructure and Governance
**Related:** ADR-0006, RFC-0003 §12, RFC-0014, [Radicle seed node operations](../operations/radicle-seed-node.md), [contributor page](https://alkaest-network.org/contribute/)

## Context

Alkaest argues that work should not belong to the platform that records it, yet its code, issues, pull requests, review history, and public site currently live on GitHub. GitHub provides discovery, familiar contribution flows, and CI at no cost, but one company controls account access, repository availability, issue and review history, and the Pages host. A suspended organization or account would remove the project's public source and collaboration record at once.

Mature alternatives exist for each layer:

- **Radicle** — a peer-to-peer git forge. Repositories, issues, and patches are replicated between seed nodes and signed with participant-held keys; there is no central server. It offers a CLI, desktop client, and web view.
- **Nostr NIP-34** (`ngit`, gitworkshop.dev) — repository announcements, patches, and issues as signed Nostr events carried by relays. Younger than Radicle, but its key model matches the NIP-98 request signing already under consideration.
- **IPFS with DNSLink** — content-addressed static hosting; a `_dnslink` TXT record maps the project domain to the current content identifier, and any gateway or local node can serve it.
- **Forgejo / Codeberg** — a non-profit, self-hostable forge working toward ForgeFed federation. It reduces single-vendor ownership but remains server-based.

## Decision

1. **Publish the site from the repository, not from a platform.** The public site lives under `site/` as plain static files with no build step. It is deployed to GitHub Pages at `alkaest-network.org` now, and the same directory must remain deployable to IPFS or any static host without changes.
2. **Add IPFS + DNSLink as the second site host.** Pin each published `site/` revision and record its content identifier in the release notes, so any participant can verify and re-serve the page. Keep GitHub Pages as a fallback until gateway availability is measured.
3. **Radicle is the canonical forge; GitHub is a mirror.** The canonical repository, its signed history, its patches (Radicle's pull requests) and its issues live on Radicle. GitHub stays a read-mostly mirror for discovery and for contributors who only use GitHub. The README and CONTRIBUTING state the Radicle Repository ID (RID) and that Radicle is canonical. Nostr NIP-34 is not adopted; it may be revisited as an additional mirror.
4. **Patches and paid work run through Radicle.** Review and merge happen on Radicle patches, and a delegate merges into the canonical default branch. Paid work follows RFC-0003 and RFC-0014: a WorkItem's evidence names the Radicle RID, patch ID, reviewed revision and merged commit; payment never follows from a GitHub pull request, label or status. A pull request opened on the GitHub mirror is a proposal: a maintainer imports it as a signed Radicle patch that links back to the discussion, and only the imported patch can become paid work. GitHub issues are accepted during the transition and are copied to Radicle issues when they become WorkItems.
5. **The project runs its own seed node as a Tor onion service.** The seed replicates the canonical repository and listens as an onion service in Radicle's mixed mode, so contributors can reach it without the project depending on one hosting provider's public address. Clearnet listening remains enabled for availability. The [operations guide](../operations/radicle-seed-node.md) records the setup; its Node ID and onion address are published alongside the RID.
6. **Sign what is published.** Maintainer commits and release tags are signed with keys documented in the repository, so authorship remains verifiable independently of any host account.
7. **Keep CI replaceable.** GitHub Actions may continue to run checks, but the commands it runs must be reproducible locally and on any CI provider; no protocol artifact may depend on a GitHub-only feature.

## Open questions

- Which maintainers are repository delegates, and the delegate threshold for merging into the canonical branch.
- Who operates additional seed nodes beyond the project's own, and whether the maintainer agent from ADR-0006 may run one (it must never hold delegate rights).
- How Radicle identities (DIDs) relate to Alkaest identities, so patch authors can be matched to WorkItem assignees without trusting forge accounts.
- Which IPFS pinning arrangement avoids replacing GitHub with a different single provider.
- When the private component repositories (node, app, Brain, chatbot) follow the same model.

## Consequences

- The project's source and history can survive the loss of any one host account.
- Contributors face one more tool during the transition; the mirror and import process must keep that cost low.
- Maintainers take on patch import, seed or pin upkeep, and key management.
