---
name: produce-campaign-report
description: Generates cross-channel campaign performance report with insights and recommendations.
usage: /marketing-analytics:produce-campaign-report --campaign "Spring Launch" --window 30d --audience exec
---

# Command: produce-campaign-report

## Inputs
- **campaign** – campaign/program identifier (matches MAP/CRM naming).
- **window** – analysis window (7d, 30d, campaign, custom).
- **audience** – exec | marketing-lead | channel-owner | async.
- **metrics** – optional override list for KPIs to highlight.
- **format** – deck | memo | dashboard | csv.

## Workflow
1. **Data Assembly** – join paid, owned, and earned channel data with CRM pipeline/revenue fields.
2. **Attribution Layer** – apply default or requested model, annotate confidence and limitations.
3. **Performance Story** – highlight wins, underperformance, and causal insights.
4. **Action Plan** – recommend optimizations, tests, or budget shifts per channel/asset.
5. **Packaging** – tailor to audience with visuals, narrative, and calls-to-action.

## Outputs
- Campaign performance package (deck/memo/dashboard) with KPIs, insights, and actions.
- Attribution summary with model notes and sensitivity ranges.
- Optimization plan with owners, due dates, and expected impact.

## Agent/Skill Invocations
- `marketing-intelligence-lead` – frames narrative + executive summary.
- `channel-performance-analyst` – provides channel diagnostics and pacing alerts.
- `attribution-architect` – validates attribution logic and caveats.
- `attribution-playbook` skill – enforces methodology templates.
- `exec-dashboard-blueprint` skill – packages outputs for leadership reviews.

---
