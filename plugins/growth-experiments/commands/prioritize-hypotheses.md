---
name: prioritize-hypotheses
description: Scores experiment backlog using impact, confidence, effort, and guardrail readiness.
usage: /growth-experiments:prioritize-hypotheses --source backlog.csv --capacity 6 --framework rice
---

# Command: prioritize-hypotheses

## Inputs
- **source** – backlog file, experiment tracker, or Notion database ID.
- **capacity** – number of experiments that can run in the next sprint/cycle.
- **framework** – ice | rice | custom; determines scoring weights.
- **guardrails** – optional JSON/CSV for mandatory guardrail requirements.
- **filters** – tags or OKRs to focus on (acquisition, activation, retention, monetization).

## Workflow
1. **Data Ingestion** – load backlog, normalize fields, and enrich with latest metrics.
2. **Scoring Engine** – calculate ICE/RICE/custom scores, factoring guardrail readiness.
3. **Portfolio Mix** – ensure balance across funnel stages and surfaces; flag conflicts.
4. **Capacity Planning** – fit highest-value tests into available slots, accounting for owners + effort.
5. **Decision Pack** – generate prioritized list, rationale, and trade-off notes for approval.

## Outputs
- Ranked backlog with scores, dependencies, and guardrail status.
- Capacity plan showing selected tests plus waitlist.
- Decision memo summarizing trade-offs and next actions.

## Agent/Skill Invocations
- `experimentation-strategist` – orchestrates prioritization + governance alignment.
- `insight-analyst` – validates data quality and metric assumptions.
- `hypothesis-library` skill – links past learnings to current ideas.
- `guardrail-scorecard` skill – enforces readiness requirements.

---
