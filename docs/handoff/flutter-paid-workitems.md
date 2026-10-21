# Draft Paid WorkItems — Flutter App

**Status:** Candidate paid tasks; not published, assigned, or funded.  
**Target repository:** [alkaest-app](https://github.com/alkaest-network/alkaest-app) (Flutter client).  
**Audience:** Flutter contributors; tasks can be offered individually so a contributor can choose a bounded scope.

These are candidate tasks for the Brain to prioritize as metrics, reports, complaints, the initial backlog, and treasury balance evolve. They are not an invitation or live bounty. Founder-set initial priorities and budget bounds inform the first decisions; the Brain decides which eligible task to open and its BTC bounty within the signed policy. The intended settlement asset is BTC through Alkaest's funded-work flow; a contributor may independently use Bisq to seek a BTC-to-fiat trade. Each task must become a protocol `WorkItem` with an exact funded BTC amount or frozen quote-to-BTC rule, source, acceptance terms, reviewer, and dates before assignment. No real payment is authorized by this draft. Until wallet, treasury, escrow, settlement, and dispute controls pass their launch gates, use simulated balances or Bitcoin `regtest` only. Alkaest must not promise fiat conversion or require a contributor to use Bisq; see [Bitcoin payouts and optional Bisq conversion](../research/bitcoin-payouts-and-bisq-conversion.md).

## Current app baseline checked

The app currently has Flutter connect mode, QR/link pairing, device-key signing through `flutter_rust_bridge`, secure device storage, Local API state refresh/stream handling, a basic spaces/WorkItem list, and generic WorkItem actions whose validity is decided by the node. Android is the documented tested target. The first task should improve this baseline rather than rebuild it.

The app architecture is set by [ADR-0005](../decisions/ADR-0005-cross-platform-app-and-deployment-modes.md): keep protocol validation and signing in Rust/`alkaest-core`, use the Local API, and treat phones as Light clients. These tasks must not reimplement protocol rules in Dart or add service/reputation capabilities before their rollout gates.

## FLUTTER-01 — Production-quality node pairing and recovery UX

**Priority:** First Flutter candidate; can proceed independently of the brand designer.  
**Current area:** `lib/ui/pair_screen.dart`, `lib/node/pairing_uri.dart`, `lib/node/device_store.dart`, and related tests.

### Scope

Make the existing scan/paste/connect flow understandable and recoverable for a non-developer pairing a phone with a self-hosted or hosted node. Preserve the existing signed pairing request and secure-storage boundaries.

### Acceptance criteria

- QR scan and pasted pairing URI both work and show the target node clearly before the user confirms pairing.
- Invalid, expired, already-used, malformed, and unreachable-node cases show actionable messages with a safe retry path.
- Camera permission denial, cancellation, slow connections, and repeated taps do not strand the screen or create duplicate pairing requests.
- Device label validation and submit/loading states are clear, keyboard/screen-reader accessible, and usable on small screens.
- Device secret, pairing code, signed headers, and full sensitive pairing URI never appear in logs, analytics, or user-visible error text.
- Successful pairing persists the device as today; a failed pairing does not persist a key as a connected node. Existing security behavior remains covered.
- Add/adjust unit and widget tests for the acceptance cases; do not change Local API or Rust protocol semantics in this task.

### Out of scope

Embedded node mode, remote discovery/relay design, changing cryptography, changing pairing-code rules, or adding account/password login.

## FLUTTER-02 — Clear WorkItem detail and action feedback

**Priority:** Second Flutter candidate; uses the existing Local API and WorkItem events.  
**Current area:** `lib/ui/home_screen.dart`, `lib/ui/texts.dart`, and Flutter widget/integration tests.

### Scope

Replace or improve the current basic WorkItem bottom sheet with a focused detail experience that helps a contributor understand the node-resolved state and available actions. The node remains authoritative: Dart may present actions but must not decide whether an event is legal.

### Acceptance criteria

- The detail view clearly shows the WorkItem title, current protocol status, version, Space, and relevant counts for applied/pending/conflicting/rejected events without presenting counts as a reputation score.
- Available actions and role selection remain driven by the current state/presentation policy; submitting an action shows progress and the exact outcome reported by the node (`applied`, `recorded`, `pending`, `conflicting`, or `rejected`).
- After a successful event, the app refreshes resolved state from the node and distinguishes “request sent/recorded” from “change applied”. It never claims a payout occurred from a PR merge, UI action, or `payout_authorized` event alone.
- Empty, loading, offline, stale, and rejected states are understandable and recoverable. No fabricated event history is shown when the Local API only provides event identifiers and aggregate state.
- Layout works on phone and wider Flutter windows; text scales, focus order, semantics, contrast, and keyboard navigation are addressed.
- Add/adjust widget tests and a node-backed integration scenario for an accepted event and a node-rejected event. Do not change node-side event authorization or protocol schemas in this task.

### Out of scope

Creating WorkItems, publishing bounties, holding funds, signing payout instructions, exposing customer chats, implementing reputation, or inventing event history that the API does not provide.

## FLUTTER-03 — Apply the professional Alkaest identity system

**Priority:** After the brand identity WorkItem delivers approved source assets and tokens.  
**Current area:** `lib/main.dart`, shared UI/theme components, pairing and home screens, and app assets.

### Scope

Implement the designer-approved visual system in Flutter, beginning with connect-mode pairing and WorkItem screens. Build reusable theme tokens and components instead of placing the identity moodboards into the UI as raster backgrounds.

### Acceptance criteria

- Flutter colors, typography, spacing, shapes, icons, and component states derive from the approved, licensed design handoff and are centralized for reuse.
- Alkaest system and Alkaest Chat marks remain distinguishable; system identity is not misrepresented as a chatbot-only app.
- Pairing, home, WorkItem detail, dialogs, errors, loading, and action states use the same system, including light/dark or other modes only if specified in the final design brief.
- Text remains legible at supported text scales, contrast is checked, non-color status cues exist, focus is visible, and reduced-motion settings are respected.
- Final editable/source assets and licenses are recorded; no unlicensed typeface, image, music, or copied board text is introduced.
- Add/adjust screenshot or widget tests for the approved key surfaces, plus existing Flutter analysis/test checks.

### Dependency

Do not start this implementation until the professional brand task has delivered approved tokens, asset files, usage rules, and rights/license terms. Do not invent a second visual direction in the app while the identity work is in progress.

## Payment and review terms required per task

Before opening any as a paid issue, publish the BTC amount or quote-to-BTC lock-in rule, funding asset, fee treatment, milestones (if any), delivery deadline, evidence required, independent reviewer, correction window, dispute path, cancellation/refund behavior, and rights/license terms. Fund every payable milestone before work on it starts. The contributor, funder, reviewer, and payout authorizer must be separately recorded; a role label does not prove that the people are independent. The recipient supplies a verified, contributor-controlled BTC destination; Alkaest never requests wallet seed words or private keys.

The three briefs are shaped to allow a contributor to select one task without taking on the entire Flutter roadmap. Start with a short portfolio/fit conversation and agree on the price and terms before assignment; record the result as a WorkItem amendment or final published version rather than leaving compensation informal.

## Architecture references

- [ADR-0005 — Cross-platform app and deployment modes](../decisions/ADR-0005-cross-platform-app-and-deployment-modes.md)
- [RFC-0009 — Node API and SDK contract](../rfc/0009-node-api-and-sdk-contract.md)
- [Flutter app README](https://github.com/alkaest-network/alkaest-app/blob/main/README.md)
- [First brand identity WorkItem](first-brand-identity-workitem.md)
