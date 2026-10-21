# Professional Tools Integration Pilot

**Status:** Research and pilot proposal; no production tool or integration has been adopted.  
**Researched:** 2026-10-19

## Purpose

Explore a small, replaceable first step toward an opt-in operating dashboard for independent professionals. The pilot should connect facts already produced by Alkaest Chatbot with accounting records the professional controls, then show useful historical reports without turning Alkaest into an accounting system.

This is a product research proposal, not a protocol requirement, implementation commitment, or accounting/tax recommendation.

## Candidate comparison

| Candidate | Fit for a solo-professional pilot | Integration and license notes | Initial assessment |
|---|---|---|---|
| [Dolibarr](https://github.com/Dolibarr/dolibarr) | Its project describes it as ERP/CRM for companies, foundations, and freelancers. Its modules include contacts, invoices, agenda, and other business functions. | GPL-3+; has an optional REST API module with HTTP/JSON and per-user API tokens. The API guide says to use SSL. | Best candidate to validate first: broad enough to hold customer/invoice facts, modular, and self-hostable. Confirm API permission granularity and deployment burden in a hands-on spike before deciding. |
| [ERPNext](https://github.com/frappe/erpnext) | Covers accounting, CRM, orders, projects, and more; likely more system than needed for the first provider. | GPL-3; REST API is provided through the Frappe framework. | Keep as a later candidate for a professional or cooperative that has outgrown a lightweight setup; do not make it the initial pilot dependency. |
| [Akaunting](https://github.com/akaunting/akaunting) | Targets small businesses and freelancers and exposes a REST API. | Its current license page describes Business Source License 1.1 and limits its production grant; it also excludes white-label and accounting-service use under that grant. | Do not embed, resell, or white-label as an Alkaest service without a separate license analysis and appropriate permission. “Open source” branding alone is not enough to establish that the intended use is allowed. |
| [Invoice Ninja](https://invoiceninja.github.io/) | Invoicing may fit a narrow need. | The project describes itself as “Free Source Available”; confirm the exact license and intended deployment rights before treating it as an open-source integration candidate. | Defer until license and workflow fit are checked. |

These are candidate assessments based on project-maintained pages, not a full security, maintenance, or legal review. A pilot must verify the exact version, license terms, API behavior, update status, backup/export, and deployment model.

## Proposed first pilot

Validate **Dolibarr as an optional, read-only finance connector** in a multitenant Alkaest product, beginning with a small cohort of independent service providers who already use Alkaest Chatbot for bookings. A single-provider demo is insufficient validation: the pilot must exercise at least two isolated tenants to prove that customer data, credentials, sync jobs, reports, exports, and deletion remain tenant-scoped. The first product question is whether connecting each provider-authorized invoice/expense ledger to that provider's appointment outcomes makes their monthly picture materially more useful.

Keep each data source authoritative for its own facts:

- Chatbot or scheduling source: booked, completed, cancelled, and missed appointments, plus service value where the provider recorded it.
- Finance tool: invoices, expenses, and payment status as maintained by the professional.
- Alkaest dashboard: derived summaries with source, period, definitions, and uncertainty visible.

The connector should begin with import/read-only access, a tenant-controlled account/token, minimal scopes and data, and an explicit disconnect/export path. If Dolibarr cannot provide sufficiently narrow read access, stop and reassess rather than use an administrator credential. Do not ingest chat transcripts, message contents, or customer details that are not needed for the report.

### Multitenancy is a launch requirement

Treat every provider/business workspace as a tenant with an explicit, authenticated tenant context. Enforce tenant isolation at every boundary: authorization, database queries, connector credentials, queues and scheduled jobs, caches, object/file storage, logs, exports, support tooling, and deletion. Never infer a tenant from an untrusted request field or trust a UI filter as the security boundary. Prevent cross-tenant joins and aggregate reporting by default.

Each tenant owns its own connector installation, external account mapping, secret, synchronization cursor, consent, retention settings, and export/disconnect lifecycle. A staff or support role must not gain broad cross-tenant access by default; exceptional support access needs a narrow purpose, explicit authorization, and an audit record. Test adversarial tenant-ID substitution and concurrent sync/report requests before onboarding real providers. Decide whether storage is shared with enforced tenant keys or physically separated per tenant based on threat model and operational constraints; either choice must provide verifiable isolation.

### First useful report

Show a period-based summary of:

- appointments booked, completed, cancelled, and missed;
- invoice amounts and payment states from the finance tool;
- expenses recorded there, if available;
- clearly separated booked value, invoiced value, and collected value;
- observed lower-demand periods as a planning aid for possible time off.

An appointment is not proof of an invoice or payment. A quiet period is a historical observation, not a promise of future demand or income. The professional makes all business decisions.

### Explicit pilot boundaries

- No automatic invoice issuance, expense entry, money movement, tax filing, tax advice, or financial guarantee.
- No consequential ranking, reputation score, work eligibility, or governance decision derived from this business data.
- No mandatory Dolibarr account; the connector remains optional and replaceable.
- No export of finance or customer records to protocol Spaces by default.
- No Alkaest copy of full accounting records when aggregate summaries and source references suffice.

## Validation gates

Before implementation, interview a small number of target professionals and confirm their current tools, bookkeeping habits, reports they actually use, consent expectations, and comfort with a self-hosted connector. Then run a technical spike with at least two test tenants and disposable Dolibarr instances to verify:

1. the smallest viable account and API permissions;
2. invoice, expense, and payment-state fields and their semantics;
3. stable record identifiers, pagination, rate behavior, and incremental sync;
4. credential storage, revocation, backup/export, and deletion behavior;
5. whether the provider can understand and reconcile every displayed total;
6. install and support burden compared with the usefulness of the report;
7. tenant isolation across API authorization, persistence, jobs, cache, logs, exports, support access, and deletion, including negative tests for cross-tenant access.

Proceed only if a provider finds the report useful, the data can be reconciled to the source, and access can be constrained and revoked. Otherwise, retain a manual CSV import or defer the integration.

## Architecture implications

Keep this feature in the product/integration layer, outside protocol core. Define an adapter boundary with normalized, provenance-bearing facts; do not make RFCs depend on Dolibarr's API or database schema. Treat external records as claims from an integration, validate sizes and types, make synchronization idempotent, and retain timestamps and source record IDs. Keep raw credentials out of logs and reports. Multitenant isolation is required in the first pilot, not a later scale-up task. Before onboarding real tenants, perform a dedicated privacy, security, data-retention, and jurisdiction review.

## Official project references

- [Dolibarr repository and project overview](https://github.com/Dolibarr/dolibarr)
- [Dolibarr REST API guide](https://github.com/Dolibarr/dolibarr/blob/develop/htdocs/api/README.md)
- [ERPNext repository](https://github.com/frappe/erpnext)
- [ERPNext open-source information](https://docs.frappe.io/erpnext/open-source)
- [Akaunting license](https://akaunting.com/license)
- [Akaunting repository](https://github.com/akaunting/akaunting)
- [Invoice Ninja project site](https://invoiceninja.github.io/)
