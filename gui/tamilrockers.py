import requests
from bs4 import BeautifulSoup
soup =BeautifulSoup(requests.get("https://www.1tamilmv.art").text,"html.parser")

for x in soup.find_all("strong"):
    for words in str(x.string):
        if words == ")":
            print(str(x.string))




