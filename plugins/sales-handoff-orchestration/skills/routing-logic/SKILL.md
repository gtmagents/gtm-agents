---
name: routing-logic
description: Use when defining or adjusting marketing-to-sales assignment rules.
---

# Routing Logic Blueprint Skill

## When to Use
- Designing new lead assignment models (round-robin, territory, pod-based).
- Troubleshooting misrouted or unassigned leads.
- Simulating capacity scenarios before changing SLAs.

## Framework
1. **Qualification Criteria** – map scoring thresholds, enrichment fields, and required consent.
2. **Owner Model** – hierarchy (account owner, named AE, SDR pod), fallback logic, and tie-breakers.
3. **Capacity Modeling** – lead volume forecasts vs available headcount, backlog thresholds.
4. **Automation Flow** – MAP/CRM steps, dedupe rules, webhook/API dependencies.
5. **Monitoring & Audits** – logging, reconciliation jobs, sample QA cadence.

## Templates
- Routing matrix (segment → owner → conditions → escalation).
- Capacity calculator (leads/day vs SLA vs reps).
- QA checklist for automation updates.

## Tips
- Keep logic declarative (YAML/JSON) for easier audits and version control.
- Add synthetic leads to test every path before go-live.
- Coordinate with data enrichment to ensure required fields populate upstream.

---
