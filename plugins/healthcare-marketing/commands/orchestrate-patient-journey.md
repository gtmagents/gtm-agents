---
name: orchestrate-patient-journey
description: Builds compliant patient engagement journey with educational content, consent flows, and support scripts.
usage: /healthcare-marketing:orchestrate-patient-journey --condition "Cardio" --stage onboarding --channels email,sms,community --duration 90d
---

# Command: orchestrate-patient-journey

## Inputs
- **condition** – therapeutic area or program name.
- **stage** – awareness | consideration | onboarding | adherence | advocacy.
- **channels** – email, sms, push, community, field, telehealth (comma-separated).
- **duration** – 30d | 60d | 90d | custom timeline for the journey.
- **consent-model** – opt-in workflow reference or data policy doc.

## Workflow
1. **Journey Discovery** – gather patient needs, clinical guidance, and support resources.
2. **Content & Touchpoint Plan** – outline education modules, reminders, escalation cues per stage.
3. **Compliance Layer** – embed consent checkpoints, disclaimers, and escalation procedures.
4. **Enablement Pack** – produce scripts, FAQs, and training notes for CS/field teams.
5. **Measurement Plan** – define KPIs (engagement, adherence, NPS) and reporting cadence.

## Outputs
- Journey storyboard with touchpoints, messaging, and consent notes.
- Enablement kit (scripts, knowledge base outline, escalation tree).
- Dashboard/analytics spec for monitoring patient engagement + safety signals.

## Agent/Skill Invocations
- `patient-engagement-program-manager` – leads journey design + enablement.
- `compliance-marketing-director` – validates consent + regulatory requirements.
- `patient-journey-mapping` skill – enforces structure + documentation.
- `regulatory-review-checklist` skill – ensures approvals before launch.

---
