from .whois_lookup import whois_info
from .virustotal import vt_info
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Manager:
    def __init__(self):
        logging.info("Manager initialized")
    def controller(self, input_type: str, value: str) -> dict[str,any]:
            # logging.info(f"controller() called with: {input_type}, {value}")
            result = {}
            try:
                if input_type in ["ipaddress", "domain"]:
                     result["whois lookup data"] = whois_info(value)
                
                result["virustotal lookup data"] = vt_info(input_type, value)

                return result
            

            except Exception as e:
                 logging.error(f"Error in controller(whois){value}: {str(e)}")
                 return{"error": str(e)}
            
            

