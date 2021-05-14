from  requests import get as server
from bs4 import BeautifulSoup as Make

album_name = input("Enter name :")
url=f"https://masstamilan.in/{album_name}"

res = server(url)
soup = Make(res.text,"html.parser")

songName =soup.find_all(class_="nostyle")
songLink =soup.find_all(class_="dlink anim")


filterName = lambda name : "".join((x  for x in name if x != "\t" and x != "\n" ))
datas = [{"name":filterName(songName[x].string),"link":songLink[x]["href"]} for x in  range(len(songLink)) ]

i = 0
for x in datas:
    print(f"{i} \t{x['name']}")
    i += 1

def Download(fileName,url):
    res = server(url)
    with open(fileName+".mp3",'wb') as file:
        file.write(res.content)
        print("Done")

num = int(input("song number to download :"))
Download(str(album_name+"_"+datas[num]["name"]),datas[num]["link"])
