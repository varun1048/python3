from tkinter import *  

class GUI:
   def __init__(self):
      self.root = Tk()


   def searchBox(self):
      Label(self.root,text = "Album",).place(x = 90,y = 50) 
      self.inner = Entry(self.root, width=35).place(x = 150,y = 50)      
      Button(self.root,text = "search").place(x = 350,y = 47)
      return self.inner



   def buttonlist(self,songs):
      yl = 100
      for x in songs:
         Button(self.root,text =x,command =lambda x=x: self.Stop(x)).place(x = 10,y = yl)
         yl += 40

   def Stop(self,songName):    
      Button(self.root,text = "Stop").place(x = 210+40,y = 350)
      Label(self.root,text =songName+"\t\t").place(x = 300,y = 350)


   def Info(self,info):
      Label(self.root,text =info).place(x = 100,y = 555)    


   def mainloop(self):
      self.root.geometry("550x650")       
      self.root.mainloop()


obj = GUI()
print(obj.searchBox())
songs = ["Kutti Story","Vaathi Coming","Vaathi Raid"]        
obj.buttonlist(songs)
info="""Starring: Vijay, Keerthy Suresh, Varalakshmi SarathKumar
Director: AR Murugadoss
Music: A R Rahman
Mp3 Quality: 128 Kbps/ 320 Kbps
Year: 2018
"""
obj.Info(info)









obj.mainloop()


        
    