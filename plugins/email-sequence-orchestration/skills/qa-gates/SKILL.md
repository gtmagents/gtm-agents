---
name: qa-gates
description: Use before launching sequences to validate content, data, compliance,
  and monitoring.
---

# Email QA Gates Skill

## When to Use
- Prior to activating new nurture or lifecycle programs.
- After major changes to segmentation, personalization tokens, or deliverability settings.
- During post-incident reviews to ensure fixes remain in place.

## Framework
1. **Content & Personalization** – placeholders resolved, links tracked, dynamic content fallback tested.
2. **Data & Routing** – trigger logic, smart lists, suppression rules, CRM fields synced.
3. **Compliance** – footer language, preference center links, consent status, regional routing.
4. **Tracking & Analytics** – UTM/tagging consistency, BI/warehouse pipes, alert webhooks.
5. **Monitoring Hooks** – dashboards referenced, alert thresholds set, rollback plan documented.

## Templates
- QA runbook with owner, status, evidence links for each checklist item.
- Proofing matrix (persona × email × device × ISP) for screenshot validation.
- Launch readiness form requiring sign-off from marketing, ops, legal, and RevOps.

## Tips
- Pair with `deliverability-ops` to confirm authentication and inbox monitoring.
- Automate regression tests via API where possible (token validation, link health).
- Store QA evidence (screenshots, logs) alongside sequence assets for audits.

---
