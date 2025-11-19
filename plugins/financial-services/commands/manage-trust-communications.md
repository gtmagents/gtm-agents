---
name: manage-trust-communications
description: Produces messaging, FAQs, and escalation workflow for financial incident or policy change communications.
usage: /financial-services:manage-trust-communications --scenario "Rate Increase" --audience retail --channels email,in-app,support --sla 48h
---

# Command: manage-trust-communications

## Inputs
- **scenario** – trigger description (rate change, outage, compliance update, incident).
- **audience** – retail | smb | enterprise | investor | partner.
- **channels** – email, in-app, push, support, field, PR (comma-separated).
- **sla** – response timeframe (24h, 48h, 72h, custom).
- **severity** – info | warning | critical.

## Workflow
1. **Context Gathering** – capture scenario details, impacted products, regulators, and stakeholders.
2. **Message Architecture** – craft headline, supporting details, disclosures, and CTAs per audience.
3. **Approval Workflow** – route to legal, risk, and exec sponsors with tasks/SLA tracking.
4. **Distribution Plan** – map channels, sequencing, assets, and owner handoffs.
5. **Monitoring & Follow-up** – define sentiment KPIs, escalation triggers, and post-mortem tasks.

## Outputs
- Communications brief with messaging, disclosures, and channel plan.
- FAQ + support script pack with escalation guidance.
- Trust KPI tracker with sentiment metrics and follow-up actions.

## Agent/Skill Invocations
- `trust-communications-lead` – authors messaging + coordinates distribution.
- `trust-compliance-director` – validates disclosures + regulator requirements.
- `regulator-briefing-playbook` skill – formats updates for legal/regulatory stakeholders.
- `customer-trust-dashboard` skill – establishes monitoring + reporting structure.

---
