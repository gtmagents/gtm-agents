---
name: assess-performance
description: Consolidates paid channel metrics, diagnoses issues, and recommends optimizations.
usage: /paid-media:assess-performance --window 14d --channels "LinkedIn,Meta,Google" --kpis "cpl,pipeline"
---

# Command: assess-performance

## Inputs
- **window** – reporting range (7d, 14d, 30d, custom).
- **channels** – comma-separated list of platforms.
- **kpis** – e.g., cpl, cac, roi, pipeline, ltv.
- **benchmarks** – optional JSON of target metrics.
- **experiments** – optional list of running tests.

## Workflow
1. **Data Aggregation** – pull spend, delivery, conversion data from named channels + warehouse; normalize naming convention.
2. **Quality Checks** – confirm attribution windows, conversion dedupe, budget pacing.
3. **Insight Generation** – highlight drivers (audience, creative, placement) and anomalies.
4. **Optimization Plan** – propose budget shifts, bid/budget tweaks, creative refreshes, or experiment priorities.
5. **Communication** – craft TL;DR + recommended actions for stakeholders.

## Outputs
- Performance summary table + narrative insights.
- Action plan with owners, deadlines, projected impact.
- Updated experiment log with status and next steps.

## Agent/Skill Invocations
- `performance-analyst` – analyzes data and crafts insights.
- `budget-optimization` skill – ensures rational reallocations.
- `campaign-architecture` skill – checks funnel/touch coverage before changes.

---
