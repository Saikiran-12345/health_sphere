
from sqlalchemy.orm import Session
from app.models.bloodbank.model import BloodbankRecord
from app.schemas.bloodbank.schema import BloodbankCreate

def get_bloodbank_record(db: Session, record_id: str):
    return db.query(BloodbankRecord).filter(BloodbankRecord.id == record_id).first()

def get_bloodbank_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BloodbankRecord).offset(skip).limit(limit).all()

def create_bloodbank_record(db: Session, record: BloodbankCreate):
    db_record = BloodbankRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
