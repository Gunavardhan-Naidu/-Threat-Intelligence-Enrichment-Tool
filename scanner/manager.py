from .whois_lookup import whois_info
from .virustotal import vt_info
from .abuseipdb import abuseipdb_info
from .shodanmod import shodan_info
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
            if input_type == "unknown":
                logging.info(f"Skipping unknown input type for value: {value}")
                return {"skipped": "unknown input type"}
            try:
                if input_type in ["ipaddress", "domain"]:
                     result["whois lookup data"] = whois_info(value)
                     result["shodan info"] = shodan_info(value)

                if input_type in ["ipaddress"]:
                     result["Abuseipdb"] = abuseipdb_info(value)
                result["virustotal lookup data"] = vt_info(input_type, value)
                return result
            except Exception as e:
                 logging.error(f"Error in controller: {value}: {str(e)}")
                 return{"error": str(e)}
            
            

