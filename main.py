import tkinter as tk
from tkinter import *
from farm import farm
from worker import worker
from customer import customer
from authority import authority
import cs


root = tk.Tk()
root.geometry("800x400")
root.title("WELCOME")
root.configure(bg="pink")
C = Canvas(root, bg="pink", height=250, width=300)
trow = tk.Label(root,bg
="blue",text="WELCOME TO WEB FORM SERVICES",font=20)
trow.place(x=50, y=20,height=50,width=600)
trow1 = tk.Label(root,bg="pink",text="Who are you?",font=14)
trow1.place(x=50, y=90,width=600)
v = tk.IntVar()

tk.Radiobutton(root,text="FARMER",padx = 50,variable=v,value=1,command=farm).pack(side=tk.LEFT)
tk.Radiobutton(root,text="CUSTOMER",padx = 50,variable=v,value=2,command=customer).pack(side=tk.LEFT)
tk.Radiobutton(root,text="HIGHER AUTHORITY",padx = 50,variable=v,value=3,command=authority).pack(side=tk.LEFT)
tk.Radiobutton(root,text="WORKER",padx = 50,variable=v,value=4,command=worker).pack(side=tk.LEFT)
exittbtn = tk.Button(root, text="WEATHER",font=10, bg='blue', command=cs.main).place(x=400, y=300)

exittbtn = tk.Button(root, text="EXIT",font=12, bg='blue', command=root.destroy).place(x=200, y=300)
root.mainloop()











