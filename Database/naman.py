import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import simpledialog


conn = sqlite3.connect('Database.db')
c = conn.cursor()

def create_table(e1,e2,e3,e4,var):
    str1=e1.get()
    str2=e2.get()
    str3=e3.get()
    str4=e4.get()
    str5=var.get()
    #print(str2,str1,str5,str4,str3)
    c.execute('CREATE TABLE IF NOT EXISTS Database(str2 TEXT, str1 TEXT,str5 INT, str4 TEXT,str3 TEXT)')
    
    c.execute("INSERT INTO Database( str2, str1,str5,str4,str3) VALUES (?, ?, ?, ?, ?)",
                      (str2,str1,str5,str4,str3))
    conn.commit()
    
    
    
def display():
    c.execute('SELECT * FROM Database')
    for row in c.fetchall():
             print(row)
       
              
def enter():
    
    root.destroy()
    frame1=Tk()
    frame1.title("Enter details")
    frame1.geometry("1000x1000")
    frame1.wm_iconbitmap('winimgg.ico')
    
    l1=Label(frame1,text="Name:",width=10,height=2,font=('Courier',-20,'bold'),fg='black')
    l2=Label(frame1,text="Roll No.:",width=10,height=2,font=('Courier',-20,'bold'),fg='black')
    l3=Label(frame1,text="Gender:",width=10,height=2,font=('Courier',-20,'bold'),fg='black')
    l4=Label(frame1,text="D.O.B.:",width=10,height=2,font=('Courier',-20,'bold'),fg='black')
    l5=Label(frame1,text="Address:",width=10,height=2,font=('Courier',-20,'bold'),fg='black')
    l1.place(x=5,y=50)
    l2.place(x=5,y=100)
    l3.place(x=5,y=150)
    l4.place(x=5,y=200)
    l5.place(x=5,y=250)

    
    e1=Entry(frame1,width=30,fg='black',bg='white',font=('Arial',14))
    e2=Entry(frame1,width=20,fg='black',bg='white',font=('Arial',14))
    e3=Entry(frame1,width=20,fg='black',bg='white',font=('Arial',14))
    e4=Entry(frame1,width=20,fg='black',bg='white',font=('Arial',14))
    
    e1.place(x=120,y=60)
    e2.place(x=120,y=110)
    e3.place(x=120,y=210)
    e4.place(x=120,y=260)

    var=StringVar()
    r1=Radiobutton(frame1,text='Female',value='Female',variable=var,font=('Courier',-20),fg='black')
    r2=Radiobutton(frame1,text='Male',value='Male',variable=var,font=('Courier',-20),fg='black')
    r1.place(x=130,y=160)
    r2.place(x=250,y=160)
    
    b1 = tk.Button(frame1,text="Submit",command=lambda : create_table(e1,e2,e3,e4,var))
    b1.place(x=300,y=550)
    
    
def view():
    root.destroy()
    frame2=Tk()
    frame2.title("Details")
    frame2.geometry("1000x1000")
    frame2.wm_iconbitmap('winimgg.ico')
    c.execute('SELECT * FROM Database')
    x = c.fetchall()
    j=100
    i=1
    for row in x:
        lt=Label(frame2,text="Sno. Name  Rno. Gender Add    DOB",font=('Courier',-20,'bold'),fg='black')
        le=Label(frame2,text=i,font=('Courier',-20),fg='black')
        l = Label(frame2,text=row,font=('Courier',-20),fg='black')
        l.place(x=25,y=j)
        le.place(x=5,y=j)
        lt.place(x=2,y=25)
        j=j+50
        i=i+1
        print(row)

def search():
    rno = tk.simpledialog.askstring("ROLL NO","ENTER A ROLL NUMBER")
    roll_no = (rno,)
    c.execute('SELECT * FROM Database WHERE str2=?',roll_no)
    for row in c.fetchall():
        root.destroy()
        frame3=Tk()
        frame3.title("Searching")
        frame3.geometry("500x500")
        l1=Label(frame3,text=row,width=35,height=5,font=('Courier',-20,'bold'),fg='black')
        l1.place(x=5,y=50)

def delete():
    name=tk.simpledialog.askstring("NAME","ENTER NAME")
    nm=(name,)
    c.execute("DELETE FROM Database WHERE str1=?", nm)
    g=50
    for row in c.fetchall():
        
        frame4=Tk()
        frame4.title("Updated  records")
        frame4.geometry("500x500")
        l8=Label(frame4,text=row,width=35,height=5,font=('Courier',-20,'bold'),fg='black')
        l8.place(x=5,y=g)
        g=g+50
    conn.commit()
    
root=Tk()
root.title("Student Database Management System")
root.geometry("1000x1000")
root.wm_iconbitmap('winimgg.ico')
myImg = PhotoImage(file= "windowwwwww.png") 

btn= Button(root, image=myImg)
btn.place(x=440,y=50)   
root.wm_iconbitmap('winimgg.ico')
b2 = tk.Button(root, text="Enter details", command=enter)
b2.place(x=150,y=290)
b3= tk.Button(root,text="View details",command=view)
b3.place(x=350,y=290)
b4 = tk.Button(root,text="Search",command=search)
b4.place(x=550,y=290)
b5=tk.Button(root,text="Delete Record",command=delete)
b5.place(x=750,y=290)
root.mainloop()
