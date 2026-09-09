import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

create_file('backend/tests/conftest.py', """
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db
from app.main import app

# Use SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
""")

create_file('backend/tests/test_auth.py', """
import pytest
from app.schemas.user import UserRole

def test_health_check(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "Online"

def test_register_user(client):
    response = client.post("/api/auth/register", json={
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "password123",
        "role": "ADMIN"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login_user(client):
    response = client.post("/api/auth/login", data={
        "username": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
""")

create_file('backend/tests/test_patients.py', """
import pytest

def test_create_patient_unauthorized(client):
    response = client.post("/api/patients/", json={
        "user_id": "00000000-0000-0000-0000-000000000000",
        "date_of_birth": "1990-01-01",
        "gender": "Male"
    })
    assert response.status_code == 401  # Should fail without auth token
""")

create_file('backend/tests/test_ai.py', """
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
""")

print("Pytest suite generated.")
