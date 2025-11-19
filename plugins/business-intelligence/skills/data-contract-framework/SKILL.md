---
name: data-contract-framework
description: Operating model for defining, enforcing, and auditing BI data contracts.
---

# Data Contract Framework Skill

## When to Use
- Establishing ownership and SLAs for mission-critical BI tables.
- Coordinating schema changes between engineering, analytics, and RevOps.
- Auditing data reliability before major launches or executive reporting cycles.

## Framework
1. **Contract Scope** – table/view name, business purpose, consumer list.
2. **Owner Matrix** – technical owner, business owner, escalation contacts.
3. **SLA Definition** – refresh cadence, acceptable latency, data quality thresholds.
4. **Change Workflow** – approval steps, testing requirements, communication plan.
5. **Compliance & Audit** – logging, version history, and retention requirements.

## Templates
- Data contract one-pager (scope, owners, SLAs, dependencies).
- Change request form with impact assessment.
- Audit checklist for quarterly reviews.

## Tips
- Keep contracts lightweight but enforceable—link to dbt/docs for deeper detail.
- Automate SLA checks via dashboards and alerting.
- Pair with `audit-data-contracts` to prioritize fixes and highlight risk.

---
