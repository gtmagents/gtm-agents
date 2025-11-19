---
name: prepare-call
description: Generates a call brief with objectives, agenda, stakeholders, talk tracks, and assets.
usage: /sales-calls:prepare-call --deal "ACME RFP" --stage discovery --personas "CTO,Security" --duration 45m
---

# Command: prepare-call

## Inputs
- **deal** – opportunity/account identifier.
- **stage** – lifecycle stage (prospect, discovery, eval, negotiation, exec).
- **personas** – comma-separated personas expected on the call.
- **duration** – meeting length to inform agenda blocks.
- **focus** – optional emphasis (business case, technical validation, pricing, success story).

## Workflow
1. **Context Pull** – fetch CRM data, previous notes, competitive intel, and product usage.
2. **Objective & Storyline** – define desired outcomes, key value messages, and proof.
3. **Agenda & Roles** – craft timed agenda with presenter/owner per section.
4. **Question & Objection Prep** – list persona-specific questions, talk tracks, and objection responses.
5. **Asset Kit** – recommend decks, demos, references, and follow-up collateral.

## Outputs
- Call brief (objective, agenda, participants, key messages).
- Persona-specific discovery/questions + objection handling.
- Asset checklist with links and owners.

## Agent/Skill Invocations
- `call-strategist` – builds agenda + storyline.
- `conversation-engineer` – supplies talk tracks + objections.
- `deal-analyst` – injects risk signals and inspection notes.
- `call-brief-framework` skill – structures the doc.
- `persona-intel` skill – adds persona-specific insights.

---
