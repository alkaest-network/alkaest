# ADR-0010 — Decentralized Source and Site Hosting

**Status:** Proposed; forge choice and migration timing remain open
**Date:** 2026-10-22
**Decision Type:** Project Infrastructure and Governance
**Related:** ADR-0006, RFC-0004, [contributor page](https://alkaest-network.org/contribute/)

## Context

Alkaest argues that work should not belong to the platform that records it, yet its code, issues, pull requests, review history, and public site currently live on GitHub. GitHub provides discovery, familiar contribution flows, and CI at no cost, but one company controls account access, repository availability, issue and review history, and the Pages host. A suspended organization or account would remove the project's public source and collaboration record at once.

Mature alternatives exist for each layer:

- **Radicle** — a peer-to-peer git forge. Repositories, issues, and patches are replicated between seed nodes and signed with participant-held keys; there is no central server. It offers a CLI, desktop client, and web view.
- **Nostr NIP-34** (`ngit`, gitworkshop.dev) — repository announcements, patches, and issues as signed Nostr events carried by relays. Younger than Radicle, but its key model matches the NIP-98 request signing already under consideration.
- **IPFS with DNSLink** — content-addressed static hosting; a `_dnslink` TXT record maps the project domain to the current content identifier, and any gateway or local node can serve it.
- **Forgejo / Codeberg** — a non-profit, self-hostable forge working toward ForgeFed federation. It reduces single-vendor ownership but remains server-based.

## Proposed decision

1. **Publish the site from the repository, not from a platform.** The public site lives under `site/` as plain static files with no build step. It is deployed to GitHub Pages at `alkaest-network.org` now, and the same directory must remain deployable to IPFS or any static host without changes.
2. **Add IPFS + DNSLink as the second site host.** Pin each published `site/` revision and record its content identifier in the release notes, so any participant can verify and re-serve the page. Keep GitHub Pages as a fallback until gateway availability is measured.
3. **Make a decentralized forge canonical, with GitHub as a mirror.** Evaluate Radicle first and NIP-34 second. Once chosen, the canonical repository and its signed history live there; GitHub stays as a read-mostly mirror for discovery and for contributors who only use GitHub. The README states which copy is canonical.
4. **Accept contributions from both sides during transition.** A maintainer imports GitHub pull requests as signed patches on the canonical forge and links back to the original discussion. Issues remain on GitHub until the canonical forge's issue flow is proven with real contributors.
5. **Sign what is published.** Maintainer commits and release tags are signed with keys documented in the repository, so authorship remains verifiable independently of any host account.
6. **Keep CI replaceable.** GitHub Actions may continue to run checks, but the commands it runs must be reproducible locally and on any CI provider; no protocol artifact may depend on a GitHub-only feature.

## Open questions

- Radicle or NIP-34 as the canonical forge, judged by contributor onboarding effort, issue and review support, seed or relay availability, and fit with Alkaest identity keys.
- Who operates seed nodes or relays, and whether the maintainer agent from ADR-0006 may run one.
- Which IPFS pinning arrangement avoids replacing GitHub with a different single provider.
- When the private component repositories (node, app, Brain, chatbot) follow the same model.

## Consequences

- The project's source and history can survive the loss of any one host account.
- Contributors face one more tool during the transition; the mirror and import process must keep that cost low.
- Maintainers take on patch import, seed or pin upkeep, and key management.
