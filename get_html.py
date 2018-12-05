import requests
from requests.exceptions import RequestException

def get_html(url,header):
    try:
        respone = requests.get(url,headers=header)
        if respone.status_code == 200:
            return respone.text
        return None
    except RequestException:
        return None
