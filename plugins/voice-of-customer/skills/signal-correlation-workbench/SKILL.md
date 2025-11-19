---
name: signal-correlation-workbench
description: Toolkit for linking VoC feedback with telemetry, revenue, and operational
  data.
---

# Signal Correlation Workbench Skill

## When to Use
- Quantifying the impact of qualitative feedback on churn, expansion, and adoption.
- Connecting support data, product usage, and survey responses into a unified narrative.
- Testing hypotheses about leading indicators for customer health.

## Framework
1. **Data Inventory** – list all relevant sources (surveys, NPS, CSAT, telemetry, CRM, finance).
2. **Join Strategy** – map IDs/keys, sampling windows, and normalization rules.
3. **Correlation Analysis** – evaluate relationships (Pearson/Spearman), cohort comparisons, regression snippets.
4. **Signal Strength Scoring** – combine volume, recency, severity, and revenue exposure.
5. **Insight Packaging** – translate stats into plain language, visuals, and actionable levers.

## Templates
- SQL/notebook snippets for merging VoC tags with product/CRM tables.
- Dashboard layout showing signal volume vs impact.
- Experiment tracker linking hypotheses to validated outcomes.

## Tips
- Watch for survivor bias; include lost customers when possible.
- Flag data quality caveats prominently to maintain trust.
- Pair with `synthesize-voc-insights` to auto-embed correlations into narratives.

---
