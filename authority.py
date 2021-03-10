import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
class authority:
    def __init__(self):

        def show():
            id1 = tk.Label(temp, text="facility id         facility name                 status             volunteer id")
            id1.place(x=5, y=10)
            cur.execute("SELECT * FROM facilities")
            i = 10
            for facilities in cur:
                for j in range(len(facilities)):
                    e = Entry(temp, width=15, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, facilities[j])
                i = i + 1

        def create():
            t3=Toplevel(temp)
            t3.geometry("500x400")
            pid1 = tk.Label(t3, text="author id").place(x=20, y=130)
            pid3 = tk.Entry(t3, width=35, )
            pid3.place(x=120, y=130, width=100)
            pid1 = tk.Label(t3, text="author name ").place(x=20, y=160)
            pname1 = tk.Entry(t3, width=35, )
            pname1.place(x=120, y=160, width=100)
            pid1 = tk.Label(t3, text="phone no").place(x=20, y=190)
            pid2 = tk.Entry(t3, width=35, )
            pid2.place(x=120, y=190, width=100)
            pid1 = tk.Label(t3, text="design").place(x=20, y=220)
            des = tk.Entry(t3, width=35, )
            des.place(x=120, y=220, width=100)
            pid1 = tk.Label(t3, text="status of project").place(x=20, y=250)
            des1 = tk.Entry(t3, width=35, )
            des1.place(x=120, y=250, width=100)
            pid1 = tk.Label(t3, text="volunteer id").place(x=20, y=280)
            des2 = tk.Entry(t3, width=35, )
            des2.place(x=120, y=280, width=100)

            def show():
                auth_id2=pid3.get()
                if (auth_id2 == ""):
                    messagebox.showinfo("show status", "id is compulsory")
                else:
                    id1 = tk.Label(t3, text="author id      authority_name    design     ph_no     status_project  volunter_id")
                    id1.place(x=0, y=2)
                    cur.execute("SELECT * FROM authorities where auth_id='"+auth_id2+"'")
                    i = 5
                    for authorities in cur:
                        j = 0
                        for j in range(len(authorities)):
                            e = Entry(t3, width=10, fg='blue')
                            e.grid(row=i, column=j)
                            e.insert(END, authorities[j])
                        i = i + 1
            def update():
                auth_id1=pid3.get()
                pstatus=des1.get()
                if (auth_id1 == "" or pstatus == "" ):
                    messagebox.showinfo("update status", "fields required(id,status)")
                else:
                    cur.execute("update authorities set p_status='"+pstatus+"'where auth_id='"+auth_id1+"'")
                    myconn.commit()
                    pid3.delete(0, END)
                    des1.delete(0, END)
                    messagebox.askokcancel("Information", "updated successfully")
            def submit():
                insert = "insert into authorities(auth_id,aname,design,phno,p_status,vol_id) values(%s,%s,%s,%s,%s,%s)"
                auth_id = pid3.get()
                aname = pname1.get()
                phno = pid2.get()
                design = des.get()
                p_status=des1.get()
                vol_id=des2.get()
                if (auth_id == "" or aname == "" or phno == "" or design == "" or p_status == ""):
                    messagebox.showinfo("insert status", "all fields required")
                else:
                    value = (auth_id, aname,design, phno,p_status,vol_id)
                    cur.execute(insert, value)
                    myconn.commit()
                    messagebox.askokcancel("Information", "Record inserted")
                    pid3.delete(0, END)
                    pname1.delete(0, END)
                    pid2.delete(0, END)
                    des.delete(0, END)
                    des1.delete(0,END)
                    des2.delete(0,END)
            addbtn = tk.Button(t3, text="add", bg='pink',command=submit).grid(row=3, column=10)
            addbtn = tk.Button(t3, text="update project status", command=update).grid(row=5, column=10)
            addbtn = tk.Button(t3, text="show authorities", command=show).grid(row=7, column=10)

        def new1():
            fid1 = tk.Label(temp, text="create account and enter details", font=10).place(x=50, y=200, )
            createtbtn = tk.Button(temp, text="CREATE or UPDATE", bg='pink', command=create).place(x=50, y=250)



        temp = tk.Tk()
        temp.geometry("600x400")
        temp.title("authorities")
        temp.configure(bg="orange")
        v1=tk.IntVar
        d = Canvas(temp, bg="blue", height=250, width=300)
        showbtn = tk.Button(temp, text="show facilities", bg='blue', command=show)
        showbtn.grid(row=10, column=5, pady=4)
        exitbtn = tk.Button(temp, text="QUIT", bg='blue', command=temp.destroy)
        exitbtn.grid(row=4, column=5, pady=4)
        row2 = tk.Radiobutton(temp, text="CREATE OR UPDATE ACCOUNT", font=10, padx=50, variable=v1, value=2, command=new1)
        row2.place(x=80, y=150)

myconn = mysql.connector.connect(host="localhost", user="Aishwarya", passwd="Ice1763", database="miniproject")
print(myconn)
cur = myconn.cursor()