from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.assets import Asset, MaintenanceLog

router = APIRouter(prefix="/api/assets", tags=["Asset & Maintenance Management"])

@router.get("/")
def get_assets(db: Session = Depends(get_db)):
    return db.query(Asset).all()

@router.get("/{asset_id}/logs")
def get_maintenance_logs(asset_id: str, db: Session = Depends(get_db)):
    return db.query(MaintenanceLog).filter(MaintenanceLog.asset_id == asset_id).all()
