# GTM Agents Workspace

This workspace provides a consistent folder structure for all GTM agent operations. Use these directories to organize client work, campaigns, content, and deliverables.

## Folder Structure

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

## Usage Guidelines

### Client Projects
Create a subfolder for each client under `clients/`:
```
clients/
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
campaigns/
├── 2025-q1-product-launch/
├── 2025-q2-abm-enterprise/
└── ongoing-nurture/
```

### Content Workflow
Structure content by type and status:
```
content/
├── blog/
│   ├── drafts/
│   ├── review/
│   └── published/
├── whitepapers/
└── case-studies/
```

### Lead Management
Organize leads by source and stage:
```
leads/
├── inbound/
├── outbound/
├── enriched/
└── qualified/
```

## Naming Conventions

- Use lowercase with hyphens: `q1-campaign-brief.md`
- Include dates where relevant: `2025-01-15-pipeline-report.csv`
- Prefix drafts: `draft-blog-post-ai-sales.md`
- Prefix finals: `final-case-study-acme.pdf`

## File Types

| Extension | Use For |
|-----------|---------|
| `.md` | Documents, briefs, strategies |
| `.csv` | Lead lists, data exports |
| `.json` | Structured data, configurations |
| `.xlsx` | Spreadsheets, reports |
| `.pdf` | Final deliverables |

## Agent Outputs

When agents generate outputs, they should save to the appropriate folder:
- Lead generation → `leads/`
- Content creation → `content/`
- Campaign plans → `campaigns/`
- Research findings → `research/`
- Performance data → `reports/` or `analytics/`
