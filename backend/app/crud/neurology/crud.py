
from sqlalchemy.orm import Session
from app.models.neurology.model import NeurologyRecord
from app.schemas.neurology.schema import NeurologyCreate

def get_neurology_record(db: Session, record_id: str):
    return db.query(NeurologyRecord).filter(NeurologyRecord.id == record_id).first()

def get_neurology_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(NeurologyRecord).offset(skip).limit(limit).all()

def create_neurology_record(db: Session, record: NeurologyCreate):
    db_record = NeurologyRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
