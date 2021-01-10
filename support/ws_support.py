from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

""" 
this file gather all usefull functionalities used in the web_scrapping
"""

def get_soup(name):
    url = f"https://www.collinsdictionary.com/us/dictionary/english/{name}"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
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

def search_definitions(tag): # catching the definitions and the examples of the searched word
    """
    assure that the web scraping returns just definitions of the word
    """
    if ' '.join(tag['class']) != 'hom':
        return False
    elif ' '.join(tag.div['class']) != 'sense':
        return False
    else:
        return True