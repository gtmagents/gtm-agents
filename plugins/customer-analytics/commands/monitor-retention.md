---
name: monitor-retention
description: Builds retention dashboards, signal briefs, and recommended save plays per cohort.
usage: /customer-analytics:monitor-retention --window quarter --grouping "plan,persona" --include-expansion true
---

# Command: monitor-retention

## Inputs
- **window** – analysis window (month, quarter, rolling-90d).
- **grouping** – comma-separated dimensions (plan, persona, region, product, acquisition-channel).
- **include-expansion** – true/false to show upsell impact alongside churn.
- **signals** – optional list of metrics to emphasize (usage, support, sentiment, billing).
- **format** – dashboard | deck | brief.

## Workflow
1. **Data Refresh** – query billing, product telemetry, support, survey, and pipeline sources.
2. **Cohort Calculations** – compute retention, churn, expansion, and health indexes per grouping.
3. **Signal Detection** – surface top risk/improvement cohorts with quantified impact.
4. **Play Recommendations** – map cohorts to lifecycle or CS save plays with owners.
5. **Packaging** – produce dashboards/decks plus action trackers for leadership reviews.

## Outputs
- Retention dashboard with drillable cohorts.
- Signal brief highlighting risks/opportunities + recommended plays.
- Action tracker with owners, due dates, and success metrics.

## Agent/Skill Invocations
- `retention-analyst` – leads analytics + insights.
- `segmentation-architect` – ensures segment definitions align.
- `customer-insights-partner` – adds qualitative proof.
- `retention-dashboard` skill – provides visualization templates.
- `save-play-library` skill – links insights to remediation programs.

---
