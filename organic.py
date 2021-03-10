import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
class organic:
    def __init__(self):
        def show():
            id1 = tk.Label(t2, text="org_id                   name                      price                  quantity")
            id1.place(x=5, y=10)
            cur.execute("SELECT * FROM organic_pesticides")
            i = 10
            for organic_pesticides in cur:
                j=0
                for j in range(len(organic_pesticides)):
                    e = Entry(t2, width=15, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, organic_pesticides[j])
                i = i + 1
        def choose():
            farmid = tk.Label(t2, text="farmer_id").place(x=50, y=180)
            f1 = tk.Entry(t2, width=35)
            f1.place(x=120, y=180, width=100)
            fid1 = tk.Label(t2, text="What you want to buy?", font=10).place(x=50, y=210, )
            fid2 = tk.Label(t2, text="Enter id of pesticides", ).place(x=50, y=250, )
            q = tk.Entry(t2, width=35, )
            q.place(x=170, y=250, width=100)
            fid2 = tk.Label(t2, text="quantity you need",).place(x=50, y=290, )
            q1 = tk.Entry(t2, width=35, )
            q1.place(x=170, y=290, width=100)
            def enter():
                org_id=q.get()
                farm_id=f1.get()
                if (org_id == "" or farm_id == ""):
                    messagebox.showinfo("show status", " both id is compulsory")
                else:
                    cur.execute("select * from organic_pesticides where org_id='"+org_id+"'")
                    res=cur.fetchall()
                    for i in res:
                        price=i[2]
                    t1=str(int(price)*int(q1.get()))
                    T = tk.Text(t2, height=8, width=25)
                    T.place(x=300,y=250)
                    quote=("total price='"+t1+"'\n please pay the amount")
                    T.insert(tk.END,quote)
                    cur.execute("update organic_pesticides set quantity=quantity-"+q1.get()+" where org_id='"+org_id+"'")
                    myconn.commit()
                    cur.execute("insert into purchased_by values('" + org_id + "','" + farm_id + "')")
                    myconn.commit()
                    q.delete(0, END)
                    q1.delete(0, END)
                    messagebox.askokcancel("Information", "please pay the amount")
            bybtn = tk.Button(t2, text="enter", bg="pink", command=enter)
            bybtn.grid(row=14, column=3)

        t2 = tk.Tk()
        t2.geometry("500x400")
        t2.title("organic pesticides")
        showbtn = tk.Button(t2, text="pesticides", bg='pink', command=show)
        showbtn.grid(row=10, column=5, pady=4)
        exittbtn = tk.Button(t2, text="EXIT", bg='blue', command=t2.destroy)
        exittbtn.grid(row=8, column=5, pady=4)
        bybtn=tk.Button(t2,text="Buy",bg="pink",command=choose)
        bybtn.grid(row=12,column=5)




myconn = mysql.connector.connect(host="localhost", user="Aishwarya", passwd="Ice1763", database="miniproject")
print(myconn)
cur = myconn.cursor()
