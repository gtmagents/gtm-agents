---
name: reinforce-program
description: Drives post-launch reinforcement, certifications, and performance measurement for enablement initiatives.
usage: /sales-enablement:reinforce-program --program "Competitive Refresh" --cadence biweekly --channels "LMS,office-hours"
---

# Command: reinforce-program

## Inputs
- **program** – name of the enablement initiative to reinforce.
- **cadence** – reinforcement frequency (weekly, biweekly, monthly).
- **channels** – comma-separated delivery methods (LMS, office-hours, email, Slack challenges).
- **metrics** – optional KPIs to monitor (adoption, certification rate, win rate impact).
- **cohorts** – optional target cohorts (new hires, enterprise, partners).

## Workflow
1. **Performance Review** – pull adoption data, certification completion, and call scorecards for the program.
2. **Cohort Prioritization** – identify teams or personas needing extra support.
3. **Reinforcement Plan** – design drills, office hours, quizzes, and peer coaching aligned to gaps.
4. **Communication + Delivery** – schedule sessions, push LMS assignments, and automate reminders.
5. **Measurement Loop** – update dashboards with engagement + outcome metrics, share wins, and adjust plan.

## Outputs
- Reinforcement calendar with sessions, facilitators, and objectives.
- Communication kit (email/slack copy, LMS notifications).
- Impact dashboard summary showing adoption and performance metrics.

## Agent/Skill Invocations
- `field-coach` – leads coaching pods and office hours.
- `enablement-strategist` – monitors KPI impact + alignment.
- `content-architect` – keeps assets current for reenforcement.
- `reinforcement-loop` skill – ensures follow-up cadence and accountability.
- `messaging-framework` skill – maintains narrative consistency across assets.

---
