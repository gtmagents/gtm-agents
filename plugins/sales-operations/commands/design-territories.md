---
name: design-territories
description: Creates territory plans, coverage rules, and communication briefs aligned to revenue targets.
usage: /sales-operations:design-territories --goal 200M --model hybrid --segments enterprise,mm --effective 2026-02-01
---

# Command: design-territories

## Inputs
- **goal** – ARR or bookings target to anchor coverage.
- **model** – geo | industry | hybrid | pod.
- **segments** – comma-separated segments/tiers.
- **effective** – go-live date for the new carve-up.
- **constraints** – optional list (named accounts, channel carve-outs, legal boundaries).

## Workflow
1. **Data Sync** – pull account universe, whitespace, current owners, attainment trends.
2. **Segmentation Logic** – bucket accounts by tier, vertical, propensity, and strategic tags.
3. **Coverage Modeling** – create multiple carve-up options with fairness/whitespace scoring.
4. **Scenario Review** – compare coverage, travel, ramp, and pipeline readiness per option.
5. **Activation Kit** – finalize assignments, ROE updates, and communication timelines.

## Outputs
- Territory maps and account assignments.
- Coverage analysis workbook with fairness metrics.
- Communication plan for CRO, field leaders, and RevOps systems teams.

## Agent/Skill Invocations
- `territory-architect` – leads modeling + governance.
- `capacity-planner` – confirms coverage vs headcount.
- `compensation-architect` – checks quota alignment.
- `territory-optimization` skill – scoring + fairness heuristics.
- `roe-governance` skill – documents rules of engagement.

---
