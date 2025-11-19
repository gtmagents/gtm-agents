---
name: audit-content
description: Reviews enablement asset inventory for freshness, adoption, and gaps, delivering prioritized actions.
usage: /sales-enablement:audit-content --audience "AEs" --region "NA" --include-metrics true
---

# Command: audit-content

## Inputs
- **audience** – target audience (AEs, SDRs, SEs, CSMs, partners).
- **region** – optional geographic focus.
- **include-metrics** – true/false to add adoption + performance metrics.
- **age-threshold** – months since last update to flag assets.
- **topics** – optional themes (competitive, product, discovery, vertical).

## Workflow
1. **Inventory Pull** – scan enablement CMS/LMS metadata (asset type, owner, last update, usage).
2. **Adoption & Impact** – analyze usage metrics and performance correlation.
3. **Gap Analysis** – compare assets vs enablement roadmap + field requests.
4. **Recommendations** – prioritize refreshes, net-new content, and retirements.
5. **Action Plan** – assign owners, timelines, and metrics for each recommendation.

## Outputs
- Content inventory report with freshness + usage metrics.
- Gap & action list with priority, owner, and due date.
- Dashboard snapshot summarizing adoption + impact if metrics included.

## Agent/Skill Invocations
- `content-architect` – owns metadata + action plan.
- `enablement-strategist` – aligns gaps with GTM goals.
- `field-coach` – provides frontline feedback and reinforcement needs.
- `content-governance` skill – enforces standards + lifecycle rules.

---
