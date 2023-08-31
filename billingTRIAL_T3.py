from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import time
from tkinter import ttk
import os
import tempfile
from customer_T1 import customerClass


 
class billing:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1520x700+0+0")
        self.root.title("MEDICAL STORE BILLING SYSTEM | DEVELOPED BY -------- ")
        self.root.config(bg="white")


        self.cart_list=[]
        self.cheque_print=0
        
        self.var_searchby= StringVar()
        self.var_searchtxt=StringVar()
        #self.var_vat=StringVar()
        #====Title====
        self.icon_title=PhotoImage(file="image/ICON 1.png")
        title=Label(self.root,text="MEDICAL STORE BILLING SYSTEM",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====btn_logout====
        btn_logout=Button(self.root,text="LOGOUT",font=("times new roman",15,"bold"),bg="red",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
        #====clock====
        self.lbl_clock=Label(self.root,text="WELCOME TO MEDICAL STORE BILLING SYSTEM\t\tDate: DD\MM\yy\t\t Time: HH:MM:SS  ", font=("times new roman",15,"bold"),bg="#4d636d",fg="white")

        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #====Product Frame=========
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        #====Product Seacrh Frame============
        self.var_search=StringVar()

        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=49,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
        
        #====Product Details Frame============
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("Category","Package_Name","Public_Price","Quantity","Status","Tax_Rate"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
        self.product_Table.heading("Category",text="Category")
        self.product_Table.heading("Package_Name",text="Package_Name")
        self.product_Table.heading("Public_Price",text="Public_Price")
        self.product_Table.heading("Quantity",text="QTY")
        self.product_Table.heading("Status",text="Status")
        self.product_Table.heading("Tax_Rate",text="Tax_Rate")
       


        self.product_Table["show"]="headings"
        
        self.product_Table.column("Category",width=90)
        self.product_Table.column("Package_Name",width=120)
        self.product_Table.column("Public_Price",width=90)
        self.product_Table.column("Quantity",width=40)
        self.product_Table.column("Status",width=90)
        self.product_Table.column("Tax_Rate",width=90)
        self.product_Table.pack(fill=BOTH,expand=1)

        self.product_Table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(ProductFrame1,text="Note | Enter 0 Quantity to remove product from Cart",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #==========Customer Frame================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",15),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",15),bg="lightyellow").place(x=380,y=35,width=140)

        #====Cal Cart Frame============
        Cust_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cust_Cart_Frame.place(x=420,y=190,width=530,height=360)

        cust_details_btn=Button(Cust_Cart_Frame,command=self.customer,text="Customer Details",font=("goudy old style",15),bg="darkgreen",fg="white").place(x=0,y=60,width=245)
        #========Search=========

        cmb_search=ttk.Combobox(Cust_Cart_Frame,textvariable=self.var_searchby,values=("Select","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=80)
        cmb_search.current(0)

        txt_search=Entry(Cust_Cart_Frame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=90,y=10,width=100)
        btn_search=Button(Cust_Cart_Frame,text="SEARCH",command=self.search_cust,font=("goudy old style",10),bg="#4caf50",fg="white",cursor="hand2").place(x=190,y=9,width=70,height=30)


        #====Cart Frame============
        cart_Frame=Frame(Cust_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)

        self.cartTitle=Label(cart_Frame,text="Cart \t  Total Product: [0]",font=("goudy old style",15),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("Category","Package_Name","Public_Price","Quantity","Tax_Rate"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
        
        self.CartTable.heading("Category",text="Category")
        self.CartTable.heading("Package_Name",text="Package_Name")
        self.CartTable.heading("Public_Price",text="Public_Price")
        self.CartTable.heading("Quantity",text="Quantity")
        self.CartTable.heading("Tax_Rate",text="Tax_Rate")
       


        self.CartTable["show"]="headings"

        self.CartTable.column("Category",width=70)
        self.CartTable.column("Package_Name",width=100)
        self.CartTable.column("Public_Price",width=100)
        self.CartTable.column("Quantity",width=80)
        self.CartTable.column("Tax_Rate",width=80)

        self.CartTable.pack(fill=BOTH,expand=1)

        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart) 


        #====Cust Frame============

        #=================================
        Cust_Frame=Frame(Cust_Cart_Frame,bd=3,relief=RIDGE)
        Cust_Frame.place(x=0,y=100,width=245,height=250)
        scrolly=Scrollbar(Cust_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cust_Frame,orient=HORIZONTAL)

        self.CustTable=ttk.Treeview(Cust_Frame,columns=("NAME","CONTACT"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CustTable.xview)
        scrolly.config(command=self.CustTable.yview)
        

        self.CustTable.heading("NAME",text="NAME")
        self.CustTable.heading("CONTACT",text="CONTACT")


        self.CustTable["show"]="headings"

       
        self.CustTable.column("NAME",width=100)
        self.CustTable.column("CONTACT",width=80)

        self.CustTable.pack(fill=BOTH,expand=1)

        self.CustTable.bind("<ButtonRelease-1>",self.get_data_cust)
        self.show_cust()
        

        #====Add to Cart Widgets Frame============
        self.var_cat=StringVar()
        self.var_packageName=StringVar()
        self.var_publicPrice=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        self.var_vat=StringVar()


        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_packageName,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=5,y=35,width=150,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price per QTY",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_publicPrice,font=("times new roman",15),bg="lightyellow",state="readonly").place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_instock=Label(Add_CartWidgetsFrame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)

        #=================Billing Area===========================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=540,height=410)

        BTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="orange red",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrollx=Scrollbar(billFrame,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        #scrollx=Scrollbar(billFrame,orient=HORIZONTAL)
        #scrollx.pack(side=BOTTOM,fill=X)

        #self.CustTable=ttk.Treeview(Cust_Frame,columns=("NAME","CONTACT"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        #scrollx.pack(side=BOTTOM,fill=X)
        #scrolly.pack(side=RIGHT,fill=Y)
        #scrollx.config(command=self.CustTable.xview)

        self.txt_bill_area=Text(billFrame,xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrollx.config(command=self.txt_bill_area.xview)
        scrolly.config(command=self.txt_bill_area.yview)
        #scrollx.config(command=self.txt_bill_area.xview)

        #======================Billing Buttons============================
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=540,height=140)

        self.lbl_amnt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=190,height=70)
 
        self.lbl_vat=Label(billMenuFrame,text="VAT Amount\n[5%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_vat.place(x=200,y=5,width=120,height=70)

        self.lbl_net_amnt=Label(billMenuFrame,text="Net Amount\n[0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_amnt.place(x=330,y=5,width=190,height=70)


        btn_print=Button(billMenuFrame,text="Print",command=self.print_bill,font=("goudy old style",15,"bold"),bg="lightgreen",fg="white",cursor="hand2")
        btn_print.place(x=330,y=80,width=190,height=50)

        btn_clear_all=Button(billMenuFrame,text="Clear All",command=self.clear_all,font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2")
        btn_clear_all.place(x=200,y=80,width=120,height=50)

        btn_generate=Button(billMenuFrame,text="Generate/Save Bill",command=self.generate_bill,font=("goudy old style",15,"bold"),bg="#009688",fg="white",cursor="hand2")
        btn_generate.place(x=2,y=80,width=190,height=50)

        #====Footer====
        lbl_footer=Label(self.root,text="MBS BILLING SYSTEM | DEVELOPED BY ------\nFOR ANY THECHNICAL ISSSUE CONTACT  :  +971XXXXXXXXX ", font=("times new roman",12,"bold"),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.show()
        self.show_cust()


    def customer(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=customerClass(self.new_win)
        
    
    def show(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            my_cursor.execute("select Category,Package_Name,Public_Price,Quantity,Status,Tax_Rate from product2 where Status='Active'")
            rows=my_cursor.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row) 
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)
    
    def show_cust(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            my_cursor.execute("select NAME,CONTACT from customer")
            rows=my_cursor.fetchall()
            self.CustTable.delete(*self.CustTable.get_children())
            for row in rows:
                self.CustTable.insert('',END,values=row) 
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    
    def search(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                my_cursor.execute("select Category,Package_Name,Public_Price,Quantity,Status,Tax_Rate from product2 where Package_Name LIKE '%"+self.var_search.get()+"%' and Status='Active'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row) 
                else:
                    messagebox.showerror("Error","No such record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)
    
    

    def search_cust(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                my_cursor.execute("select NAME,CONTACT from customer where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.CustTable.delete(*self.CustTable.get_children())
                    for row in rows:
                        self.CustTable.insert('',END,values=row) 
                else:
                    messagebox.showerror("Error","No such record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)
    
    def get_data_cust(self,ev):
        f=self.CustTable.focus()
        content=(self.CustTable.item(f))
        row=content['values']
        self.var_cname.set(row[0])
        self.var_contact.set(row[1])
    
    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_cat.set(row[0])
        self.var_packageName.set(row[1])
        self.var_publicPrice.set(row[2])
        self.lbl_instock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
        self.var_vat.set(row[5])
    
    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_cat.set(row[0])
        self.var_packageName.set(row[1])
        self.var_publicPrice.set(row[2])
        self.var_qty.set(row[3])
        self.var_vat.set(row[4])
        

        self.lbl_instock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
    
    def add_update_cart(self):
        if self.var_cat.get()=="":
            messagebox.showerror("Error","Please select product from the list",parent=self.root)
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity is required",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        else:
            #price_cal=int(self.var_qty.get())*float(self.var_publicPrice.get())
            #price_cal=float(price_cal)
            price_cal=self.var_publicPrice.get()
            #Category,Package_Name,Public_Price,Quantity,Stock
            cart_data=[self.var_cat.get(),self.var_packageName.get(),price_cal,self.var_qty.get(),self.var_vat.get(),self.var_stock.get()]
            #=======Update_Cart=========
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_packageName.get()==row[1]:
                    present='yes'
                    break
                index_=+1
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product is already present\nDo ypu want to Update / Remove from Cart ?",parent=self.root)
                if op==True:
                    if self.var_qty.get()=='0':
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_qty.get() #qty


            else:
                self.cart_list.append(cart_data)               
            self.show_cart()
            self.bill_updates()
    

    def bill_updates(self):
        self.bill_amnt=0
        self.net_amnt=0
        self.vat=0
        for row in self.cart_list:
            #Category,Package_Name,Public_Price,Quantity,Stock
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))

        self.vat=(self.bill_amnt*int(self.var_vat.get())/100)
        self.net_amnt=self.bill_amnt+self.vat
        self.lbl_amnt.config(text=f'Bill Amnt.(dhs))\n{str(self.bill_amnt)}')
        self.lbl_net_amnt.config(text=f'Net Amnt.(dhs)\n{str(self.net_amnt)}')
        self.cartTitle.config(text=f"Cart \t  Total Product: [{str(len(self.cart_list))}]")

        

    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row) 
                
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)


    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error","Please enter the Customer Details",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error","Please add Product to Cart !!!",parent=self.root)
        else:
            #======Bill Top========
            self.bill_top()
            #======Bill Middle=====
            self.bill_middle()
            #======Bill Bottom=====
            self.bill_bottom()
            

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved","Generated Bill has been saved successfully",parent=self.root)
            self.cheque_print=1
    

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tBilling Interface
\t Phone No. +971 xxxxxx000 , ADRESS-123STREET
{str("="*58)}
 Customer Name: {self.var_cname.get()}
 Ph No. : {self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*58)} 
 Product Name\t  Type
{str("="*58)}      
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
    

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*100)}
 Bill Amount\t\t\t\tAED.{self.bill_amnt}
 VAT Amount\t\t\t\tAED.{self.vat}
 Net Amount\t\t\t\tAED.{self.net_amnt}
{str("="*100)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
    
    def bill_middle(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            for row in self.cart_list:
                #Category,Package_Name,Public_Price,Quantity,Stock
                name=row[1]
                Type=row[0]
                qty=int(row[4])-int(row[3])
                vat=row[5]
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'

                price=float(row[2])*1
                price=str(price)
                self.txt_bill_area.insert(END,"\n"+name+"hh")
                #=========Uptade stock in product table==========
                my_cursor.execute('Update product set Quantity=%s,Status=%s Where Package_Name=%s',(
                    qty,
                    status,
                    name
                    ))
                conn.commit()
            conn.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)

    def clear_cart(self):
        self.var_cat.set('')
        self.var_packageName.set('')
        self.var_publicPrice.set('')
        self.var_qty.set('')
        self.lbl_instock.config(text=f"In Stock")
        self.var_stock.set('')
        self.var_vat.set('')
    
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t  Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d/%m/%Y")
        self.lbl_clock.config(text=f"WELCOME TO MEDICAL STORE BILLING SYSTEM\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
    



    def print_bill(self):
        if self.cheque_print==1:
            messagebox.showinfo("Printing...","Please wait wile printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Error","Please generate bill to print reciept",parent=self.root)
    

    def logout(self):
        self.root.destroy()
        os.system("python login_T1.py")
    


if __name__=="__main__":
    root=Tk()
    obj=billing(root)
    root.mainloop()
    