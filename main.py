import os
from web_scraping import web_scraping, write

os.system('cls')
print('What is the name of the word/expression?')
name = input()
print('scraping, wait please')
scraped_info = web_scraping(name)
os.system('cls')

count = 1
if scraped_info != None:
    print(f"The word \"{name}\" was found on the Collins website!\n\n")
    print("-"*60)
    print(str(count) +  ". infletions:" + ", ".join(scraped_info['inflections']))
    count += 1  
    print(f"{count}. Number of meanings: {str(len(scraped_info['meanings']))}")
    for meaning_count, meaning in enumerate(scraped_info['meanings']):
        print(f'Meaning number {meaning_count}')
        print(f"\tNumber of examples: {str(len(scraped_info['examples'][meaning_count]))}")
        for key, value in meaning.items():
            print(f"\t{key.capitalize()}: {value.capitalize()}")

print('\nWhich meaning number do you want to save? (ctrl+C to cancel)')
option = int(input())
write(scraped_info, option)