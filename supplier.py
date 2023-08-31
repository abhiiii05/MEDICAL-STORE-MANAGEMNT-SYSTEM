from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql
import mysql.connector
import random
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x500+220+130")
        self.root.title("SUPPLIER MANAGEMENT SYSTEM | DEVELOPED BY -------- ")
        self.root.config(bg="white")
        self.root.focus_force()
        #=============================
        #All Vairiables=====
        
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_sup_code=StringVar()
        z=random.randint(1000,1999)
        self.var_sup_code.set(str(z))
        self.var_sup_TRN=StringVar()
        self.var_sup_TLN=StringVar()
        

    


                

        #====search====
        self.var_searchby=StringVar()
        cmb_search=ttk.Combobox(self.root,textvariable=self.var_searchby,values=("Select","NAME","SUPPLIERCODE"),font=("goudy old style",14),state="readonly")
        cmb_search.place(x=670,y=60,width=130)
        cmb_search.current(0)
        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=800,y=60,width=170)
        
        btn_search=Button(self.root,text="SEARCH",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=970,y=60,width=90,height=30)
        btn_showall=Button(self.root,text="SHOW ALL",command=self.show,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=1065,y=60,width=110,height=30)

        #====title====
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)


        #====content====
        #====row1====
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=80)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=150,y=80,width=180)

        lbl_vendor_code=Label(self.root,text="Vendor Code",font=("goudy old style",15),bg="white").place(x=50,y=120)
        entry_vendor_code=Entry(self.root,textvariable=self.var_sup_code,font=("goudy old style",15),bg="lightyellow",state="readonly").place(x=170,y=120,width=180)
        


        #===row2====
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)

        lbl_vendor_TRN=Label(self.root,text="T.R.N No.",font=("goudy old style",15),bg="white").place(x=50,y=150)
        entry_vendor_TRN=Entry(self.root,textvariable=self.var_sup_TRN,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)

        

        #===row3====
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)

        lbl_vendor_TLN=Label(self.root,text="T.L.N No.",font=("goudy old style",15),bg="white").place(x=340,y=80)
        entry_vendor_TLN=Entry(self.root,textvariable=self.var_sup_TLN,font=("goudy old style",15),bg="lightyellow").place(x=450,y=80,width=180)
        #===row4====
        lbl_adress=Label(self.root,text="Adress",font=("goudy old style",15),bg="white").place(x=50,y=270)
        self.txt_adress=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_adress.place(x=150,y=270,width=300,height=60)
        
        #====buttons====
        btn_add=Button(self.root,text="SAVE",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=150,y=350,width=110,height=28)
        btn_update=Button(self.root,text="UPDATE",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=270,y=350,width=110,height=28)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=390,y=350,width=110,height=28)
        btn_clear=Button(self.root,text="CLEAR",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=510,y=350,width=110,height=28)

        #====Employee Details====

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=700,y=100,width=400,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("SUPPLIERCODE","INVOICE","NAME","TRN","TLN","CONTACT","ADRESS"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("SUPPLIERCODE",text="SUPPLIERCODE")
        self.supplierTable.heading("INVOICE",text="INVOICE")
        self.supplierTable.heading("NAME",text="NAME")
        self.supplierTable.heading("TRN",text="TRN")
        self.supplierTable.heading("TLN",text="TLN")
        self.supplierTable.heading("CONTACT",text="CONTACT")
        self.supplierTable.heading("ADRESS",text="ADRESS")


        self.supplierTable["show"]="headings"
        
        self.supplierTable.column("SUPPLIERCODE",width=90)
        self.supplierTable.column("INVOICE",width=90)
        self.supplierTable.column("NAME",width=100)
        self.supplierTable.column("TRN",width=100)
        self.supplierTable.column("TLN",width=100)
        self.supplierTable.column("CONTACT",width=100)
        self.supplierTable.column("ADRESS",width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#============================================================================
    def add(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_sup_invoice.get=="":
                    messagebox.showerror("Error","Invoice must be required",parent=self.root)
            else:
                my_cursor.execute("Select * from supplier where INVOICE=%s",(self.var_sup_invoice.get(),))
                row=my_cursor.fetchone()
                if row!=None:
                        messagebox.showerror("Error","This INVOICE is already assigned, try a different id ",parent=self.root)
                else:
                        my_cursor.execute("Insert into supplier values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                self.var_sup_code.get(),                                                
                                                                                                self.var_sup_invoice.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_sup_TRN.get(),
                                                                                                self.var_sup_TLN.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.txt_adress.get('1.0',END),
                                                                                                                                                ))
                        conn.commit()
                        conn.close()                                                                                                                        
                        
                        messagebox.showinfo("SUCCESS","SUPPLIER ADDED SUCCESSFULLY",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    
    def show(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            my_cursor.execute("select * from supplier")
            rows=my_cursor.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row) 
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']

        self.var_sup_code.set(row[0])
        self.var_sup_invoice.set(row[1])
        self.var_name.set(row[2])
        self.var_sup_TRN.set(row[3])
        self.var_sup_TLN.set(row[4])
        self.var_contact.set(row[5])
        self.txt_adress.delete('1.0',END)
        self.txt_adress.insert(END,row[6])
        
        

    

    def update(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_sup_invoice.get=="":
                    messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                my_cursor.execute("Select * from supplier where INVOICE=%s",(self.var_sup_invoice.get(),))
                row=my_cursor.fetchone()
                if row==None:
                        messagebox.showerror("Error","Invalid Invoice no. ",parent=self.root)
                else:
                        my_cursor.execute("Update supplier set NAME=%s,TLN=%s,CONTACT=%s,ADRESS=%s WHERE TRN=%s",(                                                           
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_sup_TLN.get(),       
                                                                                                                    self.var_contact.get(),
                                                                                                                    self.txt_adress.get('1.0',END),
                                                                                                                    self.var_sup_TRN.get()
                                                                                                                                                                                                        ))
                        conn.commit()
                        conn.close()                                                                                                                        
                        
                        messagebox.showinfo("SUCCESS","SUPPLIER UPDATED SUCCESSFULLY",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    def delete(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_sup_invoice.get=="":
             messagebox.showerror("Error","Invoice no. must be required",parent=self.root)
            else:
                my_cursor.execute("Select * from supplier where INVOICE=%s",(self.var_sup_invoice.get(),))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no. ",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete this record?",parent=self.root)
                    if op==True:
                        my_cursor.execute("delete from supplier where INVOICE=%s",(self.var_sup_invoice.get(),))
                        conn.commit()
                        messagebox.showinfo("DELETE","SUPPLIER DELETED SUCCESSFULLY",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_sup_TRN.set("")
        self.var_sup_TLN.set("")
        self.var_contact.set("")
        self.txt_adress.delete('1.0',END)
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        
        z=random.randint(2000,2999)
        self.var_sup_code.set(str(z))
        self.show()
    
    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                my_cursor.execute("select * from supplier where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('',END,values=row) 
                else:
                    messagebox.showerror("Error","No such record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)
    

        
        




        



        



        






if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop() 