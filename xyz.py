import requests
from bs4 import BeautifulSoup
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
data = []
data_iterator = iter(soup.find_all('a'))
while True:
    try:
        country = next(data_iterator).text
        conform = next(data_iterator).text
        death = next(data_iterator).text
        continend = next(data_iterator).text
        data.append((
            country,
            int(conform.replace(', ', ' ')),
            int(death.replace(', ', ' ')),
            continend
        ))
    except StopIteration:
        break
        data.sort(key = lambda row: row[1], reversed = True)
