---
name: test-and-report
description: Creates a copy experimentation plan with reporting template and action items.
usage: /copywriting:test-and-report --channels "email,ads" --kpis "ctr,conversion" --window 14d
---

# Command: test-and-report

## Inputs
- **channels** – channels under test.
- **kpis** – comma-separated metrics (open, CTR, CVR, CPL, pipeline).
- **window** – reporting cadence (7d, 14d, 30d).
- **variants** – optional list of existing tests.
- **segments** – optional persona/region tiers.

## Workflow
1. **Test Inventory** – list active/pending copy tests per channel.
2. **Hypothesis Framework** – define hypothesis, expected impact, measurement plan.
3. **Sample Size & Duration** – estimate recipient volume/time to significance.
4. **Reporting Template** – specify dashboards, data sources, significance tests.
5. **Action Plan** – document recommended actions based on results.

## Outputs
- Experiment tracker table (test, hypothesis, status, KPI, owner).
- Reporting template (charts/tables, significance calculations, insights).
- Action item list with owners and deadlines.

## Agent/Skill Invocations
- `copy-strategist` – prioritizes experiments.
- `offer-testing` skill – provides test design and statistical guardrails.
- `voice-editor` – confirms brand implications of winning variants.

---
