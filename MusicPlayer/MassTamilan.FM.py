from  requests import get as server
import re
from bs4 import BeautifulSoup as Make

url="https://masstamilan.fm/"
res = server(url)
soup = Make(res.text,"html.parser")

data = soup.find_all(class_="dlink anim umami--click--dl128")[0]
link = data["href"]

print (server(url+link))

