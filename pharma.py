from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox 

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        #=================add medicine=======================================
        self.refmed_var = StringVar()
        self.addmed_var= StringVar()

        #================main variable========================================
        self.ref_var = StringVar()
        self.cmpName_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideEffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.product_var = StringVar()

        lbltitle = Label(self.root,text="PHARAMACY MANAGEMENT SYSTEM", bd=15,relief=RIDGE ,bg='aliceblue', 
                            fg="darkgreen",font=("time new roman",50,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)

        img1 = Image.open("E:\Pharmacy Management System\img\logo.png")
        img1 = img1.resize((130,80),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root,image = self.photoimg1,borderwidth=0)
        b1.place(x=20,y=20)

        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20,)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,bg="aliceblue",text="Medicine Information", fg="darkblue", font=("arial",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

  #======================buttonFrame==========================
        ButtonFrame = Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

  #=======================MainButton===========================
        btnAddData = Button(ButtonFrame,text="Medicine Add", font=("arial",12,"bold"),bg="darkorange", fg="white", padx=20, command= self.add_data)
        btnAddData.grid(row=0,column=0)
        
        btnupdateMed = Button(ButtonFrame,text="UPDATE", font=("arial",13,"bold"),bg="darkorange", fg="white",padx=20, command=self.Update)
        btnupdateMed.grid(row=0,column=1)
    
        btnDeleteMed = Button(ButtonFrame,text="DELETE", font=("arial",13,"bold"),bg="darkorange", fg="white",padx=20)
        btnDeleteMed.grid(row=0,column=2)

        btnResetMed = Button(ButtonFrame,text="RESET", font=("arial",13,"bold"),bg="darkorange", fg="white",padx=20)
        btnResetMed.grid(row=0,column=3)
        
        btnExitMed = Button(ButtonFrame,text="EXIT", font=("arial",13,"bold"),bg="darkorange", fg="white",padx=20)
        btnExitMed.grid(row=0,column=4)
    
        lblSearch = Label(ButtonFrame,text="Search By", font=("arial",17,"bold"),bg="darkorange", fg="white",padx=20)
        lblSearch.grid(row=0,column=5, sticky=W)

#===============comobo box ===================================
        search_combo = ttk.Combobox(ButtonFrame,width=14, font=("arial",17,"bold"),state="readonly",)
        search_combo.grid(row=0, column=6)
        search_combo["values"]=("Ref","Medicine","Lot")
        search_combo.current(0)

        txtSearch = Entry(ButtonFrame, bd=3 , relief= RIDGE, width=14, font=("arial",17,"bold"))
        txtSearch.grid(row=0, column=7)

        SearchBtn = Button(ButtonFrame,  text='SEARCH', width=13, font=("arial",13,"bold"), bg="darkorange", fg="white",padx=15)
        SearchBtn.grid(row=0, column=8)
    
        showAll = Button(ButtonFrame, text='SHOW ALL',  width=13, font=("arial",13,"bold"),bg = "darkorange", fg="white",padx=15)
        showAll.grid(row=0, column=9)


        lblrefno = Label(DataFrameLeft,text="Reference no", font=("arial",12,"bold"), padx=2,pady=6,bg="aliceblue")
        lblrefno.grid(row=0,column=0, sticky=W)

        conn = mysql.connector.connect(host = "localhost", username="root", passwd="Shagun@2005", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row = my_cursor.fetchall()

        ref_combo = ttk.Combobox(DataFrameLeft,width=27, font=("arial",12,"bold"),state="readonly",textvariable=self.ref_var)
        ref_combo["values"]=row
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)

        lblCompany = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Company Name : ", padx=2, pady=6,bg="aliceblue")
        lblCompany.grid(row=1,column=0,sticky=W)
        txtCompany = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.cmpName_var)
        txtCompany.grid(row=1, column=1)

        lblTom = Label(DataFrameLeft,text="Type of Medicine", font=("arial",12,"bold"), padx=2,bg="aliceblue")
        lblTom.grid(row=2,column=0, sticky=W)

        Tom_combo = ttk.Combobox(DataFrameLeft,width=27, font=("arial",12,"bold"),state="readonly",textvariable=self.typeMed_var)
        Tom_combo["values"]=("Tablet","Liquid","Capsules","Topical Medicine","Drops","Inhales","Injection")
        Tom_combo.grid(row=2, column=1)
        Tom_combo.current(0)

        lblMedicineName = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Medicine Name", padx=2, pady=6,bg="aliceblue")
        lblMedicineName.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host = "localhost", username="root", passwd="Shagun@2005", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma")
        row = my_cursor.fetchall()

        comMedicineName = ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",12,"bold"),width=27,textvariable=self.medName_var)
        comMedicineName["value"]=row
        comMedicineName.current(0)
        comMedicineName.grid(row = 3, column=1)
    
        lblLotNo = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Lot No: ", padx=2, pady=6,bg="aliceblue")
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.lot_var)
        txtLotNo.grid(row=4, column=1)

        lblIssueDate = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Issue Date: ", padx=2, pady=6,bg="aliceblue")
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueNo = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.issuedate_var)
        txtIssueNo.grid(row=5, column=1)

        lblExDate = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Exp Date: ", padx=2, pady=6,bg="aliceblue")
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.expdate_var)
        txtExDate.grid(row=6, column=1)
    


        lblUses = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Uses: ", padx=2, pady=6,bg="aliceblue")
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.uses_var)
        txtUses.grid(row=7, column=1)

        lblSdEffect = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Side Effect: ", padx=2, pady=6,bg="aliceblue")
        lblSdEffect.grid(row=8,column=0,sticky=W)
        txtSdEffect = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.sideEffect_var)
        txtSdEffect.grid(row=8, column=1)

        lblPreWarning = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Prec&Warning: ",  padx=15,pady=6,bg="aliceblue")
        lblPreWarning.grid(row=0,column=2,sticky=W)
        txtPreWarning = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.warning_var)
        txtPreWarning.grid(row=0, column=3)
    
        lblDosage = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Dosage: ",  padx=15,pady=6,bg="aliceblue")
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.dosage_var)
        txtDosage.grid(row=1, column=3)

        lblPrice = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Tablets Price: ",  padx=15,pady=6,bg="aliceblue")
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.price_var)
        txtPrice.grid(row=2, column=3)
    
        lblProductQt = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Product QT: ",  padx=15,pady=6,bg="aliceblue")
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt = Entry(DataFrameLeft, bd=2 , relief= RIDGE, width=29, font=("arial",13,"bold"),textvariable=self.product_var)
        txtProductQt.grid(row=3, column=3, sticky=W)

