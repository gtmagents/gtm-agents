---
name: guardrail-scorecard
description: Framework for defining, monitoring, and enforcing guardrail metrics across
  experiments.
---

# Guardrail Scorecard Skill

## When to Use
- Setting non-negotiable metrics (stability, churn, latency, compliance) before launching tests.
- Monitoring live experiments to ensure guardrails stay within thresholds.
- Reporting guardrail status in launch packets and post-test readouts.

## Framework
1. **Metric Inventory** – list guardrail metrics, owners, data sources, refresh cadence.
2. **Threshold Matrix** – define warning vs critical bands per metric / persona / region.
3. **Alerting & Escalation** – map notification channels, DRI, and decision timelines.
4. **Exception Handling** – document when guardrail overrides are acceptable and required approvals.
5. **Retrospective Loop** – log breaches, mitigations, and rule updates for future tests.

## Templates
- Guardrail register (metric, threshold, owner, alert channel).
- Live monitoring dashboard layout.
- Exception memo structure for approvals.

## Tips
- Tie guardrails to downstream systems (billing, support) to catch second-order impacts.
- Keep thresholds dynamic for seasonality but document logic.
- Pair with `launch-experiment` to ensure readiness before flipping flags.

---
