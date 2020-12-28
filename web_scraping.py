import requests, os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def web_scraping(name):
    """
    Scrape on https://www.collinsdictionary.com/us/ for the word name
    scraped_info = {'searched word':{'word':str(), 'mp3': Response()}, 'inflections':[], 'meanings':[{'meaning': str(), 'kind': str(), 'examples': [{'example': str(), 'mp3': Response()}]}]}
    """
    scraped_info = {'searched word': {'word': name}, 'inflections': [], 'meanings': [], 'examples': []}
    soup = get_soup(scraped_info['searched word']['word'])

    # starting the web scrapping
    main = soup.find('div', id='main_content')
    center = main.find(is_class_cell_center, recursive=False) # find the center column in the website
    meaning_core = center.div.find('div', class_='he').div.find('div', class_='dictionaries dictionary').find('div', class_='dictionary Cob_Adv_US dictentry').div.div # return the main core the searched word

    # catching the searched word .mp3
    mp3_url = meaning_core.find('div', class_='mini_h2').find('span', class_='pron type-').find('span', class_='ptr hwd_sound type-hwd_sound').a['data-src-mp3']
    scraped_info['searched word']['mp3'] = requests.get(mp3_url, headers={'User-Agent': 'Mozilla/5.0'}).content

    # catching the inflections of the searched word
    meaning_searched_word = meaning_core.find('div', class_='content definitions cobuild am')
    inflections_web = meaning_searched_word.find('span', 'form inflected_forms type-infl')

    for inflection_word in inflections_web.find_all('span', class_='orth', recursive=False):
        scraped_info['inflections'].append(inflection_word.text)
    
    for meaning in meaning_searched_word.find_all(search_definitions, recursive=False):
        scraped_info['meanings'].append({'meaning':meaning.div.find('div', class_='def').text.replace('\n','')})
        scraped_info['meanings'][-1]['kind'] = meaning.find('span', class_=('gramGrp pos', 'gramGrp')).text
        example_per_meaning = []
        for example in meaning.find('div', class_='sense', recursive=False).find_all('div', class_='cit type-example', recursive=False):
            mp3_url = example.find('span', class_='ptr exa_sound type-exa_sound').a['data-src-mp3']
            mp3 = requests.get(mp3_url, headers={'User-Agent': 'Mozilla/5.0'})
            example_per_meaning.append({'example': example.find('span', class_='quote').text, 'mp3': mp3.content})
        scraped_info['examples'].append(example_per_meaning)
    return scraped_info

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

def write(scraped_info, option):
    """
    write on the disk the web scrapping
    """
    def_path = f"words/{scraped_info['searched word']['word']}/meaning_{option}"
    if not os.path.exists(def_path):
        os.makedirs(def_path)
    
    with open(f'{def_path}/meaning{option}.txt', 'wt') as def_file:
        def_file.write(scraped_info['meanings'][option-1]['meaning'].replace('\n','')) # save the meaning
    
    with  open(f'{def_path}/tag.txt', 'wt') as def_file:
        def_file.write(scraped_info['meanings'][option-1]['kind']+'\n') # save the kind

    for index_ex, example in enumerate(scraped_info['examples'][option-1]):
        open(f'{def_path}/example{index_ex}.mp3', 'wb').write(example['mp3'])
        open(f'{def_path}/example{index_ex}.txt', 'wt').write(example['example'])

    with open(f"words/{scraped_info['searched word']['word']}/{scraped_info['searched word']['word']}.mp3", 'wb') as def_file:
        def_file.write(scraped_info['searched word']['mp3'])