#============================IMAGES IN LEFT SECTION=========================
        lblHome = Label(DataFrameLeft, font= ("arial",12,"bold"), text="Stay Safe Stay Home ",  padx=2,pady=6,bg="aliceblue",fg="Darkblue")
        lblHome.place(x=530,y=145)

        img2 = Image.open("E:\Pharmacy Management System\img\img2.jpg")
        img2 = img2.resize((150,135),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root,image = self.photoimg2,borderwidth=0)
        b1.place(x=775,y=340)

        img3 = Image.open("E:\Pharmacy Management System\img\img3.jfif")
        img3 = img3.resize((150,135),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root,image = self.photoimg3,borderwidth=0)
        b1.place(x=625,y=340)

        img4 = Image.open("E:\Pharmacy Management System\img\img4.jfif")
        img4 = img4.resize((150,135),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root,image = self.photoimg4,borderwidth=0)
        b1.place(x=480,y=340)

#====================DataFrame Right ==============================================

        DataFrameRight = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",bg="aliceblue", fg="darkblue", font=("arial",14,"bold"))
        DataFrameRight.place(x=910,y=5,width=560,height=350)

        img5 = Image.open("E:\Pharmacy Management System\img\img5.jpg")
        img5 = img5.resize((200,95),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root,image = self.photoimg5,borderwidth=0)
        b1.place(x=960,y=160)

        img6 = Image.open("E:\Pharmacy Management System\img\img7.jpg")
        img6 = img6.resize((160,95),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root,image = self.photoimg6,borderwidth=0)
        b1.place(x=1160,y=160)

        img7 = Image.open("E:\Pharmacy Management System\img\img6.jfif")
        img7 = img7.resize((170,135),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(self.root,image = self.photoimg7,borderwidth=0)
        b1.place(x=1320,y=160)


        lblrefno = Label(DataFrameRight, font= ("arial",12,"bold"), text="Reference No : ",  padx=15,pady=6,bg="aliceblue")
        lblrefno.place(x=0,y=100)
        txtrefno = Entry(DataFrameRight,textvariable=self.refmed_var, bd=2 , relief= RIDGE, width=20, font=("arial",13,"bold"))
        txtrefno.place(x=145, y=100)
        lblmedName = Label(DataFrameRight, font= ("arial",12,"bold"), text="Medicine Name : ",  padx=15,pady=6,bg="aliceblue")
        lblmedName.place(x=0, y=130)
        txtmedName = Entry(DataFrameRight,textvariable=self.addmed_var, bd=2 , relief= RIDGE, width=20, font=("arial",13,"bold"))
        txtmedName.place(x=145,y=130)
       

        #======================Side Frame==================================================
        side_frame = Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=40,y=170,width=290,height=140)

        sc_x = ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y = ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table = ttk.Treeview(side_frame, column= ("ref","medname"),xscrollcommand= sc_x.set, yscrollcommand=sc_y.set) 

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)    

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name") 

        self.medicine_table["show"] ="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)   

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        #=============Medicine Add Buttons====================================================
        down_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="White")
        down_frame.place(x=360, y=150, width=135, height=160)

        btnAddmed = Button(down_frame,text="ADD", font=("arial",12,"bold"),bg="#40E0D0",width=12, fg="white", pady=4, command = self.AddMed)
        btnAddmed.grid(row=0,column=0)

        btnupdtmed = Button(down_frame,text="UPDATE", font=("arial",12,"bold"),bg="#40E0D0",width=12, fg="white", pady=4,command = self.UpdateMed)
        btnupdtmed.grid(row=1,column=0)

        btndelmed = Button(down_frame,text="DELETE", font=("arial",12,"bold"),bg="#40E0D0",width=12, fg="white", pady=4, command=self.DeleteMed)
        btndelmed.grid(row=2,column=0)

        btnclrmed = Button(down_frame,text="CLEAR", font=("arial",12,"bold"),bg="#40E0D0",width=12, fg="white", pady=4, command = self.ClearMed)
        btnclrmed.grid(row=3,column=0)

