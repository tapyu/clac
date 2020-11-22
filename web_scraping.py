# from selenium import webdriver
# driver = webdriver.Chrome("C:\\Users\\rubem\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver.get('https://www.collinsdictionary.com/us/')
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests, os

searched_word = 'bait'
url = f'https://www.collinsdictionary.com/us/dictionary/english/{searched_word}'
headers = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, features="lxml")

main = soup.find('div', id='main_content')

# print(main.prettify())
# for center in main.find_all(is_class_cell_center, recursive=False, ):
#     print(center['class'])

# for tag in main.find_all(True):
#     print(tag.name)
# print(type(center))

# Going to the main core the website
def is_class_cell_center(tag):
    """
    search if the class has the attribute "class" and if its value is "res_cel_center"
    """
    if tag.has_attr('class') and tag['class'][0] == "res_cell_center":
        return True
    else:
        return False

center = main.find(is_class_cell_center, recursive=False) # find the center column in the website
meaning_core = center.div.find('div', class_='he').div.find('div', class_='dictionaries dictionary').find('div', class_='dictionary Cob_Adv_US dictentry').div.div # return the main core the searched word

# catching the searched word sound
mp3_url = meaning_core.find('div', class_='mini_h2').find('span', class_='pron type-').find('span', class_='ptr hwd_sound type-hwd_sound').a['data-src-mp3']
mp3 = requests.get(mp3_url, headers=headers)

new_path = f'./words/{searched_word}'
if not os.path.exists(new_path):
    os.makedirs(new_path)

open(f'{new_path}/{searched_word}.mp3', 'wb').write(mp3.content)

# print(mp3.headers.get('content-type'))

# catching the inflections of the searched word
meaning_searched_word = meaning_core.find('div', class_='content definitions cobuild am')

inflections_web = meaning_searched_word.find('span', 'form inflected_forms type-infl')
inflections_list = []

for inflection_word in inflections_web.find_all('span', class_='orth', recursive=False):
    inflections_list.append(inflection_word.text)

# catching the definitions and the examples of the searched word

def search_definitions(tag):
    """
    assure that the web scraping returns just definitons of the word
    """
    if ' '.join(tag['class']) != 'hom':
        return False
    elif ' '.join(tag.div['class']) != 'sense':
        return False
    else:
        return True

definition_list = {'def': [], 'example': [], 'kind':[], 'mp3_url': [], 'mp3': []}

for index_def, definition in enumerate(meaning_searched_word.find_all(search_definitions, recursive=False)):
    def_path = f'{new_path}/def{index_def}'
    
    if not os.path.exists(def_path):
        os.makedirs(def_path)
    
    with open(f'{def_path}/definition{index_def}.txt', 'wt') as def_file:
        def_file.write(definition.find('span', class_=('gramGrp pos', 'gramGrp')).text+'\n') # save the type
        def_file.write(definition.div.find('div', class_='def').text.replace('\n','')) # save the definition
    
    for index_ex, example_audio in enumerate(definition.find('div', class_='sense', recursive=False).find_all('div', class_='cit type-example', recursive=False)):
        mp3_url = example_audio.find('span', class_='ptr exa_sound type-exa_sound').a['data-src-mp3']
        mp3 = requests.get(mp3_url, headers=headers)
        open(f'{def_path}/example{index_ex}.mp3', 'wb').write(mp3.content)
        open(f'{def_path}/example{index_ex}.txt', 'wt').write(example_audio.find('span', class_='quote').text)