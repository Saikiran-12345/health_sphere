from sqlalchemy import Column, String, ForeignKey, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class UserPasskey(BaseModel):
    __tablename__ = "user_passkeys"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    credential_id = Column(LargeBinary, nullable=False, unique=True)
    public_key = Column(LargeBinary, nullable=False)
    sign_count = Column(String(50), nullable=False)
