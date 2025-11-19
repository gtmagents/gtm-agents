---
name: build-exec-dashboard
description: Generates executive KPI dashboard spec with governance hooks and adoption plan.
usage: /business-intelligence:build-exec-dashboard --audience elt --kpis bookings,pipeline,nrr --cadence weekly --format deck
---

# Command: build-exec-dashboard

## Inputs
- **audience** – elt | board | revenue-leadership | marketing-lead | cs-lead.
- **kpis** – comma-separated KPI list to emphasize.
- **cadence** – reporting frequency (daily, weekly, monthly, quarterly).
- **format** – deck | dashboard | memo | loom.
- **drilldowns** – optional list of dimensions to include (segment, region, product).

## Workflow
1. **Requirement Intake** – align on decisions the dashboard should drive + success metrics.
2. **KPI Blueprint** – confirm definitions, formulas, source tables, and owners.
3. **Layout Design** – arrange hero metrics, drill panels, and action callouts.
4. **Governance Layer** – document refresh cadence, QA steps, and change control.
5. **Enablement Pack** – prepare walkthrough notes, adoption plan, and automation hooks.

## Outputs
- Dashboard spec with layout, queries, filters, and data sources.
- KPI dictionary snippet for the selected metrics.
- Enablement kit (talk track, adoption checklist, Slack/email rollout plan).

## Agent/Skill Invocations
- `data-architecture-lead` – validates KPI definitions + data contracts.
- `analytics-enablement-partner` – crafts rollout + training plan.
- `dashboard-playbook` skill – enforces layout + storytelling best practices.
- `executive-kpi-briefings` skill – formats exec-ready narratives.

---
