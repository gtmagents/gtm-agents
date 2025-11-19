---
name: waterfall-enrichment
description: Execute multi-provider enrichment waterfalls with credit-aware routing, validation, and export options.
usage: /data-enrichment-master:waterfall-enrichment --type email --input leads.csv --max-credits 5
---

# Waterfall Enrichment Command

Execute multi-provider enrichment waterfalls to maximize data discovery success rates while optimizing credit usage.

## Command Syntax

```bash
/data-enrichment:waterfall --type <email|phone|company|full> --input <data> --max-credits <limit>
```

## Parameters

- `--type`: Type of waterfall (email, phone, company, full)
- `--input`: Input data (name+company, email, domain, CSV file)
- `--max-credits`: Maximum credits to spend per record (default: 10)
- `--providers`: Specific provider sequence (optional, uses optimized defaults)
- `--validate`: Validate discovered data (default: true)
- `--cache`: Use cached results (default: true, 30-day TTL)
- `--parallel`: Process multiple records in parallel (default: true)
- `--output`: Output format (json|csv|salesforce|hubspot)

## Waterfall Sequences

### Email Discovery Waterfall
```yaml
Default Sequence:
  1. Cache Check (0 credits)
  2. Apollo.io (1-2 credits)
  3. Hunter (1-2 credits)
  4. RocketReach (1-2 credits)
  5. People Data Labs (1-2 credits)
  6. ContactOut (1-2 credits)
  7. Findymail (1-2 credits)
  8. BetterContact (2-5 credits)
  9. AI Web Research (2-5 credits)
  
Validation:
  - ZeroBounce (0.5 credits)
  - NeverBounce backup (0.5 credits)
```

### Phone Discovery Waterfall
```yaml
Default Sequence:
  1. Cache Check (0 credits)
  2. Apollo.io (1-2 credits)
  3. RocketReach (1-2 credits)
  4. LeadMagic (1-2 credits)
  5. SignalHire (1-2 credits)
  6. BetterContact Phone (2-5 credits)
  7. People Data Labs (1-2 credits)
  
Validation:
  - ClearoutPhone (0.5 credits)
  - Phone type detection
```

### Company Enrichment Waterfall
```yaml
Default Sequence:
  1. Clearbit (1-2 credits)
  2. Ocean.io (2-3 credits)
  3. ZoomInfo (2-3 credits) [if enterprise]
  4. Crunchbase (1-2 credits) [if funded]
  5. BuiltWith (1-2 credits) [technographics]
  6. HG Insights (2-3 credits) [tech spend]
  7. Intent providers (3-5 credits) [if qualified]
```

### Full Contact Enrichment
```yaml
Comprehensive Sequence:
  1. Email discovery waterfall
  2. Phone discovery waterfall
  3. Social profile discovery
  4. Company enrichment
  5. Technographics
  6. Intent signals
  7. Validation & scoring
```

## Examples

### Basic Email Discovery
```bash
/data-enrichment:waterfall \
  --type email \
  --input "John Smith, Acme Corp"
```

### Bulk Email Enrichment with Validation
```bash
/data-enrichment:waterfall \
  --type email \
  --input "prospects.csv" \
  --validate true \
  --max-credits 5
```

### Custom Provider Sequence
```bash
/data-enrichment:waterfall \
  --type email \
  --input "jane.doe@example.com" \
  --providers "clearbit,apollo,hunter" \
  --validate true
```

### Enterprise Full Enrichment
```bash
/data-enrichment:waterfall \
  --type full \
  --input "target_accounts.csv" \
  --max-credits 20 \
  --output salesforce
```

## Provider Selection Logic

```python
def select_providers(input_type, data_available, target_quality):
    providers = []
    
    # Email discovery logic
    if input_type == "email":
        if has_linkedin_url(data_available):
            providers = ["contactout", "rocketreach", "apollo"]
        elif has_full_name_and_company(data_available):
            providers = ["apollo", "hunter", "rocketreach"]
        elif has_domain_only(data_available):
            providers = ["hunter", "apollo", "clearbit"]
        else:
            providers = ["people_data_labs", "bettercontact", "ai_research"]
    
    # Phone discovery logic
    elif input_type == "phone":
        if has_email(data_available):
            providers = ["apollo", "rocketreach", "leadmagic"]
        else:
            providers = ["bettercontact_phone", "signalhire", "lusha"]
    
    # Quality-based filtering
    if target_quality == "high":
        providers = filter_high_accuracy_providers(providers)
    
    return providers
```

## Credit Optimization

