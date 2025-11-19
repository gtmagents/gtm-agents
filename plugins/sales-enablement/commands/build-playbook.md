---
name: build-playbook
description: Produces a complete sales playbook with messaging, assets, and success metrics for a given motion.
usage: /sales-enablement:build-playbook --motion "Product Launch" --audience "AEs" --stage "Discovery"
---

# Command: build-playbook

## Inputs
- **motion** – name of the sales motion (e.g., "Product Launch", "Competitive Takeout").
- **audience** – target role(s) (AEs, SDRs, CSMs, partners).
- **stage** – funnel stage focus (prospect, discovery, demo, negotiation, expansion).
- **assets** – optional list of required asset types (deck, talk-track, ROI tool, email sequence).
- **metrics** – optional KPIs to emphasize.

## Workflow
1. **Brief Assembly** – collect motion context, target persona, differentiators, and proof points.
2. **Messaging Framework** – craft value prop, key questions, objection handling, and success stories.
3. **Asset Production** – outline decks, scripts, templates, and enablement worksheets.
4. **Activation Plan** – define rollout channel (LMS, live workshop), owners, and timeline.
5. **Measurement** – propose KPIs, instrumentation, and review cadence.

## Outputs
- Playbook overview (motion, objectives, persona, key messages).
- Asset checklist with links/placeholders for content-architect to populate.
- Enablement rollout + measurement plan.

## Agent/Skill Invocations
- `enablement-strategist` – sets objectives + measurement.
- `content-architect` – manages asset templates + metadata.
- `field-coach` – adds reinforcement + certification plan.
- `messaging-framework` skill – provides storytelling structure.
- `battlecard-system` skill – ensures competitive insights are embedded.

---
