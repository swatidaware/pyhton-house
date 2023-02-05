import requests
from bs4 import BeautifulSoup
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
data = []
data_iterator = iter(soup.find_all('td'))
while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text
        data.append((
            country,
            int(confirmed.replace(', ', '')),
            int(deaths.replace(', ', '')),
            continent
        ))
    except StopIteration:
        break
data.sort(key = lambda row: row[1], reverse = True)
