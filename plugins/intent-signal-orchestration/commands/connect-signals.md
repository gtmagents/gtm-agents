---
name: connect-signals
description: Sets up data connections, schemas, and monitoring for intent, product, and engagement feeds.
usage: /intent-signal-orchestration:connect-signals --sources "bombora,g2,product" --accounts enterprise --topics "security,automation"
---

# Command: connect-signals

## Inputs
- **sources** – comma-separated list of feeds (bombora, 6sense, g2, product, web, community).
- **accounts** – optional filter (enterprise, midmarket, smb) or named account list file.
- **topics** – optional topics to whitelist for ingestion.
- **window** – lookback period (e.g., 30d) for initial sync.
- **warehouse** – destination schema or dataset identifier.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Signal connection typically runs **pipeline** (inventory → schema → pipelines → quality → activation). If schema mapping + pipeline provisioning run in parallel, document a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing source inventory, auth, task IDs, dependency graph (data eng, security, RevOps), error handling, and success metrics (freshness, coverage %, SLA compliance).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for schema diffs, Context7 for API docs + vendor SLAs, Sequential Thinking for rollout reviews, Playwright for any UI-based connector QA.
- **Guardrails**: Default retry limit = 2 for ingestion failures; escalation ladder = Data Engineer → Intent Analyst → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before handoff to confirm dependencies + approvals logged.

## Workflow
1. **Inventory & Access** – validate API keys, service accounts, and throttling limits per source.
2. **Schema Alignment** – map identifiers, normalize fields, and define topic taxonomy.
3. **Pipelines & Storage** – configure ingestion jobs, dedupe logic, and retention policies in the warehouse.
4. **Data Quality Gates** – set freshness monitors, anomaly detection, and alert routing.
5. **Activation Hooks** – expose curated tables/feeds to `prioritize-accounts` and downstream automations.

## Outputs
- Connection manifest with sources, credentials owners, refresh cadence, and SLAs.
- Warehouse schema doc plus sample queries for RevOps/data teams.
- Monitoring dashboard setup instructions + webhook alerts.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `intent-analyst` – ensures topics + scoring fields align with GTM objectives.
- `automation-lead` – configures pipelines and alerting.
- `signal-scoring` skill – validates data completeness for scoring weights.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., automation-lead covering analyst) when owners unavailable.
- **Escalation triggers**: escalate if freshness SLAs miss twice or security reviews fail; log remediation in plan JSON per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log whenever sources, schemas, or monitoring thresholds change to maintain audit continuity.

---
