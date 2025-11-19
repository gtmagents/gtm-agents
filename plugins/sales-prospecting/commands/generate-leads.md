---
name: generate-leads
description: Generate ICP-qualified leads with enrichment, intent signals, and export-ready outputs.
usage: /sales-prospecting:generate-leads --criteria "B2B SaaS" --count 50 --enrich comprehensive
---

# Generate Leads Command

Generate qualified leads based on ideal customer profile (ICP) criteria with enriched contact information and buying signals.

## Command Syntax
```bash
/sales-prospecting:generate-leads --criteria <criteria> --count <number> --enrich <level>
```

## Parameters

- `--criteria`: ICP definition (industry, size, tech stack, location, etc.)
- `--count`: Number of leads to generate (default: 20)
- `--enrich`: Enrichment level (basic|standard|comprehensive)
- `--intent`: Include intent signals (true|false, default: true)
- `--contacts`: Number of contacts per account (default: 3)
- `--format`: Output format (csv|json|salesforce|hubspot)

## Examples

### Basic Lead Generation
```bash
/sales-prospecting:generate-leads --criteria "SaaS companies, 50-500 employees, using Salesforce"
```

### Comprehensive Account Research
```bash
/sales-prospecting:generate-leads \
  --criteria "Financial services, >$100M revenue, Northeast US" \
  --count 50 \
  --enrich comprehensive \
  --contacts 5
```

### Intent-Based Targeting
```bash
/sales-prospecting:generate-leads \
  --criteria "Recently funded B2B companies" \
  --intent true \
  --enrich standard
```

## Process Flow

1. **Define ICP Parameters**
   - Parse criteria into searchable filters
   - Validate parameter compatibility
   - Set enrichment requirements

2. **Initial Discovery**
   - Query data sources for matching companies
   - Apply filtering and scoring logic
   - Rank by fit score

3. **Contact Discovery**
   - Identify decision makers and influencers
   - Map buying committee structure
   - Verify contact information

4. **Data Enrichment**
   - Append firmographic data
   - Add technographic insights
   - Include intent signals and triggers
   - Calculate lead scores

5. **Output Generation**
   - Format according to specification
   - Include research notes and insights
   - Generate outreach recommendations

## Output Schema

### Standard Lead Record
```json
{
  "company": {
    "name": "Acme Corp",
    "domain": "acme.com",
    "industry": "Software",
    "size": 250,
    "revenue": "$50M",
    "location": "San Francisco, CA",
    "growth_rate": "45%"
  },
  "contacts": [
    {
      "name": "John Smith",
      "title": "VP Sales",
      "email": "john.smith@acme.com",
      "linkedin": "linkedin.com/in/johnsmith",
      "phone": "+1-415-555-0100",
      "role": "Decision Maker"
    }
  ],
  "technology": {
    "crm": "Salesforce",
    "marketing": "HubSpot",
    "relevant_tools": ["Slack", "Zoom", "Google Workspace"]
  },
  "signals": {
    "intent_score": 82,
    "buying_signals": [
      "Researching competitors",
      "Downloaded pricing guides",
      "Attending industry events"
    ],
    "trigger_events": [
      "New VP Sales hired 2 months ago",
      "Series B funding closed"
    ]
  },
  "recommendations": {
    "approach": "Reference their recent funding and expansion plans",
    "value_prop": "Focus on scalability and integration with Salesforce",
    "timing": "High - active buying cycle"
  }
}
```

## Enrichment Levels

### Basic
- Company name, website, industry
- Basic size and location data
- 1-2 contacts with titles
- Lead score

### Standard
- All basic fields plus:
- Revenue and growth data
- 3-4 contacts with full details
- Technology stack overview
- Key buying signals

### Comprehensive
- All standard fields plus:
- Full buying committee mapping
- Detailed technographic profile
- Intent data and signals
- Competitive intelligence
- Personalized outreach recommendations
- Account research brief

## Integration Options

### CRM Export
```bash
# Direct to Salesforce
/sales-prospecting:generate-leads --criteria "..." --format salesforce

# HubSpot compatible
/sales-prospecting:generate-leads --criteria "..." --format hubspot
```

### Sales Engagement
```bash
# Outreach.io format
/sales-prospecting:generate-leads --criteria "..." --format outreach

# SalesLoft format
/sales-prospecting:generate-leads --criteria "..." --format salesloft
```

## Advanced Options

### Exclusion Lists
```bash
--exclude-companies "competitor1.com,competitor2.com"
--exclude-existing true  # Skip current CRM records
```

### Scoring Customization
```bash
--scoring-model "enterprise"  # Use enterprise scoring model
--minimum-score 70  # Only include leads scoring 70+
```

### Geographic Targeting
```bash
--location "San Francisco Bay Area"
--timezone "PST"
--language "English"
```

## Best Practices

1. **Start Narrow**: Begin with specific criteria and expand based on results
2. **Validate ICP**: Test initial results against known good customers
3. **Iterate Quickly**: Refine criteria based on response rates
4. **Track Performance**: Monitor which criteria generate best leads
5. **Regular Refresh**: Re-run monthly to catch new matches

## Error Handling

- **No matches found**: Broaden criteria or adjust filters
- **Too many results**: Add more specific criteria
- **Missing data**: Adjust enrichment level or data sources
- **Rate limits**: Batch processing for large requests

---

*Execution model: claude-haiku-4-5 for data processing, claude-sonnet-4 for insights generation*
