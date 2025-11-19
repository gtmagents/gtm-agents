---
name: run-win-loss-program
description: Manages end-to-end win/loss research including sampling, interviews, analysis, and routing.
usage: /competitive-intelligence:run-win-loss-program --segment enterprise --period quarter --sample-size 12 --audience product,sales
---

# Command: run-win-loss-program

## Inputs
- **segment** – target segment or region (enterprise, smb, strategic, apac, etc.).
- **period** – timeframe (month, quarter, half, custom).
- **sample-size** – number of deals to include (default 10).
- **audience** – comma-separated recipients (product, sales, marketing, exec, pricing).
- **focus-topics** – optional keywords (pricing, onboarding, security, support).

## Workflow
1. **Sampling & Prep** – select deals across wins/losses, ensure mix of personas/products.
2. **Interview Coordination** – schedule interviews, share discussion guide, capture consent.
3. **Analysis & Tagging** – tag qualitative insights, align with quantitative pipeline metrics.
4. **Insight Synthesis** – highlight key drivers, quotes, and recommended actions per audience.
5. **Routing & Tracking** – assign follow-ups to owners, track status, and plan next cycle.

## Outputs
- Win/loss insight report with themes, quotes, and data visualizations.
- Deal driver dashboard (e.g., pricing, product gap, competition) with trendlines.
- Follow-up tracker mapping insights to backlog items and deadlines.

## Agent/Skill Invocations
- `win-loss-analyst` – leads sampling, interviews, and analysis.
- `market-insights-director` – connects insights to strategic priorities.
- `win-loss-dataset` skill – structures qualitative/quantitative tags.
- `market-signal-tracker` skill – cross-links insights with other market signals.

---
