---
name: forecast-coverage
description: Calculates required pipeline coverage vs targets and highlights gaps by segment.
usage: /sales-pipeline:forecast-coverage --goal 5000000 --segment enterprise --period Q1
---

# Command: forecast-coverage

## Inputs
- **goal** – bookings target for the selected period (number).
- **segment** – optional segment/product/region filter.
- **period** – fiscal period label (Q1, H2, Month-1).
- **confidence** – default 3x coverage multiplier (override as needed).
- **include-scenarios** – true/false to add upside/downside modeling.

## Workflow
1. **Target Alignment** – pull quota data (goal, attainment to date, remaining gap).
2. **Pipeline Snapshot** – aggregate open opportunities by stage, ARR, and probability.
3. **Coverage Modeling** – calculate pipeline/goal ratios under base, stretch, conservative assumptions.
4. **Gap Analysis** – identify teams/segments below threshold and quantify required net-new pipeline.
5. **Recommendations** – map gaps to GTM plays (marketing campaigns, partner sourcing, AE blitz).

## Outputs
- Coverage dashboard with ratios per team/segment.
- Gap table listing required additional pipeline by stage.
- Scenario summary showing best/base/worst coverage outcomes.

## Agent/Skill Invocations
- `pipeline-director` – supplies targets + coverage thresholds.
- `pipeline-analyst` – runs modeling + scenarios.
- `forecast-coach` – drives action plans with frontline leaders.
- `forecast-discipline` skill – enforces consistent coverage methodology.

---
