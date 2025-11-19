---
name: analyze-enrollment-funnel
description: Audits inquiry → enrollment funnel to surface channel gaps, yield risks, and experiments.
usage: /edtech-growth:analyze-enrollment-funnel --program "STEM Bootcamp" --audience "working-professionals" --window 90d --detail full
---

# Command: analyze-enrollment-funnel

## Inputs
- **program** – program, cohort, or product line.
- **audience** – k12 | higher-ed | workforce | corporate | mixed (optional custom string).
- **window** – analysis lookback (30d | 60d | 90d | custom).
- **detail** – summary | standard | full.
- **data-links** – optional CSV/URL for funnel metrics or CRM exports.

## Workflow
1. **Data Aggregation** – pull inquiries, apps started, apps completed, admits, enrollments.
2. **Segmentation** – slice by channel, geography, persona, or program format.
3. **Benchmarking** – compare conversion rates vs internal targets and industry references.
4. **Root Cause + Experiment Map** – flag drop-off points, capacity issues, and prioritized tests.
5. **Executive Readout** – package insights, recommendations, and success metrics.

## Outputs
- Funnel diagnostic report with charts, conversion deltas, and forecast impact.
- Experiment backlog prioritized by velocity x impact.
- Data QA + instrumentation checklist for RevOps.

## Agent/Skill Invocations
- `enrollment-growth-strategist` – leads analysis and recommendations.
- `student-success-program-manager` – highlights downstream retention implications.
- `enrollment-persona-playbook` skill – ensures persona/SKU segmentation structure.
- `student-success-scorecard` skill – aligns KPIs to lifecycle outcomes.

---
