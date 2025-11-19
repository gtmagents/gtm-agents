---
name: optimize-performance
description: Monitor live campaign metrics, identify issues, and recommend budget/channel adjustments.
usage: /campaign-orchestration:optimize-performance --campaign "Q1 Launch" --lookback 7d
---

# Optimize Performance Command

## Purpose
Provide near-real-time performance insights plus prioritized optimization actions for active campaigns.

## Syntax
```bash
/campaign-orchestration:optimize-performance \
  --campaign "<name>" \
  --lookback 7d \
  --kpis "pipeline,sql,ctr,cpl" \
  --thresholds thresholds.json
```

### Parameters
- `--campaign`: Campaign identifier.
- `--lookback`: Window for analysis (e.g., 3d, 7d, 14d).
- `--kpis`: Metrics to monitor (pipeline, SQLs, CTR, CPL, ROAS, etc.).
- `--thresholds`: JSON config for alert thresholds or target ranges.
- `--experiments`: Optional backlog file for ICE scoring.

## Output Package
- KPI snapshot (table/graph) with pacing vs goal.
- Anomaly detection summary (channels, creatives, audiences under/overperforming).
- Recommended actions list (owner, impact, effort, deadline).
- Forecast update (expected pipeline/revenue if actions executed).

## Process
1. **Data Pull** – collect metrics from connected sources (ads, marketing automation, CRM).
2. **Pacing & Health Check** – compare actual vs plan; flag channels outside thresholds.
3. **Insights** – group findings by audience, creative, offer, channel.
4. **Recommendations** – propose reallocations, creative swaps, additional tests.
5. **Communication** – create summary for campaign manager + stakeholders.

---
