from tkinter import *  
from test import Masstamilan
from playsound import playsound  
from PIL import Image, ImageTk 



class GUI:  
   def __init__(self):
      self.mass = Masstamilan()
      
      self.root = Tk()
      self.name_var=StringVar()
      self.buttons = []
      self.root.geometry("500x100")       


      Label(self.root,text = "Album",).place(x = 90,y = 50) 
      Entry(self.root, width=35,textvariable=self.name_var).place(x = 150,y = 50)       
      Button(self.root,text = "search",command=lambda: self.searchBox()).place(x = 350,y = 47)
      # Button(self.root,text = "Stop",command=lambda :self.mass.online(False) ).place(x = 350,y = 150)

   def searchBox(self):
      self.root.geometry("650x650")   
      # print(self.name_var.get())
      self.mass.search(self.name_var.get())
      # self.mass.search("master")
      for ranner in range(len(self.buttons)):
         self.buttons[ranner].destroy()
      
      self.displayImage()
      self.buttons.clear()
      self.buttonlist(self.mass.datas)


      self.Info(self.mass.albumInfo())
      self.name_var.initialize("")

   def buttonlist(self,songs):
      yl = 100
      i = 0
      for x in songs:
         self.buttons.append(Button(self.root,text =x['name'],command =lambda x=x: self.Playsong(x)))
         self.buttons[i].place(x = 10,y = yl)
         i +=1
         yl += 40

   def displayImage(self):
      # Use library PIL to display png picture
      global img
      path = 'temp.jpg'
      img = ImageTk.PhotoImage(Image.open(path), Image.ANTIALIAS)
      panel = Label(self.root, image = img)
      panel.place(x = 350,y = 150)

      

   def Playsong(self,songName):    
      # Button(self.root,text = "Stop",command=lambda :self.mass.online(False) ).place(x = 210+40,y = 350)
      self.lab = Label(self.root,text =songName['name']+"\t\t").place(x = 300,y = 350)
      self.mass.playOnline(songName['link'])




   def Info(self,info):
      test = Label(self.root)   
      test.destroy()
      test = Label(self.root,text =info).place(x = 250,y = 250,width=400)    


   def mainloop(self):
      self.root.mainloop()

obj = GUI()
obj.mainloop()





# # obj.searchBox()
# songs = ["Kutti Story","Vaathi Coming","Vaathi Raid","?asdkfugt"]        
# # obj.buttonlist(songs)
# info="""Starring: Vijay, Keerthy Suresh, Varalakshmi SarathKumar
# Director: AR Murugadoss
# Music: A R Rahman
# Mp3 Quality: 128 Kbps/ 320 Kbps
# Year: 2018
# """
# # obj.Info(info)


        
    