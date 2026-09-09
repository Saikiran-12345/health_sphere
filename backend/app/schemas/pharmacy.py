from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional, List

class MedicineBase(BaseModel):
    name: str
    generic_name: Optional[str] = None
    category: str
    manufacturer: Optional[str] = None
    unit_price: float
    stock_quantity: int
    reorder_level: int

class MedicineCreate(MedicineBase): pass

class MedicineResponse(MedicineBase):
    id: UUID4
    class Config: from_attributes = True

class PrescriptionItemBase(BaseModel):
    medicine_id: UUID4
    dosage: str
    frequency: str
    duration_days: int

class PrescriptionCreate(BaseModel):
    patient_id: UUID4
    appointment_id: Optional[UUID4] = None
    notes: Optional[str] = None
    items: List[PrescriptionItemBase]
