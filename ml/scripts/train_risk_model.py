import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def generate_synthetic_patient_data(n_samples=5000):
    np.random.seed(42)
    data = {
        'age': np.random.randint(18, 90, n_samples),
        'systolic_bp': np.random.normal(120, 15, n_samples),
        'diastolic_bp': np.random.normal(80, 10, n_samples),
        'heart_rate': np.random.normal(75, 12, n_samples),
        'previous_admissions': np.random.poisson(1, n_samples),
        'bmi': np.random.normal(25, 4, n_samples)
    }
    df = pd.DataFrame(data)
    
    # Calculate synthetic risk based on factors
    risk_score = (
        (df['age'] > 65).astype(int) * 2 +
        (df['systolic_bp'] > 140).astype(int) * 3 +
        (df['previous_admissions'] > 2).astype(int) * 2 +
        (df['bmi'] > 30).astype(int) * 1
    )
    
    df['high_risk'] = (risk_score >= 5).astype(int)
    return df

def train_model():
    print("Generating synthetic healthcare data...")
    df = generate_synthetic_patient_data()
    
    X = df.drop('high_risk', axis=1)
    y = df['high_risk']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Patient Risk Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model
    os.makedirs('../models', exist_ok=True)
    joblib.dump(model, '../models/patient_risk_model.joblib')
    print("Model saved to ml/models/patient_risk_model.joblib")

if __name__ == "__main__":
    train_model()
