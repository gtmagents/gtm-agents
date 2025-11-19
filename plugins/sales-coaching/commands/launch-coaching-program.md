---
name: launch-coaching-program
description: Plans and activates multi-week coaching cohorts with communications, assets, and measurement.
usage: /sales-coaching:launch-coaching-program --program "Exec Presence" --cohort "Enterprise AEs" --start 2026-01-08 --duration 8w
---

# Command: launch-coaching-program

## Inputs
- **program** – name of the coaching initiative.
- **cohort** – audience segment or team.
- **start** – kickoff date.
- **duration** – number of weeks or sessions.
- **format** – live | async | blended.
- **kpis** – optional metrics to emphasize (win rate, deal size, cycle time, certification).

## Workflow
1. **Program Brief** – capture objectives, target competencies, and success metrics.
2. **Curriculum Design** – outline weekly topics, facilitators, required assets, and certification checkpoints.
3. **Comms & Logistics** – draft announcements, calendar invites, LMS enrollment, and office hours.
4. **Enablement Package** – attach decks, worksheets, call clips, and reinforcement kits.
5. **Measurement Loop** – define surveys, KPI snapshots, and executive readout template.

## Outputs
- Program plan with schedule, facilitators, and dependencies.
- Communication kit (emails, Slack posts, LMS descriptions).
- Measurement tracker with KPIs and survey cadence.

## Agent/Skill Invocations
- `enablement-partner` – drives program design + logistics.
- `performance-coach` – aligns curriculum with behavior change goals.
- `call-analyst` – sources clips + proof points.
- `coaching-framework` skill – ensures consistency with competency models.
- `reinforcement-drills` skill – loads post-session assignments.

---
