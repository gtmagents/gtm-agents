---
name: validation-rulebook
description: Use to define validation, freshness, and compliance checks for enriched
  data.
---

# Validation Rulebook Skill

## When to Use
- Running QA before syncing enrichment outputs to GTM systems.
- Auditing providers after schema changes or outages.
- Documenting compliance-ready validation procedures.

## Framework
1. **Rule Catalog** – list required fields, regex patterns, allowed values, and dependencies.
2. **Freshness Thresholds** – define time-based SLAs per signal type.
3. **Confidence Scoring** – set weighting for provider, validation method, and history.
4. **Exception Handling** – create workflows for quarantining, reprocessing, or escalation.
5. **Compliance Hooks** – log approvals, data residency tags, and retention policies.

## Templates
- Rule table (field, check, threshold, severity, owner).
- QA runbook with pre/post sync steps.
- Compliance audit packet ready for legal/infosec reviews.

## Tips
- Automate as many rules as possible but keep manual sampling for high-impact signals.
- Version rules alongside taxonomy updates.
- Pair with `data-quality-steward` outputs for sign-off history.

---
