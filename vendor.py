from tkinter import *
from tkinter import ttk
from turtle import clear, title
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
import mysql.connector




class Supplier:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Supplier Interface")

        #=========================Variables=====================================
        self.v_code=StringVar()
        z=random.randint(2000,2999)
        self.v_code.set(str(z))

        self.v_name=StringVar()
        self.v_TRN=StringVar()
        self.v_TLN=StringVar()
        self.v_adress1=StringVar()
        self.v_adress2=StringVar()
        self.v_contact=StringVar()
        self.v_email=StringVar()







        #Image1
        img=Image.open("image/supp1.png")
        img=img.resize((500,300),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=550,height=150)  

        #Image2   
        img_1=Image.open("image/supp2.png")
        img_1=img_1.resize((500,300),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img1=Label(self.root,image=self.photoimg_1)
        lbl_img1.place(x=500,y=0,width=550,height=150)


        #Image3
        img_2=Image.open("image/supp4.png")
        img_2=img_2.resize((500,300),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img2=Label(self.root,image=self.photoimg_2)
        lbl_img2.place(x=1000,y=0,width=550,height=150)

        lbl_title=Label(self.root,text=" Supplier ",font=("times new roman",27,"bold"),bg="#33bbf9",fg="black",relief=RAISED)
        lbl_title.place(x=0,y=130,width=1530,height=45)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title,font=("times new roman",16,"bold"),background= "#33bbf9",foreground= "black")
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        #==============Main Frame====================
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)



        #=============Vendor Frame=============================
        Vendor_Frame=LabelFrame(Main_Frame,text="Vendor Details",font=("times new roman",12,"bold"),bg="white",fg="blue")
        Vendor_Frame.place(x=10,y=5,width=350,height=423)


        self.lbl_vendor_code=Label(Vendor_Frame,text="Vendor Code",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_vendor_code.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_vendor_code=ttk.Entry(Vendor_Frame,textvariable=self.v_code,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.entry_vendor_code.grid(row=0,column=1)

        self.lbl_vendor_name=Label(Vendor_Frame,text="Vendor Name",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_vendor_name.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_vendor_name=ttk.Entry(Vendor_Frame,textvariable=self.v_name,font=("times new roman",12,"bold"),width=24)
        self.entry_vendor_name.grid(row=1,column=1)

        self.lbl_vendor_TRN=Label(Vendor_Frame,text="T.R.N No.",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_vendor_TRN.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_vendor_TRN=ttk.Entry(Vendor_Frame,textvariable=self.v_TRN,font=("times new roman",12,"bold"),width=24)
        self.entry_vendor_TRN.grid(row=2,column=1)

        self.lbl_vendor_TLN=Label(Vendor_Frame,text="Trade Liscense No.",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_vendor_TLN.grid(row=3,column=0,sticky=W,padx=5,pady=2)

        self.entry_vendor_TLN=ttk.Entry(Vendor_Frame,textvariable=self.v_TLN,font=("times new roman",12,"bold"),width=24)
        self.entry_vendor_TLN.grid(row=3,column=1)

        self.lbl_vendor_adress1=Label(Vendor_Frame,text="Adress 1",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_vendor_adress1.grid(row=4,column=0,sticky=W,padx=5,pady=2)

        self.entry_vendor_adress1=ttk.Entry(Vendor_Frame,textvariable=self.v_adress1,font=("times new roman",12,"bold"),width=24)
        self.entry_vendor_adress1.grid(row=4,column=1)

        self.lbl_vendor_adress2=Label(Vendor_Frame,text="Adress 2",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_vendor_adress2.grid(row=5,column=0,sticky=W,padx=5,pady=2)

        self.entry_vendor_adress2=ttk.Entry(Vendor_Frame,textvariable=self.v_adress2,font=("times new roman",12,"bold"),width=24)
        self.entry_vendor_adress2.grid(row=5,column=1)
        self.lbl_vendor_mob=Label(Vendor_Frame,text="Contact",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_vendor_mob.grid(row=6,column=0,sticky=W,padx=5,pady=2)

        self.entry_vendor_mob=ttk.Entry(Vendor_Frame,textvariable=self.v_contact,font=("times new roman",12,"bold"),width=24)
        self.entry_vendor_mob.grid(row=6,column=1)

        self.lbl_vendor_email=Label(Vendor_Frame,text="Email",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_vendor_email.grid(row=7,column=0,sticky=W,padx=5,pady=2)

        self.entry_vendor_email=ttk.Entry(Vendor_Frame,textvariable=self.v_email,font=("times new roman",12,"bold"),width=24)
        self.entry_vendor_email.grid(row=7,column=1)

        #=================Buttons=====================
        btnAddData=Button(Main_Frame,text="Add Vendor",command=self.add_data,font=("times new roman",15,"bold"),bg="blue",fg="white",width=13,height=1)
        btnAddData.place(x=15,y=270)

        btnAddData2=Button(Main_Frame,text="Update Vendor",command=self.update_data,font=("times new roman",15,"bold"),bg="blue",fg="white",width=13,height=1)
        btnAddData2.place(x=15,y=320)

        btnAddData3=Button(Main_Frame,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="blue",fg="white",width=13,height=1)
        btnAddData3.place(x=15,y=370)
        
        btnAddData4=Button(Main_Frame,text="Delete",command=self.delete,font=("times new roman",15,"bold"),bg="firebrick2",fg="white",width=10,height=6)
        btnAddData4.place(x=200,y=270)
        #========================================Display Frame=================================================
        FrameDetails=Frame(Main_Frame,bd=4,relief=RIDGE)
        FrameDetails.place(x=370,y=190,width=620,height=250)

        #=================================Vendor Display Frame Details=====================================================
        Table_frame=Frame(FrameDetails,bd=4,relief=RIDGE)
        Table_frame.place(x=0,y=1,width=620,height=250)

        sc_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.vendor_table=ttk.Treeview(Table_frame,column=("vendor_code","vendor_name","TRN","TLN","adress1","adress2","contact","email"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y.pack(side=RIGHT,fill=Y)

        sc_x.config(command=self.vendor_table.xview)
        sc_y.config(command=self.vendor_table.yview)

        self.vendor_table["show"]="headings"

        self.vendor_table.heading("vendor_code",text="vendor_code")  
        self.vendor_table.heading("vendor_name",text="vendor_name")
        self.vendor_table.heading("TRN",text="TRN")
        self.vendor_table.heading("TLN",text="TLN")
        self.vendor_table.heading("adress1",text="adress1")
        self.vendor_table.heading("adress2",text="adress2")
        self.vendor_table.heading("contact",text="contact")
        self.vendor_table.heading("email",text="email")
        self.vendor_table.pack(fill=BOTH,expand=1)

        self.vendor_table.column("vendor_code",width=100)
        self.vendor_table.column("vendor_name",width=100)
        self.vendor_table.column("TRN",width=100)
        self.vendor_table.column("TLN",width=100)
        self.vendor_table.column("adress1",width=100)
        self.vendor_table.column("adress2",width=100)
        self.vendor_table.column("contact",width=100)
        self.vendor_table.column("email",width=100)

        self.vendor_table.pack(fill=BOTH,expand=1)
        self.vendor_table.bind("<ButtonRelease-1>",self.Vendorget_cursor)
        self.fetch_dataVendor()


        #=======================================Database Funtions=================================================
    def add_data(self):
           if self.v_name.get()=="" or self.v_TRN.get()=="" or self.v_TLN.get()=="" :
            messagebox.showerror("Error","Please Fill All Vendor Fields",parent=self.root)
           else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into vendor values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.v_code.get(),
                                                                                            self.v_name.get(),
                                                                                            self.v_TRN.get(),
                                                                                            self.v_TLN.get(),
                                                                                            self.v_adress1.get(),
                                                                                            self.v_adress2.get(),
                                                                                            self.v_contact.get(),
                                                                                            self.v_email.get()
                                                                                ))
                    conn.commit()
                    self.fetch_dataVendor()
                    conn.close()
                    messagebox.showinfo("Success","Vendor Added Succesfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)
    #===============================Displaying Database Customer Details From Database in Customer Frame=============================
    def fetch_dataVendor(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from vendor ")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.vendor_table.delete(*self.vendor_table.get_children())
            for i in rows:
                self.vendor_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #==============================================Cursor for Customer Fame Details===============================================
    def Vendorget_cursor(self,event=""):
        cursor_row=self.vendor_table.focus()
        content=self.vendor_table.item(cursor_row)
        row=content["values"]

        self.v_code.set(row[0]),
        self.v_name.set(row[1]),
        self.v_TRN.set(row[2]),
        self.v_TLN.set(row[3]),
        self.v_adress1.set(row[4]),
        self.v_adress2.set(row[5]),
        self.v_contact.set(row[6]),
        self.v_email.set(row[7])
    
    def update_data(self):
        if self.v_TRN.get()=="" or self.v_name.get()=="":
            messagebox.showerror("Error","Please enter vendor name and Tax Registration Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE vendor set vendor_name=%s,TLN=%s,adress1=%s,adress2=%s,contact=%s,email=%s WHERE TRN=%s",(
                                                                                                                                          
                                                                                                                                          self.v_name.get(),
                                                                                                                                          self.v_TLN.get(),
                                                                                                                                          self.v_adress1.get(),
                                                                                                                                          self.v_adress2.get(),
                                                                                                                                          self.v_contact.get(),
                                                                                                                                          self.v_email.get(),
                                                                                                                                          self.v_TRN.get(),
                                                                                                                                          
                                                                                                                                          ))     
            conn.commit()        
            self.fetch_dataVendor()
            conn.close()
            messagebox.showinfo("Update","Recoed has been updated successfully",parent=self.root)
    
    def delete(self):
        delete=messagebox.askyesno("Vendor Management","Do you want to delete this vendor ?")
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            query="delete from vendor where vendor_code=%s"
            value=(self.v_code.get(),)
            my_cursor.execute(query,value)
            messagebox.showinfo("Delete","Vendor deleted succesfully")
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_dataVendor()
        conn.close()    
    
    def clear(self):
        #self.v_code.set("")
        self.v_name.set(""),
        self.v_TRN.set(""),
        self.v_TLN.set(""),
        self.v_adress1.set(""),
        self.v_adress2.set(""),
        self.v_contact.set(""),
        self.v_email.set("")
        z=random.randint(2000,2999)
        self.v_code.set(str(z))
        




    
    
    






























if __name__=='__main__':
    root=Tk()
    obj=Supplier(root)
    root.mainloop()
