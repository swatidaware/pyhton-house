import requests
from bs4 import BeautifulSoup
URL = 'http://www.values.com/inspirational-quotes'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'lmxl')
print(soup.prettify())
