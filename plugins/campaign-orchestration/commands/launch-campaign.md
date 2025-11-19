---
name: launch-campaign
description: Coordinate strategy, creative, channels, and analytics for multi-agent marketing campaigns.
usage: /campaign-orchestration:launch-campaign "Q1 Product Launch" --type product-launch --budget 100000 --timeline 8
---

# Campaign Orchestration Workflow

Multi-agent orchestration for end-to-end marketing campaign execution, coordinating strategy, creative, distribution, and analytics across multiple channels.

## Command Syntax
```bash
/campaign-orchestration:launch-campaign "<campaign_name>" --type <type> --budget <amount> --timeline <weeks>
```

## Orchestration Overview

This orchestrator coordinates 8+ specialized agents to execute comprehensive marketing campaigns:

```
┌────────────────────────────────────────┐
│        Campaign Orchestrator           │
│         (Master Coordinator)           │
└────────────────┬───────────────────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
┌───▼──────┐          ┌───────▼──────┐
│Strategy  │          │ Creative     │
│Agents    │          │ Agents       │
├──────────┤          ├──────────────┤
│Campaign  │          │Content       │
│Strategist│          │Creator       │
│Audience  │          │Designer      │
│Analyst   │          │Copy Writer   │
└──────────┘          └──────────────┘
    │                         │
    └────────────┬────────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
┌───▼──────┐          ┌───────▼──────┐
│Channel   │          │ Analytics    │
│Agents    │          │ Agents       │
├──────────┤          ├──────────────┤
│Email     │          │Data Analyst  │
│Social    │          │Attribution   │
│Paid Media│          │ROI Calculator│
│SEO       │          │Dashboard     │
└──────────┘          └──────────────┘
```

### GTM Agents Pattern & Plan Checklist
> Based on GTM Agents's orchestrator guidance @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern Selection**: default to **pipeline** (Strategy → Creative → Channels → Optimization). Switch to **diamond/fan-out** when creative/analytics work can parallelize; note pattern choice in the plan header.
- **Plan Schema**: every `/campaign-orchestration` run must emit a JSON plan saved under `.claude/plans/plan-<timestamp>.json` with objective, complexity, stages, task IDs, parallelization block, context-passing notes, error handling, and success criteria.
- **Tool Hooks**: reference `docs/gtm-essentials.md` tools inside plan steps (Serena for code/landing-page patches, Context7 for doc lookups, Sequential Thinking for retros, Playwright for QA checkpoints).
- **Guardrails & Escalation**: define retry strategy (immediate vs modified), max retries (default 2), and escalation path (Campaign Strategist → RevOps lead) for failures.
- **Review Flow**: before execution, run the checklist from `docs/usage-guide.md#orchestration-best-practices-puerto-parity` (agent availability, dependency validation, deliverables alignment).

## Workflow Phases

### Phase 1: Strategy Development (Days 1-5)
**Lead Agent**: Campaign Strategist (Sonnet)
**Supporting Agents**: Audience Analyst, Competitive Analyst

```yaml
Tasks:
  - Define campaign objectives and KPIs
  - Analyze target audience and segments
  - Research competitive landscape
  - Develop messaging framework
  - Create campaign brief

Outputs:
  - Campaign strategy document
  - Audience personas
  - Messaging matrix
  - Success metrics framework
```

### Phase 2: Creative Development (Days 6-15)
**Lead Agent**: Creative Director (Sonnet)
**Supporting Agents**: Content Creator, Designer, Copywriter

```yaml
Tasks:
  - Develop creative concepts
  - Write core content pieces
  - Design visual assets
  - Create video scripts
  - Build landing pages

Outputs:
  - Content library
  - Design assets
  - Landing pages
  - Video content
  - Email templates
```

### Phase 3: Channel Setup (Days 16-20)
**Lead Agent**: Channel Coordinator (Haiku)
**Supporting Agents**: Email Marketer, Social Manager, Paid Specialist

```yaml
Tasks:
  - Configure email automation
  - Set up social campaigns
  - Launch paid advertising
  - Optimize for SEO
  - Prepare PR outreach

Outputs:
  - Email sequences live
  - Social calendar scheduled
  - Ads launched
  - SEO optimizations complete
  - PR pitches sent
```

### Phase 4: Launch & Optimization (Days 21+)
**Lead Agent**: Performance Optimizer (Sonnet)
**Supporting Agents**: Data Analyst, Attribution Specialist

```yaml
Tasks:
  - Monitor real-time performance
  - A/B test variations
  - Optimize based on data
  - Scale winning elements
  - Report on results

Outputs:
  - Performance dashboards
  - Optimization reports
  - Test results
  - ROI analysis
  - Executive summary
```

## Agent Coordination Matrix

| Agent | Role | Phase | Handoffs |
|-------|------|-------|----------|
| Campaign Strategist | Overall strategy | 1 | → Creative Director |
| Audience Analyst | Segment definition | 1 | → All agents |
| Creative Director | Creative oversight | 2 | → Channel agents |
| Content Creator | Content production | 2 | → Channel agents |
| Email Marketer | Email execution | 3 | → Data Analyst |
| Social Manager | Social execution | 3 | → Data Analyst |
| Paid Specialist | Paid media | 3 | → ROI Calculator |
| Data Analyst | Performance tracking | 4 | → All agents |

