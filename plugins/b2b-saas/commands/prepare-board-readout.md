---
name: prepare-board-readout
description: Packages GTM + product metrics into a board-ready SaaS narrative with asks.
usage: /b2b-saas:prepare-board-readout --window quarter --themes growth,retention --format deck
---

# Command: prepare-board-readout

## Inputs
- **window** – timeframe (quarter, half, year, custom).
- **themes** – comma-separated focus areas (growth, retention, product, efficiency, roadmap).
- **format** – deck | memo | dashboard | loom.
- **audience** – board | exec | investors | async.
- **alerts** – optional boolean to include risk/mitigation appendix.

## Workflow
1. **Metric Selection** – pull KPIs tied to selected themes (ARR, NRR, CAC payback, product usage, roadmap velocity).
2. **Narrative Draft** – structure storyline (headline, driver analysis, customer proof, asks).
3. **Evidence Layer** – insert telemetry charts, customer anecdotes, competitive insights.
4. **Action & Ask** – outline decisions needed, funding requests, or roadmap trade-offs.
5. **Packaging** – format deck/memo plus appendix tags for deep dives.

## Outputs
- Board-ready briefing with KPIs, narrative, and action requests.
- Appendix library (charts, customer stories, competitive intel).
- Decision log + follow-up tracker for leadership.

## Agent/Skill Invocations
- `value-ops-lead` – curates KPI story and ROI proof.
- `industry-strategist` – aligns narrative to vertical/customer trends.
- `board-readiness-kit` skill – enforces structure and action log format.
- `usage-to-value-map` skill – injects telemetry + customer proof.

---
