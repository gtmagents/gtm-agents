---
name: plan-pursuit
description: Builds an enterprise pursuit plan with milestones, workstreams, and governance cadence.
usage: /enterprise-sales:plan-pursuit --deal "GlobalCo ERP" --deadline 2026-02-15 --type rfp --tier strategic
---

# Command: plan-pursuit

## Inputs
- **deal** – opportunity name/ID.
- **deadline** – final decision or submission date.
- **type** – rfp | inbound | proactive | renewal.
- **tier** – strategic | growth | scale.
- **workstreams** – optional list (value, security, legal, exec) to emphasize.

## Workflow
1. **Context Gathering** – ingest CRM summary, stakeholders, competitors, and requirements.
2. **Milestone Mapping** – outline key events (RFP due, validation, exec alignment, pricing, legal close).
3. **Workstream Assignment** – define owners, SMEs, and internal sponsors for each milestone.
4. **Governance Setup** – schedule cadences (daily standup, exec sync, risk review) and decision logs.
5. **Risk & Dependency Tracking** – capture blockers, approvals, and mitigation plans.

## Outputs
- Pursuit plan (timeline, milestones, workstreams, owners).
- Governance calendar + communication plan.
- Risk/action tracker seeded with initial items.

## Agent/Skill Invocations
- `pursuit-director` – orchestrates plan + governance.
- `value-architect` – aligns value workstream deliverables.
- `procurement-strategist` – maps legal/security dependencies.
- `pursuit-governance` skill – templates for cadence + decision logs.
- `risk-register` skill – standardized risk/action tracker.

---
