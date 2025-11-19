---
name: identity-resolution
description: Use to match accounts, contacts, and opportunities across enrichment
  sources with governed rules.
---

# Identity Resolution Playbook Skill

## When to Use
- Normalizing provider outputs before syncing to CRM/CDP.
- Tying intent, enrichment, and product telemetry to the same account/contact IDs.
- Diagnosing duplicate or conflicting records in downstream systems.

## Framework
1. **Key Hierarchy** – define primary/secondary keys (domain, account_id, email, person_id).
2. **Matching Logic** – configure deterministic and fuzzy rules, tie-breakers, and confidence scoring.
3. **Conflict Handling** – specify precedence rules, merge policies, and exception queues.
4. **Governance** – document owners, change control, and monitoring cadence.
5. **Audit Trail** – capture lineage metadata, before/after snapshots, and rollback steps.

## Templates
- Matching rule matrix (field, rule type, weight, confidence threshold).
- Exception queue workflow with owners + SLAs.
- Audit workbook for sampling matches vs source-of-truth.

## Tips
- Start with deterministic keys (domain, CRM ID) before fuzzy logic to reduce noise.
- Version rules so downstream teams know when behavior changes.
- Pair with `signal-taxonomy` to keep IDs aligned with schema updates.

---
