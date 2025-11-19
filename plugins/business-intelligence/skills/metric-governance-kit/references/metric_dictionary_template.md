# Metric Dictionary Template

## [Metric Name]

### Definition
**Description:** [Plain English definition of what this metric measures.]
**Business Value:** [Why do we track this? What decision does it inform?]
**Tier:** [Strategic / Operational / Exploratory]

### Technical Specs
**Formula:**
`[Numerator] / [Denominator]`

**Filters/Exclusions:**
- Exclude: [Internal Users, Test Accounts]
- Timezone: [UTC / PST]

**Source:**
- **Database:** [Snowflake/BigQuery]
- **Table:** `[schema].[table_name]`
- **Field:** `[column_name]`

### Governance
**Business Owner:** [Name/Role]
**Technical Owner:** [Name/Role]
**Review Cadence:** [Monthly/Quarterly]
**SLA:** [Freshness requirement, e.g., Daily by 8am]

### Related Metrics
- **Upstream:** [Metric A]
- **Downstream:** [Metric B]
