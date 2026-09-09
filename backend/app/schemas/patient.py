from pydantic import BaseModel, UUID4
from datetime import date, datetime
from typing import Optional
from app.models.patient import BloodGroup
from app.schemas.user import UserResponse

class PatientBase(BaseModel):
    date_of_birth: date
    gender: str
    blood_group: Optional[BloodGroup] = None
    address: Optional[str] = None
    emergency_contact_name: Optional[str] = None
    emergency_contact_number: Optional[str] = None

class PatientCreate(PatientBase):
    user_id: UUID4

class PatientUpdate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: UUID4
    user_id: UUID4
    created_at: datetime
    updated_at: datetime
    user: Optional[UserResponse] = None

    class Config:
        from_attributes = True
