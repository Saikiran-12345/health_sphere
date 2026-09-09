
from sqlalchemy.orm import Session
from app.models.radiology.model import RadiologyRecord
from app.schemas.radiology.schema import RadiologyCreate

def get_radiology_record(db: Session, record_id: str):
    return db.query(RadiologyRecord).filter(RadiologyRecord.id == record_id).first()

def get_radiology_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RadiologyRecord).offset(skip).limit(limit).all()

def create_radiology_record(db: Session, record: RadiologyCreate):
    db_record = RadiologyRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
