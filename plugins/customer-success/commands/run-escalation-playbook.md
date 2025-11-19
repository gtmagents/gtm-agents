---
name: run-escalation-playbook
description: Coordinates high-risk customer escalations with exec updates and remediation owners.
usage: /customer-success:run-escalation-playbook --account "Nimbus Corp" --severity critical --timeline 14d --comm-channel exec
---

# Command: run-escalation-playbook

## Inputs
- **account** – customer/account name or ID.
- **severity** – low | medium | high | critical.
- **timeline** – resolution target (7d, 14d, 30d, custom).
- **comm-channel** – exec | cs-lead | customer | internal-only.
- **drivers** – optional list of root causes to highlight (adoption, value, product, support, executive).

## Workflow
1. **Brief Creation** – compile account context, risk signals, contract info, and stakeholders.
2. **War Room & Owners** – assign workstream leads (product, eng, support, exec sponsor) with cadence.
3. **Remediation Plan** – outline milestones, dependencies, and success metrics.
4. **Communications** – generate internal/external updates, exec talking points, and approvals.
5. **Closeout & Lessons** – document outcomes, update risk registers, and refresh playbooks.

## Outputs
- Escalation brief with timeline, owners, and risk summary.
- Update templates (internal + external) with decisions and next steps.
- Post-mortem report with lessons, prevention actions, and follow-ups.

## Agent/Skill Invocations
- `escalation-strategist` – leads war room + comms.
- `customer-health-director` – tracks risk register + exec summaries.
- `executive-ebr-kit` skill – formats leadership-ready updates.
- `sentiment-feedback-loop` skill – incorporates customer sentiment + voice.

---
