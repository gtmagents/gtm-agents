---
name: synthesize-learnings
description: Creates experiment readouts, codifies learnings, and routes follow-up actions.
usage: /growth-experiments:synthesize-learnings --source exp-log.db --scope "Q4 funnel" --audience exec
---

# Command: synthesize-learnings

## Inputs
- **source** – experiment tracker, warehouse table, or analytics workspace.
- **scope** – filters (timeframe, product area, funnel stage, persona).
- **audience** – exec | pod | growth-guild | async memo; controls fidelity/tone.
- **format** – deck | memo | dashboard | loom.
- **follow-ups** – optional CSV/JSON for linking Jira/Asana action items.

## Workflow
1. **Data Consolidation** – assemble final metrics, guardrail outcomes, and qualitative notes.
2. **Insight Extraction** – group learnings by hypothesis theme, persona, or funnel stage.
3. **Decision Encoding** – record win/ship, iterative, or archive outcomes plus rationale.
4. **Action Routing** – create follow-up stories, backlog items, or automation triggers.
5. **Knowledge Base Update** – tag learnings in centralized library with attribution + status.

## Outputs
- Executive-ready readout with insights, decisions, and KPIs.
- Learning cards mapped to hypothesis taxonomy + next bets.
- Action log synced to backlog/project tools.

## Agent/Skill Invocations
- `insight-analyst` – leads analysis and storytelling.
- `experimentation-strategist` – ensures learnings feed roadmap + governance.
- `hypothesis-library` skill – indexes learnings against taxonomy.
- `experiment-design-kit` skill – suggests iteration ideas based on patterns.

---
