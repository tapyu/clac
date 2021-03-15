import os
from rpa import add_word
from .pyip_utils import tranform2bool
import pyinputplus as pyip
from web_scraping import web_scraping, write

def run_clac_cli(word, yes_rpa):
    """ 
    This is the main function that links the CLAC with a CLI
    """
    print('Scraping, please wait')
    try:
        scraped_info = web_scraping(word)
    except ValueError as e:
        raise ValueError(e.args[0]) from e
    except LookupError as e:
        raise LookupError(e.args[0]) from e
    
    os.system('cls')

    if scraped_info != None:
        print(f"The word \"{word}\" was found on the Collins website!\nhttps://www.collinsdictionary.com/us/dictionary/english/{word}\n\n")
        print("_"*59)
        if scraped_info['inflections'] == None:
            print('This word(s) don\'t have inflections')
        else:
            print( "Infletions:" + scraped_info['inflections'])
        count = 1
        print(f"{count}. Number of meanings: {str(len(scraped_info['items']))}")
        for item_count, item in enumerate(scraped_info['items'], start=1): # print the kind and meaning of an item
            print(f'Meaning number {item_count}')
            for key, value in item.items(): # select all components in item, except examples
                if key == 'examples': continue
                print(f"\t{key.capitalize()}: {value.capitalize()}")
            print(f"\tNumber of examples: {str(len(item['examples']))}")

    print("_"*59)
    if len(scraped_info['items']) != 1: # if there is more than one item
        option = pyip.inputInt(prompt='Which meaning number do you want to save? (ctrl+C to cancel)\n', min=0, max=len(scraped_info['items']))
        write(scraped_info, option)
        os.system('cls')
        print(f"The folder ./word/{word}/meaning_{option}/ was created and the examples and the meaning were saved.")
    else:
        option = 0
        write(scraped_info, option)
        print(f"The folder ./word/{word}/meaning_{option}/ was created and the examples and the meaning were saved.")
    if yes_rpa: # yes_rpa is an argument from the CLI
        add_word(word, option, scraped_info)
    else: # if the user don't set rpa, ask it
        is_rpa = pyip.inputYesNo(prompt="Do you want to carry out the RPA (Robotic Process Automation) on Anki? (Yes/No question) (ctrl+C to cancel)\n", postValidateApplyFunc=tranform2bool)
        if is_rpa:
            add_word(word, option, scraped_info)