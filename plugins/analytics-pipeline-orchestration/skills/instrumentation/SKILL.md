---
name: instrumentation
description: Use when defining events, fields, and governance for GTM analytics pipelines.
---

# Analytics Instrumentation Standards Skill

## When to Use
- Planning event tracking for product, marketing, or revenue analytics.
- Auditing existing tracking plans before model refreshes.
- Coordinating engineering, product, and RevOps on data contracts.

## Framework
1. **Event Naming & Structure** – action-oriented names, consistent casing, required properties.
2. **Identity Management** – user/account IDs, anonymous IDs, device IDs, cross-system mapping.
3. **Consent & Privacy** – capture consent status, honor suppression, regional storage rules.
4. **Versioning** – change logs, backward compatibility, deprecation timelines.
5. **Observability** – sampling dashboards, schema change alerts, volume anomaly detection.

## Templates
- Tracking plan sheet (event, description, properties, source, owner, status).
- Data contract checklist (fields, types, validation rules, SLA).
- Observability runbook (metrics, thresholds, notification channels).

## Tips
- Pair each event with QA instructions and sample payloads.
- Store tracking plans in version control to align with code releases.
- Review instrumentation quarterly with stakeholders.

---
