---
name: build-coaching-plan
description: Creates individualized coaching plans with goals, drills, and measurement cadences.
usage: /sales-coaching:build-coaching-plan --rep "Taylor" --focus "discovery" --timeline 6w --cadence weekly
---

# Command: build-coaching-plan

## Inputs
- **rep** – required rep or team name.
- **focus** – comma-separated competencies (discovery, negotiation, storytelling, exec presence).
- **timeline** – duration of the program (4w, 6w, quarter).
- **cadence** – meeting frequency (weekly, biweekly, async kit).
- **signals** – optional list of metrics or recordings to analyze first.

## Workflow
1. **Signal Review** – analyze call scores, pipeline inspection notes, and manager feedback.
2. **Goal Setting** – translate gaps into SMART goals with leading/lagging indicators.
3. **Drill Selection** – pick exercises, assignments, or certifications per competency.
4. **Schedule & Accountability** – define session cadence, owners, and check-ins.
5. **Measurement Plan** – log KPIs, survey cadence, and exit criteria.

## Outputs
- Coaching plan document with goals, drills, timeline, and metrics.
- Assignment list for LMS/enablement systems.
- Progress tracker template for managers.

## Agent/Skill Invocations
- `performance-coach` – leads plan design.
- `call-analyst` – provides signal insights.
- `enablement-partner` – ensures asset + certification alignment.
- `coaching-framework` skill – structures the plan.
- `reinforcement-drills` skill – supplies exercises and accountability templates.

---
