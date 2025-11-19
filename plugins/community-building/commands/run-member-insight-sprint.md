---
name: run-member-insight-sprint
description: Executes a rapid member insight sprint across forums, interviews, and surveys with routing plan.
usage: /community-building:run-member-insight-sprint --theme onboarding --sample champions,builders --window 21d --audience product,marketing
---

# Command: run-member-insight-sprint

## Inputs
- **theme** – focus topic (onboarding, ai-use-cases, integrations, advocacy, support).
- **sample** – member cohorts to include (champions, builders, execs, partners, lurkers).
- **window** – sprint duration (7d, 14d, 21d, custom).
- **audience** – comma-separated stakeholders for readout (product, marketing, cs, exec, community).
- **evidence** – optional list of threads, tickets, or recordings to ingest.

## Workflow
1. **Sprint Setup** – define questions, sampling plan, and instrumentation across channels.
2. **Signal Collection** – launch prompts, AMAs, micro-surveys, and 1:1 interviews.
3. **Tagging & Analysis** – apply taxonomy for personas, drivers, sentiment, urgency.
4. **Narrative & Actions** – craft insight summary, quotes, data, and recommended actions per audience.
5. **Follow-up & Routing** – create action register, assign owners, and message members on outcomes.

## Outputs
- Insight sprint report (deck/memo) with top findings, quotes, and metrics.
- Tagged dataset + member story snippets for reuse.
- Action tracker linking insights to owners, deadlines, and follow-up comms.

## Agent/Skill Invocations
- `member-insights-advocate` – leads data capture, tagging, and storytelling.
- `community-ecosystem-strategist` – aligns insights to strategic priorities.
- `community-insight-taxonomy` skill – enforces tagging standards.
- `closed-loop-community-playbook` skill – manages routing + member follow-up.

---
