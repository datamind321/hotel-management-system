from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector    
from time import strftime
from tkinter import * 
from tkinter import ttk ,Tk 
import tkinter 
from PIL import Image,ImageTk
from hotel import HotelManagementSystem

import os
  


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()



class login_window:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1550x800+0+0")
            self.root.title("HOTEL MANAGEMENT SYSTEM")
            self.root.wm_iconbitmap('hotel.ico')
        




            #Background-img

            img4 = Image.open(r"images\myh.jpg")
            img4 = img4.resize((1530,710),Image.ANTIALIAS)
            self.photoimg5 = ImageTk.PhotoImage(img4)
            bg_lbl = Label(self.root,image=self.photoimg5)
            bg_lbl.place(x=0,y=130,height=710,width=1530)

            
            #title-label 
            title = Label(bg_lbl,text="HOTEL MANAGEMENT SYSTEM SOFTWARE",font=("time new roman",35,"bold"),bg="black",fg='gold')
            title.place(x=0,y=0,height=45,width=1530)
 
             # add IMages 

            images = Image.open(r"images\hotel-names.jpg")
            images = images.resize((500,130),Image.ANTIALIAS)
            self.photoimg_1 = ImageTk.PhotoImage(images)

            self.f_btn = Label(self.root,image=self.photoimg_1)
            self.f_btn.place(x=0,y=0,height=130,width=500)


            img2 = Image.open(r"images\room1.jpg")
            img2 = img2.resize((500,130),Image.ANTIALIAS)
            self.photoimg4 = ImageTk.PhotoImage(img2)

            self.f_btn2 = Label(self.root,image=self.photoimg4)
            self.f_btn2.place(x=500,y=0,height=130,width=500)

            img3 = Image.open(r"images\room2.jpg")
            img3 = img3.resize((550,130),Image.ANTIALIAS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            self.f_btn3 = Label(self.root,image=self.photoimg3)
            self.f_btn3.place(x=1000,y=0,height=130,width=550) 
           


            main_frame = Frame(self.root,bd=2,bg="black")
            main_frame.place(x=610,y=200,height=450, width=450)

            img=Image.open(r"images/LoginIconAppl.png")
            img=img.resize((100,100),Image.ANTIALIAS)
            self.photoimg = ImageTk.PhotoImage(img)

            lblimg=Label(image=self.photoimg,bg="black",borderwidth=0)
            lblimg.place(x=780,y=200,height=100,width=100)

            #labels 
            get_str=Label(main_frame,text="GET STARTED",font=("times new roman",20,"bold"),bg="black",fg='white')
            get_str.place(x=130,y=100)

            studentname_lebel = Label(main_frame,text="UserName",font=("time new roman",15,"bold"),bg="black",fg="white")
            studentname_lebel.place(x=110,y=155) 



            
            self.txtuser = ttk.Entry(main_frame,width=15,font=("time new roman",15,"bold"))
            self.txtuser.place(x=90,y=180,width=270)


            
            pwd_lebel = Label(main_frame,text="Password",font=("time new roman",15,"bold"),bg="black",fg="white")
            pwd_lebel.place(x=110,y=225) 

            self.txtpwd = ttk.Entry(main_frame,width=15,font=("time new roman",15,"bold"))
            self.txtpwd.place(x=90,y=250,width=270)


            img1=Image.open(r"images/LoginIconAppl.png")
            img1=img1.resize((20,20),Image.ANTIALIAS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
            lblimg1.place(x=700,y=360,height=20,width=20)


            img2=Image.open(r"images/lock-512.png") 
            img2=img2.resize((20,20),Image.ANTIALIAS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
            lblimg2.place(x=700,y=430,height=20,width=20)

            #login-button
            login_btn=Button(main_frame,command=self.login,text="Login",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
            login_btn.place(x=150,y=300,width=120,height=35) 


            #register-button
            register_btn=Button(main_frame,command=self.reg_win,text="New User Register",font=("time new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
            register_btn.place(x=15,y=340,width=160)

            #forgot-password 
            forget_btn=Button(main_frame,command=self.forgot_pass,text="Forgot Password",font=("time new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
            forget_btn.place(x=7,y=370,width=160)



            #[=================LOgin function======================]

        def reg_win(self):
            self.new_window=Toplevel(self.root)
            self.app=register_window(self.new_window)

        def login(self):
            if self.txtuser.get()=="" or self.txtpwd.get()=="":
                messagebox.showerror("Error","All Fields Required !",parent=self.root)
            
                
                
                        
                 

            else:
                conn= mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select *from register where email=%s and pass=%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpwd.get()
                                                                                    ))
                row=my_cursor.fetchone()  
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Passwoord !",parent=self.root)
                else:
                    open_main=messagebox.askyesno("Success","you are logged in successfully",parent=self.root)
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=HotelManagementSystem(self.new_window)
                        
                
                    else: 
                        if not open_main:
                            return 
                conn.commit()
                conn.close()


    #================ Reset Password ========================

        def reset_pass(self):
            if self.combo_security_Q.get()=="select":
                messagebox.showerror("Error","select the security question",parent=self.root2)
            elif self.txt_security.get()=="":
                messagebox.showerror("Error","Please enter the answer",parent=self.root2)
            elif self.txt_newpassword.get()=="":
                messagebox.showerror("Error","Please enter new password",parent=self.root2)
            else:
                conn= mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognition")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s and secq=%s and seca=%s")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                if row==None:
                    messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
                else:
                    query=("update register set pass=%s where email=%s")
                    value=(self.txt_newpassword.get(),self.txtuser.get(),)
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Your Password reset successfully.",parent=self.root2)
                    self.root2.destroy()







    #============================ Forget Password Function  ============================


        def forgot_pass(self):
            if self.txtuser.get()=="":
                messagebox.showerror("Error","Please Enter Username to reset password",parent=self.root2)
            else:
                conn= mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognition")
                my_cursor=conn.cursor()
                query=("select *from register where email=%s")
                value=(self.txtuser.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                # print(row)
                if row==None:
                    messagebox.showerror("Error","Please enter valid username !",parent=self.root2)
                else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("340x450+610+170")
                    self.root2.wm_iconbitmap('hotel.ico')

                    l=Label(self.root2,text="Forgot Password",font=("time new roman",20,"bold"),bd=3,fg="red")
                    l.place(x=0,y=10,relwidth=1)

                     #securition-question

            
                    secq = Label(self.root2,text="Select Security Question",font=("time new roman",  15,"bold"))
                    secq.place(x=50,y=80)

                    self.combo_security_Q=ttk.Combobox(self.root2,font=("time new roman",  15,"bold"),state="readonly")
                    self.combo_security_Q["values"]=("select","your birth-date","your pet name","your gf name","your best friend name")
                    self.combo_security_Q.place(x=50,y=110,width=250)
                    self.combo_security_Q.current(0)
                    seca = Label(self.root2,text="Security Answer",font=("time new roman",  15,"bold"))
                    seca.place(x=50,y=150) 

                    self.txt_security=ttk.Entry(self.root2,font=("time new roman",  15,"bold"))
                    self.txt_security.place(x=50,y=180,width=250)

            #new-password
                    new_pwd = Label(self.root2,text="New Password",font=("time new roman",  15,"bold"))
                    new_pwd.place(x=50,y=220) 

                    self.txt_newpassword=ttk.Entry(self.root2,font=("time new roman",  15,"bold"))
                    self.txt_newpassword.place(x=50,y=250,width=250)

                    btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("time new roman",  15,"bold"),fg="white",bg="green")
                    btn.place(x=120,y=290) 

                




                    





                    
                    






                







class register_window:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1600x900+0+0")
            self.root.title("Face Recognition System")
            self.root.wm_iconbitmap('hotel.ico')


            #===========================Variables==================

            self.var_fname=StringVar()
            self.var_lname=StringVar()
            self.var_contact=StringVar()
            self.var_email=StringVar()
            self.var_sq=StringVar()
            self.var_sa=StringVar()
            self.var_pass=StringVar()
            self.var_repass=StringVar()
            self.var_check=IntVar()
            



            #bg-img
            self.bg_img=ImageTk.PhotoImage(file=r"images/0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
            bg_lbl = Label(self.root,image=self.bg_img)
            bg_lbl.place(x=0,y=0,relheight=1,relwidth=1) 

            #left-img
            self.bg_img2=ImageTk.PhotoImage(file=r"images/thought-good-morning-messages-LoveSove.jpg")
            bg_lbl = Label(self.root,image=self.bg_img2)
            bg_lbl.place(x=50,y=100,height=550,width=470) 


            #=========================frame======================
            frame=Frame(self.root,bg="white")
            frame.place(x=520,y=100,width=800,height=550)

            reg_lbl=Label(frame,text="REGISTER HERE",font=("time new roman",20,"bold"),fg="darkgreen",bg="white")
            reg_lbl.place(x=20,y=20)

            #==========================Lablels - Entries===================
            
            #first-name
            first_name = Label(frame,text="First Name",font=("time new roman",  15,"bold"),bg="white")
            first_name.place(x=50,y=100) 


            self.first_name=ttk.Entry(frame,textvariable=self.var_fname,width=20,font=("time new roman",  15,"bold"))
            self.first_name.place(x=50,y=130,width=250)


            #last-name
            last_name = Label(frame,text="Last Name",font=("time new roman",  15,"bold"),bg="white")
            last_name.place(x=370,y=100) 


            self.last_name=ttk.Entry(frame,textvariable=self.var_lname,width=20,font=("time new roman",  15,"bold"))
            self.last_name.place(x=370,y=130,width=250)


            #contact
            contact = Label(frame,text="Contact",font=("time new roman",  15,"bold"),bg="white")
            contact.place(x=50,y=170) 


            self.contact=ttk.Entry(frame,width=20,textvariable=self.var_contact,font=("time new roman",  15,"bold"))
            self.contact.place(x=50,y=200,width=250)

            #e-mail

            
            email_lab = Label(frame,text="Username",font=("time new roman",  15,"bold"),bg="white")
            email_lab.place(x=370,y=170) 


            self.email=ttk.Entry(frame,width=20,textvariable=self.var_email,font=("time new roman",  15,"bold"))
            self.email.place(x=370,y=200,width=250)

            #securition-question

            
            secq = Label(frame,text="Select your Security Question",font=("time new roman",  15,"bold"),bg="white")
            secq.place(x=50,y=240)

            self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_sq,font=("time new roman",  15,"bold"),state="readonly")
            self.combo_security_Q["values"]=("select","your birth-date","your pet name","your gf name","your best friend name")
            self.combo_security_Q.place(x=50,y=270,width=250)
            self.combo_security_Q.current(0)







            #security-answer
            seca = Label(frame,text="Security Answer",font=("time new roman",  15,"bold"),bg="white")
            seca.place(x=370,y=240) 

            self.txt_security=ttk.Entry(frame,textvariable=self.var_sa,font=("time new roman",  15,"bold"))
            self.txt_security.place(x=370,y=270,width=250)

            #password
            pwds = Label(frame,text="Password",font=("time new roman",  15,"bold"),bg="white")
            pwds.place(x=50,y=310) 

            self.new_password=ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",  15,"bold"))
            self.new_password.place(x=50,y=340,width=250)


            rpwds = Label(frame,text="Confirm Password",font=("time new roman",  15,"bold"),bg="white")
            rpwds.place(x=370,y=310) 

            self.confirm_password=ttk.Entry(frame,textvariable=self.var_repass,font=("time new roman",  15,"bold"))
            self.confirm_password.place(x=370,y=340,width=250)


            #check-box
            checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree Terms & Conditions",font=("time new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
            checkbtn.place(x=50,y=380)

            #buttons-------------------------------Register-Now button 
            img9 = Image.open(r"images\register-now-button1.jpg")
            img9 = img9.resize((200,50),Image.ANTIALIAS)
            self.photoimg9 = ImageTk.PhotoImage(img9)
            b1=Button(frame,image=self.photoimg9,borderwidth=0,cursor="hand2",bg="white",command=self.register_data)
            b1.place(x=10,y=420,width=200)

            #Login-button

            img8 = Image.open(r"images\loginpng.png")
            img8 = img8.resize((200,50),Image.ANTIALIAS)
            self.photoimg8 = ImageTk.PhotoImage(img8)
            b1=Button(frame,command=self.login_page,image=self.photoimg8,borderwidth=0,cursor="hand2",bg="white")
            b1.place(x=330,y=420,width=200)


            #=================function=============

        def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sq.get()=="select" or self.var_sa.get()=="":
                messagebox.showerror("Error","All Fields are required !",parent=self.root)
            elif self.var_pass.get()!=self.var_repass.get():
                messagebox.showerror("Error","password must be same",parent=self.root)
            elif self.var_check.get()==0:
                messagebox.showerror("Error","please agree terms & conditions",parent=self.root)
            else:
                try:
                    conn= mysql.connector.connect(host="localhost",username="root",password="12345678",database="face_recognition")
                    my_cursor=conn.cursor()
                    query=("select *from register where email=%s")
                    value=(self.var_email.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","User Already Exist !",parent=self.root)
                    else:
                        my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                               self.var_fname.get(),
                                                                                                               self.var_lname.get(),
                                                                                                               self.var_contact.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_sq.get(),
                                                                                                               self.var_sa.get(),
                                                                                                               self.var_pass.get()
                                                                                                               
                       
                                                                                            ))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Customer details has been added Successfully",parent=self.root)
                        self.root.destroy()
                except Exception as es:
                    messagebox("Error",f"Due To :{str(es)}",parent=self.root)

        def login_page(self):
                    self.root.destroy()















#===========================================main project===============================================================================






if __name__ == "__main__":
  main()