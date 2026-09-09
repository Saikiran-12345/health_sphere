import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Base ML Pipeline
create_file('ml/scripts/train_risk_model.py', """
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
""")

# 2. Anomaly Detection Pipeline
create_file('ml/scripts/train_anomaly_model.py', """
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

def train_anomaly_detection():
    print("Training Operational Anomaly Detection (Isolation Forest)...")
    # Synthetic operational metrics: [daily_appointments, cancellations, inventory_usage]
    np.random.seed(42)
    normal_data = np.random.normal(loc=[100, 5, 50], scale=[10, 2, 5], size=(1000, 3))
    anomalies = np.random.normal(loc=[200, 30, 150], scale=[20, 5, 20], size=(50, 3))
    
    X = np.vstack([normal_data, anomalies])
    
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    
    os.makedirs('../models', exist_ok=True)
    joblib.dump(model, '../models/operational_anomaly_model.joblib')
    print("Anomaly model saved to ml/models/operational_anomaly_model.joblib")

if __name__ == "__main__":
    train_anomaly_detection()
""")

# 3. FastAPI AI Router
create_file('backend/app/api/ai.py', """
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

router = APIRouter(prefix="/api/ai", tags=["AI & Analytics"])

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../../ml/models/patient_risk_model.joblib")

class PatientVitals(BaseModel):
    age: int
    systolic_bp: float
    diastolic_bp: float
    heart_rate: float
    previous_admissions: int
    bmi: float

@router.post("/predict-risk")
def predict_patient_risk(vitals: PatientVitals):
    if not os.path.exists(MODEL_PATH):
        raise HTTPException(status_code=503, detail="AI Model not loaded/trained yet")
        
    model = joblib.load(MODEL_PATH)
    
    # Format input
    input_data = pd.DataFrame([{
        'age': vitals.age,
        'systolic_bp': vitals.systolic_bp,
        'diastolic_bp': vitals.diastolic_bp,
        'heart_rate': vitals.heart_rate,
        'previous_admissions': vitals.previous_admissions,
        'bmi': vitals.bmi
    }])
    
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    
    # Explainability
    feature_importance = dict(zip(input_data.columns, model.feature_importances_))
    
    return {
        "high_risk": bool(prediction),
        "risk_probability": float(probabilities[1]),
        "disclaimer": "This is a decision-support prediction based on historical data. It is not a clinical diagnosis.",
        "important_factors": feature_importance
    }
""")

# Update main.py
path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import ai" not in content:
    content = content.replace("from app.api import auth, patients, clinical, pharmacy, laboratory", "from app.api import auth, patients, clinical, pharmacy, laboratory, ai")
    content += "\napp.include_router(ai.router)\n"
    with open(path, "w") as f:
        f.write(content)

print("AI Domain generated successfully.")
