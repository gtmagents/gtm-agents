---
name: activate-program
description: Converts advocacy candidates into live programs with approvals, incentives, and scheduling.
usage: /customer-advocacy-orchestration:activate-program --program "Q1 Reference Sprint" --type references --timeline 45d
---

# Command: activate-program

## Inputs
- **program** – name or identifier for the advocacy initiative.
- **type** – program category (references, case-study, council, community spotlight).
- **timeline** – duration or due date for activation.
- **owners** – optional comma-separated team owners.
- **incentives** – optional description of rewards/benefits to manage.

## Workflow
1. **Brief Assembly** – pull candidate roster, goals, and compliance requirements.
2. **Outreach Planner** – assign owners, craft outreach scripts, and log CRM tasks for each advocate.
3. **Consent & Legal** – trigger approvals, NDAs, release forms, and references to brand/legal guidelines.
4. **Enablement Package** – generate briefing docs, talking points, and content requirements.
5. **Tracking & Handoff** – update advocacy dashboards, tag opportunities, and notify downstream teams (sales, PMM).

## Outputs
- Program activation checklist with task owners and due dates.
- Outreach tracker (advocate, status, next action, incentive).
- Compliance packet with signed releases and approvals.

## Agent/Skill Invocations
- `reference-manager` – manages scheduling and fulfillment.
- `advocacy-strategist` – ensures overall roadmap alignment.
- `reference-ops` skill – enforces data/logging standards.
- `advocate-sourcing` skill – updates candidate status post outreach.

---
