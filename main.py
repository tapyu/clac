import os
import pyinputplus as pyip
from web_scraping import web_scraping, write
from main_support import check_is_int, tranform2bool

os.system('cls')
name = pyip.inputCustom(check_is_int, prompt='What is the name of the word/expression? (ctrl+C to cancel)\n').replace(' ', '-')
print('Scraping, please wait')
scraped_info = web_scraping(name)
os.system('cls')

count = 1
if scraped_info != None:
    print(f"The word \"{name}\" was found on the Collins website!\nhttps://www.collinsdictionary.com/us/dictionary/english/{name}\n\n")
    print("_"*60)
    print(str(count) +  ". infletions:" + ", ".join(scraped_info['inflections']))
    count += 1  
    print(f"{count}. Number of meanings: {str(len(scraped_info['meanings']))}")
    for meaning_count, meaning in enumerate(scraped_info['meanings'], start=1):
        print(f'Meaning number {meaning_count}')
        for key, value in meaning.items():
            print(f"\t{key.capitalize()}: {value.capitalize()}")
        print(f"\tNumber of examples: {str(len(scraped_info['examples'][meaning_count-1]))}")

print("_"*60)
option = pyip.inputInt(prompt='Which meaning number do you want to save? (ctrl+C to cancel)\n', min=1, max=len(scraped_info['meanings']))
write(scraped_info, option)
os.system('cls')
print(f"The folder ./word/{name}/meaning_{option}/ was created and the examples and the meanings were saved.")
is_rpa = pyip.inputYesNo(prompt="Do you want carry out the RPA (Robotic Process Automation) on Anki? (Yes/No question) (ctrl+C to cancel)\n", postValidateApplyFunc=tranform2bool)
print(is_rpa)