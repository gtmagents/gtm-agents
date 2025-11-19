---
name: plan-bi-roadmap
description: Prioritizes BI initiatives with impact, effort, and governance alignment.
usage: /business-intelligence:plan-bi-roadmap --inputs backlog.csv --capacity 5 --themes revenue,success --audience exec
---

# Command: plan-bi-roadmap

## Inputs
- **inputs** – backlog source (csv, notion, jira board, spreadsheet).
- **capacity** – number of initiatives supportable next cycle.
- **themes** – comma-separated strategic themes (revenue, success, marketing, product).
- **audience** – exec | bi-lead | revops | async.
- **constraints** – optional notes on tooling, compliance, or dependency limits.

## Workflow
1. **Backlog Normalization** – ingest initiatives, tag by theme, align to OKRs.
2. **Scoring Engine** – calculate impact, effort, risk, and sponsor readiness.
3. **Roadmap Draft** – allocate capacity, stage workstreams, and highlight dependencies.
4. **Governance Layer** – attach owners, status checkpoints, and success metrics.
5. **Packaging** – tailor roadmap deck/memo with decisions + asks for audience.

## Outputs
- Prioritized roadmap with scoring table + swimlane view.
- Governance tracker with owners, milestones, and KPI definitions.
- Decision log capturing trade-offs and follow-up actions.

## Agent/Skill Invocations
- `insights-program-director` – orchestrates prioritization + stakeholder alignment.
- `data-architecture-lead` – validates feasibility and data contract implications.
- `metric-governance-kit` skill – ensures KPI definitions are locked.
- `dashboard-playbook` skill – provides adoption considerations for planning.

---
