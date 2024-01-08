import random
from tkinter import *
import tkinter 
from PIL import Image,ImageTk
from tkinter  import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strftime,strptime


class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1295x580+230+220")
        self.root.wm_iconbitmap('hotel.ico')


        #=========== Variables =================

        self.floor=StringVar()
        self.roomno=StringVar()
        self.roomtype=StringVar()



        
        title=Label(self.root,text="ROOM DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",relief=RIDGE)
        title.place(x=0,y=0,width=1295,height=50)

           #================== LOGO =============================
        img1=Image.open(r"images\logohotel.png")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        self.lblbutton=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        self.lblbutton.place(x=5,y=2,width=100,height=40)

        lblfraneleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="NEW ROOM ADD",padx=2,font=("times new roman",12,"bold"))
        lblfraneleft.place(x=5,y=50,width=540,height=350)

        
         #floor
        lbl_floor=Label(lblfraneleft,text=" Floor :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        efloor=ttk.Entry(lblfraneleft,textvariable=self.floor,width=22,font=("times new roman",13,"bold"))
        efloor.grid(row=0,column=1,sticky=W)


          
        #room-no
        lbl_roomno=Label(lblfraneleft,text=" Room No :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W)

        eroomno=ttk.Entry(lblfraneleft,textvariable=self.roomno,width=22,font=("times new roman",13,"bold"))
        eroomno.grid(row=1,column=1,sticky=W)

          
        #room-type
        lbl_roomtype=Label(lblfraneleft,text=" Room Type :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)

        combo_room=ttk.Combobox(lblfraneleft,textvariable=self.roomtype,font=("times new roman",12,"bold"),width=22)
        combo_room["values"]=("Select","Single","Double","laxary")
        combo_room.current(0)
        combo_room.grid(row=2,column=1)         


        btn_frame=Frame(lblfraneleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=35)

        btn_Add=Button(btn_frame,text="Add",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.add_data)
        btn_Add.grid(row=0,column=0,padx=1)

        btn_Add=Button(btn_frame,text="Update",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.update_data)
        btn_Add.grid(row=0,column=1,padx=1)

        btn_Add=Button(btn_frame,text="Delete",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.idelete)
        btn_Add.grid(row=0,column=2,padx=1)
       
        btn_Add=Button(btn_frame,text="Reset",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10,command=self.reset)
        btn_Add.grid(row=0,column=3,padx=1)


        lblframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Rooms",padx=2,font=("times new roman",12,"bold"))
        lblframeright.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(lblframeright,orient=HORIZONTAL)
        
        scroll_y=ttk.Scrollbar(lblframeright,orient=VERTICAL)

        self.room_table=ttk.Treeview(lblframeright,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room-No")
        self.room_table.heading("roomtype",text="Room-Type")
        self.room_table["show"]="headings"
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.roomtype.get()=="" or self.roomno.get()=="" or self.floor.get()=="":
            messagebox.showerror("Error","All Field Requires !")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into addroom values(%s,%s,%s)",(
                                                                           self.floor.get(),
                                                                           self.roomno.get(),
                                                                           self.roomtype.get()
                                                                                          
                                                                                          
                                                                                                                                                                       
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Error",f"Something Went Wrong :{str(es)}",parent=self.root)

    
    def update_data(self):
        if self.roomtype.get()=="" or self.roomno.get()=="" or self.floor.get()=="":
            messagebox.showerror("Error","All Field Requires !")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("update addroom set floor=%s,roomtype=%s where roomno=%s",(
                                                                           self.floor.get(),
                                                                          
                                                                           self.roomtype.get(),
                                                                           self.roomno.get()
                                                                                          
                                                                                          
                                                                                                                                                                       
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Detail Update successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Error",f"Something Went Wrong :{str(es)}",parent=self.root)

    

    
    def idelete(self):
        idel=messagebox.askyesno("Hotel Management System","Do you want to delete this room ?",parent=self.root)
        if idel>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
               my_cursor=conn.cursor()
               query="delete from addroom where roomno=%s"
               val=(self.roomno.get(),)
               my_cursor.execute(query,val)
        else:
            if not idel:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()

    
    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
          my_cursor=conn.cursor()
          my_cursor.execute("select *from addroom")
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
        self.floor.set(row[0]),
        self.roomno.set(row[1]),
        self.roomtype.set(row[2])

    def reset(self):
        self.floor.set(""),
        self.roomno.set(""),
        self.roomtype.set("Select")


    

        

             



if __name__=="__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop()