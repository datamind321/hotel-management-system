import random
from tkinter import *
import tkinter 
from PIL import Image,ImageTk
from tkinter  import ttk
import mysql.connector
from tkinter import messagebox

class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x580+230+220")
        self.root.wm_iconbitmap('hotel.ico')

        
        title=Label(self.root,text="ADD CUSTOMER DETAIL",font=("times new roman",18,"bold"),bg="black",fg="gold",relief=RIDGE)
        title.place(x=0,y=0,width=1295,height=50)

        
        #================== LOGO =============================
        img1=Image.open(r"images\logohotel.png")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        self.lblbutton=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        self.lblbutton.place(x=5,y=2,width=100,height=40)

        lblfraneleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        lblfraneleft.place(x=5,y=50,width=425,height=490)


        #================================== Variables ======================

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_mname=StringVar()
        self.var_gender=StringVar()
        self.pc=StringVar()
        self.mobile=StringVar()
        self.email=StringVar()
        self.nation=StringVar()
        self.idp=StringVar()
        self.idn=StringVar()
        self.add=StringVar()
        



        
        #================== Levels & Entry =============================

        #customer-ref
        lbl_cust_ref=Label(lblfraneleft,text="Customer Ref :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(lblfraneleft,textvariable=self.var_ref,width=29,font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)


        #customer-name
        lbl_cust_name=Label(lblfraneleft,text="Customer Name :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(lblfraneleft,textvariable=self.var_name,width=29,font=("times new roman",13,"bold"))
        entry_name.grid(row=1,column=1) 

        #mother-name
        lbl_cust_mname=Label(lblfraneleft,text="Father Name :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_mname.grid(row=2,column=0,sticky=W)

        entry_mname=ttk.Entry(lblfraneleft,textvariable=self.var_mname,width=29,font=("times new roman",13,"bold"))
        entry_mname.grid(row=2,column=1) 

        #gender
        lbl_cust_gen=Label(lblfraneleft,text="Gender :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_gen.grid(row=3,column=0,sticky=W)

        combo_gen=ttk.Combobox(lblfraneleft,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=27)
        combo_gen["values"]=("Select Gender","Male","Female","Other")
        combo_gen.current(0)
        combo_gen.grid(row=3,column=1)




        #post-code
        lbl_cust_pc=Label(lblfraneleft,text="PostCode :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_pc.grid(row=4,column=0,sticky=W)

        entry_pc=ttk.Entry(lblfraneleft,textvariable=self.pc,width=29,font=("times new roman",13,"bold"))
        entry_pc.grid(row=4,column=1) 


        #mobile-no 
        lbl_cust_mb=Label(lblfraneleft,text="Mobile No :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_mb.grid(row=5,column=0,sticky=W)

        entry_mb=ttk.Entry(lblfraneleft,textvariable=self.mobile,width=29,font=("times new roman",13,"bold"))
        entry_mb.grid(row=5,column=1) 
        

        #email    
        lbl_cust_em=Label(lblfraneleft,text="Email :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_em.grid(row=6,column=0,sticky=W)

        entry_em=ttk.Entry(lblfraneleft,width=29,textvariable=self.email,font=("times new roman",13,"bold"))
        entry_em.grid(row=6,column=1)


        #nationality    
        lbl_cust_nat=Label(lblfraneleft,text="Nationality :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_nat.grid(row=7,column=0,sticky=W)

        combo_nat=ttk.Combobox(lblfraneleft,textvariable=self.nation,font=("times new roman",13,"bold"),width=27)
        combo_nat["values"]=("Select Nationality","Indian","American","Britist")
        combo_nat.current(0)
        combo_nat.grid(row=7,column=1)
        

        #id-proof
        lbl_cust_id=Label(lblfraneleft,text="ID Proof :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_id.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(lblfraneleft,textvariable=self.idp,font=("times new roman",13,"bold"),width=27)
        combo_id["values"]=("Select ID","Voter Id","Passport","Driving License","AAdhar Card","Pan Card")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)
        




        #id-number    
        lbl_cust_idn=Label(lblfraneleft,text="ID Number :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_idn.grid(row=9,column=0,sticky=W)

        entry_idn=ttk.Entry(lblfraneleft,textvariable=self.idn,width=29,font=("times new roman",13,"bold"))
        entry_idn.grid(row=9,column=1) 


        #Address     
        lbl_cust_add=Label(lblfraneleft,text="Address :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_add.grid(row=10,column=0,sticky=W)

        entry_add=ttk.Entry(lblfraneleft,textvariable=self.add,width=29,font=("times new roman",13,"bold"))
        entry_add.grid(row=10,column=1) 

        #======================= Buttons ======================

        btn_frame=Frame(lblfraneleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=35)

        btn_Add=Button(btn_frame,text="Add",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.add_data)
        btn_Add.grid(row=0,column=0,padx=1)

        btn_Add=Button(btn_frame,text="Update",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.update)
        btn_Add.grid(row=0,column=1,padx=1)

        btn_Add=Button(btn_frame,text="Delete",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.idelete)
        btn_Add.grid(row=0,column=2,padx=1)
       
        btn_Add=Button(btn_frame,text="Reset",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.reset)
        btn_Add.grid(row=0,column=3,padx=1)


          #======================= tableframe ======================
        lblframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",12,"bold"))
        lblframeright.place(x=435,y=50,width=860,height=490)

        lblsearchbar=Label(lblframeright,text="Search By :",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchbar.grid(row=0,column=0,sticky=W)
        

        self.search_bar=StringVar()
        combo_search=ttk.Combobox(lblframeright,textvariable=self.search_bar,font=("times new roman",12,"bold"),width=24)
        combo_search["values"]=("Select","Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        entry_search=ttk.Entry(lblframeright,textvariable=self.txt_search,width=24,font=("times new roman",12,"bold"))
        entry_search.grid(row=0,column=2,padx=2) 

        btn_search=Button(lblframeright,text="Search",font=("times new roman",11,"bold"),bg="black",fg="gold",width=20,command=self.search)
        btn_search.grid(row=0,column=3,padx=2)

        btn_showall=Button(lblframeright,text="Show All",font=("times new roman",11,"bold"),bg="black",fg="gold",width=20,command=self.fetch_data)
        btn_showall.grid(row=0,column=4,padx=2)

        #show data table 

        detect_frame=Frame(lblframeright,bd=2,relief=RIDGE)
        detect_frame.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(detect_frame,orient=HORIZONTAL)
        
        scroll_y=ttk.Scrollbar(detect_frame,orient=VERTICAL)

        self.customer_details=ttk.Treeview(detect_frame,columns=("ref","name","mname","gender","postcode","mobile","email","nation","idp","idn","add"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.customer_details.xview)
        scroll_y.config(command=self.customer_details.yview)

        self.customer_details.heading("ref",text="CustomerRef")
        self.customer_details.heading("name",text="Name")
        self.customer_details.heading("mname",text="Mother")
        self.customer_details.heading("gender",text="Gender")
        self.customer_details.heading("postcode",text="PostCode")
        self.customer_details.heading("mobile",text="Mobile")
        self.customer_details.heading("email",text="Email")
        self.customer_details.heading("nation",text="Nationality")
        self.customer_details.heading("idp",text="ID Proof")
        self.customer_details.heading("idn",text="ID Number")
        self.customer_details.heading("add",text="Address")
        self.customer_details["show"]="headings"
     

        self.customer_details.column("ref",width=100)
        self.customer_details.column("name",width=100)
        self.customer_details.column("mname",width=100)
        self.customer_details.column("gender",width=100)
        self.customer_details.column("postcode",width=100)
        self.customer_details.column("mobile",width=100)
        self.customer_details.column("email",width=100)
        self.customer_details.column("nation",width=100)
        self.customer_details.column("idp",width=100)
        self.customer_details.column("idn",width=100)
        self.customer_details.column("add",width=100)

        self.customer_details.pack(fill=BOTH,expand=1)
        self.customer_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.mobile.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","All Field Requires !",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                          self.var_ref.get(),
                                                                                          self.var_name.get(),
                                                                                          self.var_mname.get(),
                                                                                          self.var_gender.get(),
                                                                                          self.pc.get(),
                                                                                          self.mobile.get(),
                                                                                          
                                                                                          self.email.get(),
                                                                                          self.nation.get(),
                                                                                          self.idp.get(),
                                                                                          self.idn.get(),
                                                                                          self.add.get()                                                                             
                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Error",f"Something Went Wrong :(str(es))",parent=self.root) 

    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
          my_cursor=conn.cursor()
          my_cursor.execute("select *from customer")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
            self.customer_details.delete(*self.customer_details.get_children())
            for i in rows:
                self.customer_details.insert("",END,values=i)
            conn.commit()
          conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.customer_details.focus()
        content=self.customer_details.item(cursor_row)
        row=content["values"]
        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_mname.set(row[2]),
        self.var_gender.set(row[3]),
        self.pc.set(row[4]),
        self.mobile.set(row[5]),
        self.email.set(row[6]),
        self.nation.set(row[7]),
        self.idp.set(row[8]),
        self.idn.set(row[9]),
        self.add.set(row[10])

    
    def update(self):
            if self.mobile.get()=="" or self.var_name.get()=="":
                messagebox.showerror("Error","All Field Requires !",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update customer set Name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nation=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(
                                                                                                                                                                                   self.var_name.get(),
                                                                                                                                                                                   self.var_mname.get(),
                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                   self.pc.get(),
                                                                                                                                                                                   self.mobile.get(),
                                                                                                                                                                                   self.email.get(),
                                                                                                                                                                                   self.nation.get(),
                                                                                                                                                                                   self.idp.get(),
                                                                                                                                                                                   self.idn.get(),
                                                                                                                                                                                   self.add.get(), 
                                                                                                                                                                                   self.var_ref.get()
                                                                                                                                                                                ))
                                                                                                                                                                                                                                                                            
                                                                                                                                                                                  
                                                                                                                                             
                                                                                                                                                                                                                                                      
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Data Updated Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Error",f"Something Went Wrong : (str(es))",parent=self.root) 

            


    def idelete(self):
        idel=messagebox.askyesno("Hotel Management System","Do you want to delete this customer ?",parent=self.root)
        if idel>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
               my_cursor=conn.cursor()
               query="delete from customer where ref=%s"
               val=(self.var_ref.get(),)
               my_cursor.execute(query,val)
        else:
            if not idel:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_name.set(""),
        self.var_mname.set(""),
        self.var_gender.set("Select"),
        self.pc.set(""),
        self.mobile.set(""),
        self.email.set(""),
        self.nation.set("Select"),
        self.idp.set("Select"),
        self.idn.set(""),
        self.add.set("")
        

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from customer where "+str(self.search_bar.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
            self.customer_details.delete(*self.customer_details.get_children())
            for i in rows:
                self.customer_details.insert("",END,values=i)
            conn.commit()
           conn.close()





            
        


            


    


        
 

















if __name__=="__main__":
    root=Tk()
    obj=Customer(root)
    root.mainloop()