---
name: signal-taxonomy
description: Use to define schemas, topic tags, and lineage metadata for enriched
  signals.
---

# Signal Taxonomy Skill

## When to Use
- Normalizing multiple provider outputs into a unified schema.
- Rolling out new intent topics, enrichment attributes, or scoring dimensions.
- Auditing lineage + compliance requirements.

## Framework
1. **Schema Definition** – fields, datatypes, required/optional flags.
2. **Topic & Attribute Mapping** – align provider-specific attributes to canonical names.
3. **Versioning** – maintain change logs, effective dates, and migration steps.
4. **Validation Rules** – min/max values, allowed lists, dependency rules.
5. **Documentation** – publish data dictionary + lineage diagrams.

## Templates
- Data dictionary sheet (field, description, source, owner).
- Topic mapping table by provider.
- Migration checklist for schema changes.

## Tips
- Keep names human-readable for GTM teams but consistent with data warehouse standards.
- Tag every field with owner + refresh cadence.
- Pair with `identity-resolution` to ensure IDs and linkages stay consistent.

---
