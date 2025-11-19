---
name: orchestrate-journey
description: Generates an end-to-end automation blueprint with trigger logic, steps, and measurement.
usage: /marketing-automation:orchestrate-journey --goal onboarding --persona founders --channels "email,SMS,in-app"
---

# Command: orchestrate-journey

## Inputs
- **goal** – lifecycle stage or desired outcome (onboarding, expansion, renewal, retention).
- **persona** – audience segment with shared needs.
- **channels** – comma-delimited list of active channels.
- **length** – optional number of total steps.
- **constraints** – legal, compliance, or SLA notes.

## Workflow
1. **Brief Parsing** – gather goals, KPIs, constraints.
2. **Trigger & Entry Mapping** – define events, qualification, suppression, re-entry rules.
3. **Journey Design** – outline each step with channel, content objective, personalization, fallback logic.
4. **Data/Asset Plan** – list required fields, APIs, assets, owners, and deadlines.
5. **Testing & Measurement** – propose QA plan, launch gates, dashboards, experiments.

## Outputs
- Journey diagram (mermaid) with branching logic.
- Configuration spec (JSON/YAML) for MAP/CRM systems.
- Measurement plan with KPIs, alerts, and experiment backlog.

## Agent/Skill Invocations
- `journey-architect` – drives strategy and blueprint.
- `lifecycle-mapping` skill – enforces best-practice cadence and segmentation.
- `data-orchestrator` – confirms data requirements.

---
