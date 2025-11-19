---
name: review-financial-campaign
description: Runs FINRA/SEC/CFPB compliance review for financial services campaigns with disclosures and approvals.
usage: /financial-services:review-financial-campaign --campaign "Wealth Webinar" --channels email,landing,paid --risk-level high
---

# Command: review-financial-campaign

## Inputs
- **campaign** – campaign/program identifier.
- **channels** – comma-separated list (email, landing, paid, webinar, in-app, field).
- **risk-level** – low | medium | high (determines approval depth and SLA).
- **product** – optional product/offer reference for context.
- **audience** – retail | smb | enterprise | investor | partner.

## Workflow
1. **Intake & Context** – gather creative, copy, targeting, data flows, and offer details.
2. **Regulation Checklist** – evaluate FINRA/SEC/CFPB/GLBA rules plus state disclosures.
3. **Gap Analysis** – flag unsupported claims, disclosure gaps, record-keeping needs.
4. **Approval Routing** – assign legal, risk, compliance reviewers with due dates and tasks.
5. **Documentation** – compile approval memo, disclosure list, and archive package.

## Outputs
- Compliance assessment with risks, remediation recommendations, and required disclosures.
- Reviewer task list with owners, status, and due dates.
- Audit-ready package (annotated assets, decision log, evidence links).

## Agent/Skill Invocations
- `trust-compliance-director` – leads assessment + escalation.
- `financial-product-strategist` – validates claims vs product specs.
- `compliance-statement-library` skill – injects approved disclosures.
- `regulator-briefing-playbook` skill – formats output for legal/regulator review.

---
