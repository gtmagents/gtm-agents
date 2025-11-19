---
name: automate-delivery
description: Configures MAP/CRM automation for the approved email sequence with routing, throttling, and QA hooks.
usage: /email-sequence-orchestration:automate-delivery --sequence "Expansion Play" --platform marketo --start-date 2025-02-01
---

# Command: automate-delivery

## Inputs
- **sequence** – name or ID referencing the architecture produced by `plan-sequences`.
- **platform** – marketing automation platform or ESP (Marketo, HubSpot, Braze, Salesforce).
- **start-date** – planned launch date (YYYY-MM-DD) for scheduling.
- **throttle** – optional sends/hour or batch size.
- **approvers** – optional list of stakeholders required for sign-off.

## Workflow
1. **Pre-flight Checklist** – verify assets, personalization tokens, suppression lists, and compliance flags.
2. **Routing Logic** – configure smart lists, triggers, and branching per segment plus fallback states.
3. **QA Sandbox** – spin up test programs, send proofs, validate dynamic content + tracking links.
4. **Governance Hooks** – enable monitoring (webhooks/logging), set up pause/resume controls, document owners.
5. **Launch Plan** – publish schedule, warmup recommendations, and alert routing for real-time issues.

## Outputs
- Deployment runbook (steps, owners, environments, approvals) stored alongside automation project.
- Platform configuration checklist with screenshots/IDs for programs, flows, and assets.
- Alerting + rollback plan tied to deliverability and QA gates.

## Agent/Skill Invocations
- `marketing-ops-partner` (from lead nurture) or platform-specific ops agent for implementation support.
- `deliverability-lead` – ensures cadence + authentication alignment.
- `qa-gates` skill – enforces pre-flight checks before go-live.

---
