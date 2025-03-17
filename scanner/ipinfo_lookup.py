import ipinfo
import logging

access_token = '1cc9aca75e1842'


def ipinfo_info(value:str) -> dict[str,str]:
    try:
        handler=ipinfo.getHandler(access_token)
        info = handler.getDetails(value)
        return info.all
    except Exception as e:
        logging.error(f"IPinfo lookup failed for {value}: {e}")
        return {"error": str(e)}




    
