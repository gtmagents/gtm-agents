---
name: launch-experiment
description: Converts an approved hypothesis into a fully-instrumented test with guardrails and rollout plan.
usage: /growth-experiments:launch-experiment --id EXP-142 --surface onboarding --variant-count 3 --ramp 5,25,50,100
---

# Command: launch-experiment

## Inputs
- **id** – experiment or hypothesis identifier.
- **surface** – product area/channel (onboarding, pricing page, lifecycle email, in-app).
- **variant-count** – number of variants/arms including control.
- **ramp** – comma-separated rollout schedule (%) or JSON file reference.
- **holdout** – optional holdout/ghost-experiment definition for measurement.
- **notes** – free-text for special approvals or exception handling.

## Workflow
1. **Readiness Check** – confirm design sign-off, instrumentation coverage, and guardrails.
2. **Variant Assembly** – pull specs, assets, and targeting rules for each arm.
3. **Rollout Plan** – configure flag/experimentation platform with ramp schedule + alerts.
4. **QA & Approvals** – run smoke tests, capture screenshots, and gather stakeholder approval.
5. **Launch & Monitoring** – activate test, enable telemetry dashboards, and notify channels.

## Outputs
- Launch packet with specs, QA evidence, approvals, and rollout timeline.
- Experiment platform configuration export + guardrail monitors.
- Stakeholder announcement + escalation matrix.

## Agent/Skill Invocations
- `test-engineer` – builds variants, instrumentation, and QA evidence.
- `experimentation-strategist` – confirms governance + approvals.
- `guardrail-scorecard` skill – validates guardrail coverage + thresholds.
- `experiment-design-kit` skill – ensures templates + best practices are applied.

---
