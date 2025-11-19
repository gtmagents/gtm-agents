#### 4. Run Webinar + Video Programs
```bash
# Plan webinar series
/webinar-automation:plan-series \
  --goal pipeline \
  --cadence monthly \
  --audiences "RevOps,Marketing"

# Configure a specific session
/webinar-automation:configure-session \
  --platform on24 \
  --session "AI Launch" \
  --speakers "CPO,PMM"

# Produce video campaign assets
/video-marketing:design-video-campaign \
  --goal awareness \
  --audience "CIO" \
  --channels "YouTube,LinkedIn"

# Plan production logistics
/video-marketing:plan-production \
  --project "Customer Story" \
  --format documentary \
  --locations "NYC,Remote"
```

#### 5. Drive Customer Lifecycle & Advocacy
```bash
# Map lifecycle journey
/customer-marketing:design-lifecycle-journey \
  --segment enterprise \
  --product "Data Cloud"

# Launch adoption program
/customer-marketing:launch-adoption-program \
  --segment smb \
  --product "AI Copilot" \
  --objective activation

# Activate advocacy program
/customer-marketing:activate-advocacy \
  --program "Advisory Board" \
  --segment enterprise \
  --goal pipeline
```
# GTM Claude Code Plugins - Usage Guide

## Getting Started

Welcome to the GTM (Go-To-Market) Claude Code plugin marketplace! This guide will help you leverage AI agents to automate and enhance your sales, marketing, and growth operations.

## Installation

### Step 1: Add the Marketplace
```bash
/plugin marketplace add gtmagents/gtm-agents
```

### Step 2: Explore Available Plugins
```bash
/plugin list
```

### Step 3: Install Relevant Plugins
```bash
# For sales teams
/plugin install sales-prospecting
/plugin install sales-pipeline
/plugin install sales-enablement

# For marketing teams
/plugin install content-marketing
/plugin install email-marketing
/plugin install social-media-marketing

# For growth teams
/plugin install growth-experiments
/plugin install customer-analytics
/plugin install revenue-analytics
```

## Core Concepts

### 1. Agents
Specialized AI experts that handle specific GTM tasks:
- **Sales Agents**: Prospecting, qualification, pipeline management
- **Marketing Agents**: Content creation, campaign management, analytics
- **Growth Agents**: Experimentation, analytics, customer success

### 2. Skills
Modular knowledge packages that enhance agent capabilities:
- Activate automatically based on context
- Load progressively to minimize token usage
- Provide deep expertise in specific areas

### 3. Commands
Executable tools for specific tasks:
```bash
/[plugin-name]:[command-name] [parameters]
```

### 4. Orchestrators
Multi-agent workflows for complex operations:
- Coordinate multiple agents
- Handle end-to-end processes
- Optimize resource allocation

#### Orchestration Best Practices (GTM Agents Parity)
> Derived from GTM Agents's orchestrator system @puerto/plugins/orchestrator/README.md#1-205.

1. **Assess Complexity First**
   - Orchestrate when work involves 6+ distinct tasks, multiple specialties, or parallel execution opportunities.
   - For simple edits, reply with an "Orchestration Not Needed" note to avoid overhead.
2. **Select the Right Pattern**
   - **Pipeline** for sequential stages (e.g., brief → build → QA → launch).
   - **Diamond/Fan-out** when middle stages can run in parallel (analytics, creative, channel activation).
   - **Iterative/Conditional** for reviews, approvals, or guardrail-triggered branches.
   - Document the pattern choice in the plan so reviewers understand the architecture.
