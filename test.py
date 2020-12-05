from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests, os

searched_word = 'bait'
url = f'https://www.collinsdictionary.com/us/dictionary/english/{searched_word}'
headers = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, features="lxml")