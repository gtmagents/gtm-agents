---
name: publish-release-documentation
description: Coordinates release notes, changelog, and enablement updates for a launch.
usage: /technical-writing:publish-release-documentation --release "2026.2" --audiences developers,admins,cs --channels docs,email,in-app --deadline 2025-12-15
---

# Command: publish-release-documentation

## Inputs
- **release** – version identifier or codename.
- **audiences** – comma-separated (developers, admins, cs, marketing, exec, partners).
- **channels** – docs, email, in-app, community, enablement.
- **deadline** – target publication date.
- **locales** – optional localization requirements (en, es, jp, etc.).

## Workflow
1. **Feature Intake** – capture feature list, risk notes, screenshots, approvals needed.
2. **Artifact Plan** – map which assets are needed per audience/channel.
3. **Workback Schedule** – assign owners, deadlines, and review checkpoints.
4. **Quality Review** – enforce style, accuracy, accessibility, and localization steps.
5. **Publishing & Notification** – push updates to doc portals, status pages, comms channels; log changelog entry.

## Outputs
- Release communication packet (notes, changelog, enablement summary).
- Workback tracker with task status and owners.
- QA + localization checklist with sign-offs.

## Agent/Skill Invocations
- `release-documentation-manager` – orchestrates workflow + approvals.
- `documentation-architect` – ensures governance compliance.
- `quality-review-checklist` skill – enforces QA + accessibility steps.
- `versioning-dashboard` skill – updates version support + retirement info.

---
