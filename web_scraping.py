import requests, os, re
from utils.ws_utils import get_soup, is_class_cell_center, search_item

def web_scraping(name):
    """
    Scrape on https://www.collinsdictionary.com/us/ for the word name
    scraped_info = {'searched word':{'word':str(), 'mp3': Response()}, 'inflections':[], 'items':[{'meaning': str(), 'kind': str(), 'examples': [{'example': str(), 'mp3': Response()}]}]}
    """
    scraped_info = {'searched word': {'word': name}, 'inflections': [], 'items': []}
    soup = get_soup(scraped_info['searched word']['word'])

    # starting the web scrapping
    main = soup.find('div', id='main_content')
    center = main.find(is_class_cell_center, recursive=False) # find the center column in the website
    try:
        meaning_core = center.div.find('div', class_='he').div.find('div', class_='dictionaries dictionary').find('div', class_=re.compile('dictionary Cob_Adv_(US|Brit) dictentry')).div.div # return the main core the searched word
    except AttributeError:
        meaning_core = center.div.find('div', class_='he').div.find('div', class_='dictionaries dictionary dictionary Collins_Eng_Dict').div.div # return the main core the searched word

    # catching the searched word .mp3
    try:
        mp3_url = meaning_core.find('div', class_='mini_h2').find('span', class_='pron type-').find('span', class_='ptr hwd_sound type-hwd_sound').a['data-src-mp3']
        scraped_info['searched word']['mp3'] = requests.get(mp3_url, headers={'User-Agent': 'Mozilla/5.0'}).content
    except AttributeError:
        scraped_info['searched word']['mp3'] = None # if don't have the searched word .mp3, set it to None

    # catching the inflections of the searched word
    inflections_and_items = meaning_core.find('div', class_=re.compile('content definitions .*'))
    try:
        inflections_web = inflections_and_items.find('span', 'form inflected_forms type-infl')
        for inflection_word in inflections_web.find_all('span', class_='orth', recursive=False):
            scraped_info['inflections'].append(inflection_word.text)
        scraped_info['inflections'] = ' '.join(scraped_info['inflections']) # create a single string with all inflections
    except AttributeError:
        scraped_info['inflections'] = None
    
    for item in inflections_and_items.find_all(search_item, recursive=False): # iterating over the items
        scraped_info['items'].append({'meaning':item.div.find('div', class_='def').text.replace('\n',' ')}) # add the meaning of the item
        scraped_info['items'][-1]['kind'] = item.find('span', class_=('gramGrp pos', 'gramGrp')).text # add the kind of the new item
        example_per_item = []
        for example in item.find('div', class_='sense', recursive=False).find_all('div', class_='cit type-example', recursive=False):
            mp3_url = example.find('span', class_='ptr exa_sound type-exa_sound').a['data-src-mp3']
            mp3 = requests.get(mp3_url, headers={'User-Agent': 'Mozilla/5.0'})
            example_per_item.append({'example': example.find('span', class_='quote').text.replace('\n',' '), 'mp3': mp3.content})
        scraped_info['items'][-1]['examples'] = example_per_item # add the examples to the new item. If there aren't examples, it is a empty list
    return scraped_info


def write(scraped_info, option):
    """
    write on the disk the web scrapping
    """
    def_path = f"words/{scraped_info['searched word']['word']}/meaning_{option}"
    if not os.path.exists(def_path):
        os.makedirs(def_path)
    
    with open(f'{def_path}/meaning{option}.txt', 'wt') as def_file:
        def_file.write(scraped_info['items'][option-1]['meaning'].replace('\n','')) # save the meaning
    
    with  open(f'{def_path}/tag.txt', 'wt') as def_file:
        def_file.write(scraped_info['items'][option-1]['kind']+'\n') # save the kind

    for index_ex, example in enumerate(scraped_info['items'][option-1]['examples']): # save the example
        open(f'{def_path}/example{index_ex}.mp3', 'wb').write(example['mp3'])
        open(f'{def_path}/example{index_ex}.txt', 'wt').write(example['example'])

    if scraped_info['searched word']['mp3'] != None: # save the .mp3 word
        with open(f"words/{scraped_info['searched word']['word']}/{scraped_info['searched word']['word']}.mp3", 'wb') as def_file:
            def_file.write(scraped_info['searched word']['mp3'])
    
    if scraped_info['inflections'] != None:
        with open(f"words/{scraped_info['searched word']['word']}/inflections.txt", 'wt') as def_file:
            def_file.write(scraped_info['inflections'])