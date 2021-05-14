from  requests import get as server
from bs4 import BeautifulSoup as Make
import re

def Download(url,fileName):
    url="http://isaiminihits.net/music/view/62358"
    res = server(url)
    soup = Make(res.text,"html.parser")
    data = soup.find_all("a")[1]
    data =data['href']
    # print(data)

    with open(fileName+".mp3",'wb') as f:
        res = server("https://dslink.xyz/Masstamilan.In/Lift/Inna%20Mylu-Masstamilan.In.mp3")
        f.write(res.content)

# songName = "hero"
# res = server(f"http://isaiminihits.net/{songName}-mp3-songs.html")
# soup = Make(res.text,"html.parser")
# print(soup.h2.string)
Download("","test")
