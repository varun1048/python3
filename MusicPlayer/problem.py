from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 



class done:
    def __init__(self):
        self.root = Tk()                

    def display(self):
        # Use library PIL to display png picture
        global img
        path = 'temp.jpg'
        img = ImageTk.PhotoImage(Image.open(path), Image.ANTIALIAS)
        panel = Label(self.root, image = img)
        panel.pack()

    def oner(self):
        ButtonDisplay = ttk.Button(self.root, text="Display", command=self.display)
        ButtonDisplay.pack()

    def looper(self):
        self.root.mainloop()

obj = done()
obj.oner()
obj.looper()







# from tkinter import *
# from PIL import ImageTk,Image

# global img 
# class cake:
#     def __init__(self):
#         global img 
        
#     def foo(self):    
#         img = ImageTk.PhotoImage(Image.open("master.jpg"))     

#     def fool(self):      
#         self.img = ImageTk.PhotoImage(Image.open("master.jpg"))     
#         self.canvas.create_image(20,20, anchor=NW, image=self.img)    
#         self.canvas.image = self.img   

#     def loop(self):
#         self.root.mainloop()

# ake = cake()
# ake.foo()
# ake.fool()
# ake.loop()