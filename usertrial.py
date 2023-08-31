from tkinter import *
from tkinter import ttk
from turtle import clear, title
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
import mysql.connector

class User:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("User Interface")
    
        #Image1
        img=Image.open("image/bill1.png")
        img=img.resize((500,300),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=550,height=150)  

        #Image2   
        img_1=Image.open("image/bill2.png")
        img_1=img_1.resize((500,300),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img1=Label(self.root,image=self.photoimg_1)
        lbl_img1.place(x=500,y=0,width=550,height=150)


        #Image3
        img_2=Image.open("image/bill3.png")
        img_2=img_2.resize((500,300),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img2=Label(self.root,image=self.photoimg_2)
        lbl_img2.place(x=1000,y=0,width=550,height=150)

        lbl_title=Label(self.root,text="User Management",font=("times new roman",27,"bold"),bg="#33bbf9",fg="black",relief=RAISED)
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title,font=("times new roman",16,"bold"),background= "#33bbf9",foreground= "black")
        lbl.place(x=0,y=0,width=120,height=45)
        time()


        Main_Frame=Frame(self.root,bd=5,relief=GROOVE)
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #===================================User Display======================================================
        Table_frame=Frame(Main_Frame,bd=4,relief=RIDGE)
        Table_frame.place(x=300,y=80,width=800,height=450)

        sc_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.user_table=ttk.Treeview(Table_frame,column=("fname","lname","contact","email","securityQ","securityA","password"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y.pack(side=RIGHT,fill=Y)

        sc_x.config(command=self.user_table.xview)
        sc_y.config(command=self.user_table.yview)

        self.user_table["show"]="headings"

        self.user_table.heading("fname",text="fname")  
        self.user_table.heading("lname",text="lname")
        self.user_table.heading("contact",text="contact")
        self.user_table.heading("email",text="email")
        self.user_table.heading("securityQ",text="securityQ")
        self.user_table.heading("securityA",text="securityA")
        self.user_table.heading("password",text="password")
        self.user_table.pack(fill=BOTH,expand=1)

        self.user_table.column("fname",width=100)
        self.user_table.column("lname",width=100)
        self.user_table.column("contact",width=100)
        self.user_table.column("email",width=100)
        self.user_table.column("securityQ",width=100)
        self.user_table.column("securityA",width=100)
        self.user_table.column("password",width=100)
        self.user_table.pack(fill=BOTH,expand=1)
        self.fetch_dataUser()

    
    
    
    
    #========================Fecth Data================================================
    def fetch_dataUser(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from user_register ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.user_table.delete(*self.user_table.get_children())
            for i in rows:
                self.user_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        











if __name__=='__main__':
    root=Tk()
    obj=User(root)
    root.mainloop()

