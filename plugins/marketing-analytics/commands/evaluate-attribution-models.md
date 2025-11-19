---
name: evaluate-attribution-models
description: Compares attribution models, highlights trade-offs, and recommends rollout plans.
usage: /marketing-analytics:evaluate-attribution-models --campaigns launch_q1,evergreen_abm --models first,last,position,data-driven --audience finance
---

# Command: evaluate-attribution-models

## Inputs
- **campaigns** – list of campaigns/programs to analyze.
- **models** – attribution models to compare (first, last, linear, position, time-decay, data-driven).
- **audience** – finance | marketing-lead | ops | exec.
- **metrics** – choose KPIs (pipeline, revenue, CAC, payback, LTV, ROAS).
- **confidence** – optional minimum data confidence threshold to highlight gaps.

## Workflow
1. **Data Preparation** – pull campaign performance, cost, and pipeline/revenue outcomes.
2. **Model Execution** – run requested models, normalize windows, and apply weighting rules.
3. **Sensitivity Analysis** – compare outcomes vs benchmarks, highlight variance drivers.
4. **Narrative Assembly** – contextualize trade-offs, governance considerations, and risks.
5. **Recommendation Engine** – propose primary model, fallback, and rollout/QA checklist.

## Outputs
- Attribution comparison deck/table with KPI deltas per model.
- Recommendation memo with decision, rationale, and risk mitigations.
- Rollout plan including QA steps, owner assignments, and monitoring hooks.

## Agent/Skill Invocations
- `attribution-architect` – leads methodology comparison.
- `marketing-intelligence-lead` – ensures narrative + stakeholder alignment.
- `attribution-playbook` skill – documents rules + templates.
- `exec-dashboard-blueprint` skill – packages executive summary.

---
