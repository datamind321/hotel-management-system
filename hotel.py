from datetime import date
import os
from time import strftime
from tkinter import *
import tkinter
from tkinter import filedialog 
from PIL import Image,ImageTk
from tkinter  import ttk
from customer import Customer
from room import Room
from details import Details
from feedback import Feedback



class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        self.root.wm_iconbitmap('hotel.ico')  

            #======================== first image top ===================================

        img=Image.open(r"images\hotel1.png")
        img=img.resize((1550,140),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        self.lblbutton=Label(self.root,image=self.photoimg,bd=4,relief=RIDGE)
        self.lblbutton.place(x=0,y=0,width=1550,height=140)


        #================== LOGO =============================
        img1=Image.open(r"images\logohotel.png")
        img1=img1.resize((230,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        self.lblbuttonlogo=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        self.lblbuttonlogo.place(x=0,y=0,width=230,height=140)

        title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",relief=RIDGE)
        title.place(x=0,y=140,width=1550,height=50)

        def time():
          string=strftime("%I:%M:%S %p")
          lbl.config(text=string)
          lbl.after(1000,time)
          

        lbl=Label(title,font=("time new roman",12,"bold"),bg="black",fg="gold")
        lbl.place(x=50,y=0,width=110,height=50)
        time()

       

            #======================== Main frame ===================================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        #======================== MENU ===================================

        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

            #======================== Button Frame ===================================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTUMER",font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2",command=self.cus_detail)
        cust_btn.grid(row=0,column=0)

        cust_btn=Button(btn_frame,text="ROOM",font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2",command=self.room_detail)
        cust_btn.grid(row=1,column=0,pady=1)


        cust_btn=Button(btn_frame,text="DETAILS",font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2",command=self.detail)
        cust_btn.grid(row=2,column=0,pady=1)


        cust_btn=Button(btn_frame,text="FEEDBACK",font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2",command=self.feed)
        cust_btn.grid(row=3,column=0,pady=1)

        cust_btn=Button(btn_frame,text="LOG OUT",font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,width=22,cursor="hand2",command=self.logout)
        cust_btn.grid(row=4,column=0,pady=1)


        img2=Image.open(r"images\slide3.jpg")
        img2=img2.resize((1310,590),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        self.lblbutton2=Label(main_frame,image=self.photoimg2,bd=4,relief=RIDGE)
        self.lblbutton2.place(x=225,y=0,width=1310,height=590)


        #========================== Down Images =======================
        img3=Image.open(r"images\myh.jpg")
        img3=img3.resize((230,210),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        self.lblbutton3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        self.lblbutton3.place(x=0,y=225,width=230,height=210)

        img4=Image.open(r"images\khana.jpg")
        img4=img4.resize((230,190),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        self.lblbutton4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        self.lblbutton4.place(x=0,y=420,width=230,height=190)


    def cus_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer(self.new_window)

    
    def room_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Room(self.new_window)


    
    def detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)



     
    def feed(self):
        self.new_window=Toplevel(self.root)
        self.app=Feedback(self.new_window)

    def logout(self):
        self.root.destroy()

    def open_img1(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")),parent=self.root)
        img__8 = Image.open(fln)
        img_browse = img__8.resize((1550,140),Image.ANTIALIAS)
        self.photoimg_78 = ImageTk.PhotoImage(img_browse)
        self.lblbutton.config(image=self.photoimg_78)

    
    def open_logo(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")))
        img__9 = Image.open(fln)
        img_browse = img__9.resize((230,140),Image.ANTIALIAS)
        self.photoimg_7 = ImageTk.PhotoImage(img_browse)
        self.lblbuttonlogo.config(image=self.photoimg_7)

    
    def open_img2(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")))
        img__0 = Image.open(fln)
        img_browse = img__0.resize((1310,590),Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_browse)
        self.lblbutton2.config(image=self.photoimg_6)

    
    def open_img3(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")))
        img__3 = Image.open(fln)
        img_browse = img__3.resize((230,210),Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_browse)
        self.lblbutton.config(image=self.photoimg_3)

    
    def open_img4(self):
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("JPEG File","*.jpeg"),("ALL Files","*.*")))
        img__4 = Image.open(fln)
        img_browse = img__4.resize((230,190),Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_browse)
        self.lblbutton.config(image=self.photoimg_4)









if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
