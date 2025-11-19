---
name: target-accounts
description: Generates a prioritized ABM target list with tiering, buying committees, and activation triggers.
usage: /abm-orchestration:target-accounts --segment enterprise --count 50 --intent true
---

# Command: target-accounts

## Inputs
- **segment** – industry/region/ICP filter.
- **count** – number of accounts to return per tier.
- **intent** – whether to pull live intent signals (true/false).
- **customers** – include/exclude customers for expansion plays.
- **notes** – optional constraints (ex: “no active opps”).

## Workflow
1. **Data Merge** – combine CRM, enrichment, intent, product usage, partner data.
2. **Scoring & Tiering** – apply ideal customer fit, engagement, pipeline stage to produce T1/T2/T3 split.
3. **Buying Committee Mapping** – surface key personas, roles, known contacts.
4. **Signal Highlights** – list recent intent spikes, product usage, news, hiring signals.
5. **Activation Suggestions** – propose first-touch plays per tier.

## Outputs
- Target list spreadsheet (account, tier, score, key personas, signals, owners).
- Buying committee summary + contact gaps.
- Recommended next play per tier (event invite, executive briefing, nurture).

## Agent/Skill Invocations
- `abm-strategist` – ensures scoring logic aligns with program goals.
- `account-tiering` skill – enforces tier definitions.
- `signal-intel` skill – aggregates intent/product signals.

---
