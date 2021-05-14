from tkinter import *
root = Tk()
root.title("Gui")

inner = Entry(root,width=35, borderwidth=5)
inner.grid(row=0,column=0,columnspan=3,padx=1,pady=10)

Button(root,text="click",padx=10,command=
   lambda :Label(root,text=inner.get()).grid(row=1,column=1)
   ).grid(row=3,column=1)

root.mainloop()