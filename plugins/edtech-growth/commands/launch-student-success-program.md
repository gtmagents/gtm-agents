---
name: launch-student-success-program
description: Builds onboarding + retention program plan with interventions, enablement, and KPI stack.
usage: /edtech-growth:launch-student-success-program --program "AI Certificate" --cohort spring-2026 --risk-profile mixed --channels email,sms,community
---

# Command: launch-student-success-program

## Inputs
- **program** – program/cohort name.
- **cohort** – cohort identifier or term (e.g., fall-2025, summer-bootcamp).
- **risk-profile** – low | mixed | high (drives intervention intensity).
- **channels** – email, sms, community, coaching, in-app, live (comma-separated).
- **data-links** – optional CSAT/engagement exports for reference.

## Workflow
1. **Cohort Analysis** – review admissions mix, modality, and historical performance.
2. **Journey Design** – map onboarding, activation, momentum, and completion stages.
3. **Intervention Planning** – define nudges, coaching cadences, community events, and escalation paths.
4. **Enablement & Tooling** – assign owners, scripts, dashboards, and automation hooks.
5. **Launch & Monitoring** – publish calendar, define KPIs, and set review cadence.

## Outputs
- Student success program plan (timeline, touchpoints, content themes).
- Enablement kit for faculty/support (scripts, escalation, FAQs).
- KPI tracker + dashboard spec aligned to engagement/retention goals.

## Agent/Skill Invocations
- `student-success-program-manager` – leads journey + intervention design.
- `enrollment-growth-strategist` – ties success plan to top-of-funnel promises.
- `student-success-scorecard` skill – defines KPIs and dashboards.
- `community-advocacy-toolkit` skill – seeds community + referral motions.

---
