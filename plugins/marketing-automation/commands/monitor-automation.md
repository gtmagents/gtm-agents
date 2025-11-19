---
name: monitor-automation
description: Generates reporting + alerting plan to track automation health, experiment performance, and SLA compliance.
usage: /marketing-automation:monitor-automation --journey onboarding --window 14d --metrics "activation,retention"
---

# Command: monitor-automation

## Inputs
- **journey** – automation identifier.
- **window** – reporting cadence (7d, 14d, 30d, rolling).
- **metrics** – comma-separated KPIs (activation, retention, revenue, NPS, pipeline).
- **experiments** – optional list of A/B/C tests to track.

## Workflow
1. **KPI Mapping** – align goals to metrics, data sources, attribution windows.
2. **Instrumentation Audit** – confirm events/fields exist, dashboards, alerts, and experiment IDs.
3. **Insight Generation** – highlight drop-offs, bottlenecks, fatigue, list growth, deliverability, suppression trends.
4. **Action Plan** – recommend experiments, content refresh, cadence tweaks, or routing updates.
5. **Governance** – log changes in journey changelog, assign owners, set follow-up dates.

## Outputs
- Dashboard spec (Looker/Tableau/GDS) plus SQL snippets.
- Weekly digest template with insights + recommended actions.
- Alert configuration guide (Amplitude/Braze/Husky) for SLA breaches.

## Agent/Skill Invocations
- `data-orchestrator` – ensures accurate instrumentation.
- `workflow-testing` skill – sets up regression tests/alerts.
- `lifecycle-mapping` skill – contextualizes metrics by stage.

---
