
from sqlalchemy.orm import Session
from app.models.security.model import SecurityRecord
from app.schemas.security.schema import SecurityCreate

def get_security_record(db: Session, record_id: str):
    return db.query(SecurityRecord).filter(SecurityRecord.id == record_id).first()

def get_security_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SecurityRecord).offset(skip).limit(limit).all()

def create_security_record(db: Session, record: SecurityCreate):
    db_record = SecurityRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
