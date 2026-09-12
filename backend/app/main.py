from fastapi import FastAPI
from app.core.middleware import AdvancedAuditMiddleware, SimpleRateLimiterMiddleware
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance, telemedicine, export, forecasting, assets, dietary, notifications, analytics, audit, fhir, payments, iot, diagnostics, webauthn

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

app.include_router(telemedicine.router)

app.include_router(export.router)

app.include_router(forecasting.router)

app.include_router(assets.router)
app.include_router(dietary.router)

app.include_router(notifications.router)
app.include_router(analytics.router)

app.include_router(audit.router)
app.include_router(fhir.router)

app.include_router(payments.router)

app.include_router(iot.router)

app.include_router(diagnostics.router)

app.include_router(webauthn.router)

app.include_router(inventory_router)
app.include_router(payroll_router)
app.include_router(maintenance_router)
app.include_router(security_router)
app.include_router(cafeteria_router)
app.include_router(laundry_router)
app.include_router(transport_router)
app.include_router(mortuary_router)
app.include_router(bloodbank_router)
app.include_router(radiology_router)
app.include_router(pathology_router)
app.include_router(oncology_router)
app.include_router(neurology_router)
app.include_router(cardiology_router)
app.include_router(pediatrics_router)
app.include_router(maternity_router)
app.include_router(surgery_router)
app.include_router(anesthesia_router)
app.include_router(sterilization_router)
app.include_router(waste_management_router)
app.include_router(it_support_router)
app.include_router(legal_compliance_router)
app.include_router(procurement_router)
app.include_router(grants_router)
app.include_router(research_router)

