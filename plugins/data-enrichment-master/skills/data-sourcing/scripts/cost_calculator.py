def estimate_cost(records, enrichment_type, quality_level):
    """
    Estimate the cost of data enrichment based on volume and quality.
    
    Args:
        records (int): Number of records to enrich.
        enrichment_type (str): 'email', 'company', or 'full'.
        quality_level (str): 'budget', 'standard', or 'premium'.
        
    Returns:
        float: Estimated total cost in credits.
    """
    base_costs = {
        "email": {"budget": 1, "standard": 3, "premium": 8},
        "company": {"budget": 2, "standard": 5, "premium": 12},
        "full": {"budget": 5, "standard": 10, "premium": 25}
    }
    
    if enrichment_type not in base_costs or quality_level not in base_costs[enrichment_type]:
        raise ValueError("Invalid enrichment type or quality level")
    
    cost_per_record = base_costs[enrichment_type][quality_level]
    total_cost = records * cost_per_record
    
    # Apply volume discounts
    if records > 10000:
        total_cost *= 0.7
    elif records > 5000:
        total_cost *= 0.8
    elif records > 1000:
        total_cost *= 0.9
    
    return total_cost

if __name__ == "__main__":
    # Example usage
    print(f"Cost for 1000 standard emails: {estimate_cost(1000, 'email', 'standard')}")
