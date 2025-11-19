---
name: launch-quantitative-survey
description: Builds, fields, and analyzes a quantitative survey with segmentation + scenario modeling.
usage: /market-research:launch-quantitative-survey --audience it,ops --sample 400 --method panel --analysis conjoint
---

# Command: launch-quantitative-survey

## Inputs
- **audience** – comma-separated personas/segments/regions (e.g., buyer, user, partner, NA, EMEA).
- **sample** – target completes (default 250).
- **method** – panel | in-product | customer-list | hybrid.
- **analysis** – preferred modeling approach (conjoint, maxdiff, segmentation, pricing, tracker).
- **constraints** – optional guardrails (privacy, incentive cap, excluded markets).

## Workflow
1. **Survey Blueprint** – translate objectives into questionnaires, branching logic, and guardrails.
2. **Panel + Quota Plan** – map sample sizes, weighting, and vendor sourcing.
3. **Programming & QA** – build survey, deploy QA scripts, confirm translations/localization if needed.
4. **Field Monitoring** – watch completes, data quality, and fraud checks; trigger mitigation if variance appears.
5. **Analysis & Reporting** – run specified models, produce dashboards, and deliver narrative plus recommendations.

## Outputs
- Survey instrument + logic map.
- Field tracker with quota progress and QA notes.
- Insight deck/notebook with stats, models, and action plan.

## Agent/Skill Invocations
- `quant-insights-architect` – designs survey + leads modeling.
- `insights-research-director` – ensures business alignment + executive packaging.
- `research-brief-blueprint` skill – keeps scope/method traceable.
- `participant-operations-hub` skill – coordinates incentives, consent, compliance.

---