### Smart Routing Algorithm
```python
def optimize_provider_sequence(providers, max_credits, historical_success):
    # Sort by success rate and cost efficiency
    scored_providers = []
    
    for provider in providers:
        score = calculate_efficiency_score(
            success_rate=historical_success[provider],
            credit_cost=PROVIDER_COSTS[provider],
            data_quality=PROVIDER_QUALITY[provider]
        )
        scored_providers.append((provider, score))
    
    # Sort by efficiency score
    scored_providers.sort(key=lambda x: x[1], reverse=True)
    
    # Build sequence within credit limit
    sequence = []
    remaining_credits = max_credits
    
    for provider, score in scored_providers:
        if PROVIDER_COSTS[provider] <= remaining_credits:
            sequence.append(provider)
            remaining_credits -= PROVIDER_COSTS[provider]
    
    return sequence
```

## Success Metrics

### Tracking Performance
```yaml
Metrics:
  success_rate:
    email_found: 85%
    phone_found: 65%
    company_enriched: 95%
  
  average_credits:
    email: 2.3 credits
    phone: 3.1 credits
    company: 4.5 credits
    full_contact: 8.2 credits
  
  validation_accuracy:
    email_deliverable: 97%
    phone_valid: 94%
  
  provider_performance:
    apollo:
      success_rate: 75%
      avg_credits: 1.5
    hunter:
      success_rate: 70%
      avg_credits: 1.2
    zoominfo:
      success_rate: 90%
      avg_credits: 2.5
```

## Error Handling

### Provider Failures
```python
def handle_provider_failure(provider, error, context):
    # Log failure
    log_provider_error(provider, error)
    
    # Determine action
    if is_rate_limit(error):
        # Exponential backoff
        wait_time = calculate_backoff(provider)
        schedule_retry(provider, context, wait_time)
        
    elif is_auth_error(error):
        # Alert and skip provider
        alert_admin(f"Auth failed for {provider}")
        return next_provider()
        
    elif is_data_not_found(error):
        # Continue to next provider
        return next_provider()
        
    else:
        # Generic error - retry once then skip
        if not has_retried(provider, context):
            retry_provider(provider, context)
        else:
            return next_provider()
```

## Output Formats

### JSON Output
```json
{
  "input": {
    "name": "John Smith",
    "company": "Acme Corp"
  },
  "results": {
    "email": "john.smith@acme.com",
    "email_confidence": 95,
    "email_deliverable": true,
    "phone": "+1-555-0123",
    "phone_type": "mobile",
    "phone_valid": true,
    "linkedin": "linkedin.com/in/johnsmith",
    "providers_used": ["apollo", "zerobounce"],
    "credits_used": 2.5
  },
  "metadata": {
    "enriched_at": "2024-01-20T10:30:00Z",
    "cache_hit": false,
    "processing_time": 1.2
  }
}
```

### CSV Output
```csv
name,company,email,email_confidence,phone,phone_type,linkedin,credits_used
John Smith,Acme Corp,john.smith@acme.com,95,+1-555-0123,mobile,linkedin.com/in/johnsmith,2.5
```

### Salesforce Format
```json
{
  "Lead": {
    "FirstName": "John",
    "LastName": "Smith",
    "Company": "Acme Corp",
    "Email": "john.smith@acme.com",
    "Phone": "+1-555-0123",
    "LinkedIn__c": "linkedin.com/in/johnsmith",
    "Enrichment_Score__c": 95,
    "Last_Enriched__c": "2024-01-20T10:30:00Z"
  }
}
```

## Caching Strategy

### Cache Management
```python
CACHE_CONFIG = {
    "email": {
        "ttl_days": 30,
        "refresh_if_bounced": True
    },
    "phone": {
        "ttl_days": 60,
        "refresh_if_invalid": True
    },
    "company": {
        "ttl_days": 90,
        "refresh_on_trigger": ["funding", "acquisition", "ipo"]
    },
    "intent": {
        "ttl_days": 7,
        "always_refresh": True
    }
}
```

## Best Practices

1. **Start with cached data** - Always check cache first
2. **Set appropriate credit limits** - Balance cost vs. data quality
3. **Use parallel processing** - For bulk enrichments
4. **Validate critical data** - Especially emails before outreach
5. **Monitor provider performance** - Adjust sequences based on success rates
6. **Handle failures gracefully** - Automatic fallback to next provider
7. **Track ROI** - Measure enrichment value vs. credit cost

---

*Execution model: claude-haiku-4-5 for provider routing, parallel processing for bulk operations*
