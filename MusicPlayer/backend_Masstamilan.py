from  requests import get as server
from bs4 import BeautifulSoup as Make
from playsound import playsound  
import os

class Masstamilan:

    def __init__(self):
        print("Masstamilan connected")

    def search(self,inner):
        album = inner.replace(" ","-")
        url=f"https://masstamilan.in/{album}"
        res = server(url)
        self.fileName=""
        self.soup = Make(res.text,"html.parser")
        self.album_name = self.wast_function(self.soup.title.string)
        print(self.soup.title.string)
        
        if self.soup.title.string == "Masstamilan | High Quality Tamil Mp3 Songs Free Download":
            notvalied = """\tEnnama neenga ippadi panreengale ma. Olunga name ah type pannunga ma."""
            print(notvalied)
            self.playMode = False
        else:
            self.playMode = True
            songName =self.soup.find_all(class_="nostyle")
            songLink =self.soup.find_all(class_="dlink anim")
            filterName = lambda name : "".join((x  for x in name if x != "\t" and x != "\n" ))
            self.datas = [{"name":filterName(songName[x].string),"link":songLink[x]["href"]} for x in  range(len(songLink))]

            imageclass = self.soup.find(class_="main-image")
            imageScr=imageclass.img['src']
            imageRes = server(imageScr)
            with open("temp.jpg","wb") as file:
                file.write(imageRes.content)


    def albumInfo(self):
        if self.playMode:
            keys=["Starring","Director","Music"]
            try:
                out=self.soup.find(class_="info").p.get_text()
                return out
            except Exception as err:
                print(err)

        

    def wast_function(self,name):
        result = ""
        for  x in str(name):
            if x == ")":
                result += ")"
                break 
            result += x
        return result
    


    def displaySongs(self):
        i = 0
        if self.playMode:
            try:
                for x in self.datas:
                    print(f"\t\t{i} {x['name']}")
                    i += 1
            except  Exception as err:
                print(f"Oops!\t{err.__class__} occurred. at displaySongs")

    def Download(self):
        if self.playMode:
            try:
                num = int(input("song number to download :"))
            except  Exception as err:
                    print("Oops!\t", err.__class__, "occurred. at Download")
            else:
                if num in range(len(self.datas)):
                    print("loading")
                    self.fileName =str(self.album_name+"_"+self.datas[num]["name"])+".mp3"
                    res = server(self.datas[num]["link"])
                    with open(self.fileName,'wb') as file:
                        file.write(res.content)
                    print("Download Done")
                else:
                    print("invalied input")

    def playOnline(self,inner):
        temp="temp.mp3"
        res = server(inner)
        print("loading")

        with open(temp,'wb') as file:
            file.write(res.content)
        
        print("playing .....")
        print("press (ctrl + c) to exit")
        playsound("temp.mp3")  
        if os.path.exists(temp):
            os.remove(temp)
        else:
            print("The file does not exist") 
        print("songs ends")

 
