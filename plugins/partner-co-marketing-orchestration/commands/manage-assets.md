---
name: manage-assets
description: Coordinates co-branded asset production, approvals, and distribution across partners.
usage: /partner-co-marketing-orchestration:manage-assets --campaign "AI Launch Tour" --repo drive --approvers "brand,legal"
---

# Command: manage-assets

## Inputs
- **campaign** – reference campaign/program name.
- **repo** – asset repository (Drive, Dropbox, SharePoint, DAM) to track.
- **approvers** – comma-separated stakeholder groups (brand, legal, product, partner).
- **locales** – optional list of localization requirements.
- **compliance** – optional flags for regulated industries.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Asset management typically runs **pipeline** (inventory → guardrails → approvals → versioning → distribution). If approvals across partners can run in parallel, document a **diamond** segment and merge gate in the plan.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing campaign, repositories, task IDs, partner owners, dependency graph (legal, translation, DAM), error handling, and success metrics (approval SLA, asset quality, localization coverage).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for asset diff reviews, Context7 for partner brand/legal guidance, Sequential Thinking for cross-org approval cadences, Playwright for accessibility/landing page QA if needed.
- **Guardrails**: Default retry limit = 2 for failed approvals/uploads; escalation ladder = Asset Manager → Partner Ops → Joint governance council.
- **Review**: Use `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm owners, dependencies, deliverables.

## Workflow
1. **Inventory Setup** – pull required asset list from `co-plan-campaign`, map owners + due dates.
2. **Co-branding Guardrails** – apply templates, logos, disclaimers, and accessibility checks per partner.
3. **Approval Routing** – trigger review workflows, capture feedback, and log decisions.
4. **Version Control** – store final assets with metadata (version, locale, usage notes).
5. **Distribution** – package assets for activation teams with instructions, tracking parameters, and expiration dates.

## Outputs
- Asset tracker (status, owner, reviewer, link, compliance notes).
- Approval log referencing evidence + timestamps.
- Distribution bundle with metadata sheet and partner instructions.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `co-marketing-asset-manager` – oversees production + routing.
- `asset-approval` skill – enforces review workflows and evidence capture.
- `co-branding` skill – validates visual/messaging requirements.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Partner Marketer covering Asset Manager) when leads unavailable.
- **Escalation triggers**: if approvals exceed SLA twice, compliance issues arise, or assets violate guardrails, escalate per GTM Agents rip-cord to partner governance committee.
- **Plan maintenance**: update plan JSON/change log whenever repositories, approvers, or compliance scopes shift.

---
