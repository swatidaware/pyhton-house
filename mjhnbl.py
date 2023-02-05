import requests
from bs4 import BeautifulSoup
url = "https://www.1mg.com/drugs-all-medicines"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
title = soup.title
paras = soup.find_all('a')
url = "https://www.1mg.com/drugs-all-medicines"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
blog_titles = soup.find_all('h2',attrs={'class':"blog-card__contente-title"})
for title in blog_titles:
    print(blog_titles)
#from selenium web driver import chrome
#drive = chrome(executable_path="https://www.1mg.com/drugs-all-medicines")
#driver.get("https://www.1mg.com/drugs-all-medicine")
#print(drive)


