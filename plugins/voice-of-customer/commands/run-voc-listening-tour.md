---
name: run-voc-listening-tour
description: Plan and execute a multi-channel listening tour with curated participants and reporting cadence.
usage: /voice-of-customer:run-voc-listening-tour --focus retention --personas cxo,admin --channels survey,interview,community --window 45d
---

# Command: run-voc-listening-tour

## Inputs
- **focus** – key objective (retention, onboarding, roadmap, experience, adoption).
- **personas** – comma-separated persona or role targets.
- **channels** – listening modes to activate (survey, interview, office-hours, community, support-log, review).
- **window** – duration for the tour (30d default).
- **incentives** – optional description of incentive or thank-you program.

## Workflow
1. **Scoping & Sampling** – build participant matrix across personas, lifecycle, regions, ARR bands.
2. **Channel Setup** – configure survey instruments, interview guides, scheduling, and community prompts.
3. **Coordination** – send invites, reminders, and ensure CS/AM coverage for high-value accounts.
4. **Capture & Tagging** – collect responses, tag sentiment/driver/persona, and store in VoC workspace.
5. **Reporting & Follow-up** – assemble interim readouts, final summary, and action assignments.

## Outputs
- Listening tour project plan with channel playbooks and timelines.
- Participant tracker with status, notes, and incentives.
- Executive summary + action register for each focus area.

## Agent/Skill Invocations
- `voc-program-director` – governs strategy, sampling, and reporting cadence.
- `customer-insights-lab-analyst` – ensures tagging rigor and insight synthesis.
- `customer-feedback-taxonomy` skill – enforces tagging/metadata standards.
- `closed-loop-playbook` skill – routes insights to owners with SLA templates.

---
