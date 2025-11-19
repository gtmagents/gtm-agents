---
name: launch-retention-program
description: Builds lifecycle journeys, loyalty mechanics, and measurement plan to improve repeat purchase and LTV.
usage: /e-commerce:launch-retention-program --segment lapsing --channels email,sms --objective repeat_rate --window 60d
---

# Command: launch-retention-program

## Inputs
- **segment** – lifecycle cohort (new, active, lapsing, churned, vip, subscription).
- **channels** – comma-separated list (email, sms, push, in-app, direct-mail).
- **objective** – metric to improve (repeat_rate, ltv, subscription_save, loyalty_engagement).
- **window** – timeframe for program rollout (30d, 60d, quarter).
- **offers** – optional CSV/JSON of promo constraints or loyalty incentives.

## Workflow
1. **Segment Analysis** – review purchase history, product affinity, and channel performance for the segment.
2. **Journey Design** – map messaging arcs, offers, and triggers across the selected channels.
3. **Enablement Pack** – produce creative briefs, personalization tokens, and QA requirements.
4. **Measurement Setup** – define KPIs, dashboards, and test/holdout structure.
5. **Action Tracker** – assign owners, deadlines, and follow-up cadence for launch + iteration.

## Outputs
- Lifecycle journey blueprint (touchpoints, triggers, offers, assets).
- KPI + experiment plan with dashboards/queries to monitor results.
- Execution checklist with QA steps, segmentation logic, and escalation paths.

## Agent/Skill Invocations
- `lifecycle-retention-architect` – architects journeys + measurement.
- `growth-merchandising-director` – aligns offers + inventory constraints.
- `retention-ltv-playbook` skill – enforces lifecycle structure + offer guidance.
- `conversion-diagnostic-kit` skill – validates funnel health before/after launch.

---
