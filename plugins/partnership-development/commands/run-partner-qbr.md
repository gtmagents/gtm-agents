---
name: run-partner-qbr
description: Produces partner QBR/EBR packet with pipeline, GTM programs, and action items.
usage: /partnership-development:run-partner-qbr --partner "Nimbus AI" --window quarter --audience exec --format deck
---

# Command: run-partner-qbr

## Inputs
- **partner** – partner/alliance name or ID.
- **window** – time horizon (quarter, half, year, custom).
- **audience** – exec | partner-leadership | field | async.
- **format** – deck | memo | dashboard | loom.
- **focus** – optional emphasis (pipeline, co-marketing, product, success, expansion).

## Workflow
1. **Data Gathering** – assemble pipeline, revenue, marketing, and enablement metrics.
2. **Insight Layer** – highlight trends, wins, blockers, and benchmark comparisons.
3. **Joint Initiatives** – summarize in-flight programs, dependencies, and budget usage.
4. **Action & Decision Log** – capture required approvals, investments, and follow-ups.
5. **Packaging** – tailor presentation + briefing notes for requested audience + format.

## Outputs
- QBR/EBR deck or memo with KPIs, highlights, and blockers.
- Action tracker with owners, due dates, and status.
- Executive summary + talking points for partner and internal sponsors.

## Agent/Skill Invocations
- `partner-strategy-director` – curates narrative + investment asks.
- `partner-co-sell-lead` – provides pipeline + forecast insights.
- `partner-program-architect` – updates enablement + activation status.
- `co-marketing-governance` skill – injects program performance + next steps.
- `partner-ecosystem-map` skill – visualizes coverage vs goals.

---
