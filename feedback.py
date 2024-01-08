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


class Feedback:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1295x580+230+220")
        self.root.wm_iconbitmap('hotel.ico')


        title=Label(self.root,text="FEEDBACK TIME",font=("times new roman",18,"bold"),bg="black",fg="gold",relief=RIDGE)
        title.place(x=0,y=0,width=1295,height=50)

           #================== LOGO =============================
        img1=Image.open(r"images\logohotel.png")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        self.lblbutton=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        self.lblbutton.place(x=5,y=2,width=100,height=40)

        #bg-img
        self.bg_img=ImageTk.PhotoImage(file=r"images/taj.jpg")
        self.bg_lbl = Label(self.root,image=self.bg_img)
        self.bg_lbl.place(x=0,y=45,relheight=1,relwidth=1)

        main_frame = Frame(self.root,bd=2,bg="black")
        main_frame.place(x=430,y=100,height=400, width=400)

        img=Image.open(r"images/logohotel.png")
        img=img.resize((120,120),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photoimg,bg="black",borderwidth=0)
        lblimg.place(x=570,y=100,height=120,width=120)

        title2=Label(self.root,text="WE WANT YOUR FEEDBACK",font=("times new roman",15,"bold"),bg="black",fg="gold",relief=RIDGE)
        title2.place(x=500,y=220,width=280)

        # img2=Image.open(r"images/star.png")
        # img2=img2.resize((50,50),Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img2)

        # lblimg=Label(image=self.photoimg,bg="black",borderwidth=0)
        # lblimg.place(x=570,y=220,height=50,width=50)




        studentname_lebel = Label(main_frame,text="UserName",font=("time new roman",15,"bold"),bg="black",fg="gold")
        studentname_lebel.place(x=90,y=150)



        self.user_name=StringVar()   
        self.txtuser = ttk.Entry(main_frame,textvariable=self.user_name,width=15,font=("time new roman",15,"bold"))
        self.txtuser.place(x=70,y=180,width=270)


            
        pwd_lebel = Label(main_frame,text="Feedback",font=("time new roman",15,"bold"),bg="black",fg="gold")
        pwd_lebel.place(x=90,y=225)

        
 
        self.user_feedback=StringVar()
        combo_feedback=ttk.Combobox(main_frame,textvariable=self.user_feedback,font=("times new roman",13,"bold"),width=27)
        combo_feedback["values"]=("Give Us Feedback","Good","Average","Poor","Excellent","Extreme")
        combo_feedback.current(0)
        combo_feedback.place(x=70,y=250,width=270)

        feedback_btn=Button(main_frame,text="Send",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="gold",bg="black",activeforeground="white",activebackground="red",command=self.send_feedback)
        feedback_btn.place(x=150,y=300,width=120,height=35) 


    def send_feedback(self):
        if self.user_name.get()=="" or self.user_feedback.get()=="":
            messagebox.showerror("Error","All fields required!",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345678",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into feedback values(%s,%s)",(
                                                                    self.user_name.get(),
                                                                    self.user_feedback.get()
                                                                 ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Thanks for giving your feedback",parent=self.root)


   






if __name__=="__main__":
    root=Tk()
    obj=Feedback(root)
    root.mainloop()