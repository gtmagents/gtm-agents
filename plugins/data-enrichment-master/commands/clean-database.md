---
name: clean-database
description: Normalize, deduplicate, and validate enriched datasets to maintain accuracy and compliance.
usage: /data-enrichment:clean-database --input enriched.csv --rules rules.yaml
---

# Clean Database Command

## Purpose
Run data quality workflows (formatting, deduplication, validation, suppression) before syncing enriched records into downstream systems.

## Syntax
```bash
/data-enrichment:clean-database \
  --input enriched.csv \
  --rules rules.yaml \
  --output clean.csv \
  --gdpr true
```

### Parameters
- `--input`: Source CSV/JSON/Parquet file.
- `--rules`: YAML/JSON config defining normalization rules, required fields, dedupe logic.
- `--output`: File path or system destination (Salesforce, HubSpot, Snowflake).
- `--gdpr`: Apply regional compliance filters (default true).
- `--suppress-list`: Path to opt-out or customer suppression list.
- `--format`: Output format (csv, json, parquet, api-sync).

## Features
- Email/phone format correction, country normalization, timezone calculation.
- Deduping via fuzzy matching and configurable keys.
- Confidence scoring and rejection report for records failing validation.
- Audit log of transformations for compliance.

---
