---
name: risk-scoring-framework
description: Method for calculating customer health/risk tiers using quantitative
  + qualitative data.
---

# Risk Scoring Framework Skill

## When to Use
- Building or tuning customer health scores that drive CS prioritization.
- Aligning RevOps, CS, and product on what “healthy” vs “at-risk” looks like.
- Auditing why certain segments churn or expand more than others.

## Framework
1. **Signal Inventory** – usage, sentiment, support, commercial, product feedback, exec engagement.
2. **Weighting & Decay** – assign weights per signal, set freshness decay, define negative indicators.
3. **Tier Mapping** – convert scores to tiers (green/yellow/red) with playbook hooks.
4. **Validation Loop** – back-test against churn, expansion, and NPS outcomes.
5. **Governance** – review cadence, owner accountability, and change management process.

## Templates
- Signal catalog spreadsheet with weights and owners.
- Tier thresholds + play mapping sheet.
- Validation report template comparing scores vs outcomes.

## Tips
- Combine structured data with CSM notes or sentiment highlights for context.
- Keep tiers simple (3-4) to avoid confusion; use tags for nuance.
- Pair with `monitor-customer-health` output to auto-highlight risks.

---
