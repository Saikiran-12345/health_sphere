from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class BedResponse(BaseModel):
    id: UUID4
    ward_id: UUID4
    bed_number: str
    is_occupied: bool
    status: str
    class Config: from_attributes = True

class AdmissionCreate(BaseModel):
    patient_id: UUID4
    bed_id: UUID4
    admitting_doctor_id: UUID4
    admission_date: datetime
    reason_for_admission: str
