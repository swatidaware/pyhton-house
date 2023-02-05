import requests
from bs4 import BeautifulSoup

from mjhnbl import soup

anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link != '#'):
        link = 'https://www.1mg.com/drugs-all-medicines' +link.get('href')
        all_links.add(link)
        #print(link)
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
exit()
