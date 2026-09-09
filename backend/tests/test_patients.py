import pytest

def test_create_patient_unauthorized(client):
    response = client.post("/api/patients/", json={
        "user_id": "00000000-0000-0000-0000-000000000000",
        "date_of_birth": "1990-01-01",
        "gender": "Male"
    })
    assert response.status_code == 401  # Should fail without auth token
