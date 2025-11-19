---
name: compliance-statement-library
description: Repository pattern for pre-approved financial disclosures and claim language.
---

# Compliance Statement Library Skill

## When to Use
- Assembling marketing campaigns, sales decks, or product pages requiring disclosures.
- Responding to regulator/legal review comments.
- Updating messaging after rate changes, product updates, or new regulations.

## Framework
1. **Statement Catalog** – define taxonomy (product, channel, audience, regulation, status).
2. **Approval Metadata** – reviewer, date, expiration, evidence references, risk level.
3. **Usage Guidelines** – instructions on required pairing, placement, and typography.
4. **Localization & Accessibility** – translations, readability requirements, alt-text guidelines.
5. **Change Control** – versioning, diffs, and notification hooks for GTM teams.

## Templates
- Disclosure record form with required fields (text, context, owner, evidence, reviewer).
- Usage checklist to confirm placement and pairing rules.
- Version change log referencing prior statements.

## Tips
- Link statements to product SKUs/offers so updates cascade automatically.
- Store short and long-form variants for different channels (email vs landing page).
- Pair with `review-financial-campaign` and `build-product-go-to-market` for automation.

---
