---
name: plan-documentation-roadmap
description: Produces quarterly documentation roadmap with priorities, staffing, and KPIs.
usage: /technical-writing:plan-documentation-roadmap --quarter Q2 --audiences developers,admins --formats docs,video --capacity 2-writers
---

# Command: plan-documentation-roadmap

## Inputs
- **quarter** – planning period (e.g., Q1, Q2, H1, FY).
- **audiences** – comma-separated list (developers, admins, operators, sales, cs, internal).
- **formats** – docs, tutorials, video, release-notes, api-reference (comma-separated).
- **capacity** – optional headcount or bandwidth context.
- **tooling** – optional doc platform references.

## Workflow
1. **Audit & Signals** – pull analytics, support tickets, NPS themes, and stakeholder requests.
2. **Prioritization** – score opportunities by impact, urgency, and resource fit.
3. **Roadmap Draft** – map initiatives, milestones, dependencies, and staffing needs.
4. **Governance Layer** – define review cadences, localization, compliance steps.
5. **Executive Pack** – summarize KPIs, investments, and risks for approval.

## Outputs
- Roadmap doc/deck with initiatives, timelines, and owners.
- Resourcing + tooling plan with capacity notes.
- KPI tracker outlining target metrics and reporting cadence.

## Agent/Skill Invocations
- `documentation-architect` – leads audit + roadmap decisions.
- `release-documentation-manager` – highlights launch dependencies.
- `doc-requirements-matrix` skill – enforces requirement capture + scoring.
- `versioning-dashboard` skill – ties roadmap to version support lifecycle.

---
