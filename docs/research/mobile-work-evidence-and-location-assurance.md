# Mobile Work Evidence and Location Assurance

**Status:** Architecture research; no location-verification mechanism adopted  
**Date:** 2026-10-19  
**Related:** ADR-0003, ADR-0007, RFC-0001, RFC-0002, RFC-0003, RFC-0006 (planned), RFC-0010 (planned), RFC-0013 (Draft)

## Purpose

Alkaest should eventually let people complete a WorkItem from a phone and submit photos, documents, and location-related evidence. Examples include a repair, delivery, inspection, installation, or other service whose completion is tied to a place. This document proposes an evidence architecture and threat model; it does not make location a protocol primitive or require location collection for ordinary work.

## Security premise: location is a claim, not a fact

A phone can sign that its app submitted coordinates and an image. The signature proves which identity submitted that payload and whether it changed afterward; it does not prove that the device was physically at those coordinates or that the image depicts the claimed work.

The W3C Geolocation specification explicitly says its API is agnostic about location sources and does not guarantee the device's actual location. Android exposes an `isMock` location signal, and Apple exposes an `isSimulatedBySoftware` source flag, but these are useful detection signals, not universal proof against a modified device, a compromised app, spoofed sensors, replay, or relayed signals. Android Play Integrity can provide app/device-environment verdicts, but those verdicts do not attest to the truth of a GPS fix and require a Google-backed service.

Therefore, Alkaest MUST NOT claim that GPS, a photo's EXIF metadata, a device signature, a map geofence, or a device-integrity verdict alone “proves” presence. It must represent the evidence source and uncertainty and allow the WorkItem policy to require independent corroboration when the stakes justify it.

Primary references:

