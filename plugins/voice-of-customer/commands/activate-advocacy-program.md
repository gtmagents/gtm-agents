---
name: activate-advocacy-program
description: Turns VoC themes into advocacy campaigns, advisory boards, and reference plays.
usage: /voice-of-customer:activate-advocacy-program --theme onboarding --cohort enterprise --format roadmap --channels advisory-board,case-study
---

# Command: activate-advocacy-program

## Inputs
- **theme** – VoC theme to spotlight (onboarding, automation, AI, integrations, support, partnership).
- **cohort** – target customer cohort (segment, industry, ARR band).
- **channels** – comma list of advocacy motions (advisory-board, reference, community-circle, case-study, beta-council).
- **format** – preferred deliverable (roadmap, executive-brief, campaign-pack, notion-space).
- **guardrails** – optional compliance or legal constraints to respect.

## Workflow
1. **Cohort Selection** – score potential advocates based on health, engagement, usage, and VoC alignment.
2. **Program Blueprint** – define engagement model, agenda, incentives, and success metrics per channel.
3. **Content & Enablement** – draft briefs, NDAs, run-of-show, and storytelling prompts.
4. **Activation** – coordinate invites, logistics, and facilitation touchpoints.
5. **Measurement & Loopback** – capture feedback, update VoC system, and publish impact summary.

## Outputs
- Advocacy program brief with objectives, personas, cadence, and KPIs.
- Asset kit (agendas, outreach templates, content outlines) per channel.
- Impact dashboard showing reference pipeline, influenced revenue, and satisfaction shifts.

## Agent/Skill Invocations
- `customer-advocacy-strategist` – leads cohort selection, program blueprint, and activation.
- `voc-program-director` – ensures governance + executive visibility.
- `advocacy-roster-system` skill – scores and tracks advocate readiness.
- `closed-loop-playbook` skill – feeds outcomes back into VoC action tracker.

---
