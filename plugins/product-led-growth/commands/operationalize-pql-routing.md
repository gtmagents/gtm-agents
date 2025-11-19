---
name: operationalize-pql-routing
description: Builds scoring, routing, and follow-up workflows for product-qualified leads.
usage: /product-led-growth:operationalize-pql-routing --segment startup --threshold 80 --destinations crm,cs --alerts true
---

# Command: operationalize-pql-routing

## Inputs
- **segment** – cohort focus (startup, scaleup, enterprise, education, region).
- **threshold** – minimum PQL/PQA score for routing.
- **destinations** – systems/teams to notify (crm, cs, marketing, product-qualified team).
- **playbook** – optional follow-up play (upsell, adoption, expansion, churn-save).
- **alerts** – true/false to include Slack/email alerts for SLA breaches.

## Workflow
1. **Signal Review** – evaluate telemetry, entitlement, and intent fields for the segment.
2. **Scoring Model** – configure scoring weights, decay rules, and enrichment mapping.
3. **Routing Map** – define ownership, queue priority, and automation triggers.
4. **Playbook Assembly** – package messaging, assets, and SLAs for each destination.
5. **Monitoring Hooks** – establish dashboards + alerts for backlog, conversion, and SLA adherence.

## Outputs
- PQL scoring + routing spec (JSON/CSV + narrative).
- Automation checklist for CRM/CS/rev tools.
- Follow-up playbook with sequences, assets, and owners.

## Agent/Skill Invocations
- `pql-ops-lead` – owns scoring design + routing automation.
- `product-adoption-strategist` – ensures messaging + enablement align to journey.
- `pql-framework` skill – standardizes scoring methodology.
- `usage-health-scorecard` skill – monitors conversion + health metrics.

---
