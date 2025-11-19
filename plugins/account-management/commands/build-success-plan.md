---
name: build-success-plan
description: Produces a joint success plan with milestones, KPIs, stakeholders, and expansion hooks.
usage: /account-management:build-success-plan --account "Acme Corp" --horizon 2q --include-expansion true
---

# Command: build-success-plan

## Inputs
- **account** – customer/account name or ID.
- **horizon** – time window (quarter, 2q, year).
- **include-expansion** – true/false to automatically layer in upsell plays.
- **stakeholders** – optional list of customer/internal execs to highlight.
- **metrics** – optional KPIs to emphasize (time-to-value, adoption, ROI, NPS).

## Workflow
1. **Context Intake** – pull objectives, usage, sentiment, open projects, and exec notes.
2. **Milestone Drafting** – translate objectives into measurable milestones with KPIs + owners.
3. **Play Attach** – recommend adoption, expansion, or advocacy plays aligned to milestones.
4. **Governance Design** – set review cadence, communication plan, and escalation paths.
5. **Packaging** – output plan doc + QBR-ready summary.

## Outputs
- Joint success plan with objectives, milestones, KPIs, owners, timelines.
- Governance checklist (cadence, meetings, communication).
- Expansion opportunities mapped to milestones.

## Agent/Skill Invocations
- `success-planner` – facilitates design + alignment.
- `relationship-director` – ensures executive engagement and narratives.
- `account-health-analyst` – injects health metrics and signals.
- `success-planning-framework` skill – provides templates + rubric.
- `expansion-playbook` skill – surfaces upsell/cross-sell motions.

---
