---
name: enrich-leads
description: Enrich a single company or person record with firmographics, technographics,
  and contact intelligence.
usage: /data-enrichment:enrich --type company --domain "acme.com" --depth comprehensive
---


# Enrich Command

## Purpose
Run targeted enrichment for a specific company or contact, orchestrating provider waterfalls and AI research to fill required data fields.

## Syntax
```bash
/data-enrichment:enrich \
  --type <company|person> \
  --domain "acme.com" \
  --email "ceo@acme.com" \
  --depth <basic|standard|comprehensive>
```

### Parameters
- `--type`: company or person.
- `--domain`: company domain.
- `--email` / `--name` / `--company`: person identifiers.
- `--depth`: determines provider sequence and credit budget.
- `--providers`: optional custom order (comma-delimited).
- `--include-intent`: attach intent data (default true).

## Output
- JSON record with firmographics, technographics, contacts, intent signals, and confidence scores.
- Provider log + credit usage summary.

---
