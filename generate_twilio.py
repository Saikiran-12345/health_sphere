import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Update Requirements for Twilio
path_req = "backend/requirements.txt"
with open(path_req, "a") as f:
    f.write("\ntwilio\n")

# 2. Twilio Service Implementation
create_file('backend/app/services/sms_service.py', """
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
        \"\"\"
        Sends an automated SMS reminder for upcoming appointments.
        \"\"\"
        message_body = (
            f"Hi {patient_name}, this is a reminder from HealthSphere for your "
            f"appointment with Dr. {doctor_name} on {date_str}. "
            f"Reply CANCEL if you need to reschedule."
        )
        return self._send_sms(to_number, message_body)

    def send_critical_alert(self, to_number: str, message: str) -> bool:
        \"\"\"
        Sends high-priority alerts (e.g. ICU Vitals drop) to on-call doctors.
        \"\"\"
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
""")

# 3. Connect SMS to the IoT Alerting Engine
path_iot = "backend/app/api/iot.py"
with open(path_iot, "r") as f:
    iot_content = f.read()

if "from app.services.sms_service import SMSService" not in iot_content:
    iot_content = iot_content.replace(
        "from datetime import datetime",
        "from datetime import datetime\nfrom app.services.sms_service import SMSService"
    )
    
    # Inside the loop where the critical alert is printed
    alert_target = "print(f\"[CRITICAL ALERT] Patient {payload.get('patient_id')} vitals failing!\")"
    sms_trigger = alert_target + "\n                sms = SMSService()\n                sms.send_critical_alert('+15550199', f\"Code Blue! Patient {payload.get('patient_id')} vitals critical. HR: {payload.get('heart_rate')} SpO2: {payload.get('sp02')}\")"
    
    iot_content = iot_content.replace(alert_target, sms_trigger)
    
    with open(path_iot, "w") as f:
        f.write(iot_content)

print("Twilio SMS integration generated.")
