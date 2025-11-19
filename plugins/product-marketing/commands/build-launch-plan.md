---
name: build-launch-plan
description: Produces a coordinated launch plan covering workstreams, assets, and KPIs.
usage: /product-marketing:build-launch-plan --product "AI copilot" --tier 1 --date 2025-02-10
---

# Command: build-launch-plan

## Inputs
- **product** – name/feature being launched.
- **tier** – 1, 2, or 3 to size scope/budget.
- **date** – target GA or announcement date.
- **segments** – optional audiences or verticals.
- **dependencies** – optional list (feature flag, pricing, compliance, etc.).

## Workflow
1. **Launch Tiering** – confirm objectives, KPIs, and resource expectations.
2. **Workstream Mapping** – content, demand, enablement, success, comms, product readiness.
3. **Timeline** – backwards schedule with key milestones and checkpoints.
4. **Asset Checklist** – required collateral, demos, training, automation, tracking.
5. **Measurement** – define KPIs, instrumentation, reporting cadence, experiment ideas.

## Outputs
- Launch plan board/table (workstream, owner, deliverables, status).
- KPI framework + dashboard spec.
- Risk log with mitigations.

## Agent/Skill Invocations
- `launch-strategist` – oversees plan + governance.
- `launch-plays` skill – provides playbook templates by tier.
- `data-orchestrator` (cross-plugin) – ensures instrumentation readiness optional.

---
