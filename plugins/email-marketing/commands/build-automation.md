---
name: build-automation
description: Generates a marketing automation workflow with triggers, branching, waits, and success tracking.
usage: /email-marketing:build-automation --trigger "form submission" --goal nurture --touches 6
---

# Command: build-automation

## Inputs
- **trigger** – entry event (form submission, product action, scoring threshold).
- **goal** – nurture objective (education, onboarding, monetization, retention).
- **touches** – number of total emails/SMS/push steps.
- **channels** – optional cross-channel steps (email, in-app, SMS, webhooks).

## Workflow
1. **Trigger Mapping** – confirm data source, frequency caps, and mutual exclusivity.
2. **Journey Blueprint** – outline each step with wait times, conditional logic, fallback paths.
3. **Data & Personalization** – list fields, lookups, and APIs required per touch.
4. **QA Checklist** – testing matrix covering render, tracking, suppression, and compliance.
5. **Launch Plan** – assign owners, go-live date, monitoring dashboards, rollback plan.

## Outputs
- Visual workflow map (mermaid + textual summary).
- JSON/YAML ready spec for MA platforms (e.g., HubSpot, Marketo, Iterable, Braze).
- Measurement plan including alerting thresholds.

## Agent/Skill Invocations
- `automation-specialist` – converts plan into an executable workflow.
- `segmentation` skill – ensures entry/exit criteria, suppression lists, and re-entry windows.
- `ab-testing` skill – recommends experiment points within the flow.

---
