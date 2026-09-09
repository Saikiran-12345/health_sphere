import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Notification Engine
create_file('backend/app/models/notifications.py', """
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class NotificationLog(BaseModel):
    __tablename__ = "notification_logs"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    channel = Column(String(50), nullable=False) # EMAIL, SMS, PUSH
    subject = Column(String(255), nullable=True)
    message = Column(Text, nullable=False)
    status = Column(String(50), default="PENDING") # PENDING, SENT, FAILED
    error_message = Column(Text, nullable=True)
    sent_at = Column(DateTime, nullable=True)
""")

create_file('backend/app/services/notifications.py', """
import asyncio
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.notifications import NotificationLog

class NotificationService:
    @staticmethod
    async def send_email(to_address: str, subject: str, body: str, db: Session, user_id: str):
        \"\"\"
        Simulates an SMTP email dispatch.
        \"\"\"
        log = NotificationLog(user_id=user_id, channel="EMAIL", subject=subject, message=body)
        db.add(log)
        db.commit()
        
        # Simulate network delay
        await asyncio.sleep(1)
        
        log.status = "SENT"
        log.sent_at = datetime.utcnow()
        db.commit()
        return True

    @staticmethod
    async def send_sms(phone_number: str, message: str, db: Session, user_id: str):
        \"\"\"
        Simulates an SMS dispatch via Twilio.
        \"\"\"
        log = NotificationLog(user_id=user_id, channel="SMS", message=message)
        db.add(log)
        db.commit()
        
        # Simulate network delay
        await asyncio.sleep(0.5)
        
        log.status = "SENT"
        log.sent_at = datetime.utcnow()
        db.commit()
        return True
""")

create_file('backend/app/api/notifications.py', """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.notifications import NotificationLog
from app.api.deps import get_current_active_admin

router = APIRouter(prefix="/api/notifications", tags=["Notification Engine"])

@router.get("/logs")
def get_notification_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_active_admin)):
    return db.query(NotificationLog).order_by(NotificationLog.created_at.desc()).offset(skip).limit(limit).all()
""")

# 2. Advanced Analytics API
create_file('backend/app/api/analytics.py', """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import pandas as pd
from app.db.database import get_db
from app.models.operations import Admission
from app.models.billing import Invoice
from app.models.appointment import Appointment
from app.api.deps import get_current_active_admin

router = APIRouter(prefix="/api/analytics", tags=["Advanced Analytics"])

@router.get("/dashboard/kpi")
def get_dashboard_kpis(db: Session = Depends(get_db), current_user = Depends(get_current_active_admin)):
    \"\"\"
    Uses Pandas to aggregate massive data points into readable KPIs.
    \"\"\"
    # Simulate fetching large datasets
    invoices = pd.read_sql(db.query(Invoice).statement, db.bind)
    appointments = pd.read_sql(db.query(Appointment).statement, db.bind)
    admissions = pd.read_sql(db.query(Admission).statement, db.bind)
    
    total_revenue = float(invoices['total_amount'].sum()) if not invoices.empty else 0.0
    pending_revenue = float(invoices[invoices['status'] == 'PENDING']['total_amount'].sum()) if not invoices.empty else 0.0
    
    active_admissions = len(admissions[admissions['status'] == 'ADMITTED']) if not admissions.empty else 0
    upcoming_appointments = len(appointments[appointments['status'] == 'SCHEDULED']) if not appointments.empty else 0
    
    return {
        "financial": {
            "total_revenue_ytd": total_revenue,
            "pending_receivables": pending_revenue
        },
        "operations": {
            "active_admissions": active_admissions,
            "upcoming_appointments": upcoming_appointments
        }
    }
""")

# Update main.py and models/__init__.py
path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import notifications" not in content:
    content = content.replace("from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance, telemedicine, export, forecasting, assets, dietary", 
                              "from app.api import auth, patients, clinical, pharmacy, laboratory, ai, operations, billing, hr, ambulance, telemedicine, export, forecasting, assets, dietary, notifications, analytics")
    content += "\napp.include_router(notifications.router)\napp.include_router(analytics.router)\n"
    with open(path, "w") as f:
        f.write(content)

path2 = "backend/app/models/__init__.py"
with open(path2, "a") as f:
    f.write("\nfrom app.models.notifications import NotificationLog\n")

print("Notifications and Analytics domains generated.")
