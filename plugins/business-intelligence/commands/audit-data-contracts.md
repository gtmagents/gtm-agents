---
name: audit-data-contracts
description: Reviews BI data contracts, ownership, and quality SLAs across GTM domains.
usage: /business-intelligence:audit-data-contracts --domains revenue,success --window 30d --format memo
---

# Command: audit-data-contracts

## Inputs
- **domains** – comma-separated business areas (revenue, marketing, success, product, finance).
- **window** – lookback for incidents/changes (7d, 30d, quarter).
- **owners** – optional list of data owners to highlight.
- **format** – dashboard | memo | ticket-pack.
- **severity-threshold** – warn | breach to filter issues.

## Workflow
1. **Contract Inventory** – pull registered contracts with schemas, owners, SLAs.
2. **Issue Harvest** – gather incidents, failed tests, schema changes, and backlog tickets.
3. **Compliance Review** – compare to SLAs, governance policies, and regulatory requirements.
4. **Recommendation Engine** – prioritize fixes, assign owners, and set timelines.
5. **Packaging** – produce memo/dashboard plus follow-up tasks for RevOps + engineering.

## Outputs
- Contract health report with SLA adherence and issue list.
- Remediation tracker assigning owners, due dates, and status.
- Governance summary for leadership covering risks + decisions needed.

## Agent/Skill Invocations
- `data-architecture-lead` – leads contract evaluation + remediation planning.
- `insights-program-director` – escalates systemic risks and resource asks.
- `data-contract-framework` skill – enforces documentation + SLA standards.
- `metric-governance-kit` skill – cross-checks KPI dependencies.

---
