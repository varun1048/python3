from  requests import get as server
from bs4 import BeautifulSoup as Make

album_name = input("Enter name:")
url=f"https://masstamilan.in/{album_name}"

res = server(url)
soup = Make(res.text,"html.parser")
table =soup.find_all(class_="nostyle")
for x in table:
    print(x.string)