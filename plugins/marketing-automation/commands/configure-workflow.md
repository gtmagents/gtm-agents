---
name: configure-workflow
description: Produces implementation instructions for building the automation inside MAP/CRM tools, including QA steps.
usage: /marketing-automation:configure-workflow --journey onboarding --platform hubspot
---

# Command: configure-workflow

## Inputs
- **journey** – reference journey ID or description.
- **platform** – automation platform (hubspot, marketo, braze, iterable, customerio, etc.).
- **assets** – optional list of email/SMS/push templates to wire.
- **qa_mode** – true/false to include full regression suite.

## Workflow
1. **Blueprint Sync** – pull orchestration diagram + requirements.
2. **Platform Mapping** – translate logic into platform-specific objects (smart lists, workflows, campaigns, journeys).
3. **Configuration Steps** – detailed instructions for triggers, branches, waits, webhook/API calls, personalization tokens.
4. **QA Matrix** – build test plan (seed recipients, device/browser, fallback paths, compliance checkpoints).
5. **Launch Checklist** – approvals, scheduling, monitoring, rollback plan.

## Outputs
- Step-by-step build guide with screenshots/snippets.
- QA checklist and evidence log template.
- Launch readiness form (owners, go-live date, monitoring links).

## Agent/Skill Invocations
- `nurture-operator` – executes build tasks.
- `workflow-testing` skill – ensures QA rigor.
- `data-orchestrator` – validates data/suppression wiring.

---
