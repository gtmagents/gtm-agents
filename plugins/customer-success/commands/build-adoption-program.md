---
name: build-adoption-program
description: Crafts segment-specific adoption programs with plays, content, and measurement.
usage: /customer-success:build-adoption-program --segment scaleup --journey 60d --channels in-app,email,cs --objective expansion
---

# Command: build-adoption-program

## Inputs
- **segment** – target cohort (startup, scaleup, enterprise, strategic, partner).
- **journey** – timeframe (30d, 60d, 90d, custom).
- **channels** – comma-separated (in-app, email, webinar, cs, community).
- **objective** – adoption | expansion | advocacy | renewal.
- **assets** – optional reference to content library or template pack.

## Workflow
1. **Insight Intake** – pull health metrics, feedback, and persona research for the segment.
2. **Milestone Design** – define onboarding, activation, and expansion milestones.
3. **Play Assembly** – map actions per channel with triggers, owners, and personalization rules.
4. **Measurement Plan** – list KPIs, guardrails, and reporting cadence.
5. **Enablement Pack** – export comms templates, briefs, and training notes.

## Outputs
- Adoption program blueprint (timeline + action matrix).
- Content + comms toolkit aligned to personas and milestones.
- Measurement checklist for CS ops + analytics.

## Agent/Skill Invocations
- `adoption-program-manager` – architects program and content plan.
- `customer-health-director` – validates KPIs and guardrails.
- `adoption-playbook` skill – enforces template + milestone structure.
- `sentiment-feedback-loop` skill – integrates qualitative insights.

---
