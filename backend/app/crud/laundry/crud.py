
from sqlalchemy.orm import Session
from app.models.laundry.model import LaundryRecord
from app.schemas.laundry.schema import LaundryCreate

def get_laundry_record(db: Session, record_id: str):
    return db.query(LaundryRecord).filter(LaundryRecord.id == record_id).first()

def get_laundry_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LaundryRecord).offset(skip).limit(limit).all()

def create_laundry_record(db: Session, record: LaundryCreate):
    db_record = LaundryRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
