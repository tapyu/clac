import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def web_scraping(name):
    """
    Scrape on https://www.collinsdictionary.com/us/ for the word name
    scrapped_info = {'searched word':{'word':str(), 'mp3': Response()}, 'inflections':[], 'meanings':[{'meaning': str(), 'kind': str(), 'examples': [{'example': str(), 'mp3': Response()}]}]}
    """
    scrapped_info = {'searched word': {'word': name}, 'inflections': [], 'meanings': [], 'examples': []}
    soup = get_soup(scrapped_info['searched word']['word'])

    # starting the web scrapping
    main = soup.find('div', id='main_content')
    center = main.find(is_class_cell_center, recursive=False) # find the center column in the website
    meaning_core = center.div.find('div', class_='he').div.find('div', class_='dictionaries dictionary').find('div', class_='dictionary Cob_Adv_US dictentry').div.div # return the main core the searched word

    # catching the searched word .mp3
    mp3_url = meaning_core.find('div', class_='mini_h2').find('span', class_='pron type-').find('span', class_='ptr hwd_sound type-hwd_sound').a['data-src-mp3']
    scrapped_info['searched word']['mp3'] = requests.get(mp3_url, headers={'User-Agent': 'Mozilla/5.0'})

    # catching the inflections of the searched word
    meaning_searched_word = meaning_core.find('div', class_='content definitions cobuild am')
    inflections_web = meaning_searched_word.find('span', 'form inflected_forms type-infl')

    for inflection_word in inflections_web.find_all('span', class_='orth', recursive=False):
        scrapped_info['inflections'].append(inflection_word.text)
    
    for definition in meaning_searched_word.find_all(search_definitions, recursive=False):
        scrapped_info['meanings'].append({'meaning':definition.div.find('div', class_='def').text.replace('\n','')})
        scrapped_info['meanings'][-1]['kind'] = definition.find('span', class_=('gramGrp pos', 'gramGrp')).text
        for example_audio in definition.find('div', class_='sense', recursive=False).find_all('div', class_='cit type-example', recursive=False):
            mp3_url = example_audio.find('span', class_='ptr exa_sound type-exa_sound').a['data-src-mp3']
            mp3 = requests.get(mp3_url, headers={'User-Agent': 'Mozilla/5.0'})
            scrapped_info['examples'].append({'example': example_audio.find('span', class_='quote').text, 'mp3': mp3.content})
    return scrapped_info

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

# def write(scrapped_info):
#     """
#     write on the disk the web scrapping
#     """
#     def_path = f'{new_path}/def{index_def}'
#     if not os.path.exists(def_path):
#         os.makedirs(def_path)
#     for index_def, definition in enumerate(meaning_searched_word.find_all(search_definitions, recursive=False)):
#         with open(f'{def_path}/definition{index_def}.txt', 'wt') as def_file:
#             def_file.write(definition.find('span', class_=('gramGrp pos', 'gramGrp')).text+'\n') # save the type
#             def_file.write(definition.div.find('div', class_='def').text.replace('\n','')) # save the definition
        
#         for index_ex, example_audio in enumerate(definition.find('div', class_='sense', recursive=False).find_all('div', class_='cit type-example', recursive=False)):
#             mp3_url = example_audio.find('span', class_='ptr exa_sound type-exa_sound').a['data-src-mp3']
#             mp3 = requests.get(mp3_url, headers=headers)
#             open(f'{def_path}/example{index_ex}.mp3', 'wb').write(mp3.content)
#             open(f'{def_path}/example{index_ex}.txt', 'wt').write(example_audio.find('span', class_='quote').text)