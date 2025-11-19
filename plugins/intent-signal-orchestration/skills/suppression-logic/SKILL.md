---
name: suppression-logic
description: Use to define guardrails that pause signal-driven plays when accounts
  are risky, saturated, or in-flight elsewhere.
---

# Suppression Logic Playbook Skill

## When to Use
- Building global do-not-touch rules shared across marketing, sales, and success workflows.
- Investigating why an account never triggers despite strong intent scores.
- Coordinating with legal, finance, or product teams on sensitive outreach windows.

## Framework
1. **Reason Taxonomy** – categorize suppression triggers (legal/compliance, commercial conflicts, lifecycle constraints, technical issues).
2. **Detection Methods** – outline data sources and queries that flag each trigger (support tickets, security incidents, open opps, payment status).
3. **Routing & Ownership** – assign who can override or expire each suppression (CSM, legal, exec sponsor).
4. **Duration Logic** – define cooling periods, review cadences, and auto-expiration rules.
5. **Audit Trail** – log change history, approvals, and tie-ins to automation or orchestrator commands.

## Templates
- Suppression matrix (reason, trigger condition, owner, duration, override path).
- Compliance checklist for regulated industries (financial services, healthcare).
- Alert + reporting format for surfaced conflicts.

## Tips
- Mirror CRM/MAP suppression lists to prevent channel drift.
- Create heartbeat alerts when suppression counts spike unexpectedly.
- Pair with `signal-scoring` adjustments so suppressed accounts stop draining rep capacity.

---
