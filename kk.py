#import requests
#url = "http://www.values.com//inspirational-quotes"
#hh = requests.get(url)
#print(hh)
#print(hh.content)

import requests
url = "https://www.1mg.com/aboutUs"
a = requests.get(url)
#print(a)
#print(a.content)

url = "https://www.1mg.com/contactUs"
b = requests.get(url)
#print(b)
#print(b.content)

url = "https://www.1mg.com/PrivacyPolicy"
c = requests.get(url)
print(c)
print(c.content)