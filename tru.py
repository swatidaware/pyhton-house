import requests
url = 'https://www.1mg.com/drugs-all-medicines'
tr = requests.get(url)
print(tr)
print(tr.content)