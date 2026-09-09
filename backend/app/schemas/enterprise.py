from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import List, Optional

class InvoiceCreate(BaseModel):
    patient_id: UUID4
    issued_date: datetime
    due_date: datetime
    
class AmbulanceCreate(BaseModel):
    vehicle_number: str
    vehicle_type: str

class DispatchCreate(BaseModel):
    ambulance_id: UUID4
    driver_name: str
    pickup_location: str
    emergency_type: str
    dispatch_time: datetime
