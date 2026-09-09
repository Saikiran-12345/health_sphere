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
