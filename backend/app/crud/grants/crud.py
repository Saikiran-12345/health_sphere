
from sqlalchemy.orm import Session
from app.models.grants.model import GrantsRecord
from app.schemas.grants.schema import GrantsCreate

def get_grants_record(db: Session, record_id: str):
    return db.query(GrantsRecord).filter(GrantsRecord.id == record_id).first()

def get_grants_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GrantsRecord).offset(skip).limit(limit).all()

def create_grants_record(db: Session, record: GrantsCreate):
    db_record = GrantsRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
