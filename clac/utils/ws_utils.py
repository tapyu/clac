from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

""" 
this file gather all usefull functionalities used in the web_scrapping
"""

def get_soup(name):
    url = f"https://www.collinsdictionary.com/us/dictionary/english/{name}".replace(' ','-')
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

def search_item(tag): # catching the item of the searched word
    """
    assure that the web scraping returns the item
    """
    try:
        if ' '.join(tag['class'])=='hom': #  or tag.div == None
            try:
                if ' '.join(tag.div['class'])=='sense':
                    return True
                else:
                    return False
            except TypeError: # tag.div returned NoneType
                return False
        else:
            return False # it is not an item
    except KeyError: # tag doesn't have a class attribute
        return False