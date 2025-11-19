---
name: normalize-signals
description: Processes enriched datasets into unified schemas with identity resolution and tagging.
usage: /data-signal-enrichment:normalize-signals --source warehouse --outputs crm,cdp --taxonomy intent_v2
---

# Command: normalize-signals

## Inputs
- **source** – data origin (warehouse, csv, api, webhook).
- **outputs** – comma-separated destinations (crm, cdp, lake, orchestration).
- **taxonomy** – schema/taxonomy version to enforce.
- **window** – time window or batch ID to process.
- **dry-run** – true/false toggle for validation-only runs.

## Workflow
1. **Schema Detection** – inspect incoming fields, compare to taxonomy, flag gaps.
2. **Identity Resolution** – match accounts/contacts/opps using rules + heuristics.
3. **Normalization** – standardize values, units, topics, and metadata.
4. **Tagging & Scoring** – add freshness, confidence, and signal-type tags.
5. **Distribution** – publish to requested destinations with lineage + control tables.

## Outputs
- Normalized dataset (per destination) with schema compliance report.
- Identity resolution summary (matches, conflicts, unresolved records).
- Taxonomy drift log + remediation checklist.

## Agent/Skill Invocations
- `signal-integrator` – runs normalization + distribution.
- `data-quality-steward` – validates schema + scores.
- `provider-ops-lead` – supplies provider metadata for lineage.
- `signal-taxonomy` skill – enforces schema + naming rules.
- `identity-resolution` skill – handles matching heuristics.

---
