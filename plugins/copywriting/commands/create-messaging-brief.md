---
name: create-messaging-brief
description: Generates a messaging brief with hook banks, proof points, and CTA strategy.
usage: /copywriting:create-messaging-brief --goal pipeline --persona "RevOps" --offer "AI copilot"
---

# Command: create-messaging-brief

## Inputs
- **goal** – awareness, pipeline, expansion, etc.
- **persona** – target audience.
- **offer** – product/feature/value prop.
- **proof_assets** – optional customer quotes, metrics, analyst notes.
- **channels** – optional list (email, ads, landing page, social).

## Workflow
1. **Insight Intake** – gather positioning, ICP pain points, proof assets.
2. **Message Architecture** – build headline, pillars, supporting statements.
3. **Hook Bank** – produce multiple hook formulas per channel.
4. **CTA Strategy** – recommend CTAs per funnel stage + urgency tactics.
5. **Experiment Recommendations** – highlight copy tests with KPIs.

## Outputs
- Messaging brief document (headline, pillars, proof, CTA matrix).
- Hook bank and CTA recommendations by channel.
- Experiment backlog entries.

## Agent/Skill Invocations
- `copy-strategist` – oversees messaging structure.
- `message-architecture` skill – enforces framework consistency.
- `voice-editor` – ensures guideline alignment.

---
