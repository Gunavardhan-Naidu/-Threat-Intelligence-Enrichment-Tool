import whois
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO)

def whois_info(value:str) -> dict[str,any]:
    try:
        w = whois.whois(value)
        return w.__dict__
    except Exception as e:
        logging.error(f"WHOIS lookup failed for this {value}: {str(e)}")
    return {"error": str(e)}