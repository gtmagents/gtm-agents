---
name: run-forecast
description: Generates revenue forecast scenarios, compares to targets, and highlights risks/opportunities.
usage: /revenue-forecasting-pipeline:run-forecast --timeframe Q1 --scenario base --confidence 0.8
---

# Command: run-forecast

## Inputs
- **timeframe** – period to forecast (Q1, Q2, FY, rolling-90).
- **scenario** – base | upside | downside | custom.
- **confidence** – numeric (0-1) to tune risk weighting.
- **drivers** – optional overrides for win rates, ASP, capacity, churn, expansion.
- **notes** – optional context for scenario assumptions.

## Workflow
1. **Input Gathering** – pull pipeline snapshot, bookings actuals, macro assumptions, and overrides.
2. **Driver Application** – adjust conversion rates, stage weightings, and coverage multipliers per scenario.
3. **Model Execution** – compute bookings forecast, ARR impact, cash flow pacing, and contribution by segment.
4. **Variance Comparison** – benchmark vs targets, prior forecast, and budget.
5. **Insights & Actions** – flag risk areas, required pipeline creation, and mitigation plays.

## Outputs
- Scenario forecast table (segment → commit/upside/downside → delta vs goal).
- Driver sheet summarizing assumptions and overrides.
- Action plan for pipeline creation or acceleration.

## Agent/Skill Invocations
- `forecast-architect` – owns methodology and interpretation.
- `forecast-modeling` skill – provides model templates + sensitivity analysis.
- `revops-analyst` – validates inputs and risk tags.

---
