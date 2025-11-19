---
name: audit-pipeline
description: Inspects stage coverage, hygiene, and forecast alignment to produce recommended actions.
usage: /sales-pipeline:audit-pipeline --segment enterprise --period Q1 --detail full
---

# Command: audit-pipeline

## Inputs
- **segment** – optional filter (enterprise, midmarket, smb) to focus the audit.
- **period** – current quarter/month to evaluate.
- **detail** – summary | full to control output depth.
- **owners** – optional rep/manager list to spotlight.
- **include-forecast** – true/false to add commit/best-case analysis.

## Workflow
1. **Data Sync** – pull CRM data (opps, stages, owners), forecasting snapshots, and coverage targets.
2. **Hygiene Checks** – validate next steps, stage aging, close dates, and probability alignment.
3. **Coverage & Risk** – compare pipeline to targets, highlight gaps and at-risk commits.
4. **Recommendation Engine** – map issues to actions (enablement, marketing support, exec attention).
5. **Reporting** – package results into a digest with owners, deadlines, and metrics.

## Outputs
- Stage-by-stage health report with key metrics.
- Risk + opportunity list with recommended action owners.
- Forecast variance summary if `include-forecast=true`.

## Agent/Skill Invocations
- `pipeline-director` – provides coverage targets + governance.
- `pipeline-analyst` – executes diagnostics and variance analysis.
- `forecast-coach` – recommends inspection cadences and enablement.
- `pipeline-ops` skill – ensures CRM hygiene standards are applied.

---
