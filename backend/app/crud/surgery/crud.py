
from sqlalchemy.orm import Session
from app.models.surgery.model import SurgeryRecord
from app.schemas.surgery.schema import SurgeryCreate

def get_surgery_record(db: Session, record_id: str):
    return db.query(SurgeryRecord).filter(SurgeryRecord.id == record_id).first()

def get_surgery_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SurgeryRecord).offset(skip).limit(limit).all()

def create_surgery_record(db: Session, record: SurgeryCreate):
    db_record = SurgeryRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
