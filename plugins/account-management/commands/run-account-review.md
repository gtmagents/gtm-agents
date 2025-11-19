---
name: run-account-review
description: Produces a structured account review packet with health signals, risks, and expansion plays.
usage: /account-management:run-account-review --segment strategic --window quarter --include-advocacy true
---

# Command: run-account-review

## Inputs
- **segment** – filter accounts by tier/region/vertical.
- **window** – time range to analyze (month, quarter, rolling-120d).
- **include-advocacy** – true/false to highlight reference potential.
- **filters** – optional criteria (product, ARR band, health score).
- **detail** – summary | deep-dive to control report depth.

## Workflow
1. **Data Pull** – aggregate adoption, support, sentiment, commercial data, exec engagement, and commitments.
2. **Health & Opportunity Scoring** – update risk/opportunity indices plus advocacy readiness.
3. **Insight Narrative** – summarize key wins, issues, blockers, and expansion ideas per account.
4. **Action Mapping** – assign plays, owners, and deadlines (success plan updates, exec outreach, reference asks).
5. **Distribution** – generate decks/dashboards for CS leadership and account teams.

## Outputs
- Account review packet (table + narrative per account).
- Risk/opportunity tracker with recommended plays.
- Advocacy shortlist with next steps if enabled.

## Agent/Skill Invocations
- `account-health-analyst` – runs data + scoring.
- `relationship-director` – reviews exec narratives + escalations.
- `success-planner` – aligns updates to plan milestones.
- `account-health-framework` skill – scoring rubric + thresholds.
- `expansion-playbook` skill – suggests plays + advocacy ideas.

---