## Campaign Types

### Product Launch Campaign
```bash
/campaign-orchestration:launch-campaign "Q1 Product Launch" \
  --type product-launch \
  --budget 100000 \
  --timeline 8
```

**Specialized Workflow**:
- Pre-launch buzz building
- Launch day coordination
- Post-launch momentum
- Customer success stories

### Demand Generation Campaign
```bash
/campaign-orchestration:launch-campaign "Enterprise Lead Gen" \
  --type demand-gen \
  --budget 50000 \
  --timeline 12
```

**Specialized Workflow**:
- Content pillar development
- Lead magnet creation
- Nurture sequence design
- Sales handoff optimization

### Brand Awareness Campaign
```bash
/campaign-orchestration:launch-campaign "Brand Awareness 2024" \
  --type brand \
  --budget 200000 \
  --timeline 16
```

**Specialized Workflow**:
- Brand narrative development
- Influencer partnerships
- PR coordination
- Event integration

## Coordination Protocols

### Communication Flow
```
1. Daily Standups: Quick sync between active agents
2. Phase Gates: Formal handoffs with deliverable review
3. Escalation Path: Issues → Lead Agent → Orchestrator
4. Feedback Loops: Performance data → All agents
```

### Decision Framework
```
if (performance < target) {
  1. Data Analyst identifies issue
  2. Relevant agent proposes solution
  3. Orchestrator approves change
  4. Implementation within 24 hours
}
```

### Quality Checkpoints
- Strategy approval before creative
- Creative review before channel setup
- Soft launch before full launch
- Daily optimization cycles
- Plan file updated when scope or owners change (keep `.claude/plans` log in sync).

## Resource Allocation

### Agent Time Allocation
```
Strategy Phase: 
  - Strategist: 100%
  - Analysts: 75%
  - Others: 25%

Creative Phase:
  - Creative team: 100%
  - Strategist: 25%
  - Channel agents: 50%

Execution Phase:
  - Channel agents: 100%
  - Analytics: 100%
  - Creative: 25%
```

### Budget Distribution (Typical)
- Creative Development: 20%
- Paid Media: 40%
- Technology/Tools: 10%
- Content Creation: 20%
- Analytics/Reporting: 10%

## Success Metrics

### Campaign KPIs
```python
{
  "reach": {
    "impressions": target * 1.2,
    "unique_visitors": target,
    "engagement_rate": "5%+"
  },
  "conversion": {
    "leads_generated": 500,
    "mql_rate": "40%",
    "sql_rate": "20%"
  },
  "revenue": {
    "pipeline_generated": budget * 10,
    "revenue_attributed": budget * 3,
    "roi": "300%+"
  }
}
```

### Agent Performance Metrics
- Strategy accuracy: 85%+
- Creative approval rate: 90%+
- Channel performance: Above benchmark
- Data accuracy: 99%+

## Output Deliverables

### Campaign Launch Kit
```
📁 Campaign Assets
├── 📄 Strategy Document
├── 📁 Creative Files
│   ├── 🎨 Design Assets
│   ├── 📝 Copy Docs
│   └── 🎥 Video Files
├── 📁 Channel Configs
│   ├── 📧 Email Sequences
│   ├── 📱 Social Calendar
│   └── 💰 Ad Campaigns
└── 📊 Analytics Dashboard
```

### Executive Report Template
```
Campaign: [Name]
Duration: [Timeline]
Budget: [Amount]

Results Summary:
- Reach: [Metrics]
- Engagement: [Metrics]
- Conversions: [Metrics]
- Revenue: [Metrics]

Key Insights:
1. [Top performing element]
2. [Surprising finding]
3. [Optimization opportunity]

ROI: [Percentage]
Recommendation: [Next steps]
```

## Error Handling & Recovery

### Common Issues & Solutions
| Issue | Detection | Resolution | Recovery Time |
|-------|-----------|------------|---------------|
| Low engagement | Analytics agent | Creative refresh | 48 hours |
| Poor conversion | Attribution agent | Landing page optimization | 24 hours |
| Budget overrun | Finance monitor | Channel reallocation | Same day |
| Technical failure | System alerts | Backup activation | 1 hour |

### GTM Agents-Inspired Safeguards
- **Retry strategy**: retry once immediately with adjusted parameters; on second failure, escalate to orchestrator for manual intervention.
- **Fallback agents**: if specialized agents unavailable, document substitutions (e.g., Content Strategist covering Copywriter) in the plan.
- **Escalation triggers**: if KPIs breach guardrails twice in 48h (see lifecycle-mapping skill), notify Marketing Director + RevOps lead.

## Integration Points

- **Project Management**: Asana, Monday.com
- **Creative Tools**: Figma, Canva, Adobe
- **Marketing Platforms**: HubSpot, Marketo, Salesforce
- **Analytics**: Google Analytics, Mixpanel, Heap
- **Communication**: Slack, Teams

---

*Orchestration Model: claude-sonnet-4 for strategy, claude-haiku-4-5 for execution*
