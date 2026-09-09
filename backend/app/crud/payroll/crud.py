
from sqlalchemy.orm import Session
from app.models.payroll.model import PayrollRecord
from app.schemas.payroll.schema import PayrollCreate

def get_payroll_record(db: Session, record_id: str):
    return db.query(PayrollRecord).filter(PayrollRecord.id == record_id).first()

def get_payroll_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PayrollRecord).offset(skip).limit(limit).all()

def create_payroll_record(db: Session, record: PayrollCreate):
    db_record = PayrollRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
