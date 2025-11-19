---
name: launch-in-app-experiments
description: Coordinates in-app experiments targeting activation, expansion, or monetization.
usage: /product-led-growth:launch-in-app-experiments --surface dashboard --goal activation --variants 3 --guardrails churn,latency
---

# Command: launch-in-app-experiments

## Inputs
- **surface** – product area (dashboard, onboarding, billing, collaboration, mobile).
- **goal** – activation | engagement | monetization | retention.
- **variants** – number of experiment arms (including control).
- **guardrails** – comma-separated guardrail metrics to monitor.
- **audience** – persona/segment targeting (role, plan, region, cohort).
- **notes** – optional context or risk flags.

## Workflow
1. **Hypothesis Intake** – capture hypotheses, prior learnings, and success metrics.
2. **Design Package** – define variant specs, targeting, triggers, and messaging.
3. **Instrumentation & Guardrails** – ensure events, tracking, and guardrails are wired.
4. **Launch & Monitoring** – deploy experiment, monitor metrics, trigger alerts.
5. **Readout Prep** – summarize results, decisions, and follow-up actions.

## Outputs
- Experiment brief with hypotheses, variants, and instrumentation checklist.
- Guardrail + monitoring dashboard snapshot.
- Readout template with decision + rollout recommendation.

## Agent/Skill Invocations
- `usage-growth-scientist` – leads experiment design + analysis.
- `product-adoption-strategist` – ensures journey alignment + messaging.
- `in-app-messaging-kit` skill – generates variant messaging + prompts.
- `usage-health-scorecard` skill – monitors guardrails + success metrics.

---
