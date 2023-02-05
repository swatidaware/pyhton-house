import requests
from bs4 import BeautifulSoup

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
exit()