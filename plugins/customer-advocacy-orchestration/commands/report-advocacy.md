---
name: report-advocacy
description: Summarizes advocacy program performance, asset pipeline, and reference coverage.
usage: /customer-advocacy-orchestration:report-advocacy --window 30d --detail full --audience exec
---

# Command: report-advocacy

## Inputs
- **window** – reporting range (30d, quarter, custom dates).
- **detail** – summary | full.
- **audience** – exec | sales | product | marketing for tailored narrative.
- **dimensions** – optional breakdown (region, product, persona, program type).
- **include_pipeline** – boolean to attach influenced pipeline metrics.

## Workflow
1. **Data Refresh** – pull CRM reference usage, content downloads, NPS trends, and advocacy program statuses.
2. **Coverage Analysis** – inspect reference coverage by persona/region/stage and identify gaps.
3. **Content Pipeline Review** – summarize case studies, videos, webinars in production with stage gates.
4. **Impact Attribution** – quantify influence on pipeline/revenue, deal velocity, and retention.
5. **Action Recommendations** – propose new candidates, content refreshes, or enablement updates.

## Outputs
- Advocacy dashboard snapshot with KPIs and coverage heatmap.
- Executive-ready summary deck or memo with highlights/risks.
- Follow-up task list (owner, due date, priority) for next cycle.

## Agent/Skill Invocations
- `story-producer` – updates content pipeline status.
- `reference-manager` – supplies utilization + fatigue insights.
- `reference-ops` skill – ensures data quality and logging.
- `storytelling` skill – formats narrative for chosen audience.

---
