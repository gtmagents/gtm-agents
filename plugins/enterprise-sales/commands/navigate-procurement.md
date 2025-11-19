---
name: navigate-procurement
description: Coordinates legal, security, and procurement workflows with timelines, owners, and decision logs.
usage: /enterprise-sales:navigate-procurement --deal "GlobalCo ERP" --deadline 2026-03-10 --requirements "legal,security,dpia" --exceptions "payment-terms"
---

# Command: navigate-procurement

## Inputs
- **deal** – opportunity identifier.
- **deadline** – final contracting/PO date.
- **requirements** – comma-separated workstreams (legal, security, privacy, finance, vendor onboarding).
- **exceptions** – optional list of known exception requests (payment terms, data residency, SLAs).
- **collaboration-space** – optional link for deal room / project board.

## Workflow
1. **Requirement Intake** – ingest customer documents, questionnaires, policy summaries.
2. **Workback Plan** – generate timeline with deliverables, owners, and review gates per workstream.
3. **Evidence Library** – attach boilerplate docs (SOC2, penetration tests, insurance certs, product architecture).
4. **Redline Tracker** – maintain concession log, approval owners, and status.
5. **Communication Cadence** – schedule syncs, escalation checkpoints, and executive updates.

## Outputs
- Procurement/security project plan with milestones, owners, dependencies.
- Redline + exception tracker ready for deal desk/legal review.
- Evidence packet index with links + expiration dates.

## Agent/Skill Invocations
- `procurement-strategist` – orchestrates workflows + approvals.
- `pursuit-director` – ensures pursuit plan stays aligned.
- `value-architect` – provides commercial rationale for concessions.
- `procurement-playbook` skill – templates + evidence library.
- `risk-register` skill – captures risks, mitigations, and escalations.

---
