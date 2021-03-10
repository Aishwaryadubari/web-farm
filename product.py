import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox


class product:
    def __init__(self):

        def insert():

            farmid=tk.Label(t1,text="farmer_id").place(x=20,y=180)
            f1=tk.Entry(t1,width=35)
            f1.place(x=120,y=180,width=100)
            pid1 = tk.Label(t1, text="Product id")
            pid1.place(x=20, y=210)
            pid = tk.Entry(t1, width=35, )
            pid.place(x=120, y=210, width=100)
            pid1 = tk.Label(t1, text="Product name")
            pid1.place(x=20, y=240)
            pname1 = tk.Entry(t1, width=35, )
            pname1.place(x=120, y=240, width=100)
            pid1 = tk.Label(t1, text="price")
            pid1.place(x=20, y=270)
            price1 = tk.Entry(t1, width=35, )
            price1.place(x=120, y=270, width=100)
            pid1 = tk.Label(t1, text="quantity")
            pid1.place(x=20, y=300)
            q = tk.Entry(t1, width=35, )
            q.place(x=120, y=300, width=100)

            def submit():
                insert = "insert into products(prod_id,pname,price,quantity) values(%s,%s,%s,%s)"
                prod_id = pid.get()
                pname = pname1.get()
                price = price1.get()
                quantity = q.get()
                farm_id=f1.get()
                if (prod_id=="" or farm_id == "" or pname == "" or price == "" or quantity == ""):
                    messagebox.showinfo("insert status", "all fields required")
                else:
                    value = (prod_id, pname, price, quantity)
                    cur.execute(insert, value)
                    myconn.commit()
                    cur.execute("insert into sell values('"+farm_id+"','"+prod_id+"')")
                    myconn.commit()
                    messagebox.askokcancel("Information", "Record inserted")
                    pid.delete(0, END)
                    pname1.delete(0, END)
                    price1.delete(0, END)
                    q.delete(0, END)
                    f1.delete(0,END)
            addbtn = tk.Button(t1, text="add", bg="green",command=submit).grid(row=10, column=4)


        def product():
            id1 = tk.Label(t1, text="Product id       name       price       quantity").place(x=5,y=5)
            cur.execute("SELECT * FROM products")
            i = 5
            for products in cur:
                j=0
                for j in range(len(products)):

                    e = Entry(t1, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, products[j])
                i = i + 1



        t1 = tk.Tk()
        t1.geometry("500x400")
        t1.title("products")
        t1.configure(bg="white")
        showbtn = tk.Button(t1, text="PRODUCT", bg='pink', command=product)
        showbtn.grid(row=4, column=5, pady=4)
        addtbtn = tk.Button(t1, text="insert", bg="blue", command=insert)
        addtbtn.grid(row=10, column=5)
        exittbtn = tk.Button(t1, text="EXIT", bg='pink', command=t1.destroy)
        exittbtn.grid(row=8, column=5, pady=4)
        t1.mainloop()

myconn = mysql.connector.connect(host="localhost", user="Aishwarya", passwd="Ice1763", database="miniproject")
print(myconn)
cur = myconn.cursor()
