---
name: diagnose-conversion-drop
description: Investigates funnel drop-offs, performance issues, and UX blockers for ecommerce sites.
usage: /e-commerce:diagnose-conversion-drop --window 14d --segments mobile,paid_social --focus checkout
---

# Command: diagnose-conversion-drop

## Inputs
- **window** – lookback window (7d, 14d, 30d, campaign).
- **segments** – comma-separated segments (device, channel, geography, campaign).
- **focus** – funnel stage (landing, pdp, cart, checkout, post-purchase).
- **include-voc** – true/false to ingest VOC/CSAT comments.
- **format** – dashboard | memo | worksheet.

## Workflow
1. **Data Aggregation** – collect analytics, attribution, heatmap, replay, and performance metrics.
2. **Segment Analysis** – compare segments vs baseline, highlight anomalies.
3. **Root Cause Mapping** – correlate issues to UX, inventory, promo, or tech factors.
4. **Experiment & Fix List** – prioritize remediations with impact/effort.
5. **Packaging** – deliver requested format with visuals and recommended owners.

## Outputs
- Funnel diagnostic report with charts/tables per stage.
- Prioritized issue + experiment backlog with severity.
- Alert summary for site performance/checkout reliability.

## Agent/Skill Invocations
- `conversion-ops-lead` – drives diagnostics + recommendations.
- `growth-merchandising-director` – reviews merchandising/promo impacts.
- `conversion-diagnostic-kit` skill – ensures structured analysis.
- `site-performance-watch` skill – layers in performance telemetry.

---
