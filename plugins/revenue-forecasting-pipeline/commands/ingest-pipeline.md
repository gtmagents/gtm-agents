---
name: ingest-pipeline
description: Aggregates CRM/MAP data, cleans records, and prepares forecast-ready pipeline views.
usage: /revenue-forecasting-pipeline:ingest-pipeline --timeframe "Q1" --segments "enterprise,mm" --detail full
---

# Command: ingest-pipeline

## Inputs
- **timeframe** – forecast period (Q1, Q2, FY, rolling-90).
- **segments** – comma-separated list of segments or regions.
- **detail** – summary | full output verbosity.
- **filters** – optional stage, product, or owner filters.
- **refresh** – optional flag to force data refresh vs cached snapshot.

## Workflow
1. **Data Extraction** – pull CRM opportunities, bookings actuals, MAP signals, and enrichment fields by timeframe.
2. **Normalization & QA** – dedupe, enforce stage definitions, check close dates, align currencies, and flag missing data.
3. **Scoring & Cohorting** – compute coverage, velocity, win rate assumptions, and stage-based risk scores.
4. **Segmentation** – split pipeline by segment, region, product, partner, and channel.
5. **Packaging** – output structured tables + dashboards for forecast architect + finance partner review.

## Outputs
- Pipeline dataset (CSV/Sheets) with commit/upside/sandbag buckets.
- Data quality log detailing issues resolved or pending.
- Snapshot summary (coverage %, attainment, risk flags) per segment.

## Agent/Skill Invocations
- `revops-analyst` – runs extraction + QA steps.
- `forecast-modeling` skill – provides scoring templates and coverage math.
- `variance-analysis` skill – tags known risk cohorts for later tracking.

---
