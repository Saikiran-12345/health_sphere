
from sqlalchemy.orm import Session
from app.models.pediatrics.model import PediatricsRecord
from app.schemas.pediatrics.schema import PediatricsCreate

def get_pediatrics_record(db: Session, record_id: str):
    return db.query(PediatricsRecord).filter(PediatricsRecord.id == record_id).first()

def get_pediatrics_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PediatricsRecord).offset(skip).limit(limit).all()

def create_pediatrics_record(db: Session, record: PediatricsCreate):
    db_record = PediatricsRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
