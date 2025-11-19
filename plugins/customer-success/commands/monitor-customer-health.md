---
name: monitor-customer-health
description: Produces health dashboard with risk signals, opportunities, and follow-up actions.
usage: /customer-success:monitor-customer-health --segment enterprise --window 30d --audience exec
---

# Command: monitor-customer-health

## Inputs
- **segment** – cohort filter (enterprise, midmarket, startup, region, industry).
- **window** – lookback period (7d, 30d, quarter, custom).
- **accounts** – optional CSV/list of specific accounts.
- **audience** – exec | cs-lead | pod | async.
- **metrics** – override KPI set (adoption, sentiment, value, financial, support).

## Workflow
1. **Data Sync** – gather telemetry, product usage, support, NPS, and financial data aligned to the segment.
2. **Scoring & Segmentation** – apply health/risk models, tier accounts, and flag drivers.
3. **Insight Layer** – annotate root causes, expansion signals, and priorities.
4. **Action Plan** – recommend plays (adoption, value workshop, exec check-in, escalation) with owners.
5. **Packaging** – tailor dashboard/memo to the requested audience and push to Slack/email.

## Outputs
- Health dashboard with KPIs, traffic lights, and drill links.
- Risk + opportunity list with owners, severity, and recommended actions.
- Follow-up tracker template for CS pods.

## Agent/Skill Invocations
- `customer-health-director` – curates KPIs and narrative.
- `adoption-program-manager` – supplies adoption program recommendations.
- `risk-scoring-framework` skill – executes scoring + tiering.
- `sentiment-feedback-loop` skill – injects qualitative highlights.

---
