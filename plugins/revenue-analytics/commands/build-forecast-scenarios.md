---
name: build-forecast-scenarios
description: Generates base/upside/downside revenue forecasts with signal-based adjustments.
usage: /revenue-analytics:build-forecast-scenarios --horizon q4 --granularity weekly --confidence 80 --include-renewals true
---

# Command: build-forecast-scenarios

## Inputs
- **horizon** – timeframe (month, quarter, fiscal_year).
- **granularity** – cadence for projections (weekly, monthly, cohort).
- **confidence** – confidence band (70/80/90) for intervals.
- **include-renewals** – true/false to layer in CS signals.
- **drivers** – optional JSON/CSV with macro/product/usage adjustments.

## Workflow
1. **Signal Intake** – collect bookings actuals, pipeline, product usage, renewal, and macro drivers.
2. **Model Calibration** – update conversion rates, seasonality factors, and growth coefficients.
3. **Scenario Generation** – produce base/upside/downside plus stress tests tied to driver toggles.
4. **Variance Commentary** – explain changes vs prior forecast and targets.
5. **Action Mapping** – recommend GTM + finance moves aligned to each scenario.

## Outputs
- Forecast workbook (base/upside/downside) with drivers and confidence bands.
- Variance memo explaining deltas vs prior outlook.
- Action register tied to scenarios (investment, enablement, hiring, demand gen).

## Agent/Skill Invocations
- `revenue-forecasting-analyst` – owns modeling + scenario analysis.
- `revenue-intelligence-director` – crafts executive narrative.
- `cohort-analysis` skill – benchmarks cohorts to validate assumptions.
- `exec-briefing-kit` skill – packages summary for leadership/board.

---
