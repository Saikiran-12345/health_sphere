from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance

app = FastAPI(title="HealthSphere Enterprise API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(clinical.router)

@app.get("/api/health")
def health_check():
    return {"status": "Online", "database": "Connected"}

app.include_router(pharmacy.router)
app.include_router(laboratory.router)

app.include_router(ai.router)

app.include_router(operations.router)

app.include_router(billing.router)
app.include_router(hr.router)
app.include_router(ambulance.router)
