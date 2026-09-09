
from sqlalchemy.orm import Session
from app.models.oncology.model import OncologyRecord
from app.schemas.oncology.schema import OncologyCreate

def get_oncology_record(db: Session, record_id: str):
    return db.query(OncologyRecord).filter(OncologyRecord.id == record_id).first()

def get_oncology_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(OncologyRecord).offset(skip).limit(limit).all()

def create_oncology_record(db: Session, record: OncologyCreate):
    db_record = OncologyRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
