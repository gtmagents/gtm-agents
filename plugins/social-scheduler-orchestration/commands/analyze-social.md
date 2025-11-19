---
name: analyze-social
description: Reviews social calendar performance, pacing, and optimization opportunities.
usage: /social-scheduler-orchestration:analyze-social --window 14d --detail full --dimensions "channel,pillar"
---

# Command: analyze-social

## Inputs
- **window** – time horizon (7d, 14d, 30d) for data pull.
- **detail** – summary | full output detail level.
- **dimensions** – optional breakdowns (channel, pillar, region, format).
- **calendar** – optional calendar ID for scoped analysis.
- **alert_threshold** – optional KPI target to trigger escalation items.

## Workflow
1. **Data Refresh** – pull metrics from social tools, data warehouse, and web analytics with latest UTMs.
2. **Performance Breakdown** – evaluate KPIs by channel, pillar, creative format, region, and partner contributions.
3. **Pacing & Health** – inspect schedule coverage, backlog, frequency vs guardrails, and approval bottlenecks.
4. **Optimization Insights** – recommend timing shifts, asset swaps, amplification, or experiments.
5. **Action Packaging** – compile summary deck + backlog tickets for program manager + asset owners.

## Outputs
- Performance dashboard snapshot and CSV extracts by dimension.
- Alert list with root-cause notes and playbook recommendations.
- Experiment backlog updates or proposals.

## Agent/Skill Invocations
- `social-analytics-partner` – leads analysis and insight generation.
- `performance-metrics` skill – enforces KPI standards and alerting thresholds.
- `social-program-manager` – receives action plan and coordinates stakeholders.

---
