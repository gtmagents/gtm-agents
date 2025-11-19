---
name: inspect-pipeline-levers
description: Diagnoses pipeline coverage, conversion velocity, and stuck deal patterns.
usage: /revenue-analytics:inspect-pipeline-levers --stage commit --segments enterprise --window 30d --output dashboard
---

# Command: inspect-pipeline-levers

## Inputs
- **stage** – stage or grouping to inspect (create, qualify, pipeline, best-case, commit, closed).
- **segments** – persona, region, product, or team filters.
- **window** – lookback window (7d, 30d, quarter, custom).
- **metrics** – focus metrics (coverage, velocity, win_rate, asp, slip_rate).
- **output** – dashboard | memo | csv | slack.

## Workflow
1. **Data Extraction** – pull CRM pipeline tables plus enrichment fields and coach notes.
2. **Segmentation** – slice by requested segments, highlight outliers vs benchmark.
3. **Leakage & Velocity** – compute stage-to-stage conversion, cycle time, and stuck counts.
4. **Opportunity Drilldown** – flag top stuck/at-risk deals with context + next steps.
5. **Packaging & Alerts** – produce requested view plus Slack/Email summary for owners.

## Outputs
- Pipeline lever dashboard with stage conversion, velocity, and coverage deltas.
- Stuck/at-risk deal list with recommended plays.
- Summary memo highlighting root causes + action plan.

## Agent/Skill Invocations
- `pipeline-analytics-lead` – runs diagnostics + highlights at-risk segments.
- `revenue-intelligence-director` – frames executive-ready narrative.
- `deal-quality-model` skill – evaluates opportunity hygiene + win signals.
- `cohort-analysis` skill – benchmarks performance vs historical cohorts.

---
