---
name: signal-scoring
description: Use to design composite intent scoring models with decay, weighting,
  and governance.
---

# Signal Scoring Blueprint Skill

## When to Use
- Designing or revising multi-source signal scoring models.
- Auditing why certain accounts jump tiers or stay suppressed.
- Communicating scoring logic to RevOps, sales, and compliance stakeholders.

## Framework
1. **Source Inventory** – list each signal type, freshness cadence, coverage %, and reliability.
2. **Weighting Model** – assign base weights, adjust for persona relevance, and define topic multipliers.
3. **Decay Curves** – set time-based decay (hours/days/weeks) per signal category with thresholds for expiration.
4. **Thresholds & Tiers** – document what scores map to activation tiers, nurture status, or executive escalation.
5. **Governance** – outline ownership, review cadence, and change management triggers.

## Templates
- Scoring worksheet (source, weight, decay, threshold, notes).
- Tier definition matrix with recommended plays.
- Change log template capturing rationale, data evidence, and approvals.

## Tips
- Blend at least two independent signals before green-lighting high-effort plays.
- Version control your scoring logic and share diffs in RevOps channels.
- Pair with `suppression-logic` to avoid conflicting triggers.

---
