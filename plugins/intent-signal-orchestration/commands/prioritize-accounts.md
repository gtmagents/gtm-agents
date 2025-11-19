---
name: prioritize-accounts
description: Produces ranked account lists with signal context, coverage gaps, and play recommendations.
usage: /intent-signal-orchestration:prioritize-accounts --segment fintech --tiers 3 --min-score 65
---

# Command: prioritize-accounts

## Inputs
- **segment** – optional ICP filter (industry, region, ARR band).
- **tiers** – number of tiers to output (default 3).
- **min-score** – minimum composite signal score required for inclusion.
- **include-customers** – true/false toggle for expansion plays.
- **signals** – optional subset of signal types to weigh heavily.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Prioritization typically runs **pipeline** (score refresh → segmentation → narrative → gap check → activation mapping); if segmentation + narrative analysis run in parallel, document a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing segments, scoring weights, dependency graph (RevOps, sales, automation), error handling, and success metrics (coverage %, activation lift, SLA on follow-ups).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for scoring template diffs, Context7 for ICP documentation, Sequential Thinking for review cadence, Playwright for CRM view QA if applicable.
- **Guardrails**: Default retry limit = 2 for scoring refresh failures; escalation ladder = Intent Analyst → Sales Ops → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before exporting lists to confirm dependencies + approvals.

## Workflow
1. **Score Refresh** – pull latest composite scores from `intent-analyst` datasets and apply decay.
2. **Segmentation & Tiering** – bucket accounts by fit + intent score; highlight data sufficiency.
3. **Signal Narrative** – summarize top topics, key events, and recency for each tier.
4. **Gap & Risk Check** – flag missing personas, conflicting signals, or active suppression rules.
5. **Activation Mapping** – recommend plays (ads, SDR outreach, executive program) with owners.

## Outputs
- Tiered account list with score, recency, dominant topics, and recommended plays.
- Coverage gap report (missing contacts, stale data, disqualified signals).
- Export-ready CSV/JSON for CRM or engagement platforms.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `intent-analyst` – refreshes and validates scoring logic.
- `sales-liaison` – reviews activation suggestions and persona coverage.
- `signal-scoring` skill – documents weighting logic per tier.
- `suppression-logic` skill – ensures risky accounts remain parked.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Sales Ops covering Analyst) when owners unavailable.
- **Escalation triggers**: escalate if coverage gaps exceed threshold twice or suppression logic conflicts; log remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log when tiers, thresholds, or weighting methodology change.

---
