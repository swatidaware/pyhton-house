import urllib.request
from pprint import pprint
from html.parser import HTMLTableParser
import pandas as pd
import DB_connector as db
def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()
xhtml = url_get_contents('https://www.moneycontrol.com/india\/stockpricequote/refineries/relianceindustries/RI').decode('utf-8')
p = HTMLTableParser()
p.feed(xhtml)
pprint(p.tables[1])
print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[1]))
