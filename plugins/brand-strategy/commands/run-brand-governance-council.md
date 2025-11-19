---
name: run-brand-governance-council
description: Operates brand governance council with intake, reviews, audits, and executive reporting.
usage: /brand-strategy:run-brand-governance-council --cadence monthly --scope "product + campaigns" --regions global
---

# Command: run-brand-governance-council

## Inputs
- **cadence** – weekly | biweekly | monthly | quarterly.
- **scope** – focus areas (campaigns, product, web, partner, event, enablement).
- **regions** – comma-separated regions to include for compliance + localization.
- **intake** – optional link or ID for backlog of review requests.
- **escalations** – optional notes on urgent issues or executive asks.

## Workflow
1. **Agenda & Intake Prep** – consolidate requests, metrics, escalations, and policy updates.
2. **Review & Decisions** – evaluate submissions, capture feedback, approvals, or required revisions.
3. **Audit & QA** – queue spot checks on live assets, record scorecards, flag risks.
4. **Enablement & Follow-up** – publish decision log, templates, and office hour invites.
5. **Reporting** – generate dashboards for compliance, adoption, and risk mitigation progress.

## Outputs
- Council agenda + deck with decisions, blockers, and assignments.
- Governance decision log + action tracker with owners and SLAs.
- Compliance dashboard summarizing audits, exceptions, and training progress.

## Agent/Skill Invocations
- `brand-governance-lead` – chairs the council and tracks follow-through.
- `brand-foundation-architect` – ensures requests align with core narrative.
- `brand-governance-os` skill – runs intake, approvals, and QA workflows.
- `brand-measurement-dashboard` skill – updates metrics and executive rollups.

---
