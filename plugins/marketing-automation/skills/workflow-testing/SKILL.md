---
name: workflow-testing
description: Use when validating automation builds before launch or after significant
  changes.
---

# Workflow Testing & QA Skill

## When to Use
- Any new automation or major revision prior to go-live.
- Regression testing after data, asset, or logic changes.
- Investigating deliverability, conversion, or routing anomalies.

## Framework
1. **Unit Tests** – confirm each branch, wait step, and action path with seed contacts.
2. **Integration Tests** – verify webhook/API calls, CRM updates, enrichment, scoring.
3. **Content QA** – links, tracking, personalization tokens, accessibility, localization.
4. **Compliance** – consent, suppression, GDPR/CASL/CCPA rules, regional requirements.
5. **Performance** – throttle checks, concurrency, error handling, failover.

## Checklist
- Seed list matrix (personas, stages, regions, consent flags).
- Device/browser testing for email/SMS/push rendering.
- Logging + alerting validation.
- Rollback and kill switches documented.

## Templates
- QA evidence log (screenshot, recipient, status, owner).
- Incident runbook for automation failures.
- Release checklist referencing stakeholders.

## Tips
- Automate regression tests via APIs or synthetic users.
- Store test data separately and purge regularly to avoid reporting noise.
- Use feature flags to stage rollouts before full scale.

---
