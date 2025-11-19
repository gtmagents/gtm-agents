---
name: technical-bid-library
description: Central repository structure for manufacturing RFP responses, compliance
  statements, and solution modules.
---

# Technical Bid Library Skill

## When to Use
- Preparing RFI/RFP responses requiring technical depth, safety certifications, or compliance proof.
- Accelerating reuse of architecture diagrams, BOMs, and validation plans.
- Enabling distributed teams/partners to contribute to proposals with version control.

## Framework
1. **Module Catalog** – break components into reusable sections (architecture, safety, cybersecurity, sustainability, services).
2. **Metadata & Tagging** – account, industry, standard, version, reviewer, expiration.
3. **Compliance Evidence** – certifications, test results, maintenance schedules, ITAR/export controls.
4. **Content Governance** – approval workflows, change logs, and ownership assignments.
5. **Distribution Layer** – templates for decks, docs, and portal uploads.

## Templates
- Bid response outline with placeholders per section.
- BOM + pricing appendix template with configurable tables.
- Change log sheet capturing edits, reviewers, and attachments.

## Tips
- Store source files (CAD, spreadsheets) alongside PDFs to speed edits.
- Flag expired certifications automatically to prevent use in proposals.
- Pair with `build-technical-bid-plan` for populated submissions.

---
