import asyncio
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.iot import VitalSignStream
import json
from datetime import datetime
from app.services.sms_service import SMSService

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
    """
    High-frequency WebSocket endpoint for hospital bed monitors (ICU).
    Streams Heart Rate, SpO2, and BP directly into the Postgres DB.
    """
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
                sms = SMSService()
                sms.send_critical_alert('+15550199', f"Code Blue! Patient {payload.get('patient_id')} vitals critical. HR: {payload.get('heart_rate')} SpO2: {payload.get('sp02')}")
                
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    finally:
        db.close()