#================================frame details=====================================================================================
        Framedetails = Frame(self.root,bd=15,relief=RIDGE,)
        Framedetails.place(x=0, y=580 , width=1530, height=210)

#-================================Main Table and Scroll Bar========================================================================
        Table_frame = Frame(Framedetails, bd=15, relief=RIDGE, bg="#7fffd4")
        Table_frame.place(x=0, y=1, width=1500, height=180)

        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table = ttk.Treeview(Table_frame, column=("reg","companyname","type","tabletname","lotno",
                           "issuedate","expdate","uses","sideeffect","warning", "dosage", "price", "productqt" ), 
                           xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("reg", text="Reference No")
        self.pharmacy_table.heading("companyname", text="Company Name")
        self.pharmacy_table.heading("type", text="Type of Medicine")
        self.pharmacy_table.heading("tabletname", text="Tablet Name")
        self.pharmacy_table.heading("lotno", text="Lot No")
        self.pharmacy_table.heading("issuedate", text="Issue Date")
        self.pharmacy_table.heading("expdate", text="Exp Date")
        self.pharmacy_table.heading("uses", text="uses")
        self.pharmacy_table.heading("sideeffect", text="Side Effect")
        self.pharmacy_table.heading("warning", text="Prec&Warning")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("productqt", text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg", width=130)
        self.pharmacy_table.column("companyname", width=130)
        self.pharmacy_table.column("type", width=130)
        self.pharmacy_table.column("tabletname", width=130)
        self.pharmacy_table.column("lotno", width=130)
        self.pharmacy_table.column("issuedate", width=130)
        self.pharmacy_table.column("expdate", width=130)
        self.pharmacy_table.column("uses", width=130)
        self.pharmacy_table.column("sideeffect", width=130)
        self.pharmacy_table.column("warning", width=130)
        self.pharmacy_table.column("dosage", width=130)
        self.pharmacy_table.column("price", width=130)
        self.pharmacy_table.column("productqt", width=130)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)


###===================Add Medicine functionality Declaration==========================================
    def AddMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", passwd="Shagun@2005", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s, %s)",(
                                                                 self.refmed_var.get(),
                                                                 self.addmed_var.get(),
                                                                 ))

        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine Added")

    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", passwd="Shagun@2005", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in row:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
