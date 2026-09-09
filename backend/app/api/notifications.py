from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.notifications import NotificationLog
from app.api.deps import get_current_active_admin

router = APIRouter(prefix="/api/notifications", tags=["Notification Engine"])

@router.get("/logs")
def get_notification_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_active_admin)):
    return db.query(NotificationLog).order_by(NotificationLog.created_at.desc()).offset(skip).limit(limit).all()
