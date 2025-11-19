---
name: prioritize-keywords
description: Generates prioritized keyword clusters, intent mapping, and ownership plans.
usage: /seo-workflow-orchestration:prioritize-keywords --goal "pipeline" --regions "us,uk" --max-clusters 8
---

# Command: prioritize-keywords

## Inputs
- **goal** – business objective (pipeline, product launch, category, retention).
- **regions** – optional comma-separated locales for SERP nuance.
- **max-clusters** – numeric cap on keyword clusters returned.
- **competitors** – optional list to bias SERP/Gap analysis.
- **constraints** – optional notes (brand terms, restricted topics, resources).

## Workflow
1. **Intent Alignment** – map objectives to funnel stages + persona questions.
2. **Data Pull** – aggregate search volume, difficulty, CTR opportunity, and SERP features.
3. **Clustering** – group keywords into themes with intent, content format, and recommended owner.
4. **Prioritization** – score clusters by impact, effort, competitive gap, and timeline.
5. **Activation Plan** – outline required assets, supporting content, and measurement KPIs.

## Outputs
- Keyword cluster table (cluster, intent, volume, difficulty, priority, owner).
- Content/technical recommendations per cluster.
- Experiment backlog or refresh list tied to priority items.

## Agent/Skill Invocations
- `seo-director` – validates alignment with roadmap.
- `keyword-strategy` skill – enforces clustering + scoring methodology.
- `on-page-lead` – receives top clusters for brief development.

---
