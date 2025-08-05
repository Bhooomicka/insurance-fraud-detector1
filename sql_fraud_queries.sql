-- 1. Total Claims vs Fraudulent Claims
SELECT 
    fraud_reported,
    COUNT(*) AS claim_count
FROM insurance_claims
GROUP BY fraud_reported;

-- 2. Top 3 States with Most Fraud Cases
SELECT 
    policy_state, 
    COUNT(*) AS fraud_count
FROM insurance_claims
WHERE fraud_reported = 1
GROUP BY policy_state
ORDER BY fraud_count DESC
LIMIT 3;

-- 3. Average Claim Amount (Fraud vs Non-Fraud)
SELECT 
    fraud_reported,
    ROUND(AVG(total_claim_amount), 2) AS avg_claim_amount
FROM insurance_claims
GROUP BY fraud_reported;

-- 4. Count of Customers with Multiple Fraud Claims
-- (Assumes a column 'customer_id' exists in your dataset)
SELECT 
    customer_id,
    COUNT(*) AS fraud_claims
FROM insurance_claims
WHERE fraud_reported = 1
GROUP BY customer_id
HAVING fraud_claims > 1;

-- 5. Common Incident Types in Fraud Cases
SELECT 
    incident_type,
    COUNT(*) AS freq
FROM insurance_claims
WHERE fraud_reported = 1
GROUP BY incident_type
ORDER BY freq DESC;

-- 6. High Claim Amounts Flagged as Fraud
SELECT 
    age,
    policy_state,
    total_claim_amount
FROM insurance_claims
WHERE fraud_reported = 1
ORDER BY total_claim_amount DESC
LIMIT 5;
