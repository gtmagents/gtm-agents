---
name: channel-pacing-guardrails
description: Guardrail framework for monitoring spend, efficiency, and CAC thresholds
  by channel.
---

# Channel Pacing Guardrails Skill

## When to Use
- Reviewing weekly/monthly pacing to stay within spend and efficiency targets.
- Triggering alerts when CPL/CAC/ROAS drift beyond tolerance.
- Aligning finance + marketing on reallocation decisions.

## Framework
1. **Budget Bands** – define min/max pacing per channel, region, and campaign tier.
2. **Efficiency Guardrails** – set CAC, CPL, ROAS, payback thresholds with warning/critical bands.
3. **Alert Workflow** – specify channels, owners, escalation paths, and notification cadence.
4. **Exception Policy** – document when overrides are allowed and approval requirements.
5. **Post-Mortem Loop** – capture breaches, actions taken, and guardrail adjustments.

## Templates
- Guardrail matrix (channel x metric x threshold).
- Alert playbook with messaging, owner, and resolution steps.
- Reallocation recommendation sheet linking to finance approvals.

## Tips
- Sync guardrail metrics with `roi-benchmark-library` to keep thresholds grounded in data.
- Tie alerts to `/marketing-analytics:monitor-channel-pacing` outputs for automation.
- Include leading indicators (CTR, CPC) to catch issues before CAC blows up.

---
