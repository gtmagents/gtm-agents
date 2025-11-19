---
name: update-api-reference
description: Generates API reference + guides updates from new schema changes with samples and changelog entries.
usage: /technical-writing:update-api-reference --spec openapi.yaml --audience developers --outputs reference,guide --languages js,python
---

# Command: update-api-reference

## Inputs
- **spec** – OpenAPI/AsyncAPI file path or URL.
- **audience** – developers | partners | internal | admins.
- **outputs** – reference, guide, changelog, tutorial (comma-separated).
- **languages** – code sample languages (js, python, curl, java, go, ruby, csharp).
- **breaking-change** – true/false toggle for migration guidance.

## Workflow
1. **Spec Diff & Analysis** – compare schema version vs prior baseline, note new/changed/deprecated endpoints.
2. **Content Scope** – determine docs to update (reference tables, tutorials, SDK snippets, changelog entries).
3. **Drafting** – produce updated endpoint descriptions, parameters, responses, usage notes, and code samples per language.
4. **Review Loop** – route drafts to engineering/product for validation and to editorial for style compliance.
5. **Publishing & Versioning** – push updates, tag version support, update changelog + migration guidance.

## Outputs
- Updated API reference markdown/HTML with highlighted changes.
- Code sample bundle per requested languages.
- Changelog excerpt + migration guidance (if applicable).

## Agent/Skill Invocations
- `api-docs-editor` – leads spec diff + doc updates.
- `documentation-architect` – ensures IA + governance alignment.
- `api-style-guide` skill – enforces terminology, formatting, and code sample rules.
- `versioning-dashboard` skill – logs version info + deprecation timelines.

---
