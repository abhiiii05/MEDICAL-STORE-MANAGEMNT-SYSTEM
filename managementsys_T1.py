from tkinter import*
from PIL import Image,ImageTk
from time import strftime
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from report import reportClass
from billing_T2 import billing
import mysql.connector
from tkinter import messagebox
import os
import time


 
class MBS:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1450x800+0+0")
        self.root.title("ABC MEDICAL STORE | DEVELOPED BY Abhijith Viju ")
        self.root.config(bg="white")

        #====Title====
        self.icon_title=PhotoImage(file="image/ICON 1.png")
        title=Label(self.root,text="\t\tABC PHARMACY ",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #====btn_logout====
        btn_logout=Button(self.root,command=self.logout,text="LOGOUT",font=("times new roman",15,"bold"),fg="ghost white",bg="black",cursor="hand2").place(x=1220,y=700,height=50,width=310)

        #====adress====
        self.lbl_adress=Label(self.root,text="  \t\t Bank Street, Rolla, Sharjah, UAE  ", font=("times new roman",15,"bold"),bg="thistle",fg="black")

        self.lbl_adress.place(x=0,y=70,relwidth=1,height=30)
        
        #====clock====
        self.lbl_clock=Label(self.root,text="Date: DD\MM\yy     \t\t\tMEDICAL STORE BILLING SYSTEM\t\tTime: HH:MM:SS  ", font=("times new roman",15,"bold"),bg="RoyalBlue1",fg="white")

        self.lbl_clock.place(x=0,y=100,relwidth=1,height=30)


        

        #====Left Menu====
        self.MenuLogo=Image.open("image/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=130,width=315,height=622)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="image/side.png")
        lbl_menu=Label(LeftMenu,text="MENU",font=("times new roman",15,"bold"),bg="#009688").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text="EMPLOYEE",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="SUPPLIER",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="CATEGORY",command=self.cateogry,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="PRODUCT",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="SALES",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="REPORT",command=self.report,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_billing=Button(LeftMenu,text="BILLING",command=self.billing,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #====Right Menu====
        RightMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        RightMenu.place(x=1219,y=130,width=315,height=565)

        #====content====

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="azure2",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=1219,y=130,height=110,width=310)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="light steel blue",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=1219,y=242,height=110,width=310)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="LightSkyBlue1",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1219,y=354,height=110,width=310)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="pink2",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=1219,y=466,height=110,width=310)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="wheat1",fg="black",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=1219,y=578,height=110,width=310)

        #====footer====
        lbl_footer=Label(self.root,text="MBS BILLING SYSTEM | DEVELOPED BY ABHIJITH VIJU PRIYA RANI\nFOR ANY THECHNICAL ISSSUE CONTACT  :  +97150XXXX472 ", font=("times new roman",12,"bold"),bg="RoyalBlue1",fg="white").pack(side=BOTTOM,fill=X)

        self.update_content()

        #====project details====
        lbl_prject_details=Label(self.root,text="GRADE XII C  ;  SHARJAH INDIAN SCHOOL  ;  CBSE SUMMER VACCATION PROJECT \n DONE BY : ABHIJTIH VIJU PRIYA RANI", font=("times new roman",16,"bold"),bg="SpringGreen4",fg="white").place(x=320,y=700,width=890,height=50)
        



        #====main picture========
        self.Mainpic=Image.open("image/mian_pic.png")
        self.Mainpic=self.Mainpic.resize((892,565),Image.ANTIALIAS)
        self.Mainpic=ImageTk.PhotoImage(self.Mainpic)

        main_pic_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        main_pic_frame.place(x=320,y=130,width=892,height=565)

        lbl_mainpic=Label(main_pic_frame,image=self.Mainpic)
        lbl_mainpic.pack(side=TOP,fill=X)

        
#======================================================================================
    
    
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def cateogry(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
    
    def report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=billing(self.new_win)
    
    def update_content(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='trial')
        my_cursor=conn.cursor()
        try:
            my_cursor.execute("select * from product" )
            product=my_cursor.fetchall()
            self.lbl_product.config(text=f'Total Product\n[ {str(len(product))} ]')

            my_cursor.execute("select * from supplier" )
            supplier=my_cursor.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[ {str(len(supplier))} ]')

            my_cursor.execute("select * from category" )
            category=my_cursor.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')

            my_cursor.execute("select * from ems" )
            employee=my_cursor.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ {str(len(employee))} ]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d/%m/%Y")
            self.lbl_clock.config(text=f"Date: {str(date_)}      \t\t\t MEDICAL STORE BILLING SYSTEM\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror("Error",f"Something went wrong due to : {str(ex)}",parent=self.root)



    def logout(self):
        self.root.destroy()
        os.system("python login_T1.py")
    



if __name__=="__main__":
    root=Tk()
    obj=MBS(root)
    root.mainloop()
    
