---
name: manage-crisis
description: Generates crisis communications plan with statements, stakeholder sequencing, and monitoring tasks.
usage: /pr-communications:manage-crisis --incident "service outage" --severity high --regions "US,EU"
---

# Command: manage-crisis

## Inputs
- **incident** – short description of issue.
- **severity** – low/medium/high.
- **regions** – affected geographies.
- **audiences** – optional list (customers, partners, regulators, employees).
- **status_page** – whether status page exists (true/false).

## Workflow
1. **Triage** – capture facts, impact, known unknowns.
2. **Stakeholder Matrix** – map audiences, tone, required approval layers.
3. **Messaging Kit** – produce holding statement, FAQ, internal memo, customer email, social/status updates.
4. **Channel Sequence** – order of communications with timestamps and owners.
5. **Monitoring Plan** – sentiment listening, press tracking, escalation triggers, and post-mortem schedule.

## Outputs
- Crisis comms brief with timeline and decision tree.
- Draft statements + FAQs ready for legal review.
- Monitoring checklist + reporting template.

## Agent/Skill Invocations
- `crisis-manager` – leads response planning.
- `messaging-frameworks` skill – ensures message consistency.
- `crisis-playbooks` skill – adds templates, escalation paths, and monitoring guardrails.

---
