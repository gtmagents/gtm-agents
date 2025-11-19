---
name: monitor-revenue-health
description: Produces revenue health dashboards with leading/lagging indicators and actions.
usage: /revenue-analytics:monitor-revenue-health --window quarter --segments enterprise,midmarket --format memo
---

# Command: monitor-revenue-health

## Inputs
- **window** – time horizon (month | quarter | rolling_90 | custom).
- **segments** – comma-separated list (enterprise, midmarket, smb, channel, region).
- **metrics** – optional override for KPI set (bookings, pipeline, churn, NRR, CAC).
- **format** – dashboard | memo | briefing | csv.
- **alerts** – true/false to include guardrail breach notifications.

## Workflow
1. **Data Sync** – aggregate bookings, pipeline, retention, and leading indicator tables.
2. **Diagnostics** – run anomaly detection vs targets, YoY, and guardrail thresholds.
3. **Insight Layer** – annotate root causes, impacted teams, and decision urgency.
4. **Action Builder** – recommend plays (enablement, marketing, CS) tied to gaps.
5. **Packaging** – assemble dashboard/memo plus follow-up checklist + owners.

## Outputs
- Revenue health dashboard with KPIs, variance explanations, and drill links.
- Alert summary with guardrail status and breach details.
- Action register with owners, due dates, and playbook links.

## Agent/Skill Invocations
- `revenue-intelligence-director` – frames KPIs and narrates insights.
- `pipeline-analytics-lead` – supplies pipeline diagnostics.
- `revenue-health-dashboard` skill – standardizes visual layout + scorecards.
- `exec-briefing-kit` skill – formats leadership-ready summaries.

---
