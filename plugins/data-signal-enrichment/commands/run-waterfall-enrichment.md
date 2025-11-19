---
name: run-waterfall-enrichment
description: Executes provider waterfalls with credit governance, failover rules, and delivery targets.
usage: /data-signal-enrichment:run-waterfall-enrichment --type contact --input "Taylor Reed, Nimbus" --sequence apollo,hunter,rocketreach --max-credits 5
---

# Command: run-waterfall-enrichment

## Inputs
- **type** – contact | company | technographic | intent.
- **input** – record payload (name/company/email/domain/file).
- **sequence** – optional ordered provider list; default uses ops config.
- **max-credits** – ceiling for total credits to consume.
- **delivery** – crm | csv | warehouse specifying output target.

## Workflow
1. **Request Validation** – confirm fields, dedupe against recent runs, and enforce rate limits.
2. **Sequence Selection** – pull provider order from configs, adjust for overrides or outages.
3. **Execution Loop** – call providers, capture response metadata, apply validation logic.
4. **Aggregation & Scoring** – merge best data, attach confidence + provenance tags.
5. **Delivery & Logging** – push to destination, log credits, update success dashboards, trigger alerts if thresholds exceeded.

## Outputs
- Enrichment payload (JSON/CSV/CRM payload) with fields, provider, timestamp, confidence.
- Credit + latency report appended to provider utilization table.
- Alert entries when max-credits hit or providers fail.

## Agent/Skill Invocations
- `provider-ops-lead` – supplies sequence + credit policy.
- `signal-integrator` – handles normalization + delivery.
- `data-quality-steward` – validates results before release.
- `waterfall-blueprint` skill – enforces sequencing template.
- `provider-scorecard` skill – logs performance + cost metrics.

---
