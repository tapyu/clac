import os
from web_scraping import web_scraping

print('What is the name of the word/expression?')
name = input()
scrapped_info = web_scraping(name)
os.system('cls')

print(f"information for {scrapped_info['searched word']['word']}")
print("infletions:" + ", ".join(scrapped_info['inflections']))