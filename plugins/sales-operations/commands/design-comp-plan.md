---
name: design-comp-plan
description: Builds compensation blueprints, rate tables, and governance packets for each GTM role.
usage: /sales-operations:design-comp-plan --role "Enterprise AE" --mix 50/50 --accelerators true --spiffs adoption
---

# Command: design-comp-plan

## Inputs
- **role** – GTM role or tier (AE, SE, AM, SDR, Partner).
- **mix** – pay mix (base/variable) to target.
- **accelerators** – true/false to include accelerator tables.
- **spiffs** – optional list of incentive focus areas.
- **guardrails** – optional constraints (floor/ceilings, compliance notes).

## Workflow
1. **Benchmark Intake** – analyze historical attainment, market data, and behavioral goals.
2. **Mechanics Definition** – set quota methodology, crediting rules, accelerators, and caps.
3. **Scenario Modeling** – project plan cost, payout curves, and fairness vs attainment distribution.
4. **Governance Plan** – document approvals, exception workflows, and enablement checklist.
5. **Communication Kit** – draft plan summaries, FAQs, and launch timeline.

## Outputs
- Compensation blueprint with quota, rates, accelerators.
- Scenario workbook (cost, sensitivity, fairness metrics).
- Launch + governance packet (timeline, owners, FAQ).

## Agent/Skill Invocations
- `compensation-architect` – leads design + governance.
- `capacity-planner` – checks coverage + cost-of-sale impact.
- `territory-architect` – ensures territory/quota alignment.
- `comp-mechanics` skill – standard clauses and templates.
- `quota-health` skill – validates fairness + behaviors.

---
