---
name: design-lifecycle-journey
description: Produces a customer lifecycle journey map with stages, triggers, plays, and owners.
usage: /customer-marketing:design-lifecycle-journey --segment enterprise --product "Data Cloud"
---

# Command: design-lifecycle-journey

## Inputs
- **segment** – SMB, mid-market, enterprise, strategic, etc.
- **product** – product line or package the journey targets.
- **objectives** – adoption, expansion, advocacy, retention goals.
- **signals** – optional health metrics or telemetry to align on.
- **tooling** – optional stack info (Gainsight, HubSpot, Pendo, etc.).

## Workflow
1. **Insight Alignment** – analyze current health, usage, NPS, and pipeline targets.
2. **Stage Definition** – outline onboarding, adoption, value realization, expansion, advocacy.
3. **Trigger & Play Mapping** – define triggers (usage dips, milestone hits) with recommended plays.
4. **Owner & Channel Assignment** – map CS, product, marketing, automation responsibilities.
5. **Measurement Plan** – set KPIs per stage and dashboards/alerts for monitoring.

## Outputs
- Journey map table (stage, trigger, play, owner, channel, KPI).
- Trigger-to-play matrix for automation/CS tooling.
- Measurement checklist with dashboard queries and alert rules.

## Agent/Skill Invocations
- `lifecycle-strategist` – orchestrates journey design.
- `customer-insights` skill – supplies telemetry + signal definitions.
- `expansion-plays` skill – recommends stage-specific offers.

---
