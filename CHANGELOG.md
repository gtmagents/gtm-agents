# Changelog

All notable changes will be documented in this file. This project follows semantic versioning once v1.0 ships.

## Unreleased
- Added 20th workflow orchestrator (`customer-feedback-orchestration`) plus full marketplace registration for intent, renewal, and customer feedback workflows.
- Expanded documentation to include contributor scaffolding instructions, Husky hooks, CI workflow details, and maintenance playbook.
- Created `docs/maintenance.md` capturing weekly QA, monthly documentation refresh, and quarterly governance cadence.
- Added templated scaffolding assets (`templates/agent.md`, `templates/command.md`, `templates/skill.md`) and helper script `scripts/scaffold_asset.py`.
- Configured `.husky/pre-commit` to run `scripts/validate_marketplace.py` and `scripts/smoke_test_plugins.py` automatically, plus GitHub Actions workflow `quality-checks.yml` to mirror those checks on every push/PR.
