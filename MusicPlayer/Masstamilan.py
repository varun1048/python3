from  requests import get as server
from bs4 import BeautifulSoup as Make

class Masstamilan:

    def __init__(self,inner):
        album = inner.replace(" ","-")
        url=f"https://masstamilan.in/{album}"
        res = server(url)
        self.soup = Make(res.text,"html.parser")
        self.album_name = self._filterName(self.soup.title.string)
        # print(self.album_name)
        
        if self.soup.title.string == "Masstamilan | High Quality Tamil Mp3 Songs Free Download":
            notvalied = """\tEnnama neenga ippadi panreengale ma. Olunga address ah type pannunga ma."""
            print(notvalied)
        else:
            songName =self.soup.find_all(class_="nostyle")
            songLink =self.soup.find_all(class_="dlink anim")
            filterName = lambda name : "".join((x  for x in name if x != "\t" and x != "\n" ))
            self.datas = [{"name":filterName(songName[x].string),"link":songLink[x]["href"]} for x in  range(len(songLink))]

    def albumInfo(self):
        keys=["Starring","Director","Music"]
        info = dict.fromkeys(keys,"i")
        # print(info[0])
        out=self.soup.find(class_="info").p.get_text("|",strip=True).split("|")  #"",strip=True
        out = [out[x] for x in range(len(out)-5) if x%2 != 0]
        # i =0
        # result = {x : out[0] for x in info  }
        print(info)
        

    def _filterName(self,name):
        result = ""
        for  x in str(name):
            if x == ")":
                result += ")"
                break 
            result += x
        return result
    


    def displaySongs(self):
        i = 0
        try:
            for x in self.datas:
                print(f"{i} \t{x['name']}")
                i += 1
        except  Exception as err:
            print(f"Oops!\t{err.__class__} occurred. at displaySongs")

    def Download(self):
        try:
            num = int(input("song number to download :"))
        except  Exception as err:
                print("Oops!\t", err.__class__, "occurred. at Download")
        else:
            if num in range(len(self.datas)):

                fileName =str(self.album_name+"_"+self.datas[num]["name"])
                res = server(self.datas[num]["link"])
                with open(fileName+".mp3",'wb') as file:
                    file.write(res.content)
                print("Download Done")
            else:
                print("invalied input")

# call  = Masstamilan(input("Album name Tamil :"))
# call.displaySongs()
# call.Download()
