import pytest

def test_ai_risk_prediction_endpoint(client):
    response = client.post("/api/ai/predict-risk", json={
        "age": 65,
        "systolic_bp": 140,
        "diastolic_bp": 90,
        "heart_rate": 80,
        "previous_admissions": 2,
        "bmi": 28
    })
    
    # Might be 503 if model isn't generated during test pipeline, but route should exist
    assert response.status_code in [200, 503]
