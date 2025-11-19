---
name: sla-tracking
description: "Use to design measurement, alerting, and reporting for MQL\u2192SQL\
  \ SLAs."
---

# SLA Tracking System Skill

## When to Use
- Establishing or revisiting SLA metrics between marketing, SDR, and sales pods.
- Building dashboards/alerts for pipeline speed and follow-up compliance.
- Running retrospectives after SLA breaches or pipeline delays.

## Framework
1. **Definitions** – clarify timestamps (MQL, SAL, SQL), owner transitions, and acceptance criteria.
2. **Targets** – set response + acceptance SLAs per segment, region, or channel.
3. **Measurement** – configure data pipelines pulling MAP + CRM events, dedupe logic, and exclusions.
4. **Alerting** – thresholds, notification channels, severity levels, and on-call rotation.
5. **Review Cadence** – weekly dashboards, monthly retros, quarterly recalibration.

## Templates
- SLA scorecard (segment → target → actual → variance → owner).
- Alert playbook with trigger conditions and escalation steps.
- Retro template capturing root cause, fixes, and follow-up experiments.

## Tips
- Anchor SLAs to revenue impact (pipeline $) to drive accountability.
- Include qualitative context (reason codes) to separate data gaps vs true SLA misses.
- Pair with `routing-logic` updates when volume spikes create bottlenecks.

---
