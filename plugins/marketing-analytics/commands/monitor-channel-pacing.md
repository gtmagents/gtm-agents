---
name: monitor-channel-pacing
description: Tracks spend, performance, and guardrails across paid and owned channels.
usage: /marketing-analytics:monitor-channel-pacing --window month --channels paid_search,linkedin,display --alerts true
---

# Command: monitor-channel-pacing

## Inputs
- **window** – day | week | month | quarter | campaign.
- **channels** – comma-separated list (paid_search, paid_social, display, events, content, email).
- **budget** – optional target spend to compare pacing against.
- **alerts** – true/false to include guardrail breach alerts.
- **format** – dashboard | memo | slack.

## Workflow
1. **Spend & Performance Sync** – pull channel spend, impressions, clicks, CPL, pipeline, revenue.
2. **Normalization** – convert currencies, align attribution windows, reconcile UTMs.
3. **Guardrail Checks** – compare to CAC, CPL, payback, or custom thresholds.
4. **Optimization Signals** – flag channels/assets needing creative refresh or budget shift.
5. **Packaging & Alerts** – publish dashboard/memo and optional Slack digest for owners.

## Outputs
- Channel pacing dashboard with KPIs vs targets.
- Alert summary for guardrail breaches + recommended actions.
- Reallocation recommendations with projected impact.

## Agent/Skill Invocations
- `channel-performance-analyst` – leads pacing diagnostics.
- `marketing-intelligence-lead` – confirms priorities + narratives.
- `channel-pacing-guardrails` skill – enforces budget/efficiency thresholds.
- `roi-benchmark-library` skill – supplies benchmarks for comparison.

---
