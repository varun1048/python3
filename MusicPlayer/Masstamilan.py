from  requests import get as server
from bs4 import BeautifulSoup as Make

class Masstamilan:
    def __init__(self,inner):
        self.album_name = inner
        url=f"https://masstamilan.in/{self.album_name}"
        res = server(url)
        soup = Make(res.text,"html.parser")
        
        songName =soup.find_all(class_="nostyle")
        songLink =soup.find_all(class_="dlink anim")
        filterName = lambda name : "".join((x  for x in name if x != "\t" and x != "\n" ))
        self.datas = [{"name":filterName(songName[x].string),"link":songLink[x]["href"]} for x in  range(len(songLink))]
            

    def displaySongs(self):
        i = 0
        for x in self.datas:
            print(f"{i} \t{x['name']}")
            i += 1

    def (self):
        num = int(input("song number to download :"))
        if num in range(len(self.datas)):
            fileName =str(self.album_name+"_"+self.datas[num]["name"])
            res = server(self.datas[num]["link"])
            with open(fileName+".mp3",'wb') as file:
                file.write(res.content)
            print("Done")
        else:
            print("invalied input")

call  = Masstamilan(input("Album name Tamil :"))
call.displaySongs()
call.Download()
