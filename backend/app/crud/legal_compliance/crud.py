
from sqlalchemy.orm import Session
from app.models.legal_compliance.model import Legal_complianceRecord
from app.schemas.legal_compliance.schema import Legal_complianceCreate

def get_legal_compliance_record(db: Session, record_id: str):
    return db.query(Legal_complianceRecord).filter(Legal_complianceRecord.id == record_id).first()

def get_legal_compliance_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Legal_complianceRecord).offset(skip).limit(limit).all()

def create_legal_compliance_record(db: Session, record: Legal_complianceCreate):
    db_record = Legal_complianceRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
