
from sqlalchemy.orm import Session
from app.models.it_support.model import It_supportRecord
from app.schemas.it_support.schema import It_supportCreate

def get_it_support_record(db: Session, record_id: str):
    return db.query(It_supportRecord).filter(It_supportRecord.id == record_id).first()

def get_it_support_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(It_supportRecord).offset(skip).limit(limit).all()

def create_it_support_record(db: Session, record: It_supportCreate):
    db_record = It_supportRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
