# Analytics QA Checklist

## 1. Schema & Structure
- [ ] **Column Names:** Follow naming convention (snake_case)?
- [ ] **Data Types:** Correct types (INT, FLOAT, TIMESTAMP, STRING)?
- [ ] **Primary Key:** Unique and non-null?
- [ ] **Foreign Keys:** Valid relationships to dimension tables?

## 2. Data Freshness & Volume
- [ ] **Freshness:** Data matches source system timestamp?
- [ ] **Row Count:** Matches expected volume (vs. yesterday/last week)?
- [ ] **Completeness:** No unexpected NULL values in critical columns?

## 3. Logic & Accuracy
- [ ] **Calculations:** Spot-checked 5-10 records against source?
- [ ] **Aggregations:** Sum of parts equals total?
- [ ] **Filters:** Exclusions (e.g., test accounts) applied correctly?
- [ ] **Joins:** No fan-outs (row duplication) from many-to-many joins?

## 4. Performance
- [ ] **Query Time:** Runs within acceptable SLA?
- [ ] **Partitioning:** Pruning effective on date/key columns?

## 5. Documentation
- [ ] **Description:** Table and column descriptions added?
- [ ] **Owner:** Tagged with owner and tier?
