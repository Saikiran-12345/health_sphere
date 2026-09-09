
from sqlalchemy.orm import Session
from app.models.maternity.model import MaternityRecord
from app.schemas.maternity.schema import MaternityCreate

def get_maternity_record(db: Session, record_id: str):
    return db.query(MaternityRecord).filter(MaternityRecord.id == record_id).first()

def get_maternity_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MaternityRecord).offset(skip).limit(limit).all()

def create_maternity_record(db: Session, record: MaternityCreate):
    db_record = MaternityRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
