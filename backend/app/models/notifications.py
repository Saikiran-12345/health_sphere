from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class NotificationLog(BaseModel):
    __tablename__ = "notification_logs"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    channel = Column(String(50), nullable=False) # EMAIL, SMS, PUSH
    subject = Column(String(255), nullable=True)
    message = Column(Text, nullable=False)
    status = Column(String(50), default="PENDING") # PENDING, SENT, FAILED
    error_message = Column(Text, nullable=True)
    sent_at = Column(DateTime, nullable=True)
