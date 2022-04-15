import json
import string

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

def to_json(str: string) -> dict:
    dict_str = json.loads(str)
    return dict_str

def get_page_html( page):
    html = bs(page, "html.parser")
    return html


def get_page(url):
        
        page = None

        try:
                       
            with uReq(url) as uClient:
                page = uClient.read()
        except Exception as ex:
            print(ex)
        finally:
            if uClient:
                uClient.close()
            

        return page