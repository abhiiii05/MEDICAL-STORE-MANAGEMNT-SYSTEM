from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql
import mysql.connector
import random


class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x530+220+130")
        self.root.title("PRODUCTS MANAGEMENT SYSTEM | DEVELOPED BY -------- ")
        self.root.config(bg="white")
        self.root.focus_force()
        #=============================
        #============Variables=============
        self.var_searchby= StringVar()
        self.var_searchtxt=StringVar()


        self.var_cat=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_prd_code=StringVar()
        z=random.randint(3000,3999)
        self.var_prd_code.set(str(z))
        self.var_drug_code=StringVar()
        self.var_generic_name=StringVar()
        self.var_package_name=StringVar()
        self.var_uses=StringVar()
        self.var_sideeffect=StringVar()
        self.var_supplier=StringVar()
        self.var_pharmacy_price=StringVar()
        self.var_public_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_vat=StringVar()

        
        

        #=========Prd Frame===========
        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=510)

        #======title=====
        title=Label(product_frame,text="Product Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        lbl_category=Label(product_frame,text="Category",font=("goudy old style",15),bg="white").place(x=10,y=120)
        lbl_product_code=Label(product_frame,text="Product Code",font=("goudy old style",15),bg="white").place(x=10,y=40)
        lbl_drug_code=Label(product_frame,text="Drug Code",font=("goudy old style",15),bg="white").place(x=10,y=160)
        lbl_genericname=Label(product_frame,text="Generic Name",font=("goudy old style",15),bg="white").place(x=10,y=200)
        lbl_packagename=Label(product_frame,text="Package Name",font=("goudy old style",15),bg="white").place(x=10,y=240)
        lbl_uses=Label(product_frame,text="Uses",font=("goudy old style",15),bg="white").place(x=10,y=280)
        lbl_sideeffect=Label(product_frame,text="Side Effects",font=("goudy old style",15),bg="white").place(x=10,y=320)
        lbl_supplier=Label(product_frame,text="Supplier",font=("goudy old style",15),bg="white").place(x=10,y=80)
        lbl_pharmacy_price=Label(product_frame,text="Pharmacy Price",font=("goudy old style",15),bg="white").place(x=10,y=360)
        lbl_public_price=Label(product_frame,text="Public Price",font=("goudy old style",15),bg="white").place(x=10,y=400)
        lbl_qty=Label(product_frame,text="Quantity",font=("goudy old style",15),bg="white").place(x=10,y=440)
        lbl_status=Label(product_frame,text="Status",font=("goudy old style",15),bg="white").place(x=260,y=40)
        lbl_vat=Label(product_frame,text="VAT",font=("goudy old style",15),bg="white").place(x=260,y=70)


        #====combo box====
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",13))
        cmb_cat.place(x=140,y=120,width=150)
        cmb_cat.current(0)
        
        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_supplier,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",13))
        cmb_sup.place(x=90,y=80,width=150)
        cmb_sup.current(0)

        txt_prd_code=Entry(product_frame,textvariable=self.var_prd_code,state='readonly',font=("goudy old style",15)).place(x=130,y=40,width=100)
        txt_drug_code=Entry(product_frame,textvariable=self.var_drug_code,font=("goudy old style",15),bg="lightyellow").place(x=140,y=160,width=150)
        txt_generic_name=Entry(product_frame,textvariable=self.var_generic_name,font=("goudy old style",15),bg="lightyellow").place(x=140,y=200,width=150)
        txt_package_name=Entry(product_frame,textvariable=self.var_package_name,font=("goudy old style",15),bg="lightyellow").place(x=140,y=240,width=150)

        cmb_uses=ttk.Combobox(product_frame,textvariable=self.var_uses,values=("Select","Internal","External"),state='readonly',justify=CENTER,font=("goudy old style",13))
        cmb_uses.place(x=140,y=280,width=150)
        cmb_uses.current(0)

        cmb_side_effects=ttk.Combobox(product_frame,textvariable=self.var_sideeffect,values=("Select","N/A","Nausea","Headache","Body Pain","Drowziness","Other"),state='readonly',justify=CENTER,font=("goudy old style",13))
        cmb_side_effects.place(x=140,y=320,width=150)
        cmb_side_effects.current(0)

        txt_pharmacy_price=Entry(product_frame,textvariable=self.var_pharmacy_price,font=("goudy old style",15),bg="lightyellow").place(x=140,y=360,width=150)
        txt_public_price=Entry(product_frame,textvariable=self.var_public_price,font=("goudy old style",15),bg="lightyellow").place(x=140,y=400,width=150)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=140,y=440,width=150)
        txt_vat=Entry(product_frame,textvariable=self.var_vat,font=("goudy old style",15),bg="lightyellow").place(x=320,y=70,width=120)

        cmb_side_effects=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Select","Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",13))
        cmb_side_effects.place(x=320,y=40,width=120)
        cmb_side_effects.current(0)

        #====buttons====
        btn_add=Button(product_frame,text="SAVE",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=480,width=90,height=28)
        btn_update=Button(product_frame,text="UPDATE",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=110,y=480,width=90,height=28)
        btn_delete=Button(product_frame,text="DELETE",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=210,y=480,width=90,height=28)
        btn_clear=Button(product_frame,text="CLEAR",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=310,y=480,width=90,height=28)


        #====searchframe====
        SearchFrame=LabelFrame(self.root,text="SEARCH PRODUCT",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=465,y=10,width=630,height=70)
        #====options====
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Product_Code","Supplier","Package_Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="SEARCH",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=100,height=30)
        btn_showall=Button(SearchFrame,text="SHOW ALL",command=self.show,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=520,y=9,width=105,height=30)

        #====Product Details====

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=465,y=90,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("Product_Code","Supplier","Category","Drug_Code","Generic_name","Package_Name","Uses","Side_Effects","Pharmacy_Price","Public_Price","Quantity","Status","VAT"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
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
        self.product_table.heading("VAT",text="VAT")

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
        self.product_table.column("VAT",width=100)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        



#============================================================================
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            my_cursor.execute("Select NAME from category")
            cat=my_cursor.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            


            my_cursor.execute("Select NAME from supplier")
            sup=my_cursor.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])           
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    

    def add(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_generic_name.get()=="" or self.var_pharmacy_price.get()=="" or self.var_qty.get()=="":
                    messagebox.showerror("Error","All fiels are required",parent=self.root)
            else:
                my_cursor.execute("Select * from product2 where Product_Code=%s",(self.var_prd_code.get(),))
                row=my_cursor.fetchone()
                if row!=None:
                        messagebox.showerror("Error","This Product already exists, please enter another project",parent=self.root)
                else:
                        my_cursor.execute("Insert into product2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(                                                           
                                                                                                        self.var_prd_code.get(),
                                                                                                        self.var_supplier.get(),
                                                                                                        self.var_cat.get(),
                                                                                                        self.var_drug_code.get(),
                                                                                                        self.var_generic_name.get(),
                                                                                                        self.var_package_name.get(),
                                                                                                        self.var_uses.get(),               
                                                                                                        self.var_sideeffect.get(),
                                                                                                        self.var_pharmacy_price.get(),
                                                                                                        self.var_public_price.get(),
                                                                                                        self.var_qty.get(),
                                                                                                        self.var_status.get(),
                                                                                                        self.var_vat.get()
                                                                                                                                                ))
                        conn.commit()
                        conn.close()                                                                                                                        
                        
                        messagebox.showinfo("SUCCESS","PRODUCT ADDED SUCCESSFULLY",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    
    def show(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            my_cursor.execute("select * from product2")
            rows=my_cursor.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row) 
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_prd_code.set(row[0])
        self.var_supplier.set(row[1])
        self.var_cat.set(row[2])
        self.var_drug_code.set(row[3])
        self.var_generic_name.set(row[4])
        self.var_package_name.set(row[5])
        self.var_uses.set(row[6])               
        self.var_sideeffect.set(row[7])
        self.var_pharmacy_price.set(row[8])
        self.var_public_price.set(row[9])
        self.var_qty.set(row[10])
        self.var_status.set(row[11])
        self.var_vat.set(row[12])
        
    

    def update(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_prd_code.get=="":
                    messagebox.showerror("Error","Please select product from list ",parent=self.root)
            else:
                my_cursor.execute("Select * from product2 where Product_Code=%s",(self.var_prd_code.get(),))
                row=my_cursor.fetchone()
                if row==None:
                        messagebox.showerror("Error","Invalid Product ",parent=self.root)
                else:
                        my_cursor.execute("Update product2 set Supplier=%s,Category=%s,Drug_Code=%s,Generic_name=%s,Package_Name=%s,Uses=%s,Side_Effects=%s,Pharmacy_Price=%s,Public_Price=%s,Quantity=%s,Status=%s,VAT=%s WHERE Product_Code=%s",(                                                     
                                                                                                                                                                                                                                            self.var_supplier.get(),
                                                                                                                                                                                                                                            self.var_cat.get(),
                                                                                                                                                                                                                                            self.var_drug_code.get(),
                                                                                                                                                                                                                                            self.var_generic_name.get(),
                                                                                                                                                                                                                                            self.var_package_name.get(),
                                                                                                                                                                                                                                            self.var_uses.get(),               
                                                                                                                                                                                                                                            self.var_sideeffect.get(),
                                                                                                                                                                                                                                            self.var_pharmacy_price.get(),
                                                                                                                                                                                                                                            self.var_public_price.get(),
                                                                                                                                                                                                                                            self.var_qty.get(),
                                                                                                                                                                                                                                            self.var_status.get(),
                                                                                                                                                                                                                                            self.var_vat.get(),
                                                                                                                                                                                                                                            self.var_prd_code.get()
                                                                                                                                                                                                        ))
                        conn.commit()
                        conn.close()                                                                                                                        
                        
                        messagebox.showinfo("SUCCESS","PRODUCT UPDATED SUCCESSFULLY",parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    def delete(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_prd_code.get=="":
             messagebox.showerror("Error","Select Product from the list",parent=self.root)
            else:
                my_cursor.execute("Select * from product2 where Product_Code=%s",(self.var_prd_code.get(),))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete this record?",parent=self.root)
                    if op==True:
                        my_cursor.execute("delete from product2 where Product_Code=%s",(self.var_prd_code.get(),))
                        conn.commit()
                        messagebox.showinfo("DELETE","PRODUCT DELETED SUCCESSFULLY",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_supplier.set("Select")
        self.var_cat.set("Select")
        self.var_drug_code.set("")
        self.var_generic_name.set("")
        self.var_package_name.set("")
        self.var_uses.set("Select")               
        self.var_sideeffect.set("Select")
        self.var_pharmacy_price.set("")
        self.var_public_price.set("")
        self.var_qty.set("")
        self.var_status.set("Select")
        #self.var_prd_code.set("")
        z=random.randint(3000,3999)
        self.var_prd_code.set(str(z))
        
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.var_vat.set("")
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
                my_cursor.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
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
    obj=productClass(root)
    root.mainloop()