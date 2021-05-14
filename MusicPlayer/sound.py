from bs4 import BeautifulSoup 
from requests import get 
import requests

domain ="http://www.purehumbug.com" 
urlm="http://www.purehumbug.com/shows/2006/1-99/"
page = requests.get(urlm)
html = page.text
soup = BeautifulSoup(html,"html.parser")

for link in soup.find_all("a"):
    url = link.get("href")
    if ".mp3" in url:
        print(url)
        file_name = url.split("1-99",1)[1]

        with open(file_name,"wb") as file:
            res = get(domain,url)
            file.write(res.content)
    else:
        continue



