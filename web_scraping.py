# from selenium import webdriver
# driver = webdriver.Chrome("C:\\Users\\rubem\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver.get('https://www.collinsdictionary.com/us/')
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


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

center_he = center.div.find('div', attr={'class':'he'})

print(center_he['class'])