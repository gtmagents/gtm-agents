---
name: run-pricing-council
description: Facilitates pricing council sessions with agendas, approvals, and launch actions.
usage: /pricing-strategy:run-pricing-council --agenda "Packaging refresh" --scenarios "good,better,best" --date 2025-12-05 --participants "product,finance,sales"
---

# Command: run-pricing-council

## Inputs
- **agenda** – focus topic (packaging refresh, price increase, pilot results, discount policy).
- **scenarios** – list of proposals/scenarios to review.
- **date** – council meeting date.
- **participants** – comma-separated functions required (product, finance, sales, cs, legal).
- **artifacts** – optional links to models, decks, or briefs.

## Workflow
1. **Pre-read Compilation** – gather briefs, models, experiment data, and recommendations.
2. **Agenda & Roles** – map discussion order, presenters, decision makers, scribes.
3. **Decision Framework** – document evaluation criteria, guardrails, and required approvals.
4. **Session Facilitation** – capture discussion notes, objections, action items, and decisions.
5. **Launch Plan** – outline follow-up tasks (enablement, billing updates, marketing comms) with owners/dates.

## Outputs
- Council agenda + pre-read packet.
- Decision log with approvals, blockers, and next steps.
- Launch checklist aligned to selected scenario.

## Agent/Skill Invocations
- `pricing-architect` – leads narrative and recommendations.
- `monetization-analyst` – presents data + modeling.
- `deal-desk-partner` – surfaces field implications.
- `pricing-governance` skill – maintains decision log + approvals.
- `enablement-kit` skill – outlines rollout communications + training.

---
