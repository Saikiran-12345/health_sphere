
from sqlalchemy.orm import Session
from app.models.sterilization.model import SterilizationRecord
from app.schemas.sterilization.schema import SterilizationCreate

def get_sterilization_record(db: Session, record_id: str):
    return db.query(SterilizationRecord).filter(SterilizationRecord.id == record_id).first()

def get_sterilization_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SterilizationRecord).offset(skip).limit(limit).all()

def create_sterilization_record(db: Session, record: SterilizationCreate):
    db_record = SterilizationRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
