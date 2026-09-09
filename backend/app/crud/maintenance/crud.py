
from sqlalchemy.orm import Session
from app.models.maintenance.model import MaintenanceRecord
from app.schemas.maintenance.schema import MaintenanceCreate

def get_maintenance_record(db: Session, record_id: str):
    return db.query(MaintenanceRecord).filter(MaintenanceRecord.id == record_id).first()

def get_maintenance_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MaintenanceRecord).offset(skip).limit(limit).all()

def create_maintenance_record(db: Session, record: MaintenanceCreate):
    db_record = MaintenanceRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
