import requests
from bs4 import BeautifulSoup as bs
import json

paieska = {'q':('picapica')}
rr = requests.get("http://google.com/search", params=paieska)

lll=(rr.text)


soup = bs(lll, "html.parser")


iii=soup.find_all(class_='srp')
print(iii)