from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://www.collinsdictionary.com/us/dictionary/english/bait'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = BeautifulSoup(webpage, features="lxml")

print(page_soup)