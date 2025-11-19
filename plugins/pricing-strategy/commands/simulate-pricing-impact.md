---
name: simulate-pricing-impact
description: Models pricing changes across cohorts, projecting ARR, margin, and adoption shifts.
usage: /pricing-strategy:simulate-pricing-impact --scenario "+10% list" --segments "growth,enterprise" --metric seats --elasticity moderate
---

# Command: simulate-pricing-impact

## Inputs
- **scenario** – description of proposed change (e.g., "+10% list", "usage tier change").
- **segments** – comma-separated segments/cohorts to model.
- **metric** – pricing driver (seats, usage, API calls, storage).
- **elasticity** – conservative | moderate | aggressive modeling assumption.
- **experiment-window** – timeframe to measure post-launch impact.

## Workflow
1. **Data Aggregation** – pull billing, usage, pipeline, and win/loss data for impacted cohorts.
2. **Elasticity Modeling** – apply elasticity assumptions, sensitivity bands, and attach-rate shifts.
3. **Scenario Simulation** – calculate ARR, margin, churn, and expansion impacts per segment.
4. **Risk & Opportunity Analysis** – highlight customer personas or regions most affected.
5. **Output Packaging** – assemble summary decks, spreadsheets, and recommendation notes.

## Outputs
- Scenario comparison table (current vs proposed) with KPIs.
- Elasticity charts + cohort breakdowns.
- Recommendation brief for pricing council.

## Agent/Skill Invocations
- `monetization-analyst` – runs modeling + analysis.
- `pricing-architect` – aligns assumptions with strategy.
- `deal-desk-partner` – surfaces field implications.
- `elasticity-lab` skill – provides modeling templates + guardrails.
- `pricing-governance` skill – logs approvals + next steps.

---
