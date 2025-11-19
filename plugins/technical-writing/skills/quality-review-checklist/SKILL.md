---
name: quality-review-checklist
description: Checklist covering accuracy, style, accessibility, and localization requirements
  for documentation releases.
---

# Quality Review Checklist Skill

## When to Use
- Pre-publication QA for docs, tutorials, and release notes.
- Auditing inherited content during migrations.
- Training new contributors on required review steps.

## Framework
1. **Accuracy & Coverage** – verify features, parameters, screenshots, and examples match latest build.
2. **Style & Voice** – enforce style guide, terminology, formatting, and tone per audience.
3. **Accessibility** – heading hierarchy, alt-text, captions, contrast, keyboard navigation, screen-reader cues.
4. **Localization & Compliance** – translation scope, legal disclaimers, export controls, privacy statements.
5. **Version Control** – version tags, changelog entries, rollback plan, owner assignments.

## Templates
- QA checklist spreadsheet with pass/fail + notes fields.
- Reviewer sign-off sheet with timestamps and comments.
- Issue log for follow-up fixes grouped by severity.

## Tips
- Pair reviewers (technical + editorial) for faster turnarounds.
- Automate linting scripts (links, markdown, accessibility) and attach results to the checklist.
- Use with `publish-release-documentation` for final approvals.

---
