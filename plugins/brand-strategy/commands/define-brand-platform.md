---
name: define-brand-platform
description: Builds brand platform with positioning, pillars, tone, and rollout plan.
usage: /brand-strategy:define-brand-platform --audience enterprise --proof kpi,customer --format deck
---

# Command: define-brand-platform

## Inputs
- **audience** – primary audience or segment focus (enterprise, smb, developer, partner).
- **proof** – comma list of proof asset types to highlight (kpi, customer, analyst, product, roadmap).
- **format** – deck | narrative | workspace.
- **constraints** – optional guardrails (legal, regulatory, naming, localization).
- **references** – URLs/docs of existing research, messaging, or campaigns.

## Workflow
1. **Discovery Alignment** – absorb research, GTM goals, competitive narratives.
2. **Narrative Drafting** – craft purpose, promise, pillars, RTBs, and tone guidance.
3. **Proof Mapping** – align customer stories, metrics, product proof to each pillar.
4. **Validation & Iteration** – gather feedback from execs, product, sales, customers.
5. **Rollout Plan** – define enablement, asset updates, KPIs, and governance owners.

## Outputs
- Brand platform deck/narrative with positioning statements, pillars, and messaging matrix.
- Proof asset map referencing customers, metrics, analysts, and demos.
- Rollout & adoption plan with milestones, owners, and success metrics.

## Agent/Skill Invocations
- `brand-foundation-architect` – leads narrative + stakeholder alignment.
- `brand-governance-lead` – ensures compliance and rollout processes.
- `brand-narrative-playbook` skill – enforces template + voice guardrails.
- `brand-voice-glossary` skill – codifies tone, vocabulary, and localization notes.

---
