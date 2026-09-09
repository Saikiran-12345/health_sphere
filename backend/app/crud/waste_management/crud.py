
from sqlalchemy.orm import Session
from app.models.waste_management.model import Waste_managementRecord
from app.schemas.waste_management.schema import Waste_managementCreate

def get_waste_management_record(db: Session, record_id: str):
    return db.query(Waste_managementRecord).filter(Waste_managementRecord.id == record_id).first()

def get_waste_management_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Waste_managementRecord).offset(skip).limit(limit).all()

def create_waste_management_record(db: Session, record: Waste_managementCreate):
    db_record = Waste_managementRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
