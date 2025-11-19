---
name: plan-sequences
description: Builds multi-touch email sequence architectures with segments, offers, and testing roadmap.
usage: /email-sequence-orchestration:plan-sequences "Expansion Play" --stage expansion --length 6
---

# Command: plan-sequences

## Inputs
- **name** – internal title for the sequence or program.
- **stage** – lifecycle moment (onboarding, nurture, expansion, win-back).
- **length** – number of touches (integer) or timeframe (e.g., 6weeks).
- **audiences** – optional CSV/list describing primary segments.
- **offers** – optional summary of value props to rotate.

## Workflow
1. **Brief Intake** – confirm goals, ICP, compliance constraints, and triggering events.
2. **Segment Mapping** – align audiences with triggers, suppression rules, and dynamic content tokens.
3. **Sequence Drafting** – define each touch with timing, channel, offer, personalization notes.
4. **Testing Roadmap** – pair priority steps with hypotheses, sample sizes, and guardrails.
5. **Handoff Packet** – consolidate creative requirements, data needs, and measurement plan.

## Outputs
- Sequence architecture table (touch #, delay, audience, CTA, owner, KPI).
- Personalization requirements matrix (field, fallback, source system).
- Experiment backlog prioritized by potential lift + complexity.

## Agent/Skill Invocations
- `email-architect` – leads overall journey design and architecture.
- `cadence-design` skill – ensures spacing and pacing best practices.
- `experiment-analyst` – partners on testing roadmap creation.

---
