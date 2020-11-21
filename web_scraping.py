# from selenium import webdriver
# driver = webdriver.Chrome("C:\\Users\\rubem\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver.get('https://www.collinsdictionary.com/us/')
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

def is_class_cell_center(tag):
    """
    search if the class has the attribute "class" and if its value is "res_cel_center"
    """
    if tag.has_attr('class') and tag['class'][0] == "res_cell_center":
        return True
    else:
        return False


url = 'https://www.collinsdictionary.com/us/dictionary/english/bait'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, features="lxml")

main = soup.find('div', id='main_content')

# print(main.prettify())

# for center in main.find_all(is_class_cell_center, recursive=False, ):
#     print(center['class'])

# for tag in main.find_all(True):
#     print(tag.name)

center = main.find(is_class_cell_center, recursive=False)
# print(type(center))

meaning_core = center.div.find('div', class_='he').div.find('div', class_='dictionaries dictionary').find('div', class_='dictionary Cob_Adv_US dictentry').div.div

mp3_url = meaning_core.find('div', class_='mini_h2').find('span', class_='pron type-').find('span', class_='ptr hwd_sound type-hwd_sound').a['data-src-mp3']

mp3 = requests.get(mp3_url, allow_redirects=True)

#print(mp3_url)

open('bait.mp3', 'wb').write(mp3.content)

print(mp3.headers.get('content-type'))