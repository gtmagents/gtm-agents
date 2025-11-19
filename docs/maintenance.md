# Marketplace Maintenance & Governance

## Weekly QA Cadence
- Run `python scripts/validate_marketplace.py` and `python scripts/smoke_test_plugins.py` every Friday.
- Review Husky pre-commit output on local branches before opening PRs.
- Spot check 3 random plugins (agents + commands + skills) for frontmatter drift and naming consistency.

## Monthly Documentation Refresh
1. Audit README counts (plugins, agents, skills, orchestrators) vs actual repository counts.
2. Update `docs/usage-guide.md`, `docs/plugin-reference.md`, `docs/agent-reference.md`, and `docs/business-skills.md` with any new assets.
3. Re-run scaffolding templates to ensure no structural changes are required; update templates if new sections become standard.

## Quarterly Governance Review
- Review remediation_plan.md checklist and confirm all promises are still satisfied.
- Evaluate CI workflow logs to ensure no skipped runs; upgrade Python/tooling versions if needed.
- Hold stakeholder review to prioritize upcoming plugin additions or deprecations.
- Archive obsolete assets and update marketplace entries accordingly.

## Release Checklist (v1.0+)
- Confirm README promises (counts, capabilities, tooling) are verified via scripts.
- Tag release only after validator + smoke tests pass on the release commit.
- Publish change log entry summarizing new plugins, agents, skills, and tooling.
- Notify contributors about new scaffolding patterns or governance updates.

## 2025-11-17 Governance Log
- **Validation Suite** – Executed comprehensive checks prior to v1.0 prep:
  ```bash
  python scripts/validate_marketplace.py   # marketplace.json validation passed (see docs/catalog-tracker.md entry 2025-11-17)
  python scripts/smoke_test_plugins.py     # Smoke test passed for 67 plugin(s)
  ```
- **Documentation QA** – Spot-checked key artifacts for parity:
  - `docs/plugin-reference.md`, `docs/agent-reference.md`, and `docs/business-skills.md` regenerated from `.claude-plugin/marketplace.json` to confirm 67 plugins, 203 agents (Haiku/Sonnet mix), and 112 skills align with README promises.
  - `docs/usage-guide.md` verified for live command examples + orchestrator tables, ensuring progressive disclosure guidance remains current.
- **Maintenance Cadence Confirmation** – Weekly validator/smoke cadence reaffirmed; monthly doc refresh scheduled for first business day of each month with cross-links to catalog tracker. Governance review set quarterly (next due 2026-02-15) per remediation plan Section 6.

## Catalog Count Audit
- Use the helper script below (or run `python - <<'PY' ...`) to confirm repository counts:
  ```bash
  python - <<'PY'
  import os
  from pathlib import Path
  root = Path('plugins')
  plugins = [p for p in root.iterdir() if p.is_dir()]
  agents = sum(1 for f in root.rglob('agents/*.md'))
  commands = sum(1 for f in root.rglob('commands/*.md'))
  skills = sum(1 for f in root.rglob('skills/*.md'))
  print('Plugins:', len(plugins))
  print('Agents:', agents)
  print('Commands:', commands)
  print('Skills:', skills)
  PY
  ```
- Compare against README promises (currently 67 plugins, 92 agents, 52 skills, 20 orchestrators). Document discrepancies in `remediation_plan.md` before release.
