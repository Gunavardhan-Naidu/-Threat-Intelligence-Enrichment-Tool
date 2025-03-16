import shodan
import logging

api_key = shodan.Shodan('TmrNDo7QxhVr4VUzIZk23POFenBZ9kfr')


def shodan_info(value:str) -> dict[str,str]:
    try:
        info = api_key.host(value, history = True)
        return info.__dict__
    except shodan.APIError as e:
        logging.error(f"API error in shodan: {e}")




    
