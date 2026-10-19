# Contributing to Alkaest

Alkaest is an early-stage, protocol-first project exploring how people can coordinate work through local nodes, cryptographic identities, verifiable evidence, and portable reputation. We welcome careful contributions that make the protocol clearer, safer, and more useful.

**Start here:** [Project overview](README.md) · [Roadmap](docs/overview/roadmap.md) · [Contribution guide](CONTRIBUTING.md)

Browse [open issues](https://github.com/alkaest-network/alkaest/issues) or [open a new issue](https://github.com/alkaest-network/alkaest/issues/new/choose) in the public protocol repository.

## Choose a repository

This repository is the public home for protocol specifications, decisions, research, and planning. It does not contain the Rust node, Flutter app, Brain, agent toolkit, or chatbot implementation.

| Area | Repository | Contribution notes |
|---|---|---|
| Protocol, RFCs, ADRs, research, and documentation | [alkaest](https://github.com/alkaest-network/alkaest) | Public. Documentation changes can be proposed directly here; no build setup is required. |
| Agent definitions and reusable development guides | [alkaest-ai](https://github.com/alkaest-network/alkaest-ai) | Public repository. Its `main` branch has no `LICENSE` file as of 2026-10-19; clarify licensing before contributing or reusing material. |
| Rust node and protocol core | [alkaest-node](https://github.com/alkaest-network/alkaest-node) | Private repository; request access from a maintainer. Includes an MIT `LICENSE`. |
| Flutter app | [alkaest-app](https://github.com/alkaest-network/alkaest-app) | Private repository; request access from a maintainer. No top-level `LICENSE` is present; clarify licensing before contributing or reusing code. |
| Treasury Brain | [alkaest-brain](https://github.com/alkaest-network/alkaest-brain) | Private repository; request access from a maintainer. Includes an MIT `LICENSE`. |
| WhatsApp scheduling product | [alkaest-chatbot](https://github.com/alkaest-network/alkaest-chatbot) | Private repository; request access from a maintainer. No top-level `LICENSE` is present; clarify licensing before contributing or reusing code. |

Repository visibility and access can change. The app, node, Brain, and chatbot repositories are private, so access is by invitation from a maintainer. Do not post credentials or private repository content here. The protocol specifications remain the public place to raise design questions and propose cross-project changes.

Each repository has its own license. Do not assume this repository's MIT license applies to companion projects. As of 2026-10-19, `alkaest-ai`, `alkaest-app`, and `alkaest-chatbot` have no top-level license file; clarify licensing before contributing to or reusing those projects.

## Good first contributions

You can contribute to the protocol repository without access to a private component or a paid-work pilot. Useful first changes include:

- point to one RFC rule that is ambiguous and give a concrete event sequence that exposes the ambiguity;
- cross-check one related RFC/ADR pair and report a specific contradiction with section links;
- improve a glossary entry, navigation link, or explanation without changing the underlying protocol rule;
- review an issue or pull request and state which assumptions you checked.

The [roadmap](docs/overview/roadmap.md) is a dependency plan, not a list of approved bounties. No contribution is promised payment, and no real-money protocol operation is enabled.

## What is open for contribution

The public work in this repository is protocol specifications, architecture decisions, research, and planning. Other Alkaest components may have separate access and contribution requirements; confirm those with a maintainer before assuming a repository is available or a component is production-ready.

Useful contributions include:

- finding ambiguity, contradictions, missing cases, or security assumptions in an RFC
- proposing well-scoped protocol improvements and documentation changes in this repository
- improving accessibility, localization, privacy, and operational clarity in the public documentation
- reporting reproducible bugs and asking focused questions

The protocol is not tied to GitHub. GitHub is a collaboration and integration surface, not the source of protocol truth.

## Before you start

1. Read the [project overview](README.md) and [vision](docs/overview/vision.md).
2. Check the [roadmap](docs/overview/roadmap.md), current [handoff notes](docs/handoff/current-state.md), and open issues for existing work.
3. For a substantial change, open an issue first and describe the problem, proposed scope, and affected RFCs or components. This helps us agree on direction before you invest in implementation. Use the [issue tracker](https://github.com/alkaest-network/alkaest/issues) and check for an existing discussion.
4. For a small documentation fix or clearly scoped bug in this repository, a pull request is welcome directly.

Please distinguish current MVP requirements from future architecture. Do not present an exploratory idea as a settled protocol rule.

## How to contribute

1. Fork the relevant repository and create a focused branch.
2. Keep changes small enough to review. Explain the problem and why the proposed change addresses it.
3. Follow the local `AGENTS.md`, README, and component-specific instructions. They take precedence for that component's workflow.
4. When changing protocol behavior, update the relevant RFC and terminology. Record a durable architectural choice as an ADR.
5. Include tests for implementation changes, following the component's test-first workflow. Documentation-only changes do not need tests.
6. Open a pull request with context, important trade-offs, and the checks you ran. Link related issues and RFC sections.
7. Stay available for questions and revise the proposal when review finds a correctness or clarity issue.

For stacked changes, base a new branch on an earlier contribution only when the dependency is explicit in the pull request. Otherwise, branch from the repository's default branch so maintainers can review and merge each change independently.

### Documentation-only changes

No language runtime or package installation is needed to edit this repository's Markdown documents. Keep links relative, use English for specifications, preserve the RFC's maturity label, and update the documentation index or handoff pages when the change affects priorities or current state. Before opening a pull request, run `git diff --check` and inspect the rendered Markdown links you changed. There is no automated documentation build configured yet.

For implementation work, follow the commands and prerequisites in the selected component repository. Do not assume a passing documentation review is a substitute for that component's tests.

## Design principles

- Keep the protocol generic; workflow-specific behavior belongs in modules.
- Preserve user control over identities, nodes, and local data.
- Prefer verifiable evidence over platform-owned scores or unsupported claims.
- Treat external platforms as integrations, not authorities.
- Make node profiles work for different devices and capabilities; do not assume every participant runs a powerful always-on machine.
- Specify security and trust assumptions instead of hiding them behind implementation details.
- Use stable protocol terms such as `Identity`, `Space`, `Membership`, `Object`, `Event`, `Relation`, `Message`, `Decision`, `Envelope`, `WorkItem`, and `Evidence`.

## Pull request checklist

- [ ] The change has a clear scope and explains its motivation.
- [ ] Relevant RFCs, ADRs, docs, or component instructions are updated.
- [ ] Protocol changes preserve the boundary between core and workflow modules.
- [ ] Implementation changes include appropriate tests, run before opening the PR.
- [ ] No secrets, private data, or unrelated formatting changes are included.
- [ ] Remaining questions and known limitations are stated plainly.

## Review and decision-making

Contributions are proposals until reviewed and merged. A pull request may need revision, more discussion, or a decision to defer it. For protocol changes, correctness, clarity, security, and compatibility matter more than the size of the patch. A maintainer may ask for an RFC or ADR update before implementation proceeds.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md). Be respectful and specific in review. Critique the proposal and its effects, not the person. If a contribution is outside the current scope, we will try to explain why and point to a useful next step.

## Current limitations

Alkaest is early-stage. Some architecture and economic mechanisms remain open questions, and the network is not yet a mature production system. Do not rely on proposed reputation, settlement, or funding flows as operational guarantees. Review the relevant RFC and ADR status before building on them.

Security concerns should not be posted with exploit details in public issues. Follow [SECURITY.md](SECURITY.md) for the private reporting route; the RFC review form accepts design-level threat analysis only.

## License

By submitting a contribution, you agree that it may be distributed under the license in the relevant repository. Please do not submit material you do not have the right to contribute. See the repository's [LICENSE](LICENSE) for the applicable terms.

## Thank you

Every precise question, careful review, bug report, and well-scoped patch helps turn Alkaest from an idea into a protocol people can inspect and use. Thank you for helping build it in the open.
