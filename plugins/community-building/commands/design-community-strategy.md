---
name: design-community-strategy
description: Creates multi-channel community strategy with personas, programming, and KPI plan.
usage: /community-building:design-community-strategy --personas builder,leader --objectives adoption,advocacy --horizon 2q --format deck
---

# Command: design-community-strategy

## Inputs
- **personas** – comma-separated member segments (builder, admin, exec, partner, champion).
- **objectives** – adoption | advocacy | retention | research | expansion (multi-select via comma list).
- **horizon** – time window for planning (quarter, half, year).
- **format** – deck | memo | workspace.
- **constraints** – budget, tooling, or compliance notes.

## Workflow
1. **Insight Review** – pull latest product, GTM, and customer signals to anchor priorities.
2. **Persona Journey Mapping** – define value exchanges, needs, and hero moments per persona.
3. **Programming Blueprint** – outline channels, cadences, content pillars, and staffing requirements.
4. **Measurement Architecture** – map KPIs, dashboards, and attribution to business outcomes.
5. **Enablement & Governance** – document owners, councils, escalation paths, and tooling stack.

## Outputs
- Community strategy deck/memo with objectives, personas, and programming roadmap.
- KPI + instrumentation plan tied to adoption, advocacy, or revenue impact.
- Stakeholder alignment summary with decisions, risks, and next steps.

## Agent/Skill Invocations
- `community-ecosystem-strategist` – leads strategy synthesis and stakeholder management.
- `community-operations-lead` – validates operational feasibility + tooling.
- `community-program-matrix` skill – structures programming calendar.
- `community-kpi-dashboard` skill – defines measurement system.

---
