import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
class customer:
    def __init__(self):
        def create():
            t5 = Toplevel(t4)
            t5.geometry("500x400")
            t5.title("customer")
            pid1 = tk.Label(t5, text="customer id").place(x=20, y=130)
            pid3 = tk.Entry(t5, width=35, )
            pid3.place(x=120, y=130, width=100)
            pid1 = tk.Label(t5, text="customer name ").place(x=20, y=160)
            pname1 = tk.Entry(t5, width=35, )
            pname1.place(x=120, y=160, width=100)
            pid1 = tk.Label(t5, text="phon no").place(x=20, y=190)
            pid2 = tk.Entry(t5, width=35, )
            pid2.place(x=120, y=190, width=100)
            pid1 = tk.Label(t5, text="address").place(x=20, y=220)
            des = tk.Entry(t5, width=35, )
            des.place(x=120, y=220, width=100)
            pid1 = tk.Label(t5, text="payment type").place(x=20, y=250)
            pay1 = tk.Entry(t5, width=35, )
            pay1.place(x=120, y=250, width=100)
            def show():
                cust_id2=pid3.get()
                if (cust_id2 == ""):
                    messagebox.showinfo("show status", "id is compulsory")
                else:
                    id1 = tk.Label(t5, text="customer id      name     ph_no     type_of payment   address")
                    id1.place(x=2, y=2)
                    cur.execute("SELECT * FROM customer where cust_id='"+cust_id2+"'")
                    i = 6
                    for customer in cur:
                        j=0
                        for j in range(len(customer)):
                            e = Entry(t5, width=10, fg='blue')
                            e.grid(row=i, column=j)
                            e.insert(END, customer[j])
                        i = i + 1

            def update():
                cust_id1=pid3.get()
                phno=pid2.get()
                payment=pay1.get()
                address=des.get()
                if (cust_id1 == "" or phno == "" or payment == "" or address == ""):
                    messagebox.showinfo("update status", "all fields required(id,phno,payment,address)")
                else:
                    update="update customer set payment_type='%s',mobno='%s',address='%s'where cust_id='%s'"%(payment,phno,address,cust_id1)
                    cur.execute(update)
                    myconn.commit()
                    pid3.delete(0, END)
                    pid2.delete(0, END)
                    pay1.delete(0,END)
                    des.delete(0,END)
                    messagebox.showinfo("info","succesfully updated")
            def submit():
                insert = "insert into customer(cust_id,cname,mobno,payment_type,address) values(%s,%s,%s,%s,%s)"
                cust_id= pid3.get()
                cname = pname1.get()
                mobno = pid2.get()
                address = des.get()
                payment_type=pay1.get()
                if (cust_id == "" or cname == "" or mobno == "" or address == "" or payment_type == ""):
                    messagebox.showinfo("insert status", "all fields required")
                else:
                    value = (cust_id, cname, mobno,payment_type,address)
                    cur.execute(insert, value)
                    myconn.commit()
                    messagebox.askokcancel("Information", "Record inserted")
                    pid3.delete(0, END)
                    pname1.delete(0, END)
                    pid2.delete(0, END)
                    des.delete(0, END)
                    pay1.delete(0,END)

            addbtn = tk.Button(t5, text="add", command=submit).grid(row=10, column=10)
            addbtn = tk.Button(t5, text="update ph_no payment address", command=update).grid(row=5, column=10)
            addbtn = tk.Button(t5, text="enter id to check", command=show).grid(row=7, column=10)

            showbtn = tk.Button(t5, text="exit", bg='blue', command=t5.destroy)
            showbtn.grid(row=20, column=5)

        def new1():
            fid1 = tk.Label(t4, text="create account and enter details", font=10).place(x=50, y=260, )
            createtbtn = tk.Button(t4, text="CREATE OR UPDATE", bg='pink', command=create).place(x=50, y=290)
        def products():
            id1 = tk.Label(t4, text="Product id       name       price       quantity").place(x=5, y=10)
            cur.execute("SELECT * FROM products")
            i = 5
            for products in cur:
                for j in range(len(products)):
                    e = Entry(t4, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, products[j])
                i = i + 1

        def choose():
            t6 = Toplevel(t4)
            t6.geometry("500x400")
            t6.title("customer")
            fid = tk.Label(t6, text="Enter your id", ).place(x=50, y=100, )
            q2 = tk.Entry(t6, width=35, )
            q2.place(x=170, y=100, width=100)
            fid1 = tk.Label(t6, text="What you want to buy?", font=10).place(x=50, y=150, )
            fid2 = tk.Label(t6, text="Enter id of products", ).place(x=50, y=200, )
            q = tk.Entry(t6, width=35, )
            q.place(x=170, y=200, width=100)
            fid2 = tk.Label(t6, text="quantity you need", ).place(x=50, y=250, )
            q1 = tk.Entry(t6, width=35, )
            q1.place(x=170, y=250, width=100)

            def enter():
                cust_id=q2.get()
                prod_id = q.get()
                if (cust_id == "" or prod_id == ""):
                    messagebox.showinfo("show status", " both id is compulsory")
                else:
                    cur.execute("select * from products where prod_id='"+prod_id+"'")
                    res = cur.fetchall()
                    for i in res:
                        price = i[2]
                    t1 = str(int(price) * int(q1.get()))
                    T = tk.Text(t6, height=5, width=25)
                    T.place(x=300, y=250)
                    quote = ("total price='" + t1 + "'\n please pay the amount")
                    T.insert(tk.END, quote)
                    cur.execute("update products set quantity=quantity-" + q1.get() + " where prod_id='" + prod_id + "'")
                    myconn.commit()
                    cur.execute("insert into purchase values('" + cust_id + "','" + prod_id + "')")
                    myconn.commit()
                    q.delete(0, END)
                    q1.delete(0, END)
                    messagebox.askokcancel("Information", "pleas pay the amount")
            bybtn = tk.Button(t6, text="enter", bg="pink", command=enter)
            bybtn.grid(row=14, column=3)



        t4 = tk.Tk()
        t4.geometry("500x400")
        t4.title("customer")
        d = Canvas(t4, bg="blue", height=250, width=300)
        showtbtn = tk.Button(t4, text=" AVAILABLE PRODUCTS", bg='pink', command=products)
        showtbtn.grid(row=4, column=8, )
        exittbtn = tk.Button(t4, text="EXIT", bg='blue', command=t4.destroy)
        exittbtn.grid(row=8, column=8,)
        bybtn = tk.Button(t4, text="Buy products", bg="pink", command=choose)
        bybtn.grid(row=12, column=8)
        v1 = IntVar()
        row2 = tk.Radiobutton(t4, text="CREATE OR UPDATE ACCOUNT", font=12, padx=50, variable=v1, value=2, command=new1)
        row2.place(x=100, y=230)
        t4.mainloop()
myconn = mysql.connector.connect(host="localhost", user="Aishwarya", passwd="Ice1763", database="miniproject")
print(myconn)
cur = myconn.cursor()
