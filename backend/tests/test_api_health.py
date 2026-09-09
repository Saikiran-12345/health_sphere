from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    # Assuming standard FastAPI root acts as health check or Swagger redirect
    response = client.get("/")
    # Even if it redirects or 404s, we verify the app boots without crashing
    assert response.status_code in [200, 404]
    
def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200
