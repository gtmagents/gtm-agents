---
name: monitor-abm
description: Builds an ABM operations dashboard + action plan for engagement, pipeline, and experiment tracking.
usage: /abm-orchestration:monitor-abm --window 14d --kpis "engagement,pipeline" --tiers "T1,T2"
---

# Command: monitor-abm

## Inputs
- **window** – reporting cadence (7d, 14d, 30d).
- **kpis** – comma-separated metrics (engagement, meetings, pipeline, win rate, velocity).
- **tiers** – tiers to highlight.
- **experiments** – optional test IDs or hypotheses to report on.
- **alerts** – optional thresholds for notifications.

## Workflow
1. **Data Consolidation** – CRM, MAP, ads, web analytics, SDR activity, events.
2. **KPI Visualization** – build charts/tables by tier, persona, channel, play.
3. **Insight & Action** – detect drop-offs, accounts needing intervention, creative fatigue.
4. **Experiment Review** – summarize running tests, significance, next steps.
5. **Governance** – document owner assignments, follow-ups, escalation paths.

## Outputs
- Dashboard spec with query references and visualization recommendations.
- Weekly digest framework (insights, actions, blocked items).
- Alert + SLA tracker for tiered escalations.

## Agent/Skill Invocations
- `abm-analyst` – drives data synthesis.
- `signal-intel` skill – ensures intent/product signals surface in reporting.
- `account-tiering` skill – keeps metrics aligned to tier definitions.

---
