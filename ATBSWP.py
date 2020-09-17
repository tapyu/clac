import requests, bs4

res = requests.get('https://nostarch.com')
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

print(res.text)