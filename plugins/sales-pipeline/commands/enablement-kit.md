---
name: enablement-kit
description: Generates pipeline inspection agendas, coaching scripts, and follow-up plans for frontline managers.
usage: /sales-pipeline:enablement-kit --team "Enterprise West" --focus "stage hygiene" --duration 30
---

# Command: enablement-kit

## Inputs
- **team** – manager or region name to tailor materials.
- **focus** – theme (stage hygiene, forecast accuracy, deal strategy, discovery).
- **duration** – length of sessions (minutes) to shape agendas.
- **include-assets** – true/false to attach template decks + worksheets.
- **cadence** – single-session | ongoing to indicate follow-up plan.

## Workflow
1. **Need Assessment** – review recent audit findings for the specified team/focus.
2. **Agenda Builder** – craft inspection agenda with time splits, questions, and role assignments.
3. **Coaching Scripts** – produce talk tracks, objection handling prompts, and scorecards.
4. **Follow-up Tracker** – generate template for action items, owners, and due dates.
5. **Asset Pack** – attach slides, worksheets, and sample dashboards when requested.

## Outputs
- Enablement agenda with objectives, topics, and timing.
- Coaching script cheat sheet plus inspection scorecard.
- Follow-up tracker template referencing CRM fields.

## Agent/Skill Invocations
- `forecast-coach` – provides coaching best practices + prompts.
- `pipeline-director` – aligns agenda with governance expectations.
- `pipeline-ops` skill – ensures fields/tasks referenced exist in CRM.
- `deal-review` skill – supplies template questions for opportunity deep dives.

---
