import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import logging

logger = logging.getLogger(__name__)

class SMSService:
    def __init__(self):
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'AC_mock_sid')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'mock_token')
        self.from_number = os.getenv('TWILIO_FROM_NUMBER', '+1234567890')
        
        # Initialize client only if we have real credentials
        self.client = None
        if not self.account_sid.startswith('AC_mock'):
            self.client = Client(self.account_sid, self.auth_token)

    def send_appointment_reminder(self, to_number: str, patient_name: str, date_str: str, doctor_name: str) -> bool:
        """
        Sends an automated SMS reminder for upcoming appointments.
        """
        message_body = (
            f"Hi {patient_name}, this is a reminder from HealthSphere for your "
            f"appointment with Dr. {doctor_name} on {date_str}. "
            f"Reply CANCEL if you need to reschedule."
        )
        return self._send_sms(to_number, message_body)

    def send_critical_alert(self, to_number: str, message: str) -> bool:
        """
        Sends high-priority alerts (e.g. ICU Vitals drop) to on-call doctors.
        """
        urgent_body = f"[URGENT - HEALTHSPHERE] {message}"
        return self._send_sms(to_number, urgent_body)

    def _send_sms(self, to_number: str, body: str) -> bool:
        if not self.client:
            logger.info(f"[MOCK SMS] To: {to_number} | Body: {body}")
            return True
            
        try:
            message = self.client.messages.create(
                body=body,
                from_=self.from_number,
                to=to_number
            )
            logger.info(f"SMS Sent Successfully. SID: {message.sid}")
            return True
        except TwilioRestException as e:
            logger.error(f"Failed to send SMS via Twilio: {e}")
            return False
