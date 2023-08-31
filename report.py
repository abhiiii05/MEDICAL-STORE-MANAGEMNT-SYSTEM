from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import time
from tkinter import ttk
import os
import tempfile
from customer_T1 import customerClass


class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("REPORT MANAGEMENT SYSTEM | DEVELOPED BY -------- ")
        self.root.config(bg="white")
        self.root.focus_force()
    #All Vairiables=====
        self.var_searchby= StringVar()
        self.var_searchtxt=StringVar()
        self.var_searchby2= StringVar()
        self.var_searchtxt2=StringVar()
        self.var_searchby3= StringVar()
        self.var_searchtxt3=StringVar()
    
     #====title====
        title=Label(self.root,text="Report Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=140,width=1000)
    
    #====searchframe====
        SearchFrame=LabelFrame(self.root,text="SEARCH BY",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=40,y=20,width=1040,height=100)
    #====options====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Product_Code","Supplier","Category","Drug_Code","Generic_name","Package_Name","Uses","Side_Effects","Pharmacy_Price","Public_Price","Quantity","Status"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=150)
        cmb_search.current(0)

        cmb_search2=ttk.Combobox(SearchFrame,textvariable=self.var_searchby2,values=("Select","Product_Code","Supplier","Category","Drug_Code","Generic_name","Package_Name","Uses","Side_Effects","Pharmacy_Price","Public_Price","Quantity","Status"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search2.place(x=350,y=10,width=150)
        cmb_search2.current(0)

        cmb_search3=ttk.Combobox(SearchFrame,textvariable=self.var_searchby3,values=("Select","Product_Code","Supplier","Category","Drug_Code","Generic_name","Package_Name","Uses","Side_Effects","Pharmacy_Price","Public_Price","Quantity","Status"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search3.place(x=690,y=10,width=150)
        cmb_search3.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=170,y=10,width=170)
        txt_search2=Entry(SearchFrame,textvariable=self.var_searchtxt2,font=("goudy old style",15),bg="lightyellow").place(x=510,y=10,width=170)
        txt_search3=Entry(SearchFrame,textvariable=self.var_searchtxt3,font=("goudy old style",15),bg="lightyellow").place(x=850,y=10,width=170)
        btn_search=Button(SearchFrame,text="SEARCH",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=350,y=45,width=150,height=30)
        btn_showall=Button(SearchFrame,text="SHOW ALL",command=self.show,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=510,y=45,width=150,height=30)



        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=45,y=180,width=1000,height=320)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("Product_Code","Supplier","Category","Drug_Code","Generic_name","Package_Name","Uses","Side_Effects","Pharmacy_Price","Public_Price","Quantity","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        self.product_table.heading("Product_Code",text="Product_Code")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("Drug_Code",text="Drug_Code")
        self.product_table.heading("Generic_name",text="Generic_name")
        self.product_table.heading("Package_Name",text="Package_Name")
        self.product_table.heading("Uses",text="Uses")
        self.product_table.heading("Side_Effects",text="Side_Effects")
        self.product_table.heading("Pharmacy_Price",text="Pharmacy_Price")
        self.product_table.heading("Public_Price",text="Public_Price")
        self.product_table.heading("Quantity",text="Quantity")
        self.product_table.heading("Status",text="Status")

        self.product_table["show"]="headings"

        self.product_table.column("Product_Code",width=90)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("Category",width=100)
        self.product_table.column("Drug_Code",width=100)
        self.product_table.column("Generic_name",width=100)
        self.product_table.column("Package_Name",width=100)
        self.product_table.column("Uses",width=100)
        self.product_table.column("Side_Effects",width=100)
        self.product_table.column("Pharmacy_Price",width=100)
        self.product_table.column("Public_Price",width=100)
        self.product_table.column("Quantity",width=100)
        self.product_table.column("Status",width=100)
        self.product_table.pack(fill=BOTH,expand=1)

        self.show()
    

    def show(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            my_cursor.execute("select * from product")
            rows=my_cursor.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row) 
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)




    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_searchby.get()=="Select" and self.var_searchby.get()=="Select" and self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="" and self.var_searchtxt2.get()=="" and self.var_searchtxt3.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                my_cursor.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'" "AND " +self.var_searchby2.get()+" LIKE '%"+self.var_searchtxt2.get()+"%'" "AND " +self.var_searchby2.get()+" LIKE '%"+self.var_searchtxt2.get()+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row) 
                else:
                    messagebox.showerror("Error","No such record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()