#####=============medgetcursor===========================
    def Medget_cursor(self,event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row  = content["values"]  
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])

#####==============medupdate==============================
    def UpdateMed(self):
        
        if self.refmed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All the fields are Required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", passwd="Shagun@2005", database="pharmacy")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                self.addmed_var.get(),
                self.refmed_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success", "Medicine has been Updated")

#####==============medupdate==============================
    def DeleteMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", passwd="Shagun@2005", database="pharmacy")
        my_cursor = conn.cursor()

        sql = "delete from pharma where Ref=%s"
        val = (self.refmed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success", "Medicine has been deleted")

#######===========ClearMedicine==================================
    def ClearMed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")

#####============Main Table========================================
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
                
            conn = mysql.connector.connect(host="localhost", username="root", passwd="Shagun@2005", database="pharmacy")
            my_cursor = conn.cursor()

            my_cursor.execute("insert into pharmadetail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.ref_var.get(),
                                                                                        self.cmpName_var.get(),
                                                                                        self.typeMed_var.get(),
                                                                                        self.medName_var.get(),
                                                                                        self.lot_var.get(),
                                                                                        self.issuedate_var.get(),
                                                                                        self.expdate_var.get(),
                                                                                        self.uses_var.get(),
                                                                                        self.sideEffect_var.get(),
                                                                                        self.warning_var.get(),
                                                                                        self.dosage_var.get(),
                                                                                        self.price_var.get(),
                                                                                        self.product_var.get()
                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Medicine Data has been Inserted")

    
    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", passwd="Shagun@2005", database="pharmacy")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from pharmadetail")
            row = my_cursor.fetchall()
            if len(row)!=0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in row:
                    self.pharmacy_table.insert("",END, values=i)
                conn.commit()
            conn.close()


#####=============getcursor===========================
    def get_cursor(self,event=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row  = content["values"]  

        self.ref_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])
        self.issuedate_var.set(row[5])
        self.expdate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideEffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.product_var.set(row[12])

#####==============update==============================
    def Update(self):
        
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All the fields are Required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", passwd="Shagun@2005", database="pharmacy")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharmadetail set CmpName=%s, TypeMed=%s, Medname=%s, LotNo=%s, Issuedate=%s, Expdate=%s, Uses=%s, Sideeffect=%s, warning=%s,dosage=%s,Price=%s,product=%s, where Ref_no=%s",(
                                                                                                                                
                                                                                                                                                self.cmpName_var.get(),
                                                                                                                                                self.typeMed_var.get(),
                                                                                                                                                self.medName_var.get(),
                                                                                                                                                self.lot_var.get(),
                                                                                                                                                self.issuedate_var.get(),
                                                                                                                                                self.expdate_var.get(),
                                                                                                                                                self.uses_var.get(),
                                                                                                                                                self.sideEffect_var.get(),
                                                                                                                                                self.warning_var.get(),
                                                                                                                                                self.dosage_var.get(),
                                                                                                                                                self.price_var.get(),
                                                                                                                                                self.product_var.get(),
                                                                                                                                                self.ref_var.get()                                           
                                                                                                                                            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("UPDATE", "Record has been Updated Successfully")
      


if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
