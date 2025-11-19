---
name: assemble-war-room
description: Produces launch governance plan with tiering, workstreams, cadences, and risk controls.
usage: /product-launch-orchestration:assemble-war-room --product "AI Copilot" --tier 1 --date 2025-02-10
---

# Command: assemble-war-room

## Inputs
- **product** – launch name/identifier.
- **tier** – 1/2/3 severity.
- **date** – GA/announce date.
- **workstreams** – optional list (content, demand, enablement, success, ops, comms).
- **budget** – optional budget allocation.

## Workflow
1. **Tiering Confirmation** – validate scope, KPIs, required workstreams, governance level.
2. **Workstream Chartering** – assign leads, deliverables, milestones, dependencies.
3. **War-Room Cadence** – define standups, risk reviews, exec syncs, communication channels.
4. **Risk & Decision Logs** – create templates and owners for mitigation + decision tracking.
5. **Enablement Hooks** – ensure enablement captain + workstream leads have onboarding instructions.

## Outputs
- War-room charter (tier, goals, KPIs, stakeholders, cadence).
- Workstream RACI + timeline board outline.
- Risk/decision log templates with owners + escalation paths.

## Agent/Skill Invocations
- `launch-director` – leads governance plan.
- `workstream-lead` – confirms deliverables per function.
- `launch-tiering` skill – enforces tier criteria + budgets.

---
