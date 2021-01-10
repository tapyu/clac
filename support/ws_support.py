from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

""" 
this file gather all usefull functionalities used in the web_scrapping
"""

def get_soup(root):
    url = f"https://www.collinsdictionary.com/us/dictionary/english/{root}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    return BeautifulSoup(webpage, features="lxml")

def is_class_cell_center(tag):
    """
    search if the class has the attribute "class" and if its value is "res_cel_center"
    """
    if tag.has_attr('class') and tag['class'][0] == "res_cell_center":
        return True
    else:
        return False