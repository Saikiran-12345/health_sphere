import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class HL7Parser:
    """
    Enterprise HL7 v2.x Message Parser.
    Extracts clinical data from raw pipe-delimited (|) hospital messages.
    """
    
    @staticmethod
    def parse_message(raw_hl7: str) -> Dict[str, Any]:
        segments = raw_hl7.strip().split('\n')
        parsed_data = {
            "metadata": {},
            "patient": {},
            "observations": []
        }
        
        try:
            for segment in segments:
                fields = segment.split('|')
                segment_type = fields[0]
                
                if segment_type == "MSH":
                    parsed_data["metadata"] = {
                        "sending_app": fields[2] if len(fields) > 2 else "",
                        "receiving_app": fields[4] if len(fields) > 4 else "",
                        "message_time": fields[6] if len(fields) > 6 else "",
                        "message_type": fields[8] if len(fields) > 8 else "",
                    }
                elif segment_type == "PID":
                    names = fields[5].split('^') if len(fields) > 5 else ["", ""]
                    parsed_data["patient"] = {
                        "patient_id": fields[3] if len(fields) > 3 else "",
                        "last_name": names[0],
                        "first_name": names[1] if len(names) > 1 else "",
                        "dob": fields[7] if len(fields) > 7 else "",
                        "gender": fields[8] if len(fields) > 8 else ""
                    }
                elif segment_type == "OBX":
                    parsed_data["observations"].append({
                        "type": fields[2] if len(fields) > 2 else "",
                        "observation": fields[3] if len(fields) > 3 else "",
                        "value": fields[5] if len(fields) > 5 else "",
                        "units": fields[6] if len(fields) > 6 else "",
                        "reference_range": fields[7] if len(fields) > 7 else "",
                        "abnormal_flags": fields[8] if len(fields) > 8 else ""
                    })
                    
            return parsed_data
        except Exception as e:
            logger.error(f"HL7 Parsing Failed: {str(e)}")
            raise ValueError(f"Invalid HL7 format: {str(e)}")
