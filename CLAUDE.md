# CLAUDE.md - GTM Agents

## Project Overview

**GTM Agents** is an AI-powered automation platform for Go-To-Market teams. It provides 67 specialized plugins with 203 AI agents, 243 business skills, and 20+ workflow orchestrators designed for sales, marketing, growth, customer success, and revenue operations teams.

**Mission:** Save GTM professionals 15+ hours per week on repetitive busywork by automating prospecting, content creation, analytics, and campaign orchestration.

**Value Proposition:** Average value saved: $25,000+ per user per year.

---

## Repository Structure

```
gtm-agents/
├── .claude-plugin/
│   └── marketplace.json          # Plugin marketplace definition (67 plugins)
├── plugins/                       # 67 GTM-focused plugins
│   └── [plugin-name]/
│       ├── agents/               # Specialized AI agents (.md files)
│       ├── commands/             # Tools and workflows (.md files)
│       └── skills/               # Modular knowledge packages (SKILL.md)
├── workspace/                     # Agent working directory (see below)
├── docs/                         # Documentation
│   ├── agent-reference.md        # All 203 agents
│   ├── business-skills.md        # All 243 skills
│   ├── plugin-reference.md       # Plugin catalog
│   ├── usage-guide.md            # Commands and workflows
│   └── use-cases/                # Real-world examples
├── scripts/                      # Validation and scaffolding
│   ├── scaffold_asset.py         # Create new agents/commands/skills
│   ├── validate_marketplace.py   # Marketplace validation
│   └── smoke_test_plugins.py     # Plugin smoke tests
├── templates/                    # Asset templates
│   ├── agent.md
│   ├── command.md
│   └── skill.md
├── examples/                     # Example implementations
└── inventory.json                # Complete repository state
```

---

## Workspace Structure

The `workspace/` directory provides a consistent folder structure for all agent operations. **All agent outputs should be saved to the appropriate workspace folder.**

### Folder Structure

| Folder | Purpose |
|--------|---------|
| `clients/` | Client-specific folders and projects |
| `campaigns/` | Marketing and sales campaign materials |
| `content/` | Blog posts, articles, and content assets |
| `strategies/` | Content strategies and marketing plans |
| `research/` | Market research and data analysis |
| `social-media/` | Social media content and calendars |
| `email-campaigns/` | Email marketing materials and sequences |
| `reports/` | Performance reports and analytics |
| `templates/` | Reusable templates for deliverables |
| `assets/` | Brand assets, images, and media |
| `leads/` | Lead lists, prospect data, and enrichment |
| `pipelines/` | Sales pipeline snapshots and forecasts |
| `analytics/` | Analytics dashboards and data exports |
| `competitive-intel/` | Competitive research and battlecards |
| `personas/` | Buyer personas and ICP documentation |

### Agent Output Routing

When agents generate outputs, save to the appropriate folder:

| Agent Type | Output Folder |
|------------|---------------|
| Lead generation | `workspace/leads/` |
| Content creation | `workspace/content/` |
| Campaign planning | `workspace/campaigns/` |
| Research & analysis | `workspace/research/` |
| Performance data | `workspace/reports/` or `workspace/analytics/` |
| Competitive intel | `workspace/competitive-intel/` |
| Email sequences | `workspace/email-campaigns/` |
| Social content | `workspace/social-media/` |
| Strategy docs | `workspace/strategies/` |
| Persona development | `workspace/personas/` |

### Client Project Structure

Create subfolders for each client:
```
workspace/clients/
├── acme-corp/
│   ├── briefs/
│   ├── deliverables/
│   └── notes/
└── techstart-inc/
    ├── briefs/
    └── deliverables/
```

### Campaign Organization

Organize campaigns by quarter or initiative:
```
workspace/campaigns/
├── 2025-q1-product-launch/
├── 2025-q2-abm-enterprise/
└── ongoing-nurture/
```

### Naming Conventions

- **Lowercase with hyphens**: `q1-campaign-brief.md`
- **Include dates**: `2025-01-15-pipeline-report.csv`
- **Prefix drafts**: `draft-blog-post-ai-sales.md`
- **Prefix finals**: `final-case-study-acme.pdf`

### File Types

| Extension | Use For |
|-----------|---------|
| `.md` | Documents, briefs, strategies |
| `.csv` | Lead lists, data exports |
| `.json` | Structured data, configurations |
| `.xlsx` | Spreadsheets, reports |
| `.pdf` | Final deliverables |

---

## Core Concepts

