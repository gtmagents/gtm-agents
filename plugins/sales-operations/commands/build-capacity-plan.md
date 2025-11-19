---
name: build-capacity-plan
description: Produces headcount, quota, and productivity scenarios mapped to revenue targets.
usage: /sales-operations:build-capacity-plan --target 220M --segment enterprise --horizon FY26 --scenarios base,upside,downside
---

# Command: build-capacity-plan

## Inputs
- **target** – bookings/ARR goal to model.
- **segment** – optional focus segment(s) (enterprise, commercial, smb, partner).
- **horizon** – time period (quarter, FY, rolling-12).
- **scenarios** – comma-separated list of scenarios to generate.
- **assumptions** – optional JSON (ramp months, win rate, ACV, attrition).

## Workflow
1. **Data Pull** – gather pipeline coverage, quota attainment, win rates, and productivity benchmarks.
2. **Assumption Alignment** – apply ramp curves, hiring plans, and attrition to each scenario.
3. **Capacity Modeling** – calculate required headcount, quota per rep, and bookings contribution by month.
4. **Risk & Sensitivity** – highlight gaps vs target, identify levers (enablement, hiring, pricing).
5. **Deliverables** – assemble summary deck and spreadsheet with pivot-ready tables.

## Outputs
- Scenario comparison table (headcount, quota, bookings, gap).
- Hiring plan + ramp schedule.
- Action recommendations for CRO/RevOps/Finance.

## Agent/Skill Invocations
- `capacity-planner` – runs modeling + analysis.
- `territory-architect` – validates coverage alignment.
- `compensation-architect` – ensures quota design fits incentive plans.
- `capacity-modeling` skill – provides calculators + formulas.
- `quota-health` skill – evaluates attainment distribution + risk.

---
