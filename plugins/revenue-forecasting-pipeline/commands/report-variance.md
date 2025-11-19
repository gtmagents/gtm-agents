---
name: report-variance
description: Produces variance analysis, executive-ready narratives, and mitigation requests.
usage: /revenue-forecasting-pipeline:report-variance --timeframe Q1 --audience exec --window 30d
---

# Command: report-variance

## Inputs
- **timeframe** – reporting period.
- **audience** – exec | board | functional for tone/format.
- **window** – lookback window for variance drivers.
- **dimensions** – optional breakdown (segment, product, geo, channel).
- **include_actions** – boolean to append mitigation plan.

## Workflow
1. **Data Synthesis** – combine actuals, forecast, and budget targets for selected timeframe.
2. **Variance Attribution** – isolate drivers (volume, conversion, price, mix, churn) with supporting data.
3. **Narrative Building** – craft storyline, highlight risks/opportunities, and cite owner insights.
4. **Action Planning** – enumerate remediation or acceleration plays with due dates and impact estimates.
5. **Distribution** – package slides/memos plus dashboard links for audience-specific channels.

## Outputs
- Variance table (actual vs forecast/budget) with driver notes.
- Executive brief or board memo ready for delivery.
- Action tracker summarizing owners, mitigation steps, and status.

## Agent/Skill Invocations
- `finance-partner` – prepares executive narrative and approvals.
- `variance-analysis` skill – ensures methodical attribution.
- `executive-briefs` skill – formats outputs for audience expectations.

---
