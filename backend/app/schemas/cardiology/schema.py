
from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class CardiologyCreate(BaseModel):
    reference_code: str
    status: Optional[str] = "ACTIVE"
    assigned_staff_id: Optional[UUID4] = None
    cost: Optional[float] = 0.0
    requires_review: Optional[bool] = False
    custom_field_1: Optional[str] = None
    custom_field_2: Optional[str] = None
    custom_field_3: Optional[str] = None
    custom_field_4: Optional[str] = None
    custom_field_5: Optional[str] = None
    custom_field_6: Optional[str] = None
    custom_field_7: Optional[str] = None
    custom_field_8: Optional[str] = None
    custom_field_9: Optional[str] = None
    custom_field_10: Optional[str] = None
    custom_field_11: Optional[str] = None
    custom_field_12: Optional[str] = None
    custom_field_13: Optional[str] = None
    custom_field_14: Optional[str] = None
    custom_field_15: Optional[str] = None
    custom_field_16: Optional[str] = None
    custom_field_17: Optional[str] = None
    custom_field_18: Optional[str] = None
    custom_field_19: Optional[str] = None
    custom_field_20: Optional[str] = None
    custom_field_21: Optional[str] = None
    custom_field_22: Optional[str] = None
    custom_field_23: Optional[str] = None
    custom_field_24: Optional[str] = None
    custom_field_25: Optional[str] = None
    custom_field_26: Optional[str] = None
    custom_field_27: Optional[str] = None
    custom_field_28: Optional[str] = None
    custom_field_29: Optional[str] = None
    custom_field_30: Optional[str] = None
    custom_field_31: Optional[str] = None
    custom_field_32: Optional[str] = None
    custom_field_33: Optional[str] = None
    custom_field_34: Optional[str] = None
    custom_field_35: Optional[str] = None
    custom_field_36: Optional[str] = None
    custom_field_37: Optional[str] = None
    custom_field_38: Optional[str] = None
    custom_field_39: Optional[str] = None
    custom_field_40: Optional[str] = None
    custom_field_41: Optional[str] = None
    custom_field_42: Optional[str] = None
    custom_field_43: Optional[str] = None
    custom_field_44: Optional[str] = None
    custom_field_45: Optional[str] = None
    custom_field_46: Optional[str] = None
    custom_field_47: Optional[str] = None
    custom_field_48: Optional[str] = None
    custom_field_49: Optional[str] = None
    custom_field_50: Optional[str] = None


class {domain.capitalize()}Response({domain.capitalize()}Create):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True
