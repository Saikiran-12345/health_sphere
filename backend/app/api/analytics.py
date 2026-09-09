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
    """
    Uses Pandas to aggregate massive data points into readable KPIs.
    """
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