### 1. Plugins (67 total)
Self-contained capability packages organized by GTM function:
- **Core Sales** (8): prospecting, pipeline, enablement, coaching, calls, enterprise, operations, account-management
- **Marketing** (13): content, email, social, SEO, paid-media, video, events, PR, brand, automation
- **Growth & Analytics** (9): experiments, revenue-analytics, customer-analytics, BI, PLG, pricing
- **Industry Verticals** (6): B2B SaaS, e-commerce, healthcare, financial services, EdTech, manufacturing
- **Orchestrators** (19): campaign, ABM, nurture, launch, content-pipeline, analytics-pipeline, etc.

### 2. Agents (203 total)
Specialized AI experts with defined roles, activation criteria, and model assignments:
- **Haiku (95)**: Fast execution for data processing, routine tasks
- **Sonnet (80)**: Complex reasoning for strategy and creative work
- **Opus (28)**: Deep analysis for research and executive-level work

### 3. Skills (243 total)
Modular knowledge packages using progressive disclosure:
- Metadata loads first (~100 tokens)
- Full instructions load when needed (<5k tokens)
- Bundled files/scripts load only as required

### 4. Commands
Executable tools following pattern: `/[plugin-name]:[command-name] [parameters]`

---

## Key Commands by Function

### Sales
```bash
/sales-prospecting:generate-leads --criteria "B2B SaaS, 50-500 employees"
/sales-pipeline:analyze-pipeline --quarter Q1
/sales-enablement:create-battlecard --competitor "Competitor X"
/sales-calls:prepare-call --account "Acme Corp"
```

### Marketing
```bash
/content-marketing:content-pipeline "Q1 Thought Leadership" --duration 3months
/campaign-orchestration:launch-campaign "Spring Launch" --budget 75000
/email-marketing:design-campaign --segment enterprise
/seo:build-keyword-strategy --topic "AI automation"
```

### Growth & Analytics
```bash
/growth-experiments:design-experiment --hypothesis "Simplified signup +20%"
/customer-analytics:segment-customers --method behavioral
/revenue-analytics:calculate-ltv --segment Enterprise
```

### Orchestration
```bash
/abm-orchestration:target-accounts --tier 1 --vertical "financial services"
/product-launch-orchestration:assemble-war-room --launch "Q2 Product"
/lead-nurture-orchestration:design-nurture --segment "MQL"
```

---

## Development Guidelines

### Creating New Assets

Use scaffolding scripts:
```bash
python scripts/scaffold_asset.py agent plugins/[plugin]/agents/[name].md
python scripts/scaffold_asset.py command plugins/[plugin]/commands/[name].md
python scripts/scaffold_asset.py skill plugins/[plugin]/skills/[name]/SKILL.md
```

### Naming Conventions
- **Files**: lowercase with hyphens (`lead-researcher.md`)
- **Plugins**: lowercase with hyphens (`sales-prospecting`)
- **Commands**: verb-noun format (`generate-leads`)

### Quality Standards
- All skills require `SKILL.md` with YAML frontmatter (`name`, `description`)
- Skills follow structure: When to Use / Framework / Templates / Tips
- Agents include role descriptions, frameworks, workflows, deliverables
- No placeholder content or TODOs in production files

### Validation
Run before committing:
```bash
python scripts/validate_marketplace.py
python scripts/smoke_test_plugins.py
```

Pre-commit hooks (Husky) run these automatically.

---

## Architecture Principles

### Business-First Design
- Designed for non-technical GTM users
- No coding required
- Natural language interaction supported

