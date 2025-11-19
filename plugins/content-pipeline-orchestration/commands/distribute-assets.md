---
name: distribute-assets
description: Creates a distribution + amplification plan with schedule, UTMs, and partner alignment.
usage: /content-pipeline-orchestration:distribute-assets --pillar "AI readiness" --channels "blog,email,linkedin" --partners "Acme"
---

# Command: distribute-assets

## Inputs
- **pillar** – content pillar or campaign name.
- **channels** – comma-separated list (blog, CMS, email, social, paid, partner, enablement).
- **partners** – optional partner/community co-marketing list.
- **utm** – optional base UTM template.
- **boosts** – optional paid boost budget or parameters.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator guidance @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Default to **pipeline** (mapping → prep → amplification → measurement → feedback). If channel prep + amplification can run in parallel, log a **diamond** with merge gate.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing objective, stages, task IDs, channel groupings, context passing (UTMs, assets), guardrails, and success metrics (engagement, pipeline, partner reach).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack (Serena for CMS/pixel patches, Context7 for platform docs, Sequential Thinking for retro cadence, Playwright for landing/social QA).
- **Guardrails**: Set retry limit (default 2) for failed publishes; escalation ladder = Distribution Lead → Editorial Director → Marketing Director.
- **Review**: Use `docs/usage-guide.md#orchestration-best-practices-puerto-parity` checklist before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Channel Mapping** – assign assets to channels with timing, CTA, and owner.
2. **Publishing Prep** – outline CMS/social scheduler steps, asset variants, localization, and approvals.
3. **Amplification Plan** – coordinate paid boosts, influencer/partner drops, internal comms, enablement uploads.
4. **Measurement Hooks** – define UTMs, dashboards, alerting, and reporting cadence.
5. **Feedback & Recycling** – schedule retro checkpoints and repurposing opportunities.

## Outputs
- Distribution calendar with timestamps, channels, owners, UTMs, and status.
- Amplification checklist (partners, paid, internal enablement, ABM tie-ins).
- Measurement + feedback plan.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `distribution-lead` – drives publishing + amplification.
- `distribution-checklist` skill – ensures operational rigor per channel.
- `editorial-director` – confirms narrative alignment.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Editorial Director covering Distribution Lead) when specialists unavailable.
- **Escalation triggers**: if UTMs misfire, partner SLAs slip, or alert thresholds breach twice within 48h, trigger escalation to Content + Growth leadership per GTM Agents runbook.
- **Plan maintenance**: update plan JSON + change log whenever channels, partners, or measurement hooks change to maintain GTM Agents-grade auditability.

---
