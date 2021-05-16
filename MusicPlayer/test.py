from tkinter import *  

class GUI:
    def __init__(self):
        self.root = Tk()
        


    def searchBox(self):
        Label(self.root,text = "Album",).place(x = 90,y = 50) 
        self.inner = Entry(self.root, width=35).place(x = 150,y = 50)      
        Button(self.root,text = "search").place(x = 350,y = 47)



        Label(self.root,text =info).place(x = 100,y = 555)  




    def buttonlist(self):
        songs = ["Kutti Story","Vaathi Coming","Vaathi Raid"]        
        yl = 100
        for x in songs:
            Button(self.root,text =x,command =lambda x=x: self.Stop(x)).place(x = 10,y = yl)
            yl += 40

    def Stop(self,name):    
        Button(self.root,text = "Stop").place(x = 50,y = 550)
        Label(self.root,text =name).place(x = 100,y = 555)  

    def Info(self,info):
        Label(self.root,text =info).place(x = 100,y = 555)  

    def mainloop(self):
        self.root.geometry("550x650")       
        self.root.mainloop()


obj = GUI()
obj.searchBox()
obj.buttonlist()
obj.mainloop()
        
    