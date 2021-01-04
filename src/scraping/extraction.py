import requests
import re
from bs4 import BeautifulSoup

def truncateURL(URL):
    base = 'https://www.amazon.com'

    pattern = r'/dp/\d+'

    try: 
        productNumber = re.findall(pattern, URL)[0]
    except:
        productNumber = ''

    shortURL = base + productNumber

    return shortURL

    
