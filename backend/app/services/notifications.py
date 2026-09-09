import asyncio
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.notifications import NotificationLog

class NotificationService:
    @staticmethod
    async def send_email(to_address: str, subject: str, body: str, db: Session, user_id: str):
        """
        Simulates an SMTP email dispatch.
        """
        log = NotificationLog(user_id=user_id, channel="EMAIL", subject=subject, message=body)
        db.add(log)
        db.commit()
        
        # Simulate network delay
        await asyncio.sleep(1)
        
        log.status = "SENT"
        log.sent_at = datetime.utcnow()
        db.commit()
        return True

    @staticmethod
    async def send_sms(phone_number: str, message: str, db: Session, user_id: str):
        """
        Simulates an SMS dispatch via Twilio.
        """
        log = NotificationLog(user_id=user_id, channel="SMS", message=message)
        db.add(log)
        db.commit()
        
        # Simulate network delay
        await asyncio.sleep(0.5)
        
        log.status = "SENT"
        log.sent_at = datetime.utcnow()
        db.commit()
        return True
