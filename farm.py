import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
from product import product
from organic import organic

class farm:
    def __init__(self):
       def old():
            showbtn = tk.Button(temp, text=" SELL PRODUCTS", bg='pink', command=product)
            showbtn.grid(row=3, column=3)
            showbtn = tk.Button(temp, text="BUY ORGANICS", bg='pink', command=organic)
            showbtn.grid(row=5, column=3)
            hirebtn = tk.Button(temp, text="HIRE WORKER", bg='pink', command=works)
            hirebtn.grid(row=4, column=3)
            hirebtn = tk.Button(temp, text="CHECK FACILITIES", bg='pink', command=facility)
            hirebtn.grid(row=6, column=3)
       def create():
           t5=Toplevel(temp)
           t5.geometry("500x400")
           pid1 = tk.Label(t5, text="farmer id").place(x=20, y=130)
           pid3 = tk.Entry(t5, width=35, )
           pid3.place(x=120, y=130, width=100)
           pid1 = tk.Label(t5, text="farmer name ").place(x=20, y=160)
           pname1 = tk.Entry(t5, width=35, )
           pname1.place(x=120, y=160, width=100)
           pid1 = tk.Label(t5, text="phon no").place(x=20, y=190)
           pid2 = tk.Entry(t5, width=35, )
           pid2.place(x=120, y=190, width=100)
           pid1 = tk.Label(t5, text="design").place(x=20, y=220)
           des = tk.Entry(t5, width=35, )
           des.place(x=120, y=220, width=100)

           def submit():
               insert = "insert into farmer(farm_id,name,ph_no,design) values(%s,%s,%s,%s)"
               farm_id = pid3.get()
               name = pname1.get()
               ph_no = pid2.get()
               design= des.get()
               if (farm_id == "" or name == "" or ph_no == "" or design == ""):
                   messagebox.showinfo("insert status", "all fields required")
               else:
                    value = (farm_id, name, ph_no,design)
                    cur.execute(insert, value)
                    myconn.commit()
                    messagebox.askokcancel("Information", "Record inserted")
                    pid3.delete(0, END)
                    pname1.delete(0, END)
                    pid2.delete(0, END)
                    des.delete(0,END)
           addbtn = tk.Button(t5, text="add", command=submit).grid(row=10, column=4)


       def new1():
           fid1 = tk.Label(temp, text="create account and enter details",font=10).place(x=50, y=190,)
           createtbtn = tk.Button(temp, text="CREATE", bg='pink', command=create).place(x=50, y=230)
       def facility():
           t9 = Toplevel(temp)
           t9.geometry("500x400")
           def show():
               id1 = tk.Label(t9,text="facility id         facility name                 status             volunteer id")
               id1.place(x=5, y=5)
               cur.execute("SELECT * FROM facilities")
               i = 15
               for facilities in cur:
                   for j in range(len(facilities)):
                       e = Entry(t9, width=15, fg='blue')
                       e.grid(row=i, column=j)
                       e.insert(END, facilities[j])
                   i = i + 1

           showbtn = tk.Button(t9, text="show facilities", bg='blue', command=show)
           showbtn.grid(row=10, column=5, pady=4)
           pid1 = tk.Label(t9, text="ARE YOU VOLUNTEER").place(x=20, y=180)
           pid1 = tk.Label(t9, text="volunteer id").place(x=20, y=210)
           pid3 = tk.Entry(t9, width=35, )
           pid3.place(x=120, y=210, width=100)
           pid1 = tk.Label(t9, text="status of project").place(x=20, y=250)
           des1 = tk.Entry(t9, width=35, )
           des1.place(x=120, y=250, width=100)

           def update():
               fid = pid3.get()
               pstatus = des1.get()
               if (fid == "" or pstatus==""):
                   messagebox.showinfo("show status", "id  and status is compulsory")
               else:
                   cur.execute("update facilities set status='" + pstatus + "'where vol_id='" + fid + "'")
                   myconn.commit()
                   pid3.delete(0, END)
                   des1.delete(0, END)
           addbtn = tk.Button(t9, text="update project status", command=update).grid(row=5, column=5)


       def works():
           t7 = tk.Tk()
           t7.geometry("500x400")
           t7.title("hiring")
           def workers1():
               id1 = tk.Label(t7, text="worker id        name           design      phone_no     volunteerId")
               id1.place(x=3, y=10)
               cur.execute("SELECT * FROM workers")
               i = 12
               for workers in cur:
                   j=0
                   for j in range(len(workers)):
                       e = tk.Entry(t7, width=10, fg='blue')
                       e.grid(row=i, column=j)
                       e.insert(END, workers[j])
                   i = i + 1
           def hire():
               pid1 = tk.Label(t7, text="farmer id").place(x=20, y=230)
               pid3 = tk.Entry(t7, width=35, )
               pid3.place(x=120, y=230, width=100)
               pid1 = tk.Label(t7, text="worker id ").place(x=20, y=260)
               pname1 = tk.Entry(t7, width=35, )
               pname1.place(x=120, y=260, width=100)
               def enter():
                   wid = pname1.get()
                   farm_id1 = str(pid3.get())
                   if (wid == "" or farm_id1==""):
                       messagebox.showinfo("show status", "id is compulsory")
                   else:
                        cur.execute("select * from workers where wid='" + wid + "'")
                        res = cur.fetchall()
                        update="update workers set farm_id='%s' where wid='%s'"%(farm_id1,wid)
                        cur.execute(update)
                        myconn.commit()
                        messagebox.askokcancel("Information", "updated successfully")
                        pid3.delete(0, END)
                        pname1.delete(0, END)
               bybtn = tk.Button(t7, text="enter", bg="pink", command=enter)
               bybtn.grid(row=25, column=7)
           showbtn = tk.Button(t7, text="WORKER", bg='pink', command=workers1)
           showbtn.grid(row=10, column=12, pady=4)
           trow = tk.Label(t7, bg="yellow", text="Want to hire worker enter id of worker and yours")
           trow.place(x=100, y=150, width=270, height=50)
           bybtn = tk.Button(t7, text="Hire worker", bg="pink", command=hire)
           bybtn.grid(row=12, column=12)
       temp = tk.Tk()
       temp.geometry("500x400")
       temp.title("farmer")
       C = Canvas(temp, bg="pink", height=250, width=300)
       v1 = tk.IntVar()
       trow = tk.Label(temp, bg="blue", text="WELCOME", font=20)
       trow.place(x=150, y=20,width=200,height=50)
       row1=tk.Radiobutton(temp, text="HAS ACCOUNT",font=10, padx=50, value=1,variable=v1, command=old)
       row1.place(x=100,y=100)
       row2=tk.Radiobutton(temp, text="NEW ACCOUNT",font=10, padx=50,value=2,variable=v1, command=new1)
       row2.place(x=100,y=150)
       exittbtn = tk.Button(temp, text="EXIT", bg='blue', command=temp.destroy).grid(row=2, column=3)
       temp.mainloop()


myconn = mysql.connector.connect(host="localhost", user="Aishwarya", passwd="Ice1763", database="miniproject")
print(myconn)
cur = myconn.cursor()