### Token Optimization
- Average 3.2 components per plugin (follows Anthropic's 2-8 pattern)
- Progressive disclosure for skills
- Model selection based on task complexity

### Orchestration Patterns
1. **Pipeline**: Sequential stages (brief → build → QA → launch)
2. **Diamond/Fan-out**: Parallel middle stages
3. **Iterative/Conditional**: Reviews, approvals, guardrail branches

### Model Selection Strategy
- **Haiku**: Data processing, routine tasks, fast execution
- **Sonnet**: Strategy, creative work, complex reasoning
- **Opus**: Deep research, executive-level analysis

---

## Plugin Categories

| Category | Count | Examples |
|----------|-------|----------|
| Core Sales | 8 | sales-prospecting, sales-pipeline, enterprise-sales |
| Marketing | 13 | content-marketing, email-marketing, paid-media |
| Growth & Revenue | 9 | growth-experiments, customer-analytics, pricing-strategy |
| Industry Verticals | 6 | b2b-saas, healthcare-marketing, financial-services |
| Strategic Ops | 8 | competitive-intelligence, market-research, brand-strategy |
| Data & Analytics | 5 | data-enrichment-master, revenue-analytics |
| Communication | 7 | copywriting, technical-writing, pr-communications |
| Orchestration | 19 | campaign-orchestration, abm-orchestration, renewal-orchestration |

---

## Common Workflows

### Lead Generation to Close
1. `/sales-prospecting:generate-leads` → Find prospects
2. `/sales-prospecting:build-sequence` → Create outreach
3. `/sales-pipeline:analyze-pipeline` → Track progress
4. `/sales-enablement:create-battlecard` → Competitive prep

### Campaign Launch
1. `/content-marketing:content-pipeline` → Plan content
2. `/campaign-orchestration:launch-campaign` → Execute multi-channel
3. `/marketing-analytics:campaign-report` → Measure results

### Customer Lifecycle
1. `/customer-analytics:segment-customers` → Understand base
2. `/customer-success:monitor-customer-health` → Track health
3. `/renewal-orchestration:forecast-renewals` → Predict retention

---

## Integration Points

### CRM Export
```bash
/sales-prospecting:generate-leads --format salesforce
```

### Marketing Automation
```bash
/email-marketing:sync-hubspot --bidirectional
```

### Analytics
```bash
/analytics:connect-tableau --real-time
```

---

## Testing & Debugging

### Debug Mode
```bash
/debug on
[run command]
/debug off
```

### Get Help
```bash
/help [plugin-name]
```

---

## Agent Skills Compliance

This repository is migrating to the [Agent Skills](https://agentskills.io) open standard maintained by Anthropic. This enables interoperability with Claude Code, Cursor, VS Code, GitHub Copilot, OpenAI Codex, and other compatible agents.

### Compliance Status

| Component | Standard | Status |
|-----------|----------|--------|
| Skills (243) | Agent Skills spec | ✅ Compliant |
| Agents (203) | GTM-specific | Custom extension |
| Commands | GTM-specific | Custom extension |
| Plugins (67) | GTM-specific | Custom extension |

### Skill Structure (Agent Skills Compliant)

Each skill follows the Agent Skills specification:
```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: additional documentation
└── assets/           # Optional: templates, resources
```

### SKILL.md Format

```yaml
---
name: skill-name                    # Required (must match directory)
description: What it does...        # Required (max 1024 chars)
license: Apache-2.0                 # Optional
compatibility: Claude Code          # Optional
metadata:                           # Optional
  author: gtm-agents
  version: "1.0"
  category: sales|marketing|growth
---

# Skill Title

## When to Use
...

## Framework
...

## Templates
...

## Tips
...
```

### Validating Skills

```bash
# Validate single skill
python scripts/validate_skills.py plugins/[plugin]/skills/[skill]

# Validate all skills
python scripts/validate_skills.py

# Generate skills index JSON
python scripts/generate_skills_index.py

# Generate skills index with XML for agent prompts
python scripts/generate_skills_index.py --xml
```

### Skills Index

The repository includes auto-generated skill discovery files:

| File | Purpose |
|------|---------|
| `skills-index.json` | Complete skills catalog with metadata |
| `available_skills.xml` | XML format for agent prompt injection |

Regenerate after adding/modifying skills:
```bash
python scripts/generate_skills_index.py --xml
```

### Portability Notes

- **Skills**: Portable to any Agent Skills compatible product
- **Agents**: GTM-specific format (not portable)
- **Commands**: GTM-specific format (not portable)

See [Migration Plan](docs/MIGRATION_PLAN_AGENTSKILLS.md) for full compliance roadmap.

---

## File Locations

| Resource | Path |
|----------|------|
| Plugin definitions | `.claude-plugin/marketplace.json` |
| Agent files | `plugins/[name]/agents/*.md` |
| Skill files | `plugins/[name]/skills/*/SKILL.md` |
| Command files | `plugins/[name]/commands/*.md` |
| Skills index | `skills-index.json` |
| Skills XML (for prompts) | `available_skills.xml` |
| Documentation | `docs/` |
| Templates | `templates/` |
| Validation scripts | `scripts/` |
| Repository inventory | `inventory.json` |

---

## Contributing

1. Fork and clone the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Use scaffolding scripts for new assets
4. Run validation scripts
5. Update documentation in same PR
6. Follow conventional commits: `feat:`, `fix:`, `docs:`

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Resources

- [Getting Started Guide](GETTING_STARTED.md) - Complete setup for beginners
- [Quick Start Guide](QUICK_START.md) - First commands and workflows
- [Usage Guide](docs/usage-guide.md) - Comprehensive command reference
- [Plugin Reference](docs/plugin-reference.md) - All 67 plugins
- [Agent Reference](docs/agent-reference.md) - All 203 agents
- [Business Skills](docs/business-skills.md) - All 243 skills
- [FAQ](docs/FAQ.md) - Common questions

---

## License

Apache License 2.0 - Copyright 2025 LaunchIQ AI, Inc.

---

## Support

- **Slack**: [GTM Agents Community](https://join.slack.com/t/gtmagents/shared_invite/zt-3iubtzxrn-RpYOb0fPFnTtdoZVcZK3Ww)
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and ideas
- **Buy Me a Coffee**: [Support Development](https://buymeacoffee.com/gtmagents)
