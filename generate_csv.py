import pandas as pd
import random

# Generate 200 rows of synthetic insurance claim data
n = 200
data = {
    'age': [random.randint(18, 75) for _ in range(n)],
    'policy_state': [random.choice(['IN', 'OH', 'IL']) for _ in range(n)],
    'incident_type': [random.choice(['Single Vehicle Collision', 'Multi-vehicle Collision', 'Parked Car', 'Vehicle Theft']) for _ in range(n)],
    'incident_severity': [random.choice(['Minor Damage', 'Major Damage', 'Total Loss']) for _ in range(n)],
    'total_claim_amount': [random.randint(1000, 25000) for _ in range(n)],
    'fraud_reported': [random.choice([0, 1]) for _ in range(n)]
}

df = pd.DataFrame(data)
df.to_csv('data/insurance_claims1.csv', index=False)

print(" insurance_claims1.csv created with", len(df), "rows.")
