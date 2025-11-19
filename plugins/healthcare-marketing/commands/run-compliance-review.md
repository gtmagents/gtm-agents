---
name: run-compliance-review
description: Executes HIPAA/FDA/FTC compliance review for healthcare marketing campaigns.
usage: /healthcare-marketing:run-compliance-review --campaign "Cardio Webinar" --channels email,landing --risk-level moderate
---

# Command: run-compliance-review

## Inputs
- **campaign** – campaign/program identifier or brief ID.
- **channels** – comma-separated list (email, landing, paid, webinar, field, events).
- **risk-level** – low | moderate | high; influences approval path and SLA.
- **claims** – optional file/URL to clinical claims or messaging hierarchy.
- **audience** – providers | payers | patients | mixed.

## Workflow
1. **Brief Intake** – pull campaign context, creative, data flows, and offer details.
2. **Regulatory Checklist** – evaluate HIPAA, FDA, FTC, regional privacy rules per channel.
3. **Gap Analysis** – flag unsupported claims, consent gaps, or escalation requirements.
4. **Approval Routing** – generate reviewer list (legal, medical, privacy) with tasks + due dates.
5. **Documentation** – log decisions, conditions, and expiration dates in compliance archive.

## Outputs
- Compliance memo summarizing risks, mitigations, and approvals needed.
- Reviewer task list with due dates and supporting materials.
- Audit-ready packet (evidence, annotated assets, approval history).

## Agent/Skill Invocations
- `compliance-marketing-director` – leads assessment + escalation.
- `clinical-campaign-strategist` – validates claims vs supporting evidence.
- `compliance-briefing-kit` skill – enforces checklist + output format.
- `regulatory-review-checklist` skill – ensures routing rules and documentation completeness.

---
