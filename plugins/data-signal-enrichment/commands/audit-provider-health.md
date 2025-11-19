---
name: audit-provider-health
description: Evaluates enrichment provider performance, coverage, and compliance posture.
usage: /data-signal-enrichment:audit-provider-health --providers apollo,hunter --window 30d --metrics success,latency,credits
---

# Command: audit-provider-health

## Inputs
- **providers** – comma-separated provider IDs (optional, defaults to all).
- **window** – lookback window (7d, 30d, quarter).
- **metrics** – success | latency | credits | quality (single or multi-select).
- **include-incidents** – true/false to append incident log details.
- **format** – dashboard | memo | csv.

## Workflow
1. **Data Pull** – aggregate success logs, latency metrics, credit usage, and quality flags.
2. **Benchmarking** – compare against SLA targets, cost thresholds, and historical averages.
3. **Incident Review** – attach outages, compliance issues, or ticket history (if requested).
4. **Recommendation Engine** – flag providers for scale-up, optimization, or pause.
5. **Packaging** – compile memo/dashboard plus Jira-ready action list.

## Outputs
- Provider scorecard per vendor with KPIs and SLA deltas.
- Optimization recommendations (route changes, contract updates, new tests).
- Incident appendix with remediation owners and due dates.

## Agent/Skill Invocations
- `provider-ops-lead` – owns analysis + recommendations.
- `data-quality-steward` – confirms quality/compliance findings.
- `signal-integrator` – ensures logging/telemetry coverage.
- `provider-scorecard` skill – standardizes scorecard layout.
- `waterfall-blueprint` skill – updates workflows based on findings.

---
