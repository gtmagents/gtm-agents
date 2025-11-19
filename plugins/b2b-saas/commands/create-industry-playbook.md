---
name: create-industry-playbook
description: Produces vertical-specific POV, solution brief, and enablement kit for B2B SaaS teams.
usage: /b2b-saas:create-industry-playbook --industry fintech --persona revops --depth full
---

# Command: create-industry-playbook

## Inputs
- **industry** – vertical focus (fintech, healthcare, manufacturing, education, media, public sector).
- **persona** – target persona (cio, revops, marketing, product, finance, cs).
- **depth** – summary | standard | full; controls output fidelity.
- **assets** – optional references to existing case studies or assets.
- **format** – deck | memo | docset.

## Workflow
1. **Research Digest** – pull market trends, buyer pains, and competitive signals.
2. **Narrative Building** – craft POV, messaging pillars, and proof points.
3. **Solution Packaging** – outline recommended bundles, integrations, and usage scenarios.
4. **Enablement Kit** – create talk track, objection handling, and resource links.
5. **Action Plan** – recommend next steps (campaigns, ABM, references) for GTM teams.

## Outputs
- Industry POV deck/memo with messaging and differentiation.
- Solution brief plus recommended bundles/integrations.
- Enablement checklist including talk track, objection handling, and asset links.

## Agent/Skill Invocations
- `industry-strategist` – leads research + narrative creation.
- `value-ops-lead` – adds ROI/TCO benchmarks and customer proof.
- `vertical-solution-templates` skill – enforces layout + asset structure.
- `board-readiness-kit` skill – prepares exec-ready snippets for leadership.

---