- [W3C Geolocation specification](https://www.w3.org/TR/geolocation/) — location API sources are implementation-dependent; actual device location is not guaranteed.
- [Android `Location` API](https://developer.android.com/reference/android/location/Location) — exposes `isMock()` for locations marked as mock.
- [Apple Core Location source information](https://developer.apple.com/documentation/corelocation/cllocationsourceinformation) — exposes whether a location was simulated by software.
- [Google Play Integrity overview](https://developer.android.com/google/play/integrity/overview) — app/device integrity signals and tiered enforcement; not a location truth attestation.

## Threat model

Assume an adversary may:

- upload an old or unrelated image, edit metadata, reuse the same image across tasks, or submit a screenshot instead of a camera capture;
- set a mock location, tamper with the app or operating system, root/jailbreak the device, or supply fabricated sensor input;
- relay a challenge or beacon from a different location, clone a QR code, or collude with a witness/customer;
- replay a valid evidence bundle for another WorkItem or after its validity window;
- exploit weak GPS accuracy, indoor reception, geofence-edge ambiguity, offline clocks, or delayed uploads;
- submit genuine but misleading evidence, or refuse location permission for a legitimate privacy reason.

The design should raise the cost of fraud and make honest mistakes reviewable. It cannot establish a universal, unforgeable “proof of physical presence” on commodity phones alone.

## Evidence architecture

### 1. WorkItem declares the evidence profile

Before work begins, the WorkItem declares the evidence needed, the location precision and freshness window (if any), who can access raw evidence, retention/deletion expectations, and what happens when a signal is missing, low-confidence, or contested. A project chooses the profile based on the real risk and value of the task. Location must be optional for work that does not need it.

Suggested profiles for simulation:

| Profile | Evidence | Suitable use | Limit |
|---|---|---|---|
| A. Remote/self-reported | Contributor uploads media and optionally declares a place | Low-risk work, or tasks where location is only context | No anti-spoof assurance |
| B. Fresh mobile capture | In-app camera capture, WorkItem-specific one-time challenge, signed manifest, media digest, location sample and accuracy metadata | Ordinary onsite work where basic fraud resistance is useful | A modified device can still fabricate or relay inputs |
| C. Platform-attested capture | Profile B plus platform simulation/mock flags and an optional fresh app/device-integrity attestation bound to this WorkItem | Higher-risk tasks where supported devices/services are available | Vendor-dependent; missing attestation cannot be treated as proof of fraud or a false location |
| D. Independently corroborated | Profile B/C plus customer/recipient co-signature, independent witness, or task-specific physical checkpoint | High-value or dispute-prone work | Witnesses and checkpoints can collude, be cloned, or be relayed; needs appeal |

No profile is universally “verified.” The display should name exactly what was checked (for example, “fresh capture + recipient confirmation”), not turn multiple weak signals into an unexplained trust score.

### 2. Mobile client captures a task-bound evidence bundle

For a task that requires onsite evidence, the mobile client requests a fresh challenge from the local Alkaest node, bound to the WorkItem ID, evidence policy version, nonce, expiry, and intended evidence type. The app captures image/media and location as close together as the operating system permits, then creates a signed manifest containing:

- WorkItem ID, nonce, policy version, submitting Identity, and device-key reference;
- digest and size of the original media, capture method, and any derived preview digest;
- capture timestamp, upload timestamp, and freshness/clock-quality metadata;
- location coordinates and reported accuracy only if the task policy requires them, plus the platform's mock/simulation indicators where available;
- optional platform/app attestation bound to a digest of the challenge and submitted evidence;
- optional counterparty/witness signature over the same challenge and evidence digest.

The node verifies signatures, challenge freshness, policy version, replay status, sizes, media type, and integrity digests deterministically. It labels the source and assurance. It does not infer that a valid signature makes the location or scene true.

Where feasible, the client should capture through the app rather than selecting an arbitrary gallery image. Gallery evidence remains a valid lower-assurance path when the task permits it. Editing, compression, redaction, or thumbnail generation must create derived artifacts with their own digests; preserve the original only when policy and consent require it.

### 3. Combine independent signals by risk

Potential corroboration signals include:

- temporal plausibility: fresh nonce, short validity window, monotonic elapsed-time checks, and duplicate/replay detection;
- spatial plausibility: reported horizontal accuracy, boundary tolerance, impossible-travel checks, and consistency with other task evidence;
- platform signals: Android mock flag, Apple software-simulation flag, and optional app/device integrity verdict;
- scene evidence: task-specific visible marker or challenge phrase in the image, without exposing it publicly before capture;
- counterparty evidence: recipient/customer co-signs the same challenge and bundle digest;
- independent physical evidence: a controlled site device or access-controlled check-in, where appropriate.

Each signal has limits. A QR code or beacon can be photographed, cloned, or relayed; device attestation can raise confidence in app/device integrity but cannot prove GPS truth; IP-derived location is coarse and must never be treated as presence proof. Use multiple independently controlled sources for high-impact decisions, and provide a dispute path.

### 4. Preserve privacy and control of evidence

- Keep raw media and precise coordinates off-chain. Bitcoin anchors or public protocol logs may commit only to compact digests that do not reveal raw evidence.
- Store sensitive evidence encrypted with explicit access grants and a stated retention period. Do not put sensitive location/media in a public content-addressed store where deletion or access revocation cannot be relied upon.
- Publish only the minimum needed for the task: for example, a coarse area or a policy result rather than exact coordinates. Validators receive raw evidence only when authorized by the WorkItem policy and relevant parties.
- Treat location as potentially sensitive personal data. Obtain informed, task-specific consent, explain who can see it and for how long, and provide a location-free path when the task can be validated another way.
- A hash proves integrity against a known original; it does not make private data private, prove capture time, or prove that the content depicts the claimed event.

### 5. Handle offline capture honestly

A phone may capture while offline and sync later. The client can sign a task-bound nonce and record local wall-clock and monotonic-clock readings, but an ordinary phone cannot provide a universally trusted timestamp in this scenario. Offline submissions must disclose delayed synchronization and receive lower or different assurance unless an independent timestamp/witness exists. Do not silently treat the device clock as a trusted timestamp.

## Decision and dispute rules

- Evidence policy is frozen before funded work starts; changing it later requires a visible policy change and must not retroactively invalidate already accepted evidence.
- Missing or low-confidence location should lead to an allowed alternative, an explicit review state, or a documented rejection under the WorkItem rules—not an automatic fraud finding.
- Device attestation failure or lack of Google/Apple services must not automatically exclude a contributor unless the task's disclosed risk profile truly requires it and an accessible alternative exists.
- Automated anomaly detection may flag evidence for review but must not alone confiscate a bond, mature reputation, or decide a high-impact dispute.
- Contributors and requesters need a challenge/appeal path. A mediator sees only the minimum evidence necessary and records which sources were considered.
- Payment, location assurance, and reputation maturity remain separate decisions. Strong location evidence alone does not prove work quality; accepted work alone does not prove physical presence.

## Recommended specification path

1. Keep RFC-0001 `AttachmentRef` generic; add privacy, access-control, retention, and replication requirements in the planned data-availability/privacy specification (RFC-0010).
2. Extend RFC-0003's generic `EvidenceRecord` with a versioned, policy-selected evidence profile only when mobile/service workflows enter implementation scope. Do not make geolocation required for the development-workflow MVP.
3. Define WorkItem evidence policy, challenge binding, signature verification, replay/freshness rules, and deterministic status transitions in the applicable domain RFC.
4. Define disclosure, permission, retention, redaction, and dispute access in RFC-0010 and RFC-0013 before handling sensitive real-world location data.
5. Prototype on Android and iOS with spoofed/mock locations, modified clients, replay, offline capture, cloned QR/beacon, low accuracy, and privacy refusal. Measure false positives and accessible fallback behavior before any enforcement policy.

## Open design questions

- Which initial non-code service workflow is valuable enough to justify onsite location evidence?
- Is a task-specific QR/customer co-signature sufficient for ordinary value, or is a device-attested route required on supported platforms?
- What precision is needed: exact point, a radius/geofence result, or only a trusted counterparty confirmation?
- How long should raw media and precise coordinates remain available to the contributor, requester, and mediator?
- How should task policies avoid excluding older, de-Googled, jailbroken-for-accessibility, or offline devices when the task does not truly require attestation?
- What thresholds trigger an anomaly review, and what evidence is enough to overturn it on appeal?
