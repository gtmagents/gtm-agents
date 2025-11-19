---
name: run-deal-health-review
description: Produces executive-ready status memo with risk register, forecast confidence, and action plan for manufacturing pursuits.
usage: /manufacturing-sales:run-deal-health-review --account "Northwind Plants" --stage negotiate --week 46 --audience "ELT"
---

# Command: run-deal-health-review

## Inputs
- **account** – pursuit/account identifier.
- **stage** – discover | validate | propose | negotiate | close.
- **week** – reporting period or calendar week.
- **audience** – exec | deal-desk | partner | delivery | mixed.
- **focus** – risk | forecast | execution | escalation (optional multi-select).

## Workflow
1. **Data Sync** – pull CRM stage, pipeline weight, partner updates, and engineering tasks.
2. **Milestone Check** – compare planned vs actual progress on technical, commercial, and legal tracks.
3. **Risk Assessment** – evaluate blockers across stakeholders, solution gaps, or procurement.
4. **Action Planning** – define mitigations, owner assignments, and escalation path.
5. **Executive Write-up** – assemble summary, KPIs, and asks tailored to audience.

## Outputs
- Deal health dashboard slide/memo with KPIs, forecast confidence, and risks.
- Risk/mitigation tracker with owners and due dates.
- Escalation packet with required decisions or resources.

## Agent/Skill Invocations
- `industrial-account-director` – authors summary + exec asks.
- `channel-integration-program-manager` – updates partner/integration readiness.
- `deal-health-dashboard` skill – provides KPI structure and visuals.
- `account-based-blueprint` skill – ensures stakeholder/context coverage.

---
