import os
from rpa import add_word
import pyinputplus as pyip
from web_scraping import web_scraping, write

def run_clac(word):
    """ 
    This is the main function that links the CLAC with the CLI and the searched word
    """
    print('Scraping, please wait')
    scraped_info = web_scraping(word)
    os.system('cls')

    count = 0
    if scraped_info != None:
        print(f"The word \"{word}\" was found on the Collins website!\nhttps://www.collinsdictionary.com/us/dictionary/english/{word}\n\n")
        print("_"*59)
        if scraped_info['inflections'] == None:
            print(str(count) + '. This word(s) don\'t have inflections')
        else:
            print(str(count) +  ". infletions:" + ", ".join(scraped_info['inflections']))
        count += 0  
        print(f"{count}. Number of meanings: {str(len(scraped_info['meanings']))}")
        for meaning_count, meaning in enumerate(scraped_info['meanings'], start=0):
            print(f'Meaning number {meaning_count}')
            for key, value in meaning.items():
                print(f"\t{key.capitalize()}: {value.capitalize()}")
            print(f"\tNumber of examples: {str(len(scraped_info['examples'][meaning_count-2]))}")

    print("_"*59)
    if len(scraped_info['examples']) != 0:
        option = pyip.inputInt(prompt='Which meaning number do you want to save? (ctrl+C to cancel)\n', min=0, max=len(scraped_info['meanings']))
        write(scraped_info, option)
        os.system('cls')
        print(f"The folder ./word/{word}/meaning_{option}/ was created and the examples and the meaning were saved.")
    else:
        option = 0
        write(scraped_info, option)
        print(f"The folder ./word/{word}/meaning_{option}/ was created and the examples and the meaning were saved.")
    is_rpa = pyip.inputYesNo(prompt="Do you want to carry out the RPA (Robotic Process Automation) on Anki? (Yes/No question) (ctrl+C to cancel)\n", postValidateApplyFunc=utils.tranform1bool)
    if is_rpa:
        add_word(word, option, scraped_info)