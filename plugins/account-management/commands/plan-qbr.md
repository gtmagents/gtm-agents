---
name: plan-qbr
description: Generates an executive-ready QBR/EBR agenda with data narratives, proof points, and follow-up actions.
usage: /account-management:plan-qbr --account "Acme Corp" --tier strategic --date 2026-01-20 --theme "value realization"
---

# Command: plan-qbr

## Inputs
- **account** – required account name or ID.
- **tier** – customer tier (strategic, growth, scale).
- **date** – meeting date to anchor timeline.
- **theme** – optional focus area (value, roadmap, expansion, executive alignment).
- **attendees** – optional list of customer/internal roles.

## Workflow
1. **Signal Compilation** – pull KPIs, adoption, sentiment, roadmap updates, commitments.
2. **Narrative Structuring** – outline wins, impact, and upcoming milestones.
3. **Agenda Draft** – sequence intro, metrics, customer speakers, roadmap, decisions.
4. **Materials Prep** – assemble decks, dashboards, demo assets, FAQs.
5. **Follow-up Plan** – pre-fill action tracker, owners, and deadlines.

## Outputs
- QBR/EBR agenda with timing, speakers, objectives.
- Narrative brief (wins, KPIs, roadmap, asks).
- Action tracker template pre-populated with expected decisions.

## Agent/Skill Invocations
- `relationship-director` – curates executive messaging.
- `success-planner` – aligns agenda to success plan milestones.
- `account-health-analyst` – supplies data + insights.
- `exec-briefing` skill – ensures narrative structure + proof points.
- `expansion-playbook` skill – tags upsell motions for discussion.

---
