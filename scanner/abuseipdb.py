import requests
import logging


api_key = "81504e1a2910ac60649c74bfed0b111e259cfd3490a71b53712b3b13b9ffaeb177885ed3d7d0a4a3"

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

