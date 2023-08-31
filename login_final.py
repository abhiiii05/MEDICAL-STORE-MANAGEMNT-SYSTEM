from distutils.log import error
from logging import root
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("999x665+220+89")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sviju\Desktop\prject\TRIAL 2\image\2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="sienna4")
        frame.place(x=350,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\sviju\Desktop\prject\TRIAL 2\image\user.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="sienna4",borderwidth=0)
        lblimg1.place(x=470,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="sienna4")
        get_str.place(x=95,y=100)


        #label
        username=lbl=Label(frame,text="Username : ",font=("times new roman",15,"bold"),fg="white",bg="sienna4")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270) 


        password=lbl=Label(frame,text="Password : ",font=("times new roman",15,"bold"),fg="white",bg="sienna4")
        password.place(x=70,y=225)

        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpassword.place(x=40,y=250,width=270)
        
        #icon images needed?

        #Login Button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="sienna4",bg="PeachPuff2",activebackground="PeachPuff2",activeforeground="sienna4")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #Rgister(Sign up)Button
        registerbtn=Button(frame,text="Sign Up",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="PeachPuff2",bg="sienna4",activebackground="sienna4",activeforeground="PeachPuff2")
        registerbtn.place(x=0,y=350,width=100)

        #Forgot password Button
        forgotbtn=Button(frame,text="Forgot Password ?",command=self.forgot_password_winidow,font=("times new roman",15,"bold"),borderwidth=0,fg="PeachPuff2",bg="sienna4",activebackground="sienna4",activeforeground="PeachPuff2")
        forgotbtn.place(x=10,y=390,width=160)
    

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()==""  or  self.txtpassword.get()=="":
             messagebox.showerror("Error","All Fields Are Required")
        elif self.txtuser.get()=="Abhi101"  and  self.txtpassword.get()=="12345":
            messagebox.showinfo("Success","Welcome")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from user_register where email=%s and password=%s",(
                                                                                          self.txtuser.get(),
                                                                                          self.txtpassword.get()
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("Admin?","Only admin can acess")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=PharmacyManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    #=============================Reset Password=================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Please enter your answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password ",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from user_register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please input the correct details ",parent=self.root2)
            else:
                query=("update user_register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login using the new password",parent=self.root2)
                self.root2.destroy()












    #=============================Forgot Password Window=================================
    def forgot_password_winidow(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Yoyr Email Adress To Reset The Password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from  user_register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter a valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+570+260")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="navajo white",bg="sienna4")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Favourite Colour","Best Friend's Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
                security_A.place(x=50,y=150)

                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security_A.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15),fg="navajo white",bg="sienna4")
                btn.place(x=100,y=290)










        


            




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign Up")
        self.root.geometry("1920x1280+0+0")

        #=============================Variables=================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #=============================BG Image=================================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sviju\Desktop\prject\TRIAL 2\image\signup1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1) 


        #=============================Main Frame=================================
        frame=Frame(self.root,bg="lemon chiffon")
        frame.place(x=350,y=170,width=800,height=550)

        register_lbl=Label(frame,text="Sign Up Here",font=("times new roman",20,"bold"),fg="saddle brown",bg="lemon chiffon")
        register_lbl.place(x=20,y=20)

        #=============================Label & Entries=================================
        fname=Label(frame,text="First Name : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #------------------------row 2----------------

        contact=Label(frame,text="Contact No : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")        
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #------------------------row 3----------------

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Favourite Colour","Best Friend's Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
        security_A.place(x=370,y=240)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security_A.place(x=370,y=270,width=250)

        #------------------------row 4----------------

        pswd=Label(frame,text="Password : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password : ",font=("times new roman",15,"bold"),fg="saddle brown",bg="lemon chiffon")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #=============================Checkbox=================================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree To The Terms & Conditions",font=("times new roman",12,"bold"),fg="saddle brown",bg="lemon chiffon",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #=============================Bottom Buttons=================================
        img=Image.open(r"C:\Users\sviju\Desktop\prject\TRIAL 2\image\signupbtn.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=420,width=200)


        img1=Image.open(r"C:\Users\sviju\Desktop\prject\TRIAL 2\image\loginbtn.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,command=self.retun_login,borderwidth=0,cursor="hand2")
        b2.place(x=370,y=420,width=200)


    #=============================Function Declaration=================================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwords doesn't match")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree To The Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from user_register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists. Please try another email.")
            else:
                my_cursor.execute("insert into user_register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             self.var_fname.get(),
                                                                                             self.var_lname.get(),
                                                                                             self.var_contact.get(),
                                                                                             self.var_email.get(),
                                                                                             self.var_securityQ.get(),
                                                                                             self.var_securityA.get(),
                                                                                             self.var_pass.get()
                                                                                           ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Signed Up Successfully")
        
    def retun_login (self):
        self.root.destroy()
            












class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Medical Store Management Sysytem")
        self.root.geometry("1550x800+0+0")



        #=============================Add Medicine Variable( RIGHT )=================================
        self.Addmed_var=StringVar()
        self.refMed_var=StringVar()

        #=============================Add Medicine Variable( LEFT )=================================
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()


        
        lbltitle=Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg="#33bbf9",fg="black",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open("image/newicon.png")
        img1=img1.resize((80,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)

        #=============================DataFrame=================================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="dark green",font=("arial",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)


        


        #=============================ButtonFrame=================================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)


        #=============================MainButton===================================
        btnAddData=Button(ButtonFrame,command=self.add_data,text="Add Medcine",font=("arial",12,"bold"),width=13,bg="dark green",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,command=self.Update,text="UPDATE",font=("arial",13,"bold"),width=13,bg="dark green",fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,command=self.delete,text="DELETE",font=("arial",13,"bold"),width=13,bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)

        btnRestMed=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",13,"bold"),width=13,bg="dark green",fg="white")
        btnRestMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,command=self.iExit,text="EXIT",font=("arial",13,"bold"),width=13,bg="red",fg="white")
        btnExitMed.grid(row=0,column=4)

        #=============================SearchBy===================================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="blue",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)


        #variable
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",17,"bold"),state="readonly")
        search_combo["values"]=("Batch Code","Med Name","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchtxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchtxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)


        searchBtn=Button(ButtonFrame,command=self.search_data,text="Search",font=("arial",13,"bold"),width=13,bg="dark green",fg="white")
        searchBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("arial",13,"bold"),width=13,bg="red",fg="white")
        showAll.grid(row=0,column=9)

        #=============================Label & Entry===================================
        Framedetails=Frame(self.root, bd=15,padx=20,relief=RIDGE)
        Framedetails.place(x=0,y=590,width=1530,height=210)

        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT Batch FROM PHARMA")
        row=my_cursor.fetchall()

        lblbatch=Label(DataFrameLeft,font=("arial",12,"bold"),text="Batch Code",padx=2,pady=6)
        lblbatch.grid(row=0,column=0,sticky=W)


        batch_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=("arial",12,"bold"),state="readonly")
        batch_combo["values"]=row
        batch_combo.grid(row=0,column=1)
        batch_combo.current(0)


        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6,)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1)

        lblTypeofMed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type of Medicine",padx=2,pady=6,)
        lblTypeofMed.grid(row=2,column=0,sticky=W)

        TypeofMed=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=27,font=("arial",12,"bold"),state="readonly")
        TypeofMed["values"]=("Tablets","Capsules","Drops","Inhales","Injection")
        TypeofMed.current(0)
        TypeofMed.grid(row=2,column=1)


        #=============================Add Medicine===================================

        lblMedName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6,)
        lblMedName.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT MedName FROM pharma")
        med=my_cursor.fetchall()

        MedName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,width=27,font=("arial",12,"bold"),state="readonly")
        MedName["values"]=med
        MedName.current(0)
        MedName.grid(row=3,column=1)



        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6,)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6,)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6,)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtExpDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6,)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects:",padx=2,pady=6,)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)

        lblPrec=Label(DataFrameLeft,font=("arial",12,"bold"),text="Precautions:",padx=2,pady=6,)
        lblPrec.grid(row=0,column=2,sticky=W)
        txtPrec=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=25)
        txtPrec.grid(row=0,column=3)

        

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Price:",padx=2,pady=6,)
        lblPrice.grid(row=1,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=25)
        txtPrice.grid(row=1,column=3)

        lblPrdQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prd Quantity:",padx=2,pady=6,)
        lblPrdQt.grid(row=2,column=2,sticky=W)
        txtPrdQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",13,"bold"),bg="white",bd=2, relief=RIDGE,width=25)
        txtPrdQt.grid(row=2,column=3,sticky=W)

        #=============================Images===================================
        
        lblhome=Label(DataFrameLeft,font=("arial",12,"bold"),text="Stay Home Stay Safe",padx=2,pady=6,bg="dark green",fg="white",width=37,)
        lblhome.place(x=426,y=130)

        img2=Image.open("image/newimg.png")
        img2=img2.resize((430,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=489,y=330)


        #=============================DataframeRight===================================


        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Add Medicine Information",fg="dark green",font=("arial",14,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)


        img3=Image.open("image/newimg2.png")
        img3=img3.resize((200,75),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=960,y=160)

        lblbatchno=Label(DataFrameRight,font=("arial",12,"bold"),text="Batch No:",padx=2,pady=6,)
        lblbatchno.place(x=0,y=80)
        txtbatchno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",15,"bold"),bg="white",bd=2, relief=RIDGE,width=14)
        txtbatchno.place(x=135,y=80)

        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6,)
        lblmedName.place(x=0,y=110)
        txtmedName=Entry(DataFrameRight,textvariable=self.Addmed_var,font=("arial",15,"bold"),bg="white",bd=2, relief=RIDGE,width=14)
        txtmedName.place(x=135,y=110)

        #=============================Display Frame (right)===================================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.med_table=ttk.Treeview(side_frame,column=("Batch No","Med Name"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.med_table.xview)
        sc_y.config(command=self.med_table.yview)

        self.med_table.heading("Batch No",text="Batch No")
        self.med_table.heading("Med Name",text="Medicine Name")

        self.med_table["show"]="headings"
        self.med_table.pack(fill=BOTH,expand=1)

        self.med_table.column("Batch No",width=100)
        self.med_table.column("Med Name",width=100)

        self.med_table.bind("<ButtonRelease-1>",self.Medget_cursor)


        #=============================Add Medicine Buttons===================================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="blue")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddMed=Button(down_frame,text="Add",command=self.AddMed,font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=2)
        btnAddMed.grid(row=0,column=0)

        btnUpdateMed=Button(down_frame,text="Update",command=self.UpdateMed,font=("arial",12,"bold"),width=12,bg="dark green",fg="white",pady=2)
        btnUpdateMed.grid(row=1,column=0)

        btnDelMed=Button(down_frame,text="Delete",command=self.DeleteMEd,font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=2)
        btnDelMed.grid(row=2,column=0)

        btnClearMed=Button(down_frame,text="Clear",command=self.ClearMed,font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=2)
        btnClearMed.grid(row=3,column=0)


        #=============================Add Medicine Buttons===================================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)


        #=============================Add Medicine Buttons===================================
        Table_frame=Frame(Framedetails,bd=15,relief=RIDGE)
        Table_frame.place(x=0,y=1,width=1460,height=180)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("Batch No","CmpName","Med Name","Type","Lotno","IssueDate","ExpDate","Uses","Precautions","Price","Prd Quantity"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("Batch No",text="Batch No")
        self.pharmacy_table.heading("CmpName",text="Company Name")
        self.pharmacy_table.heading("Med Name",text="Medicine Name")
        self.pharmacy_table.heading("Type",text="Type")
        self.pharmacy_table.heading("Lotno",text="Lot No")
        self.pharmacy_table.heading("IssueDate",text="Issue Date")
        self.pharmacy_table.heading("ExpDate",text="Exp Date")
        self.pharmacy_table.heading("Uses",text="Use")
        self.pharmacy_table.heading("Precautions",text="Precaution")
        self.pharmacy_table.heading("Price",text="Price")
        self.pharmacy_table.heading("Prd Quantity",text="Quantity")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("Batch No",width=100)
        self.pharmacy_table.column("CmpName",width=100)
        self.pharmacy_table.column("Med Name",width=100)
        self.pharmacy_table.column("Type",width=100)
        self.pharmacy_table.column("Lotno",width=100)
        self.pharmacy_table.column("IssueDate",width=100)
        self.pharmacy_table.column("ExpDate",width=100)
        self.pharmacy_table.column("Uses",width=100)
        self.pharmacy_table.column("Precautions",width=100)
        self.pharmacy_table.column("Price",width=100)
        self.pharmacy_table.column("Prd Quantity",width=100)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)


    #=============================Add Medicine Functionality Deleclaration===================================

    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO pharma(Batch,MedName) VALUES(%s,%s)",(self.refMed_var.get(),self.Addmed_var.get()))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()

        messagebox.showinfo("=Success=","Added Medicine Scuccesfuly")

    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.med_table.delete(*self.med_table.get_children())
            for i in rows:
                self.med_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #=============================Med Get Cursor===================================
    def Medget_cursor(self,event=""):
        cursor_row=self.med_table.focus()
        content=self.med_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.Addmed_var.set(row[1])
        
        
    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.Addmed_var.get()=="":
            messagebox.showerror("!Error!","All feilds are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE pharma set MedName=%s WHERE Batch=%s",(
                                                                             self.Addmed_var.get(),
                                                                             self.refMed_var.get(),
                                                                        ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("=Success=","Medicine has been updated")

    def DeleteMEd(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        sql="delete from pharma where Batch=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()

    def ClearMed(self):
        self.refMed_var.set("")
        self.Addmed_var.set("")
    


    #=============================Main table pharma (2)===================================

    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("!Error!","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO pharma2 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(           self.ref_var.get(),
                                                                                                            self.cmpName_var.get(),
                                                                                                            self.typeMed_var.get(),
                                                                                                            self.medName_var.get(),
                                                                                                            self.lot_var.get(),
                                                                                                            self.issuedate_var.get(),
                                                                                                            self.expdate_var.get(),
                                                                                                            self.uses_var.get(),
                                                                                                            self.sideEffect_var.get(),
                                                                                                            self.warning_var.get(),
                                                                                                            self.price_var.get(),
                                                                                                            self.product_var.get()                                                                                                               
                
                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("=Success=","Data has been inserted")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM pharma2")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,ev=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.price_var.set(row[10]),
        self.product_var.set(row[11])

    
    def Update(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("!Error!","All feilds are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE pharma2 set CmpName=%s,TypeMed=%s,MedName=%s,LotNo=%s,IssueDate=%s,ExpDate=%s,Uses=%s,SideEffects=%s,Precaution=%s,Price=%s,Product=%s WHERE Batch=%s",(
                                                                                                                                                                                                self.cmpName_var.get(),
                                                                                                                                                                                                self.typeMed_var.get(),
                                                                                                                                                                                                self.medName_var.get(),
                                                                                                                                                                                                self.lot_var.get(),
                                                                                                                                                                                                self.issuedate_var.get(),
                                                                                                                                                                                                self.expdate_var.get(),
                                                                                                                                                                                                self.uses_var.get(),
                                                                                                                                                                                                self.sideEffect_var.get(),
                                                                                                                                                                                                self.warning_var.get(),
                                                                                                                                                                                                self.price_var.get(),
                                                                                                                                                                                                self.product_var.get(),
                                                                                                                                                                                                self.ref_var.get()
                                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("=Success=","Medicine has been updated")
    

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        sql="delete from pharma2 where Batch=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("!=Delete=!","Information deleted succesfully")
    

    def reset(self):
        #self.ref_var.set(""),
        self.cmpName_var.set(""),
        #self.typeMed_var.set(""),
        #self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.price_var.set(r""),
        self.product_var.set(r"")

    def iExit(self):
        iExit=messagebox.askyesno("Pharmacy Management System","Do you want to exit ?")
        if iExit>0:
            self.root.destroy()
            return
           
        

    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma2 where "+(self.search_var)+"LIKE"+str(self.searchtxt_var.get())+"%")

        r=my_cursor.fetchall()
        if len(r)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in r:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

























if __name__== "__main__":
    main()
       
