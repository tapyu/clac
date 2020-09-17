from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

data = {'meaning':'', 'conjugations':[], 'conjugations sp':[], 'examples':[], 'examples sp':[], 'tag':''} # sp = sound path

print('What is the name that you would like to search?')
word = input()

driver = webdriver.Chrome("C:\\Users\\rubem\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get('https://www.collinsdictionary.com/us/')