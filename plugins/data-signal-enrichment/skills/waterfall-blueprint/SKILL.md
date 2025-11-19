---
name: waterfall-blueprint
description: Use to design provider sequences, throttling logic, and credit policies
  for enrichment waterfalls.
---

# Waterfall Blueprint Skill

## When to Use
- Building contact/company enrichment workflows across multiple providers.
- Updating fallback rules after provider outages or cost shifts.
- Documenting waterfall logic for RevOps + engineering handoffs.

## Framework
1. **Goal & Constraints** – define enrichment type, data requirements, credit ceiling, SLA.
2. **Provider Catalog** – list eligible providers with success %, latency, compliance notes.
3. **Routing Logic** – determine sequence, branching, and retry intervals.
4. **Safeguards** – set throttles, dedupe checks, and exception triggers.
5. **Versioning** – log changes, approvals, and effective dates.

## Templates
- Waterfall diagram (sequence, inputs, outputs, fallback paths).
- Routing table (provider, criteria, cost, notes).
- Change log with owners + rationale.

## Tips
- Keep sequences short for real-time use cases; reserve long chains for batch mode.
- Use A/B tests to validate new providers before full rollout.
- Pair with `provider-scorecard` to continuously optimize routing.

---
