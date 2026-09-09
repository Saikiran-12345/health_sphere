import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Audit & Compliance
create_file('backend/app/models/audit.py', """
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class AuditLog(BaseModel):
    __tablename__ = "audit_logs"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    action = Column(String(255), nullable=False) # READ, CREATE, UPDATE, DELETE
    resource_type = Column(String(100), nullable=False) # PATIENT, RECORD, BILLING
    resource_id = Column(String(255), nullable=True)
    ip_address = Column(String(50), nullable=True)
    details = Column(JSON, nullable=True) # Changes made
""")

create_file('backend/app/api/audit.py', """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.audit import AuditLog
from app.api.deps import get_current_active_admin

router = APIRouter(prefix="/api/audit", tags=["Compliance & Audit"])

@router.get("/")
def get_audit_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_active_admin)):
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).offset(skip).limit(limit).all()
""")

# 2. HL7 / FHIR Interoperability
create_file('backend/app/services/fhir.py', """
from app.models.patient import Patient
from typing import Dict, Any

class FHIRMapper:
    @staticmethod
    def patient_to_fhir(patient: Patient) -> Dict[str, Any]:
        \"\"\"
        Maps internal SQLAlchemy Patient model to standard FHIR R4 Patient Resource.
        \"\"\"
        return {
            "resourceType": "Patient",
            "id": str(patient.id),
            "identifier": [
                {
                    "use": "usual",
                    "value": f"PAT-{str(patient.id).split('-')[0]}"
                }
            ],
            "active": True,
            "name": [
                {
                    "use": "official",
                    "family": patient.user.last_name if patient.user else "Unknown",
                    "given": [patient.user.first_name if patient.user else "Unknown"]
                }
            ],
            "telecom": [
                {
                    "system": "phone",
                    "value": patient.user.phone_number if patient.user else "",
                    "use": "mobile"
                }
            ],
            "gender": patient.gender.lower() if patient.gender else "unknown",
            "birthDate": patient.date_of_birth.isoformat() if patient.date_of_birth else None,
            "address": [
                {
                    "use": "home",
                    "text": patient.address
                }
            ]
        }
""")

create_file('backend/app/api/fhir.py', """
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.database import get_db
from app.models.patient import Patient
from app.services.fhir import FHIRMapper

router = APIRouter(prefix="/fhir/r4", tags=["FHIR Interoperability"])

@router.get("/Patient/{patient_id}")
def get_fhir_patient(patient_id: UUID, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return FHIRMapper.patient_to_fhir(patient)
""")

# 3. Background Workers (Tasks)
create_file('backend/app/worker.py', """
import asyncio
from datetime import datetime

async def background_daily_report_generator():
    \"\"\"
    Simulated background task runner for massive data crunching at midnight.
    \"\"\"
    print(f"[{datetime.utcnow()}] Starting massive background report generation...")
    await asyncio.sleep(5) # Simulate heavy IO
    print(f"[{datetime.utcnow()}] Background reports generated and cached successfully.")

async def background_inventory_reorder_check():
    \"\"\"
    Simulated worker that checks pharmacy inventory against reorder levels.
    \"\"\"
    print(f"[{datetime.utcnow()}] Scanning inventory for shortages...")
    await asyncio.sleep(2)
    print(f"[{datetime.utcnow()}] Inventory scan complete. Auto-purchase orders dispatched.")
""")

# Update main.py and models/__init__.py
path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import audit" not in content:
    content = content.replace("from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance, telemedicine, export, forecasting, assets, dietary, notifications, analytics", 
                              "from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance, telemedicine, export, forecasting, assets, dietary, notifications, analytics, audit, fhir")
    content += "\napp.include_router(audit.router)\napp.include_router(fhir.router)\n"
    with open(path, "w") as f:
        f.write(content)

path2 = "backend/app/models/__init__.py"
with open(path2, "a") as f:
    f.write("\nfrom app.models.audit import AuditLog\n")

print("Compliance, FHIR, and Workers generated.")
