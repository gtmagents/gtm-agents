---
name: decision-trees
description: Use when designing branching logic, eligibility rules, and fallback paths.
---

# Personalization Decision Trees Skill

## When to Use
- Planning logic for dynamic experiences across web, in-app, email, or sales plays.
- Auditing existing decision flows for complexity, coverage, or compliance gaps.
- Simulating new branches before deploying rule or model updates.

## Framework
1. **Objective Mapping** – tie each node to business KPIs and user intents.
2. **Signal Hierarchy** – prioritize deterministic signals (consent, account tier, lifecycle) before behavioral or predictive ones.
3. **Fallback Design** – ensure every branch has a safe default when data is missing or risk flags appear.
4. **Experiment Hooks** – embed test slots at key decision points with guardrail metrics.
5. **Monitoring** – log path selections, success rates, and anomaly alerts for continuous tuning.

## Templates
- Decision tree canvas (node, condition, action, fallback, owner).
- Signal priority matrix (signal → freshness → reliability → privacy risk).
- Simulation checklist (scenarios, expected path, validation steps).

## Tips
- Keep trees shallow where possible; offload complexity to scoring models or external services.
- Version control decision logic alongside content assets for traceability.
- Pair with `governance` skill to log approvals for high-impact branches.

---
