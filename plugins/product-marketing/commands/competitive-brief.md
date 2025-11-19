---
name: competitive-brief
description: Generates a competitor teardown and battlecard-focused enablement brief.
usage: /product-marketing:competitive-brief --competitor "Acme.io" --region global --audience enterprise
---

# Command: competitive-brief

## Inputs
- **competitor** – target vendor.
- **region** – market focus.
- **audience** – persona/segment to tailor messaging.
- **opportunity_stage** – optional sales stage to emphasize.
- **proof_assets** – optional links to customers, analysts, benchmarks.

## Workflow
1. **Signal Intake** – gather pricing, product updates, marketing campaigns, customer chatter.
2. **Feature/Value Comparison** – highlight differences in roadmap, integrations, services.
3. **Messaging & Positioning** – identify competitor claims vs vulnerabilities.
4. **Objection Handling** – craft rebuttals, proof points, switching stories.
5. **Enablement Kit** – produce slide/snippet ready content for reps and success teams.

## Outputs
- Competitive dossier (table + narrative insights).
- Battlecard PDF/slide summary with quick-reference sections.
- Talk track + objection script plus recommended assets.

## Agent/Skill Invocations
- `competitive-intel-lead` – compiles insights and drafts brief.
- `competitive-intel` skill – provides templates and guardrails.
- `product-narrative-lead` – ensures differentiation messaging stays consistent.

---