3. **Standard Plan Structure**
   - Include objective, complexity rating, strategy, stages with task IDs, parallelization block, context-passing details, error handling, and success criteria (see GTM Agents JSON example @puerto/plugins/orchestrator/README.md#283-325).
   - Save plans under `.claude/plans/plan-<timestamp>.json` for auditing and reuse.
4. **Bot + Tool Pairing**
   - Planner agent (Sonnet) designs the workflow.
   - Main Claude executes tasks, referencing the orchestration skill for coordination patterns.
   - Use `docs/gtm-essentials.md` tools inside plans (Serena for code edits, Context7 for docs, Sequential Thinking for retros, Playwright for QA).
5. **Error Handling & Guardrails**
   - Define retry strategy (immediate vs with-modification) and max retries.
   - Provide fallbacks for missing agents or tool failures.
   - Set escalation criteria (e.g., escalate to RevOps lead if forecast plan fails twice).
6. **Review Checklist**
   - Confirm agent availability and required tools per task.
   - Validate dependencies and parallel groups.
   - Ensure success criteria + deliverables map to user goals.
   - Once approved, track execution status and update plan if scope changes.

Use this checklist whenever authoring or reviewing GTM orchestration plans to stay aligned with GTM Agents's orchestration standards.

## Common Workflows

### Sales Workflow: Lead Generation to Close

#### 1. Generate and Research Leads
```bash
# Find prospects matching your ICP
/sales-prospecting:generate-leads \
  --criteria "B2B SaaS, 50-500 employees, raised funding last 12 months" \
  --count 50 \
  --enrich comprehensive

# Research specific accounts
/sales-prospecting:research-account "acme.com" --depth detailed
```

#### 2. Build Outreach Sequences
```bash
# Create personalized sequences
/sales-prospecting:build-sequence \
  --industry "SaaS" \
  --persona "VP Sales" \
  --length 5 \
  --personalization high
```

#### 3. Manage Pipeline
```bash
# Analyze current pipeline
/sales-pipeline:analyze-pipeline --quarter Q1

# Forecast revenue
/sales-pipeline:forecast-revenue --method weighted
```

#### 4. Create Sales Collateral
```bash
# Generate battlecards
/sales-enablement:create-battlecard --competitor "Competitor X"

# Build sales playbook
/sales-enablement:build-playbook --segment "Enterprise"
```

### Marketing Workflow: Campaign Launch & Lifecycle

#### 1. Develop Content Strategy
```bash
# Create content plan
/content-marketing:content-pipeline \
  "Q1 Thought Leadership Series" \
  --duration 3months \
  --frequency weekly
```

#### 2. Launch Multi-Channel Campaign
```bash
# Orchestrate full campaign
/campaign-orchestration:launch-campaign \
  "Spring Product Launch" \
  --type product-launch \
  --budget 75000 \
  --timeline 6weeks
```

#### 3. Analyze Performance
```bash
# Get campaign analytics
/marketing-analytics:campaign-report --campaign "Spring Launch"

# Calculate ROI
/marketing-analytics:calculate-roi --period Q1
```

### Growth Workflow: Experimentation

#### 1. Design Experiments
```bash
# Create A/B test
/growth-experiments:design-experiment \
  --hypothesis "Simplified signup increases conversion 20%" \
  --type "A/B" \
  --duration 2weeks
```

#### 2. Analyze Customer Data
```bash
# Segment customers
/customer-analytics:segment-customers \
  --method "behavioral" \
  --output detailed

# Predict churn
/customer-analytics:predict-churn --timeframe 90days
```

#### 3. Calculate Revenue Metrics
```bash
# Analyze cohorts
/revenue-analytics:cohort-analysis --period 12months

# Calculate LTV/CAC
/revenue-analytics:calculate-ltv --segment "Enterprise"
```

## Best Practices

### 1. Start with Clear Objectives
Before using any plugin, define:
- What you want to achieve
- Success metrics
- Timeline and resources

### 2. Use Progressive Complexity
- Start with simple commands
- Add parameters as needed
- Move to orchestrators for complex workflows

### 3. Leverage Skills Intelligently
Skills activate automatically, but you can also:
- Request specific expertise
- Combine multiple skills
- Build on previous context

### 4. Monitor and Iterate
- Track command outputs
- Measure results against objectives
- Refine parameters based on performance

## Advanced Usage

### Chaining Commands
```bash
# Generate leads, then build sequences
/sales-prospecting:generate-leads --criteria "..." | 
/sales-prospecting:build-sequence --personalized
```

### Custom Workflows
```python
# Example: Automated lead nurturing
1. Generate leads weekly
2. Score and prioritize
3. Create personalized content
4. Deploy email sequences
5. Track engagement
6. Alert sales on MQLs
```

### Integration Patterns
```bash
# Export to CRM
/sales-prospecting:generate-leads --format salesforce

# Sync with marketing automation
/email-marketing:sync-hubspot --bidirectional

# Connect to analytics
/analytics:connect-tableau --real-time
```

## Command Reference

### Sales Commands
| Plugin | Command | Description |
|--------|---------|-------------|
| sales-prospecting | generate-leads | Find and enrich prospects |
| sales-prospecting | build-sequence | Create outreach campaigns |
| sales-pipeline | analyze-pipeline | Pipeline health analysis |
| sales-pipeline | forecast-revenue | Predict future revenue |
| sales-enablement | create-battlecard | Competitive intelligence |

### Marketing Commands
| Plugin | Command | Description |
|--------|---------|-------------|
| content-marketing | content-pipeline | Plan content strategy |
| email-marketing | design-campaign | Create email campaigns |
| social-media | social-calendar | Build posting schedule |
| seo-optimization | keyword-research | Find target keywords |

### Growth Commands
| Plugin | Command | Description |
|--------|---------|-------------|
| growth-experiments | design-experiment | Create A/B tests |
| customer-analytics | segment-customers | Behavioral segmentation |
| revenue-analytics | calculate-ltv | Customer lifetime value |

### Orchestration Commands
| Plugin | Command | Description |
|--------|---------|-------------|
| campaign-orchestration | launch-campaign | Full campaign execution |
| abm-orchestration | target-accounts | Account-based account planning |
| lead-nurture-orchestration | design-nurture | Automated nurture journey design |
| product-launch-orchestration | assemble-war-room | Launch governance + war room setup |
| content-pipeline-orchestration | plan-pillar | Content pillar planning to distribution |
| analytics-pipeline-orchestration | define-events | Instrumentation + analytics pipeline prep |
| email-sequence-orchestration | plan-sequences | Lifecycle email sequencing blueprint |
| sales-handoff-orchestration | monitor-sla | SLA tracking + handoff remediation |
| personalization-engine | configure-rules | Personalization decisioning + governance deployment |
| social-scheduler-orchestration | plan-calendar | Social calendar orchestration |
| seo-workflow-orchestration | prioritize-keywords | Keyword strategy + technical workflow |
| revenue-forecasting-pipeline | run-forecast | Revenue forecast scenarios + variance tracking |
| customer-journey-orchestration | map-journey | CX journey mapping + remediation |
| customer-advocacy-orchestration | identify-advocates | Advocacy sourcing + activation |
| community-orchestration | plan-community-calendar | Programming roadmap + event ops |
| intent-signal-orchestration | connect-signals | Signal ingestion + activation readiness |
| renewal-orchestration | forecast-renewals | Renewal forecasting + save plays |
| customer-feedback-orchestration | run-survey | VOC programs + roadmap routing |
| loyalty-lifecycle-orchestration | plan-loyalty | Loyalty design, rewards, and analytics |

### Sales Pipeline & Enablement Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| sales-pipeline | audit-pipeline | Stage hygiene + forecast inspection with recommended actions |
| sales-pipeline | forecast-coverage | Coverage modeling vs goals with gap recommendations |
| sales-pipeline | enablement-kit | Inspection agendas, coaching scripts, follow-up trackers |
| sales-enablement | build-playbook | Motion-specific playbooks with messaging + assets |
| sales-enablement | launch-program | Workback plan for rolling out enablement initiatives |
| sales-enablement | reinforce-program | Post-launch reinforcement cadences and metrics |
| sales-enablement | audit-content | Inventory freshness, adoption, and gap recommendations |

### Sales Operations Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| sales-operations | design-territories | Territory carve-up options with fairness scoring and ROE updates |
| sales-operations | build-capacity-plan | Capacity scenarios vs bookings targets with hiring recommendations |
| sales-operations | design-comp-plan | Compensation blueprints, rate tables, and governance packets |

### Sales Coaching Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| sales-coaching | build-coaching-plan | Individualized coaching plans with goals, drills, and measurement |
| sales-coaching | review-call | Annotated call reviews with scores, clips, and action steps |
| sales-coaching | launch-coaching-program | Cohort program blueprint with curriculum, comms, and KPIs |

### Account Management Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| account-management | build-success-plan | Joint success plan with milestones, KPIs, and expansion hooks |
| account-management | plan-qbr | Executive-ready QBR/EBR agenda with narratives and follow-ups |
| account-management | run-account-review | Account review packet with health signals and plays |

### Sales Calls Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| sales-calls | prepare-call | Call brief with agenda, personas, questions, and asset checklist |
| sales-calls | analyze-call | Post-call analysis with scores, clips, and MEDDIC coverage |
| sales-calls | run-call-review | Manager-led call review kit with scorecards and assignments |

### Enterprise Sales Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| enterprise-sales | plan-pursuit | Pursuit plan with milestones, workstreams, and governance |
| enterprise-sales | build-value-narrative | ROI/TCO models with executive-ready value story |
| enterprise-sales | navigate-procurement | Legal/security procurement workback plan with decision logs |

### Design & Creative Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| design-creative | develop-concepts | Creative concepts, mood boards, and copy hooks from a brief |
| design-creative | manage-production | Production workback plan with tasks, owners, QA checkpoints |
| design-creative | launch-brand-kit | Brand kit packaging with comms + enablement plan |

### Pricing Strategy Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| pricing-strategy | design-packaging | Pricing/packaging matrix with value fences and modeling |
| pricing-strategy | simulate-pricing-impact | Scenario modeling across cohorts with elasticity assumptions |
| pricing-strategy | run-pricing-council | Pricing council agenda, decisions, and launch plan |

### Marketing Analytics Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| marketing-analytics | produce-campaign-report | Cross-channel campaign report with insights + actions |
| marketing-analytics | monitor-channel-pacing | Channel pacing dashboard with guardrail alerts |
| marketing-analytics | evaluate-attribution-models | Attribution comparison with rollout recommendations |

### Paid Media Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| paid-media | design-campaign | Paid media campaign brief with channel mix + budget plan |
| paid-media | launch-ads | Trafficking + QA checklist for launching paid campaigns |
| paid-media | assess-performance | Performance readout with optimization recommendations |

### Marketing Automation Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| marketing-automation | orchestrate-journey | Lifecycle journey orchestration plan with KPIs + segments |
| marketing-automation | configure-workflow | Automation workflow configuration with scoring + routing |
| marketing-automation | monitor-automation | Automation health dashboard with guardrail alerts |

### SEO Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| seo | build-keyword-strategy | Keyword strategy with topic clusters + intent mapping |
| seo | audit-site | Technical SEO audit with prioritized fixes |
| seo | optimize-page | On-page optimization brief with copy + metadata updates |

### Copywriting Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| copywriting | create-messaging-brief | Messaging brief with audience insights + creative hooks |
| copywriting | generate-channel-copy | Multi-channel copy pack with variations + guardrails |
| copywriting | test-and-report | Copy test plan with results summary + next steps |

### Event Marketing Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| event-marketing | design-event | Event strategy brief with goals, personas, and programming |
| event-marketing | manage-production | Production workback plan with vendors + run of show |
| event-marketing | follow-up-impact | Post-event recap with pipeline impact + follow-ups |

### Product Marketing Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| product-marketing | craft-positioning | Positioning + messaging framework with proof points |
| product-marketing | build-launch-plan | Launch workback plan with enablement + KPIs |
| product-marketing | create-competitive-brief | Competitive brief with battlecards + objection handling |

### PR & Communications Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| pr-communications | plan-launch | PR launch plan with messaging, media list, and timeline |
| pr-communications | pitch-media | Media pitch packet with target outlets + talking points |
| pr-communications | manage-crisis | Crisis comms playbook with response templates + escalation |

### Brand Strategy Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| brand-strategy | define-brand-platform | Brand platform with positioning, pillars, proof, rollout plan |
| brand-strategy | design-multi-channel-brand-experience | Multi-channel creative toolkit aligned to brand pillars |
| brand-strategy | run-brand-governance-council | Brand governance council operations with audits + dashboards |

### Competitive Intelligence Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| competitive-intelligence | analyze-competitive-landscape | Competitive landscape brief with threat levels + actions |
| competitive-intelligence | build-battlecard-suite | Battlecard suite refresh with plays + adoption plan |
| competitive-intelligence | run-win-loss-program | End-to-end win/loss program with insights + routing |

### Voice of Customer Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| voice-of-customer | run-voc-listening-tour | Multi-channel listening tour with sampling, tagging, and reporting |
| voice-of-customer | synthesize-voc-insights | VoC insight synthesis with quantified impact + exec narrative |
| voice-of-customer | activate-advocacy-program | Advocacy activation plan tied to VoC themes + cohorts |

### Market Research Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| market-research | run-market-landscape-study | Market landscape study with TAM/SAM/SOM + scenario modeling |
| market-research | orchestrate-qualitative-lab | Qualitative lab orchestration with recruiting + highlight reel |
| market-research | launch-quantitative-survey | Quant survey build, field, and analysis with segmentation |

### Community Building Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| community-building | design-community-strategy | Community strategy with personas, programming, KPIs |
| community-building | launch-community-activation-series | Activation series plan with logistics + follow-up |
| community-building | run-member-insight-sprint | Insight sprint across channels with routing + actions |

### Social Media Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| social-media | plan-calendar | Organic content calendar with briefs + approvals |
| social-media | produce-assets | Asset production workflow with specs + assignments |
| social-media | monitor-performance | Channel performance dashboard with insights |

### Social Media Marketing Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| social-media-marketing | plan-channel-roadmap | Quarterly channel roadmap with goals + experiment plan |
| social-media-marketing | build-social-calendar | Content calendar with briefs, approvals, publishing flow |
| social-media-marketing | monitor-community-sentiment | Sentiment dashboard + escalation recommendations |

### Technical Writing Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| technical-writing | plan-documentation-roadmap | Quarterly documentation roadmap with staffing + KPIs |
| technical-writing | publish-release-documentation | Release documentation workflow with QA + comms plan |
| technical-writing | update-api-reference | API reference updates with samples + changelog |

### Growth Experiments Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| growth-experiments | prioritize-hypotheses | Backlog scoring + capacity plan with guardrail checks |
| growth-experiments | launch-experiment | Launch packet with variants, QA, guardrails, and rollout |
| growth-experiments | synthesize-learnings | Experiment readouts, learnings, and follow-up routing |

### Business Intelligence Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| business-intelligence | plan-bi-roadmap | Prioritized BI roadmap with governance + decision log |
| business-intelligence | build-exec-dashboard | Executive KPI dashboard spec + enablement plan |
| business-intelligence | audit-data-contracts | Data contract health report with remediation tracker |

### Partnership Development Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| partnership-development | design-partner-ecosystem | Partner ecosystem roadmap, tiers, and investment plan |
| partnership-development | build-co-sell-playbook | Co-selling playbook with incentives and enablement |
| partnership-development | run-partner-qbr | Partner QBR packet with KPIs and action tracker |

### B2B SaaS Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| b2b-saas | create-industry-playbook | Vertical POV + solution brief + enablement kit |
| b2b-saas | build-land-adopt-expand-plan | Land/adopt/expand action plan for strategic accounts |
| b2b-saas | prepare-board-readout | Board-ready SaaS briefing with KPIs and asks |

### E-commerce Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| e-commerce | diagnose-conversion-drop | Funnel diagnostic with prioritized experiments |
| e-commerce | plan-merchandising-campaign | Omni-channel merchandising + promo plan |
| e-commerce | launch-retention-program | Lifecycle retention program with KPIs + offers |

### Healthcare Marketing Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| healthcare-marketing | run-compliance-review | HIPAA/FDA campaign compliance review package |
| healthcare-marketing | design-clinical-campaign | Clinically validated campaign brief with review plan |
| healthcare-marketing | orchestrate-patient-journey | Patient journey design with consent + enablement |

### Financial Services Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| financial-services | review-financial-campaign | FINRA/SEC/CFPB compliance review workflow |
| financial-services | build-product-go-to-market | Compliant product GTM brief with pricing + disclosures |
| financial-services | manage-trust-communications | Trust communications kit with FAQ + monitoring plan |

### EdTech Growth Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| edtech-growth | analyze-enrollment-funnel | Inquiry→enrollment diagnostic with prioritized experiments |
| edtech-growth | design-curriculum-partnership | Curriculum alignment + pilot plan for institutional partners |
| edtech-growth | launch-student-success-program | Student success journey with interventions + KPIs |

### Manufacturing Sales Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| manufacturing-sales | qualify-industrial-opportunity | Complex pursuit qualification with stakeholder map |
| manufacturing-sales | build-technical-bid-plan | Technical bid plan with architecture, validation, pricing |
| manufacturing-sales | run-deal-health-review | Executive deal health memo with risks + actions |

### Revenue Analytics Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| revenue-analytics | monitor-revenue-health | Revenue health dashboard with insights + guardrail alerts |
| revenue-analytics | inspect-pipeline-levers | Pipeline diagnostics with stuck-deal callouts |
| revenue-analytics | build-forecast-scenarios | Scenario modeling with action recommendations |

### Customer Success Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| customer-success | monitor-customer-health | Customer health dashboard + risk/opp action plan |
| customer-success | build-adoption-program | Segment-specific adoption program blueprint |
| customer-success | run-escalation-playbook | Escalation governance package with exec comms |

### Product-Led Growth Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| product-led-growth | design-onboarding-journey | Persona-based onboarding journeys with measurement plan |
| product-led-growth | operationalize-pql-routing | PQL scoring + routing automation with playbooks |
| product-led-growth | launch-in-app-experiments | In-app experiments with guardrails and readouts |

### Customer Analytics Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| customer-analytics | segment-customers | Customer segmentation models, scoring logic, and activation plan |
| customer-analytics | monitor-retention | Retention dashboards with risk signals and save plays |
| customer-analytics | synthesize-insights | Cross-channel insight digest with actions per stakeholder |

### Data & Signal Infrastructure Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| data-signal-enrichment | run-waterfall-enrichment | Provider waterfall execution with credit governance |
| data-signal-enrichment | normalize-signals | Signal normalization + identity resolution for downstream systems |
| data-signal-enrichment | audit-provider-health | Provider scorecards with SLA + compliance insights |

### Data Enrichment Master Commands

| Plugin | Command | Summary |
| --- | --- | --- |
| data-enrichment-master | clean-database | Data hygiene workflow with normalization + dedupe checks |
| data-enrichment-master | append-data | Append missing firmo/demographic fields with provider policy guardrails |
| data-enrichment-master | enrich-leads | Lead enrichment workflow with scoring + QA tracking |
| data-enrichment-master | waterfall-enrichment | Master waterfall orchestration with provider fallback rules |

## Troubleshooting

### Common Issues

#### 1. No Results Returned
- Check parameter syntax
- Verify data availability
- Broaden search criteria

#### 2. Slow Performance
- Reduce enrichment level
- Batch large requests
- Use appropriate agent model

#### 3. Integration Failures
- Verify API credentials
- Check rate limits
- Confirm permissions

### Getting Help

1. **Check Documentation**
   ```bash
   /help [plugin-name]
   ```

2. **Debug Mode**
   ```bash
   /debug on
   [run command]
   /debug off
   ```

## Tips & Tricks

### 1. Save Common Workflows
Create aliases for frequently used commands:
```bash
/alias create lead-gen "/sales-prospecting:generate-leads --criteria 'B2B SaaS' --enrich comprehensive"
```

### 2. Use Templates
Many commands support templates:
```bash
/email-marketing:design-campaign --template "webinar-followup"
```

### 3. Bulk Operations
Process multiple items efficiently:
```bash
/sales-prospecting:enrich-bulk --file "prospects.csv"
```

### 4. Schedule Recurring Tasks
```bash
/schedule weekly "/customer-analytics:health-scores --alert-on-risk"
```

## Contributor Automation & Quality Gates

Even though this guide focuses on using the marketplace, creators shipping new assets should follow the built-in tooling:

1. **Scaffold Templates Quickly**
   ```bash
   python scripts/scaffold_asset.py agent plugins/example/agents/new-agent.md
   python scripts/scaffold_asset.py command plugins/example/commands/run-new.md
   python scripts/scaffold_asset.py skill plugins/example/skills/new-skill/SKILL.md
   ```
   These commands copy the canonical structure from `templates/` so frontmatter, sections, and formatting stay consistent.

2. **Local Husky Hook** – every commit automatically runs `scripts/validate_marketplace.py` and `scripts/smoke_test_plugins.py`. Fix failures locally before pushing.

3. **GitHub Actions Workflow** – `.github/workflows/quality-checks.yml` repeats the validator + smoke suite on all pushes/PRs to block regressions in CI.

4. **Documentation Updates** – whenever assets change, update README + docs (usage guide, references) in the same PR to keep parity with the quality gates.

## Security & Compliance

### Data Handling
- All data processed follows GDPR/CCPA guidelines
- PII is encrypted in transit and at rest
- Audit logs maintained for compliance

### Access Control
- Role-based permissions
- API key management
- IP whitelisting available

### Best Practices
1. Never share API credentials
2. Use read-only access where possible
3. Regularly rotate keys
4. Monitor usage logs

## Performance Optimization

### Token Usage
- Skills use progressive disclosure
- Agents selected based on task complexity
- Batch operations to reduce overhead

### Speed Optimization
- Haiku models for routine tasks
- Sonnet models for complex reasoning
- Parallel processing where applicable

### Cost Management
- Monitor token consumption
- Use appropriate enrichment levels
- Cache frequently accessed data

---

Need more help? Check our other documentation:
- [Plugin Reference](plugin-reference.md) - Complete plugin catalog
- [Agent Reference](agent-reference.md) - All agents detailed
- [Business Skills](business-skills.md) - Skills documentation
- [Architecture](architecture.md) - Technical details
