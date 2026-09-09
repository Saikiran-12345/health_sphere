
from sqlalchemy.orm import Session
from app.models.pathology.model import PathologyRecord
from app.schemas.pathology.schema import PathologyCreate

def get_pathology_record(db: Session, record_id: str):
    return db.query(PathologyRecord).filter(PathologyRecord.id == record_id).first()

def get_pathology_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PathologyRecord).offset(skip).limit(limit).all()

def create_pathology_record(db: Session, record: PathologyCreate):
    db_record = PathologyRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
