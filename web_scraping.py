# from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# data = {'meaning':'', 'conjugations':[], 'conjugations sp':[], 'examples':[], 'examples sp':[], 'tag':''} # sp = sound path

# print('What is the name that you would like to search?')
# word = input()

# driver = webdriver.Chrome("C:\\Users\\rubem\\Downloads\\chromedriver_win32\\chromedriver.exe")

# driver.get('https://www.collinsdictionary.com/us/')

url = 'https://www.collinsdictionary.com/us/dictionary/english/bait'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, features="lxml")

search = soup.find('div', class_='hom')

print(search.prettify())
print(search.span.text)