---
name: launch-program
description: Builds a launch plan for rolling out new enablement initiatives, including communications, training, and certification steps.
usage: /sales-enablement:launch-program --program "Competitive Refresh" --audience "AEs,SEs" --start 2025-12-01 --format blended
---

# Command: launch-program

## Inputs
- **program** – name of the enablement initiative.
- **audience** – comma-separated roles/segments.
- **start** – desired launch date.
- **format** – live | async | blended.
- **deliverables** – optional list of assets (deck, LMS module, certification).
- **owners** – optional list of facilitators/SMEs.

## Workflow
1. **Program Brief** – outline objectives, personas, success metrics, and prerequisites.
2. **Timeline & Milestones** – create workback plan (asset creation, pilot, launch, reinforcement).
3. **Comms Plan** – draft announcements, reminders, and stakeholder updates.
4. **Training Logistics** – schedule sessions, facilitators, registration, and LMS assignments.
5. **Certification & Measurement** – define assessment approach, score thresholds, and reporting cadence.

## Outputs
- Launch plan with timeline, milestones, and owners.
- Communication package (email/slack copy, LMS announcements).
- Certification + measurement checklist.

## Agent/Skill Invocations
- `enablement-strategist` – aligns objectives and success metrics.
- `content-architect` – manages asset readiness.
- `field-coach` – handles training/coaching logistics.
- `reinforcement-loop` skill – ensures follow-up checkpoints.
- `program-operations` skill – coordinates registration + tooling.

---
