import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import warnings
warnings.filterwarnings('ignore')

# === Setup folders ===
os.makedirs('models', exist_ok=True)
os.makedirs('images', exist_ok=True)

# === Load dataset ===
df = pd.read_csv('data/insurance_claims1.csv')
print(" Dataset Loaded. Shape:", df.shape)
print(df.head())
print("Columns:", df.columns.tolist())

# === Preprocessing ===
df.dropna(inplace=True)

# (Optional mapping if using a dataset where fraud_reported = 'Y'/'N')
# df['fraud_reported'] = df['fraud_reported'].map({'Y': 1, 'N': 0})

# Handle date column if present
if 'incident_date' in df.columns:
    df['incident_date'] = pd.to_datetime(df['incident_date'])
    df['incident_year'] = df['incident_date'].dt.year
    df['incident_month'] = df['incident_date'].dt.month
    df.drop(['incident_date'], axis=1, inplace=True)

# One-hot encode categorical variables
df = pd.get_dummies(df, drop_first=True)
print("Data Preprocessing Complete. New shape:", df.shape)

# === Train/test split ===
X = df.drop('fraud_reported', axis=1)
y = df['fraud_reported']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Train model ===
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# === Evaluate model ===
y_pred = model.predict(X_test)
print("Model Trained.")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# === Save model ===
joblib.dump(model, 'models/insurance_fraud_model.pkl')
print("Model saved as 'models/insurance_fraud_model.pkl'.")

# === Feature Importance ===
importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 8))
sns.barplot(x='Importance', y='Feature', data=importance_df.head(10))
plt.title('Top 10 Important Features for Fraud Detection')
plt.tight_layout()
plt.savefig('images/feature_importance.png')
plt.show()

# === Fraud case distribution ===
plt.figure(figsize=(6, 4))
sns.countplot(x='fraud_reported', data=df, palette='viridis')
plt.title('Distribution of Fraud Cases')
plt.xlabel('Fraud Reported (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('images/fraud_distribution.png')
plt.show()

# === Correlation Matrix ===
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .7})
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('images/correlation_matrix.png')
plt.show()

print("\n✅ All tasks completed. Model + Visuals saved.")
# === Debugging output ===


# --- IGNORE ---
# This section is ignored in the final output.
# It is used for debugging or additional information.
# --- IGNORE ---
# Debugging output to check the columns in the dataset


