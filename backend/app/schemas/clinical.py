from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional
from app.models.appointment import AppointmentStatus
from app.models.medical_record import RecordType

class AppointmentBase(BaseModel):
    patient_id: UUID4
    doctor_id: UUID4
    department_id: UUID4
    scheduled_time: datetime
    reason_for_visit: Optional[str] = None
    notes: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    status: Optional[AppointmentStatus] = None
    scheduled_time: Optional[datetime] = None
    notes: Optional[str] = None

class AppointmentResponse(AppointmentBase):
    id: UUID4
    status: AppointmentStatus
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class MedicalRecordBase(BaseModel):
    patient_id: UUID4
    doctor_id: UUID4
    appointment_id: Optional[UUID4] = None
    record_type: RecordType
    title: str
    content: str
    attachments: Optional[str] = None

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecordResponse(MedicalRecordBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
