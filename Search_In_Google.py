se=input("Search:\n")

import requests

from bs4 import BeautifulSoup # pip install bs4

url=f"https://www.google.com/search?q={se}"

req=requests.get(url)

so=BeautifulSoup(req.text,"html.parser")

res=so.find("div",class_="BNeawe").text

print(res)