import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
class worker:
    def __init__(self):

        def create():
            t5 = Toplevel(t3)
            t5.geometry("500x400")
            pid1 = tk.Label(t5, text="worker id").place(x=20, y=130)
            pid3 = tk.Entry(t5, width=35, )
            pid3.place(x=120, y=130, width=100)
            pid1 = tk.Label(t5, text="worker name ").place(x=20, y=160)
            pname1 = tk.Entry(t5, width=35, )
            pname1.place(x=120, y=160, width=100)
            pid1 = tk.Label(t5, text="phone no").place(x=20, y=190)
            pid2 = tk.Entry(t5, width=35, )
            pid2.place(x=120, y=190, width=100)
            pid1 = tk.Label(t5, text="design").place(x=20, y=220)
            des = tk.Entry(t5, width=35, )
            des.place(x=120, y=220, width=100)
            pid1 = tk.Label(t5, text="owner id if present").place(x=20, y=250)
            des1 = tk.Entry(t5, width=35, )
            des1.place(x=120, y=250, width=100)
            def show():
                wid1=pid3.get()
                if (wid1 == ""):
                    messagebox.showinfo("show status", "id is compulsory")
                else:
                    id1 = tk.Label(t5, text="worker id     worker_name    design     ph_no     owner_id if present")
                    id1.place(x=2, y=2)
                    cur.execute("SELECT * FROM workers where wid='"+wid1+"'")
                    i = 6
                    for workers in cur:
                        j = 0
                        for j in range(len(workers)):
                            e = Entry(t5, width=10, fg='blue')
                            e.grid(row=i, column=j)
                            e.insert(END, workers[j])
                        i = i + 1

            def update():
                wid2=pid3.get()
                phno=pid2.get()
                owner_id=des1.get()
                if (wid2 == "" or phno == "" or owner_id == ""):
                    messagebox.showinfo("update status", "all fields required(id,phno,owner_id")
                else:
                    update = "update workers set phno='%s',farm_id='%s'where wid='%s'" % (phno, owner_id, wid2)
                    cur.execute(update)
                    myconn.commit()
                    pid3.delete(0, END)
                    pid2.delete(0, END)
                    des1.delete(0,END)
                    messagebox.showinfo("info", "succesfully updated")
            def submit():
                insert = "insert into workers(wid,wname,design,phno,farm_id) values(%s,%s,%s,%s,%s)"
                wid = pid3.get()
                wname = pname1.get()
                phno = pid2.get()
                design = des.get()
                farm_id=des1.get()
                if (wid == "" or wname == "" or phno == "" or design == "" or farm_id == ""):
                    messagebox.showinfo("insert status", "all fields required")
                else:
                    value = (wid, wname,design, phno,farm_id)
                    cur.execute(insert, value)
                    myconn.commit()
                    messagebox.askokcancel("Information", "Record inserted")
                    pid3.delete(0, END)
                    pname1.delete(0, END)
                    pid2.delete(0, END)
                    des.delete(0, END)
                    des1.delete(0,END)
            addbtn = tk.Button(t5, text="add", command=submit).grid(row=10, column=4)
            addbtn = tk.Button(t5, text="update phno and owner id", command=update).grid(row=5, column=12)
            addbtn = tk.Button(t5, text="enter id to check", command=show).grid(row=7, column=10)

        def new1():
            fid1 = tk.Label(t3, text="create account and enter details", font=10).place(x=50, y=190, )
            createtbtn = tk.Button(t3, text="CREATE OR UPDATE", bg='pink', command=create).place(x=50, y=230)

        t3 = tk.Tk()
        t3.geometry("500x300")
        t3.title("worker")
        d = Canvas(t3, bg="blue", height=250, width=300)
        v1=IntVar()
        exitbtn = tk.Button(t3, text="QUIT", bg='blue', command=t3.destroy)
        exitbtn.grid(row=4, column=5, pady=4)
        row2 = tk.Radiobutton(t3, text="CREATE OR UPDATE ACCOUNT", font=12, padx=50, variable=v1, value=2, command=new1)
        row2.place(x=80, y=100)



myconn = mysql.connector.connect(host="localhost", user="Aishwarya", passwd="Ice1763", database="miniproject")
print(myconn)
cur = myconn.cursor()