---
name: report-performance
description: Consolidates video performance metrics, diagnoses trends, and recommends optimizations.
usage: /video-marketing:report-performance --window 30d --kpis "views,watch_time,pipeline"
---

# Command: report-performance

## Inputs
- **window** – reporting timeframe (7d, 30d, quarter).
- **kpis** – comma-separated metrics (views, completion, CTR, attributed pipeline, CAC).
- **segments** – optional breakdown (persona, channel, creative concept).
- **experiments** – optional list of running tests.
- **data_sources** – optional BI queries or warehouse tables.

## Workflow
1. **Data Intake** – pull metrics from YouTube, LinkedIn, paid platforms, website analytics, CRM.
2. **Quality Checks** – ensure UTM alignment, dedupe views, normalize naming.
3. **Insight Generation** – highlight top performing videos, creative themes, hooks, and drop-offs.
4. **Optimization Plan** – recommend creative refresh, distribution adjustments, additional cuts.
5. **Action Tracking** – log owners, deadlines, expected impact.

## Outputs
- Performance summary table with deltas vs targets.
- Insight brief + prioritized recommendations.
- Experiment log updates with next tests.

## Agent/Skill Invocations
- `video-strategist` – aligns insights with strategy.
- `distribution-analytics` skill – provides measurement templates.
- `video-post-production-lead` – receives feedback for edits/localizations.

---
