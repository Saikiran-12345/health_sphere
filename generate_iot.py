import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. IoT Schema and Models
create_file('backend/app/models/iot.py', """
from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class VitalSignStream(BaseModel):
    __tablename__ = "iot_vital_streams"
    patient_id = Column(UUID(as_uuid=True), ForeignKey("patients.id"), nullable=False)
    device_id = Column(String(100), nullable=False)
    heart_rate = Column(Float, nullable=True)
    sp02 = Column(Float, nullable=True)
    blood_pressure_sys = Column(Float, nullable=True)
    blood_pressure_dia = Column(Float, nullable=True)
    temperature = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False)
""")

# 2. IoT WebSockets/API Endpoints
create_file('backend/app/api/iot.py', """
import asyncio
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.iot import VitalSignStream
import json
from datetime import datetime

router = APIRouter(prefix="/api/iot", tags=["IoT Devices"])

class IOTConnectionManager:
    def __init__(self):
        self.active_devices: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_devices.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_devices:
            self.active_devices.remove(websocket)

manager = IOTConnectionManager()

@router.websocket("/stream/{device_id}")
async def iot_vitals_stream(websocket: WebSocket, device_id: str):
    \"\"\"
    High-frequency WebSocket endpoint for hospital bed monitors (ICU).
    Streams Heart Rate, SpO2, and BP directly into the Postgres DB.
    \"\"\"
    await manager.connect(websocket)
    db = SessionLocal()
    try:
        while True:
            data_str = await websocket.receive_text()
            payload = json.loads(data_str)
            
            # Save stream to DB (In reality, use TimescaleDB or InfluxDB for this)
            vital = VitalSignStream(
                patient_id=payload.get("patient_id"),
                device_id=device_id,
                heart_rate=payload.get("heart_rate"),
                sp02=payload.get("sp02"),
                blood_pressure_sys=payload.get("sys"),
                blood_pressure_dia=payload.get("dia"),
                temperature=payload.get("temp"),
                timestamp=datetime.utcnow()
            )
            db.add(vital)
            db.commit()
            
            # If critical, trigger Celery Alert (Mocked here)
            if payload.get("heart_rate", 80) < 40 or payload.get("sp02", 98) < 88:
                print(f"[CRITICAL ALERT] Patient {payload.get('patient_id')} vitals failing!")
                
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    finally:
        db.close()
""")

# 3. Add to Main and Init
path_main = "backend/app/main.py"
with open(path_main, "r") as f:
    content = f.read()

if "from app.api import iot" not in content:
    content = content.replace("from app.api import payments, audit", "from app.api import payments, audit, iot")
    content += "\napp.include_router(iot.router)\n"
    with open(path_main, "w") as f:
        f.write(content)

path_init = "backend/app/models/__init__.py"
with open(path_init, "a") as f:
    f.write("\nfrom app.models.iot import VitalSignStream\n")

print("IoT Real-Time Vitals engine generated.")
