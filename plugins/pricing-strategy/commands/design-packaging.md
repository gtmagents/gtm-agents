---
name: design-packaging
description: Creates pricing packages, usage metrics, and value fences aligned to target segments.
usage: /pricing-strategy:design-packaging --product "AI Platform" --segments "growth,enterprise" --pricing_metric seats --deliverables 3
---

# Command: design-packaging

## Inputs
- **product** – offering or bundle name.
- **segments** – comma-separated segments (smb, growth, enterprise, partner, public sector).
- **pricing_metric** – usage driver (seats, volume, consumption, feature tier).
- **deliverables** – number of packaging options to present.
- **constraints** – optional guardrails (target ASP, margin, required features).

## Workflow
1. **Signal Intake** – pull customer insights, usage data, competitive benchmarks, and GTM priorities.
2. **Packaging Framework** – define good/better/best or modular structure with feature mapping.
3. **Value Fences** – outline metrics, thresholds, and add-on eligibility per package.
4. **Financial Modeling** – estimate ASP, margin, attach rate, and adoption across segments.
5. **Decision Kit** – produce comparison tables, positioning narratives, and approval checklist.

## Outputs
- Packaging matrix (features, limits, pricing metric, add-ons).
- Scenario model (ASP, margin, ARR impact) per package.
- Enablement-ready summary deck.

## Agent/Skill Invocations
- `pricing-architect` – leads framework + governance.
- `monetization-analyst` – models financial impact.
- `deal-desk-partner` – validates guardrails + exception policies.
- `packaging-framework` skill – provides structural templates.
- `value-messaging` skill – crafts positioning statements per tier.

---
