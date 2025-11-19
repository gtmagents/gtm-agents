---
name: append-data
description: Append missing attributes to bulk lead lists using configurable provider waterfalls and mapping rules.
usage: /data-enrichment:append-data --input leads.csv --fields "title,phone,linkedin"
---

# Append Data Command

## Purpose
Bulk-enrich a CSV/JSON dataset by filling specified fields (titles, phones, LinkedIn URLs, firmographics) while respecting credit budgets and compliance rules.

## Syntax
```bash
/data-enrichment:append-data \
  --input leads.csv \
  --fields "title,phone,linkedin" \
  --priority "apollo,hunter,rocketreach" \
  --max-credits 5 \
  --output enriched.csv
```

### Parameters
- `--input`: Path to CSV/JSON file with seed data.
- `--fields`: Comma-separated field names to append.
- `--priority`: Ordered provider sequence (defaults to recommended waterfall per field).
- `--max-credits`: Credit ceiling per record.
- `--parallel`: Number of concurrent requests.
- `--output`: Destination file.
- `--cache-ttl`: Override default caching window.

## Features
- Automatic batching for provider rate limits.
- Field-level confidence scoring and attribution to provider.
- Retry + fallback strategy when providers fail.
- Progress reporting (records completed, credits consumed, ETA).

---
