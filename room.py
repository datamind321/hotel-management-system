import os
import random
from tkinter import *
import tkinter
from tkinter import filedialog 
from PIL import Image,ImageTk
from tkinter  import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strftime,strptime


class Room:
    def __init__(self,root):
        self.root=root 
        self.root.title("Library Management System")
        self.root.geometry("1295x580+230+220")
        self.root.wm_iconbitmap('hotel.ico')

        #============================= Variables ==================
        
        self.var_ref = StringVar()
        self.checkin=StringVar()
        self.checkout=StringVar()
        self.roomtype=StringVar()
        self.avlroom=StringVar()
        self.meal=StringVar()
        self.noofday=StringVar()
        self.paidtax=StringVar()
        self.subtotal=StringVar()
        self.total=StringVar()

        title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",relief=RIDGE)
        title.place(x=0,y=0,width=1295,height=50)

           #================== LOGO =============================
        img1=Image.open(r"images\logohotel.png")
        img1=img1.resize((100,40))
        self.photoimg1=ImageTk.PhotoImage(img1)
        self.lblbutton=Button(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        self.lblbutton.place(x=5,y=2,width=100,height=40) 

        lblfraneleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",12,"bold"))
        lblfraneleft.place(x=5,y=50,width=425,height=490)

         #customer-contact
        lbl_cust_contact=Label(lblfraneleft,text=" Customer Ref ID :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(lblfraneleft,textvariable=self.var_ref,width=22,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        btn_fetch=Button(lblfraneleft,text="Fetch Data",command=self.fetch_details,font=("times new roman",8,"bold"),bg="black",fg="gold",width=8)
        btn_fetch.place(x=347,y=4)

        #check-in-data
        lbl_cust_checkin=Label(lblfraneleft,text=" Check_In Date :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_checkin.grid(row=1,column=0,sticky=W)

        entry_checkin=ttk.Entry(lblfraneleft,textvariable=self.checkin,width=29,font=("times new roman",13,"bold"))
        entry_checkin.grid(row=1,column=1)


        
        #check-out-data
        lbl_cust_checkout=Label(lblfraneleft,text=" Check_Out Date :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_checkout.grid(row=2,column=0,sticky=W)

        entry_checkout=ttk.Entry(lblfraneleft,width=29,textvariable=self.checkout,font=("times new roman",13,"bold"))
        entry_checkout.grid(row=2,column=1)


        #Room-type
        lbl_cust_room=Label(lblfraneleft,text=" Room Type :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_room.grid(row=3,column=0,sticky=W)


        
        conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select  roomtype from addroom")
        ide=my_cursor.fetchall()

        combo_room=ttk.Combobox(lblfraneleft,textvariable=self.roomtype,font=("times new roman",13,"bold"),width=27)
        combo_room["values"]=ide
        combo_room.current(0)
        combo_room.grid(row=3,column=1)

            
        #available-room
        lbl_cust_avroom=Label(lblfraneleft,text=" Available Room :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_avroom.grid(row=4,column=0,sticky=W)
        

        conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select  roomno from addroom")
        rows=my_cursor.fetchall()
        combo_aroom=ttk.Combobox(lblfraneleft,textvariable=self.avlroom,font=("times new roman",13,"bold"),width=27)
        combo_aroom["values"]=rows
        combo_aroom.current(0)
        combo_aroom.grid(row=4,column=1)

        # entry_avroom=ttk.Entry(lblfraneleft,textvariable=self.avlroom,width=29,font=("times new roman",13,"bold"))
        # entry_avroom.grid(row=4,column=1)

            
        #meal
        lbl_cust_meal=Label(lblfraneleft,text=" Meal :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_meal.grid(row=5,column=0,sticky=W)


        
        
        combo_meal=ttk.Combobox(lblfraneleft,textvariable=self.meal,font=("times new roman",13,"bold"),width=27)
        combo_meal["values"]=("Select","BreakFast","Launch","Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1,padx=2)

    

            
        #no-of-days
        lbl_cust_days=Label(lblfraneleft,text=" No Of Days :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_days.grid(row=6,column=0,sticky=W)

        entry_days=ttk.Entry(lblfraneleft,width=29,textvariable=self.noofday,font=("times new roman",13,"bold"))
        entry_days.grid(row=6,column=1)

            
        #paid-tax
        lbl_cust_tax=Label(lblfraneleft,text=" Paid Tax :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_tax.grid(row=7,column=0,sticky=W)

        entry_tax=ttk.Entry(lblfraneleft,textvariable=self.paidtax,width=29,font=("times new roman",13,"bold"))
        entry_tax.grid(row=7,column=1)

            
        #sub-total
        lbl_cust_subtotal=Label(lblfraneleft,text="Sub Total :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_subtotal.grid(row=8,column=0,sticky=W)

        entry_subtotal=ttk.Entry(lblfraneleft,textvariable=self.subtotal,width=29,font=("times new roman",13,"bold"))
        entry_subtotal.grid(row=8,column=1)


            
        #total-cost
        lbl_cust_total=Label(lblfraneleft,text="Total Cost :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_total.grid(row=9,column=0,sticky=W)

        entry_total=ttk.Entry(lblfraneleft,textvariable=self.total,width=29,font=("times new roman",13,"bold"))
        entry_total.grid(row=9,column=1)











        btn_bill=Button(lblfraneleft,text="Bill",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.total_bill)
        btn_bill.grid(row=10,column=0,padx=1,sticky=W)



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

        #============================ Right Image =========================

        img2=Image.open(r"images\bed.jpg")
        img2=img2.resize((520,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        self.lblbutton=Button(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        self.lblbutton.place(x=760,y=55,width=520,height=200)



        #======================= tableframe ======================
        lblframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",12,"bold"))
        lblframeright.place(x=435,y=280,width=860,height=260)

        lblsearchbar=Label(lblframeright,text="Search By :",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchbar.grid(row=0,column=0,sticky=W)
        

        self.search_bar=StringVar()
        combo_search=ttk.Combobox(lblframeright,textvariable=self.search_bar,font=("times new roman",12,"bold"),width=24)
        combo_search["values"]=("Select","ref","avlroom")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        entry_search=ttk.Entry(lblframeright,textvariable=self.txt_search,width=24,font=("times new roman",12,"bold"))
        entry_search.grid(row=0,column=2,padx=2) 

        btn_search=Button(lblframeright,text="Search",font=("times new roman",11,"bold"),bg="black",fg="gold",width=20,command=self.search)
        btn_search.grid(row=0,column=3,padx=2)

        btn_showall=Button(lblframeright,text="Show All",font=("times new roman",11,"bold"),bg="black",fg="gold",width=20,command=self.fetch_data)
        btn_showall.grid(row=0,column=4,padx=2)


        #========================= Customer Detail====================
        detect_frame=Frame(lblframeright,bd=2,relief=RIDGE)
        detect_frame.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(detect_frame,orient=HORIZONTAL)
        
        scroll_y=ttk.Scrollbar(detect_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(detect_frame,columns=("Ref Id","checkin","checkout","roomtype","avroom","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Ref Id",text="Ref Id")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout",text="Check-Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("avroom",text="Available Room")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No Of Days")

       
        self.room_table["show"]="headings"
     

        self.room_table.column("Ref Id",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("avroom",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
      
       

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def fetch_details(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Error","Please Enter Customer Reference Id",parent=self.root)
        else:
              conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
              my_cursor=conn.cursor()
              query="select Name from customer where ref=%s"
              val=(self.var_ref.get(),)
              my_cursor.execute(query,val)
              row=my_cursor.fetchone()
              if row==None:
                messagebox.showerror("Error","This reference Not Found",parent=self.root)
              else:
                conn.commit()
                conn.close()

                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showdataframe,text="Name :",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)


                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                my_cursor=conn.cursor()
                query="select gender from customer where ref=%s"
                val=(self.var_ref.get(),)
                my_cursor.execute(query,val)
                row=my_cursor.fetchone()

                lblName=Label(showdataframe,text="Gender :",font=("arial",12,"bold"))
                lblName.place(x=0,y=30)

                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=30)

                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                my_cursor=conn.cursor()
                query="select email from customer where ref=%s"
                val=(self.var_ref.get(),)
                my_cursor.execute(query,val)
                row=my_cursor.fetchone()

                lblName=Label(showdataframe,text="Email :",font=("arial",12,"bold"))
                lblName.place(x=0,y=60)

                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=60)

                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                my_cursor=conn.cursor()
                query="select nation from customer where ref=%s"
                val=(self.var_ref.get(),)
                my_cursor.execute(query,val)
                row=my_cursor.fetchone()

                lblName=Label(showdataframe,text="Nationality:",font=("arial",12,"bold"))
                lblName.place(x=0,y=90)

                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90)

                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                my_cursor=conn.cursor()
                query="select address from customer where ref=%s"
                val=(self.var_ref.get(),)
                my_cursor.execute(query,val)
                row=my_cursor.fetchone()

                lblName=Label(showdataframe,text="Address:",font=("arial",12,"bold"))
                lblName.place(x=0,y=120)

                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)


    def total_bill(self):
        inDate=self.checkin.get()
        outDate=self.checkout.get()
        inDate=datetime.strptime(inDate, "%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.noofday.set(abs(outDate-inDate).days)
        if(self.meal.get()=="BreakFast" and self.roomtype.get()=="Single"):
            q1=float(200)
            q2=float(500)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)
        elif(self.meal.get()=="BreakFast" and self.roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)
        elif(self.meal.get()=="BreakFast" and self.roomtype.get()=="laxary"):
            q1=float(400)
            q2=float(1000)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)


      
        elif(self.meal.get()=="Dinner" and self.roomtype.get()=="Single"):
            q1=float(500)
            q2=float(500)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)
        elif(self.meal.get()=="Dinner" and self.roomtype.get()=="Double"):
            q1=float(500)
            q2=float(700)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)
        elif(self.meal.get()=="Dinner" and self.roomtype.get()=="laxary"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)
        elif(self.meal.get()=="Launch" and self.roomtype.get()=="Single"):
            q1=float(500)
            q2=float(500)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)
        elif(self.meal.get()=="Launch" and self.roomtype.get()=="Double"):
            q1=float(500)
            q2=float(700)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)
        elif(self.meal.get()=="Launch" and self.roomtype.get()=="laxary"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.noofday.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paidtax.set(Tax)
            self.subtotal.set(ST)
            self.total.set(TT)
        




        

    
    def add_data(self):
        if self.var_ref.get()=="" or self.checkin.get()=="":
            messagebox.showerror("Error","All Field Requires !",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                          self.var_ref.get(),
                                                                                          self.checkin.get(),
                                                                                          self.checkout.get(),
                                                                                          self.roomtype.get(),
                                                                                          self.avlroom.get(),
                                                                                          self.meal.get(),
                                                                                          self.noofday.get()
                                                                                          
                                                                                                                                                                       
                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Error",f"Something Went Wrong :(str(es))",parent=self.root) 

         
    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
          my_cursor=conn.cursor()
          my_cursor.execute("select *from room")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
          conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        self.var_ref.set(row[0]),
        self.checkin.set(row[1]),
        self.checkout.set(row[2]),
        self.roomtype.set(row[3]),
        self.avlroom.set(row[4]),
        self.meal.set(row[5]),
        self.noofday.set(row[6])

    def update(self):
            if self.var_ref.get()=="" or self.checkin.get()=="":
                messagebox.showerror("Error","All Field Requires !",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update room set ref=%s,checkin=%s,checkout=%s,roomtype=%s,meal=%s,noofdays=%s where avlroom=%s",(
                                                                                                                                             self.var_ref.get(),
                                                                                          
                                                                                                                                             self.checkin.get(),
                                                                                          
                                                                                                                                             self.checkout.get(),
                                                                                                                                             self.roomtype.get(),
                                                                                         
                                                                                          
                                                                                                                                             self.meal.get(),
                                                                                          
                                                                                                                                             self.noofday.get(),
                                                                                                                                             self.avlroom.get()
                                                                                                                                                                                  
                                                                                                                                            ))
                                                                                                                                                                                                                                                                            
                                                                                                                                                                                  
                                                                                                                                             
                                                                                                                                                                                                                                                      
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Data Updated Successfully",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Error",f"Something Went Wrong : (str(es))",parent=self.root) 

    def idelete(self):
        idel=messagebox.askyesno("Hotel Management System","Do you want to delete this room ?",parent=self.root)
        if idel>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
               my_cursor=conn.cursor()
               query="delete from room where avlroom=%s"
               val=(self.avlroom.get(),)
               my_cursor.execute(query,val)
        else:
            if not idel:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(""),
        self.checkin.set(""),
        self.checkout.set(""),
        self.roomtype.set("Select"),
        self.avlroom.set(""),
        self.meal.set(""),
        self.noofday.set(""),
        self.paidtax.set(""),
        self.subtotal.set(""),
        self.total.set("")

    def search(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from room where "+str(self.search_bar.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
           conn.close()

    



if __name__=="__main__":
    root=Tk()
    obj=Room(root)
    root.mainloop()