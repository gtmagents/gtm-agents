---
name: build-product-go-to-market
description: Creates a compliant go-to-market brief for a financial product with pricing, disclosures, and enablement assets.
usage: /financial-services:build-product-go-to-market --product " SMB Line of Credit" --audience smb --channels email,field,partners --format deck
---

# Command: build-product-go-to-market

## Inputs
- **product** – financial product/offer identifier.
- **audience** – retail | smb | enterprise | partner | investor.
- **channels** – comma-separated channels to activate (email, field, partner, paid, branch, webinar).
- **format** – deck | memo | docset | loom.
- **rate-sheet** – optional file/URL with pricing and underwriting criteria.

## Workflow
1. **Product Intake** – summarize features, eligibility, underwriting, and risk notes.
2. **Persona & Value Mapping** – tailor messaging, proof, and objection handling per audience.
3. **Pricing & Offer Architecture** – outline pricing scenarios, incentives, and guardrails.
4. **Disclosure & Compliance Layer** – attach required disclosures, consent steps, and record-keeping rules.
5. **Enablement Pack** – assemble playbook, FAQs, ROI model references, and success metrics.

## Outputs
- Go-to-market brief (deck/memo) with messaging, pricing, enablement plan.
- Disclosure + compliance appendix referencing approved language.
- Launch checklist with owners, timelines, and measurement plan.

## Agent/Skill Invocations
- `financial-product-strategist` – leads product narrative + pricing guidance.
- `trust-compliance-director` – ensures disclosures and regulatory requirements.
- `financial-product-blueprint` skill – enforces template + data requirements.
- `compliance-statement-library` skill – injects pre-approved disclosures.

---
