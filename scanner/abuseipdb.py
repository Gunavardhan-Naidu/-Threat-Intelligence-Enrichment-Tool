import requests
import logging


api_key = ""

def abuseipdb_info(value:str) -> dict[str,any]:

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
            "Key": api_key,
            "Accept": "application/json"
        }
    params = {"ipAddress": value, "maxAgeInDays": 90}
        
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return(response.json())

