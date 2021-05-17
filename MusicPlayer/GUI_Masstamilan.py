from tkinter import *  
from backend_Masstamilan import Masstamilan
from playsound import playsound  
from PIL import Image, ImageTk 

class GUI:  
   def __init__(self):
      self.mass = Masstamilan()
      
      self.root = Tk()
      self.name_var=StringVar()
      self.buttons = []
      self.root.geometry("500x100")       

      Label(self.root,text = "Mass Tamilan",fg="red", pady=10, padx=10, font=10).pack() 
      Label(self.root,text = "Album",).place(x = 90,y = 50) 
      Entry(self.root, width=35,textvariable=self.name_var).place(x = 150,y = 50)       
      Button(self.root,text = "search",command=lambda: self.searchBox()).place(x = 350,y = 47)



   def searchBox(self):
      self.root.geometry("650x550")   

      self.mass.search(self.name_var.get())
      for ranner in range(len(self.buttons)):
         self.buttons[ranner].destroy()
      
      self.wast_function()
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
      global img
      path = 'temp.jpg'
      img = ImageTk.PhotoImage(Image.open(path), Image.ANTIALIAS)
      panel = Label(self.root, image = img)
      panel.place(x = 350,y = 150)

      

   def Playsong(self,songName):    
      self.lab = Label(self.root,text =songName['name']+"\t\t").place(x = 300,y = 350)
      self.mass.playOnline(songName['link'])




   def Info(self,info):
      test = Label(self.root)   
      test.destroy()
      test = Label(self.root,text =info).place(x = 259,y = 330,width=400)    

   def wast_function(self,):
      noname = self.mass.album_name.split(" ")
      bank= []
      for flash in  noname:
         if flash == "Mp3":
               bank.pop()
               bank.pop()
               break
         bank.append(flash+" ") 
      out = "".join(bank)
      self.alNmae = Label(self.root,text = out+"\t\t\t\t\t").place(x = 350,y = 130) 

   def mainloop(self):
      self.root.mainloop()

obj = GUI()
obj.mainloop()




