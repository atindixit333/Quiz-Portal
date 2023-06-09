import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from quizmail import *
import random
import re
# from sendingmailresult import *
import pymysql
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
t=tkinter.Tk()
t.geometry("1700x1700")
t.title("Quiz Portal")
def minimize():
    t.iconify()
       
        

def adminlogin():
    tpl_adminlogin=Toplevel(t)
    tpl_adminlogin.geometry("1700x1700")
    tpl_adminlogin.title("Admin login details")
    minimize()
    
    #admin login
    
    def adminselectdata():
   
        adminname=adminname_entry1.get()
        password1=password_entry1.get()
        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
        cur=db.cursor()
        sql = "SELECT adminid,password FROM admininfo WHERE adminid = '%s'" % (adminname)
        cur.execute(sql)
        result = cur.fetchone()
        db.close()
        
    
        
            
        if result is not None and adminname == result[0] and password1 == result[1]:    
            
            tpl_adminselectdata=Toplevel(tpl_adminlogin)
            tpl_adminselectdata.geometry("1600x1600")
            tpl_adminselectdata.title("Select Data")
            
            
            
            def showadmin():

                tpl_showadmin=Toplevel(tpl_adminselectdata)
                tpl_showadmin.geometry("1600x1600")
                tpl_showadmin.title("admin FIUD")
                def showsave():
                    r=[]
                    def is_valid_adminpassword(password):
                    # Check if the password meets the minimum length requirement
                        if len(password) < 8:
                            return False
                        
                        # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
                        if not re.search(r'[A-Z]', password) or \
                           not re.search(r'[a-z]', password) or \
                           not re.search(r'\d', password):
                            return False
                        
                        # Check if the password contains at least one special character
                        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                            return False
                        
                        return True
                    # create new admin
                    def savedata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                    
                        a=adminid_cbox.get()
                        b=adminname_entry.get()
                        c=password_entry11.get()
                        if len(a)==0 or len(b)==0 or len(c)==0:
                                messagebox.showerror('status','check details..')
                        # else:
                                if not is_valid_adminpassword(c):
                                    messagebox.showerror('status', 'Password is not strong enough. Please choose a password that contains at least 8 characters, including uppercase and lowercase letters, digits, and special characters.')
                                    return
                                else:
                                    sql="select * from admininfo where adminid ='%s'"%a
                                    cur.execute(sql)
                                    result = cur.fetchone()
                                    if result is not None:
                                        messagebox.showerror("status","ADMIN ID already exists")
                                        adminid_cbox.delete(0,100)
                                        adminname_entry.delete(0,100)
                                        password_entry11.delete(0,100)
                        else:
                            
                            sql="select * from admininfo where adminid ='%s'"%a
                            cur.execute(sql)
                            result = cur.fetchone()
                            if result is not None:
                                messagebox.showerror("status","ADMIN ID already exists")
                                adminid_cbox.delete(0,100)
                                adminname_entry.delete(0,100)
                                password_entry11.delete(0,100)
                            else:
                                sql="insert into admininfo values('%s','%s','%s')"%(a,b,c)
                                cur.execute(sql)
                                db.commit()
                                messagebox.showinfo('Status','Data Saved...')
                                adminid_cbox.delete(0,100)
                                adminname_entry.delete(0,100)
                                password_entry11.delete(0,100)
                                db.close()
                    
                        
                    def cleardata():
                         adminid_cbox.delete(0,100)
                         adminname_entry.delete(0,100)
                         password_entry11.delete(0,100)
                         
                    def searchid():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=adminid_cbox.get()
                        sql="select count(*) from admininfo where adminid='%s'"%(a)
                        cur=db.cursor()
                        cur.execute(sql)
                        data=cur.fetchone()
                        x=data[0]
                        if x==0:
                            lblstatus.config(text='OK GO AHEAD',bg='blue',fg='white')
                        else:
                            lblstatus.config(text='ALREADY PRESENT',bg='red',fg='white')  
                    def filldata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        sql="Select adminid from admininfo"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                              r.append(res[0]) 
                        db.close()        
                    cnv2=Canvas(tpl_showadmin,width=1600,height=800,bg="#b4eef5")
                    cnv2.place(x=150,y=80)
        
        
    
                    btnsearch=Button(tpl_showadmin,text='Search',bg="blue",fg="white",command=searchid)    
                    btnsearch.place(x=900,y=240)
                    lblstatus=Label(tpl_showadmin,text='status',fg='yellow',bg='red')
                    lblstatus.place(x=1000,y=240)
                      
                
                
                    admininfo_label=Label(tpl_showadmin,text='    Admin Information   (INSERT)',font=('Edwardian Script ITC',25),fg="white",bg='#5e65a1')
                    admininfo_label.place(x=600,y=100)
                            
                    adminid_label=Label(tpl_showadmin,text='Admin_id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    adminid_label.place(x=500,y=235)
                    
                    # filldata()
                    adminid_cbox=Entry(tpl_showadmin,width=30)
                    # adminid_cbox['values']=r
                    adminid_cbox.place(x=650,y=240)
                      
                    adminname_label=Label(tpl_showadmin,text='Admin_Name',bg="#b4eef5",font=('Eras Bold ITC',15))
                    adminname_label.place(x=500,y=285)
                    
                    adminname_entry=Entry(tpl_showadmin,width=30)
                    adminname_entry.place(x=650,y=290)
                      
                    password_label=Label(tpl_showadmin,text='Password',bg="#b4eef5",font=('Eras Bold ITC',15))
                    password_label.place(x=500,y=325)
                    password_entry11=Entry(tpl_showadmin,width=30)
                    password_entry11.place(x=650,y=330)
                            
                  
                    save_bt=Button(tpl_showadmin,text='SAVE',bg='yellow',width=10,fg='black',font=('Algerian',15),command=savedata)
                    save_bt.place(x=600,y=400)
                    clear_bt=Button(tpl_showadmin,text='CLEAR',bg='yellow',width=10,fg='black',font=('Algerian',14),command=cleardata)
                    clear_bt.place(x=750,y=400)
                
               
                c1=Canvas(tpl_showadmin,height=80,width=1700,bg='#5e65a1')
                c1.place(x=0,y=0)
                quiz_label=Label(c1,text="Quiz Portal",font=("comic sans ms",40),bg='#5e65a1',fg="white")
                quiz_label.place(x=50,y=1)
                
                c2=Canvas(tpl_showadmin,width=1600,height=800,bg="white")
                c2.place(x=0,y=80)
                c3=Canvas(tpl_showadmin,width=150,height=800,bg="#5e65a1")
                c3.place(x=0,y=80)
                
                
                
                # find admin
                def showfind():
                    r=[]
                    def finddata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=adminid_entry.get()
                        sql="Select aname,password from admininfo where adminid='%s'"%(a)
                        cur=db.cursor()
                        cur.execute(sql)
                        data=cur.fetchone()
                        if data==None:
                            adminid_entry.delete(0,100)
                            messagebox.showerror('Status','Not found')
                        else:
                            adminname_entry.delete(0,100)
                            password_entry.delete(0,100)
        
        
                        adminname_entry.insert(0, data[0])
                        password_entry.insert(0, data[1])
                        db.close()
               
                    def cleardata():
                        adminid_entry.delete(0,100)
                        adminname_entry.delete(0,100)
                        password_entry.delete(0,100)
         
            
           
                    c2=Canvas(tpl_showadmin,width=1600,height=800,bg="#b4eef5")
                    c2.place(x=150,y=80)
        
        
                    admininfo_label=Label(c2,text='    Admin Information find   ',font=('Edwardian Script ITC',25),fg="white",bg='#5e65a1')
                    admininfo_label.place(x=400,y=70)
                
                    adminid_label=Label(c2,text='Admin_id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    adminid_label.place(x=350,y=150)
                    adminid_entry=Entry(c2,width=30)
                    adminid_entry.place(x=500,y=150)
                        
                    adminname_label=Label(c2,text='Admin_Name',bg="#b4eef5",font=('Eras Bold ITC',15))
                    adminname_label.place(x=350,y=190)
                    adminname_entry=Entry(c2,width=30)
                    adminname_entry.place(x=500,y=190)
                    
                    password_label=Label(c2,text='Password',bg="#b4eef5",font=('Eras Bold ITC',15))
                    password_label.place(x=350,y=230)
                    password_entry=Entry(c2,width=30)
                    password_entry.place(x=500,y=230)
                    
                    
                    find_bt=Button(c2,text='FIND',bg='yellow',width=10,fg='black',font=('Algerian',15),command=finddata)
                    find_bt.place(x=380,y=300)
                    clear_bt=Button(c2,text='CLEAR',bg='yellow',width=10,fg='black',font=('Algerian',15),command=cleardata)
                    clear_bt.place(x=550,y=300)
                
                
                # delete the admin
                def showdelete():
                    def searchidd():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=adminid_entry.get()
                        sql="Select aname,password from admininfo where adminid='%s'"%(a)
                        cur=db.cursor()
                        cur.execute(sql)
                        data=cur.fetchone()
                        if data==None:
                            adminid_entry.delete(0,100)
                            messagebox.showerror('Status','Not found')
                        else:
                            adminname_entry.delete(0,100)
                            password_entry.delete(0,100)
        
        
                        adminname_entry.insert(0, data[0])
                        password_entry.insert(0, data[1])
                        db.close()
                    def deletedata():
                        db=pymysql.connect(host="localhost",user="root",password="root",database="quiz_portal")
                        cur=db.cursor()
                        a=adminid_entry.get()
                        sql="delete from admininfo where adminid='%s'"%(a)
                        cur.execute(sql)
                        db.commit()
                        adminid_entry.delete(0,100)
                        adminname_entry.delete(0,100)
                        password_entry.delete(0,100)
        
                        messagebox.showinfo('Status','deleted....')
                    def cleardata():
                        adminid_entry.delete(0,100)
                        adminname_entry.delete(0,100)
                        password_entry.delete(0,100)
        
                    c4=Canvas(tpl_showadmin,width=1600,height=800,bg="#b4eef5")
                    c4.place(x=150,y=80)
                    
                    admininfo_label=Label(c4,text='    Admin Information Delete   ',font=('Edwardian Script ITC',25),fg="white",bg='#5e65a1')
                    admininfo_label.place(x=400,y=70)     
                    adminid_label=Label(c4,text='Admin_id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    adminid_label.place(x=350,y=150)
                    adminid_entry=Entry(c4,width=30)
                    adminid_entry.place(x=500,y=150)
                    
                    adminname_label=Label(c4,text='Admin_Name',bg="#b4eef5",font=('Eras Bold ITC',15))
                    adminname_label.place(x=350,y=190)
                    adminname_entry=Entry(c4,width=30)
                    adminname_entry.place(x=500,y=190)
          
                    password_label=Label(c4,text='Password',bg="#b4eef5",font=('Eras Bold ITC',15))
                    password_label.place(x=350,y=230)
                    password_entry=Entry(c4,width=30)
                    password_entry.place(x=500,y=230)
                
        
        
                    delete_bt=Button(c4,text='DELETE',bg='yellow',fg='black',font=('Algerian',14),width=10,command=deletedata)
                    delete_bt.place(x=380,y=300)
                    clear_bt=Button(c4,text='CLEAR',bg='yellow',fg='black',font=('Algerian',14),width=10,command=cleardata)
                    clear_bt.place(x=550,y=300)
                    checkd_bt=Button(c4,text='Check',bg='red',fg='black',command=searchidd)
                    checkd_bt.place(x=900,y=240)
                
                
                # change and update admin data
                def showupdate():
                    def searchidu():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=adminid_entry.get()
                        sql="Select aname,password from admininfo where adminid='%s'"%(a)
                        cur=db.cursor()
                        cur.execute(sql)
                        data=cur.fetchone()
                        if data==None:
                            adminid_entry.delete(0,100)
                            messagebox.showerror('Status','Not found')
                        else:
                            adminname_entry.delete(0,100)
                            password_entry.delete(0,100)
        
        
                        adminname_entry.insert(0, data[0])
                        password_entry.insert(0, data[1])
                        db.close()
                    def updatedata():
                        db=pymysql.connect(host="localhost",user="root",password="root",database="quiz_portal")
                        cur=db.cursor()
                        a=adminid_entry.get()
                        b=adminname_entry.get()
                        c=password_entry.get()
                        if len(a)==0 or len(b)==0 or len(c)==0:
                            messagebox.showerror('status','check all values..')
                        elif not all((a, b, c)):
                            messagebox.showerror('status', 'Fill remaining values')
                        else:
                            sql="UPDATE admininfo SET adminid ='%s',aname ='%s',password = '%s' where adminid='%s'"%(a,b,c,a)
                            cur.execute(sql)
                            messagebox.showinfo('Status','Update successfully...')
                            db.commit()
                            adminid_entry.delete(0,100)
                            adminname_entry.delete(0,100)
                            password_entry.delete(0,100)
                        db.close()
                        adminid_entry.delete(0,100)
                        adminname_entry.delete(0,100)
                        password_entry.delete(0,100)
                        
               
                    def cleardata():
              
                        adminid_entry.delete(0,100)
                        adminname_entry.delete(0,100)
                        password_entry.delete(0,100)
                        
                              
                    c5=Canvas(tpl_showadmin,width=1600,height=800,bg="#b4eef5")
                    c5.place(x=150,y=80)
                    
                    admininfo_label=Label(c5,text='    Admin Information   ',font=('Edwardian Script ITC',25),fg="white",bg='#5e65a1')
                    admininfo_label.place(x=400,y=70)     
                    adminid_label=Label(c5,text='Admin_id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    adminid_label.place(x=350,y=150)
                    adminid_entry=Entry(c5,width=30)
                    adminid_entry.place(x=500,y=150)
                    
                    adminname_label=Label(c5,text='Admin_Name',bg="#b4eef5",font=('Eras Bold ITC',15))
                    adminname_label.place(x=350,y=190)
                    adminname_entry=Entry(c5,width=30)
                    adminname_entry.place(x=500,y=190)
                      
                    password_label=Label(c5,text='Password',bg="#b4eef5",font=('Eras Bold ITC',15))
                    password_label.place(x=350,y=230)
                    password_entry=Entry(c5,width=30)
                    password_entry.place(x=500,y=230)
                    
                                
                     
                    update_bt=Button(c5,text='UPDATE',bg='yellow',fg='black',font=('Algerian',14),width=10,command=updatedata)
                    update_bt.place(x=380,y=300)
                    clear_bt=Button(c5,text='CLEAR',bg='yellow',fg='black',font=('Algerian',14),width=10,command=cleardata)
                    clear_bt.place(x=550,y=300)
                    checku_bt=Button(c5,text='Check',bg='red',fg='black',command=searchidu)
                    checku_bt.place(x=900,y=200)
                
                # button for change the admin data 
                b1=Button(c3,text="FIND",fg="black",bg="yellow",font=('Algerian',15),width=10,command=showfind)  #,command=showfind
                b1.place(x=20,y=100)
                b2=Button(c3,text="INSERT",fg="black",bg="yellow",font=('Algerian',15),width=10,command=showsave)
                b2.place(x=20,y=200)
                b3=Button(c3,text="DELETE",fg="black",bg="yellow",font=('Algerian',15),width=10,command=showdelete)   #,command=showdelete
                b3.place(x=20,y=300)
                b4=Button(c3,text="UPDATE",fg="black",bg="yellow",font=('Algerian',15),width=10,command=showupdate)    #command=showupdate
                b4.place(x=20,y=400)
                        
                tpl_showadmin.mainloop()
      
            
            
            c2=Canvas(tpl_adminselectdata,width=1600,height=800,bg="#b4eef5")
            c2.place(x=0,y=0)
            adminlogin_label=Label(tpl_adminselectdata,text="ADMIN PORTAL",bg="#5e65a1",fg="white",width=100,height=2,font=('comic sans ms',30))
            adminlogin_label.pack()
            
            # Function for admin to check user details            
            def useradmin():
                tpl_useradmin=Toplevel(tpl_adminselectdata)
                tpl_useradmin.geometry("1700x1700")
                tpl_useradmin.title("Admin login details")
                minimize()
                cs1=Canvas(tpl_useradmin,height=80,width=1700,bg='#5e65a1')
                cs1.place(x=0,y=0)
                quiz_label=Label(cs1,text="User Information",font=("comic sans ms",40),bg='#5e65a1',fg="white")
                quiz_label.place(x=50,y=1)
                
                
                
                def finduser():
                    r=[]
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    sql="SELECT userid from userinfo"
                    cur.execute(sql)
                    r= cur.fetchall()
                    # userpassword_entry.insert(0, data[0])
                    def find_user():
                        # userids=[]
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=combo_box.get()
                        sql="SELECT upassword,uname,adress,city,email,phon,govid,govid_number FROM userinfo where userid='%s'"%(a)
                        cur.execute(sql)
                        data = cur.fetchone()
                        userpassword_entry.delete(0,100)
                        username1_entry.delete(0,100)
                        useradress_entry.delete(0,100)
                        usercity_entry.delete(0,100)
                        useremail_entry.delete(0,100)
                        userphon_entry.delete(0,100)
                        usergovid_entry.delete(0,100)
                        usergovidno_entry.delete(0,100)
                        
                        userpassword_entry.insert(0, data[0])
                        username1_entry.insert(0, data[1])
                        useradress_entry.insert(0,data[2])
                        usercity_entry.insert(0,data[3])
                        useremail_entry.insert(0,data[4])
                        userphon_entry.insert(0,data[5])
                        usergovid_entry.insert(0,data[6])
                        usergovidno_entry.insert(0,data[7])
                        db.close()
                    
                    def clearuser():
                        userpassword_entry.delete(0,100)
                        username1_entry.delete(0,100)
                        useradress_entry.delete(0,100)
                        usercity_entry.delete(0,100)
                        useremail_entry.delete(0,100)
                        userphon_entry.delete(0,100)
                        usergovid_entry.delete(0,100)
                        usergovidno_entry.delete(0,100)
                        
                    
                    
                    
                    
                    
                        
                    
                    
                    
                    cs2=Canvas(tpl_useradmin,width=1600,height=800,bg="#b4eef5")
                    cs2.place(x=150,y=80)
                    
                    userid_label=Label(cs2,text='User Id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userid_label.place(x=500,y=100)
                    combo_box = ttk.Combobox(cs2)
                    
                    combo_box['values'] = r
                    combo_box.place(x=605,y=105)
                    
                    userpassword_label=Label(cs2,text='Password',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userpassword_label.place(x=500,y=125)
                    userpassword_entry=Entry(cs2,width=30)
                    userpassword_entry.place(x=605,y=130)
                    
                    username1_label=Label(cs2,text='Name',bg="#b4eef5",font=('Eras Bold ITC',15))
                    username1_label.place(x=500,y=170)
                    username1_entry=Entry(cs2,width=30)
                    username1_entry.place(x=605,y=175)
                    
                    useradress_label=Label(cs2,text='Address',bg="#b4eef5",font=('Eras Bold ITC',15))
                    useradress_label.place(x=500,y=210)
                    useradress_entry=Entry(cs2,width=30)
                    useradress_entry.place(x=605,y=215)
                    
                    usercity_label=Label(cs2,text='City',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usercity_label.place(x=500,y=250)
                    usercity_entry=Entry(cs2,width=30)
                    usercity_entry.place(x=605,y=255)
                    
                    useremail_label=Label(cs2,text='Email',bg="#b4eef5",font=('Eras Bold ITC',15))
                    useremail_label.place(x=500,y=290)
                    useremail_entry=Entry(cs2,width=30)
                    useremail_entry.place(x=605,y=295)
                    
                    userphon_label=Label(cs2,text='Phone No',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userphon_label.place(x=500,y=330)
                    userphon_entry=Entry(cs2,width=30)
                    userphon_entry.place(x=605,y=335)
                    
                    usergovid_label=Label(cs2,text='Gov Id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usergovid_label.place(x=500,y=370)
                    usergovid_entry=Entry(cs2,width=30)
                    usergovid_entry.place(x=605,y=375)
                    
                    usergovidno_label=Label(cs2,text='Gov Id No',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usergovidno_label.place(x=500,y=410)
                    
                    usergovidno_entry=Entry(cs2,width=30)
                    # usergovidno_entry=ttk.Combobox(cs2,values=["Adhaar Card","Voter ID"])
                    usergovidno_entry.place(x=605,y=415)
                    
                                     
                    
                    
                    find_bt=Button(cs2,text='FIND',bg='yellow',width=10,fg='black',font=('Algerian',15),command=find_user)#,command=finddata
                    find_bt.place(x=500,y=500)
                    clear_bt=Button(cs2,text='CLEAR',bg='yellow',width=10,fg='black',font=('Algerian',15),command=clearuser)#,command=cleardata
                    clear_bt.place(x=650,y=500)
                
                
                        
                    
                cs3=Canvas(tpl_useradmin,width=150,height=800,bg="#5e65a1")
                cs3.place(x=0,y=80)
                
                

                # delete the user
                def delete_user():
                    
                
                    r=[]
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    sql="SELECT userid from userinfo"
                    cur.execute(sql)
                    r= cur.fetchall()
                    
                    def check_user():
                       
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=combo_box.get()
                        sql="SELECT upassword,uname,adress,city,email,phon,govid,govid_number FROM userinfo where userid='%s'"%(a)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data==None:
                            userpassword_entry.delete(0,100)
                            username1_entry.delete(0,100)
                            useradress_entry.delete(0,100)
                            usercity_entry.delete(0,100)
                            useremail_entry.delete(0,100)
                            userphon_entry.delete(0,100)
                            usergovid_entry.delete(0,100)
                            usergovidno_entry.delete(0,100)
                            messagebox.showerror('Status','Not found')
                        else:
                        
                            userpassword_entry.insert(0, data[0])
                            username1_entry.insert(0, data[1])
                            useradress_entry.insert(0,data[2])
                            usercity_entry.insert(0,data[3])
                            useremail_entry.insert(0,data[4])
                            userphon_entry.insert(0,data[5])
                            usergovid_entry.insert(0,data[6])
                            usergovidno_entry.insert(0,data[7])
                        db.close()
                    def deleteuserdata():
                        db=pymysql.connect(host="localhost",user="root",password="root",database="quiz_portal")
                        cur=db.cursor()
                        a=combo_box.get()
                        sql="delete from userinfo where userid='%s'"%(a)
                        cur.execute(sql)
                        db.commit()
                        combo_box.delete(0,100)
                    
                        userpassword_entry.delete(0,100)
                        username1_entry.delete(0,100)
                        useradress_entry.delete(0,100)
                        usercity_entry.delete(0,100)
                        useremail_entry.delete(0,100)
                        userphon_entry.delete(0,100)
                        usergovid_entry.delete(0,100)
                        usergovidno_entry.delete(0,100)
        
                        messagebox.showinfo('Status','deleted....')
                        db.close()
                    def clear_user():
                        userpassword_entry.delete(0,100)
                        username1_entry.delete(0,100)
                        useradress_entry.delete(0,100)
                        usercity_entry.delete(0,100)
                        useremail_entry.delete(0,100)
                        userphon_entry.delete(0,100)
                        usergovid_entry.delete(0,100)
                        usergovidno_entry.delete(0,100)
                    
                    
                    cs4=Canvas(tpl_useradmin,width=1600,height=800,bg="#b4eef5")
                    cs4.place(x=150,y=80)
                    
                    
                    userid_label=Label(cs4,text='User Id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userid_label.place(x=400,y=100)
                    combo_box = ttk.Combobox(cs4)
                    
                    combo_box['values'] =r
                    combo_box.place(x=505,y=105)
                    
                    userpassword_label=Label(cs4,text='Password',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userpassword_label.place(x=400,y=125)
                    userpassword_entry=Entry(cs4,width=30)
                    userpassword_entry.place(x=505,y=130)
                    
                    username1_label=Label(cs4,text='Name',bg="#b4eef5",font=('Eras Bold ITC',15))
                    username1_label.place(x=400,y=170)
                    username1_entry=Entry(cs4,width=30)
                    username1_entry.place(x=505,y=175)
                    
                    useradress_label=Label(cs4,text='Address',bg="#b4eef5",font=('Eras Bold ITC',15))
                    useradress_label.place(x=400,y=210)
                    useradress_entry=Entry(cs4,width=30)
                    useradress_entry.place(x=505,y=215)
                    
                    usercity_label=Label(cs4,text='City',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usercity_label.place(x=400,y=250)
                    usercity_entry=Entry(cs4,width=30)
                    usercity_entry.place(x=505,y=255)
                    
                    useremail_label=Label(cs4,text='Email',bg="#b4eef5",font=('Eras Bold ITC',15))
                    useremail_label.place(x=400,y=290)
                    useremail_entry=Entry(cs4,width=30)
                    useremail_entry.place(x=505,y=295)
                    
                    userphon_label=Label(cs4,text='Phone No',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userphon_label.place(x=400,y=330)
                    userphon_entry=Entry(cs4,width=30)
                    userphon_entry.place(x=505,y=335)
                    
                    usergovid_label=Label(cs4,text='Gov Id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usergovid_label.place(x=400,y=370)
                    usergovid_entry=Entry(cs4,width=30)
                    usergovid_entry.place(x=505,y=375)
                    
                    usergovidno_label=Label(cs4,text='Gov Id No',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usergovidno_label.place(x=400,y=410)
                    usergovidno_entry=Entry(cs4,width=30)
                    usergovidno_entry.place(x=505,y=415)
                    
                    
                    delete_bt=Button(cs4,text='DELETE',bg='yellow',fg='black',font=('Algerian',14),width=10,command=deleteuserdata)#,command=deletedata
                    delete_bt.place(x=400,y=460)
                    clear_bt=Button(cs4,text='CLEAR',bg='yellow',fg='black',font=('Algerian',14),width=10,command=clear_user)#,command=cleardata
                    clear_bt.place(x=550,y=460)
                    checkd_bt=Button(cs4,text='Check',bg='red',fg='black',command=check_user)#,command=searchidd
                    checkd_bt.place(x=900,y=140)
            
                # change the user detail and update..    
                def userupdate():
                    r=[]
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    sql="SELECT userid from userinfo"
                    cur.execute(sql)
                    r= cur.fetchall()
                    def check__user():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=combo_box.get()
                        sql="SELECT upassword,uname,adress,city,email,phon,govid,govid_number FROM userinfo where userid='%s'"%(a)
                        cur.execute(sql)
                        data = cur.fetchone()
                        userpassword_entry.delete(0,100)
                        username1_entry.delete(0,100)
                        useradress_entry.delete(0,100)
                        usercity_entry.delete(0,100)
                        useremail_entry.delete(0,100)
                        userphon_entry.delete(0,100)
                        usergovid_entry.delete(0,100)
                        usergovidno_entry.delete(0,100)
                        
                        userpassword_entry.insert(0, data[0])
                        username1_entry.insert(0, data[1])
                        useradress_entry.insert(0,data[2])
                        usercity_entry.insert(0,data[3])
                        useremail_entry.insert(0,data[4])
                        userphon_entry.insert(0,data[5])
                        usergovid_entry.insert(0,data[6])
                        usergovidno_entry.insert(0,data[7])
                        db.close()
                        
                    def updatedata():
                        db=pymysql.connect(host="localhost",user="root",password="root",database="quiz_portal")
                        cur=db.cursor()
                        a=combo_box.get()
                        b=userpassword_entry.get()
                        c=username1_entry.get()
                        d=useradress_entry.get()
                        e=usercity_entry.get()
                        f=useremail_entry.get()
                        g=userphon_entry.get()
                        h=usergovid_entry.get()
                        j=usergovidno_entry.get()
                        if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(g)==0 or len(h)==0 or len(j)==0:
                            messagebox.showerror('status','check all values..')
                        elif not all((a, b, c, d, e, f, g, h, j)):
                            messagebox.showerror('status', 'Fill remaining values')
                        else:
                            sql="UPDATE userinfo SET userid ='%s',upassword ='%s',uname = '%s',adress = '%s',city = '%s',email = '%s',phon = '%s',govid = '%s',govid_number = '%s' where userid='%s'"%(a,b,c,d,e,f,g,h,j,a)
                            cur.execute(sql)
                            messagebox.showinfo('Status','Update successfully...')
                            db.commit()
                            userpassword_entry.delete(0,100)
                            username1_entry.delete(0,100)
                            useradress_entry.delete(0,100)
                            usercity_entry.delete(0,100)
                            useremail_entry.delete(0,100)
                            userphon_entry.delete(0,100)
                            usergovid_entry.delete(0,100)
                            usergovidno_entry.delete(0,100)
                            db.close()
                            userpassword_entry.delete(0,100)
                            username1_entry.delete(0,100)
                            useradress_entry.delete(0,100)
                            usercity_entry.delete(0,100)
                            useremail_entry.delete(0,100)
                            userphon_entry.delete(0,100)
                            usergovid_entry.delete(0,100)
                            usergovidno_entry.delete(0,100)
                        
               
                    def cleardata():
              
                        userpassword_entry.delete(0,100)
                        username1_entry.delete(0,100)
                        useradress_entry.delete(0,100)
                        usercity_entry.delete(0,100)
                        useremail_entry.delete(0,100)
                        userphon_entry.delete(0,100)
                        usergovid_entry.delete(0,100)
                        usergovidno_entry.delete(0,100)
                              
                    cs5=Canvas(tpl_useradmin,width=1600,height=800,bg="#b4eef5")
                    cs5.place(x=150,y=80)
                    
                    userid_label=Label(cs5,text='User Id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userid_label.place(x=400,y=100)
                    combo_box = ttk.Combobox(cs5)
                    
                    combo_box['values'] =r
                    combo_box.place(x=505,y=105)
                    
                    userpassword_label=Label(cs5,text='Password',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userpassword_label.place(x=400,y=125)
                    userpassword_entry=Entry(cs5,width=30)
                    userpassword_entry.place(x=505,y=130)
                    
                    username1_label=Label(cs5,text='Name',bg="#b4eef5",font=('Eras Bold ITC',15))
                    username1_label.place(x=400,y=170)
                    username1_entry=Entry(cs5,width=30)
                    username1_entry.place(x=505,y=175)
                    
                    useradress_label=Label(cs5,text='Address',bg="#b4eef5",font=('Eras Bold ITC',15))
                    useradress_label.place(x=400,y=210)
                    useradress_entry=Entry(cs5,width=30)
                    useradress_entry.place(x=505,y=215)
                    
                    usercity_label=Label(cs5,text='City',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usercity_label.place(x=400,y=250)
                    usercity_entry=Entry(cs5,width=30)
                    usercity_entry.place(x=505,y=255)
                    
                    useremail_label=Label(cs5,text='Email',bg="#b4eef5",font=('Eras Bold ITC',15))
                    useremail_label.place(x=400,y=290)
                    useremail_entry=Entry(cs5,width=30)
                    useremail_entry.place(x=505,y=295)
                    
                    userphon_label=Label(cs5,text='Phone No',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userphon_label.place(x=400,y=330)
                    userphon_entry=Entry(cs5,width=30)
                    userphon_entry.place(x=505,y=335)
                    
                    usergovid_label=Label(cs5,text='Gov Id',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usergovid_label.place(x=400,y=370)
                    usergovid_entry=Entry(cs5,width=30)
                    usergovid_entry.place(x=505,y=375)
                    
                    usergovidno_label=Label(cs5,text='Gov Id No',bg="#b4eef5",font=('Eras Bold ITC',15))
                    usergovidno_label.place(x=400,y=410)
                    usergovidno_entry=Entry(cs5,width=30)
                    usergovidno_entry.place(x=505,y=415)
                    
                    
                    update_bt=Button(cs5,text='UPDATE',bg='yellow',fg='black',font=('Algerian',14),width=10,command=updatedata)#,command=deletedata
                    update_bt.place(x=400,y=460)
                    clear_bt=Button(cs5,text='CLEAR',bg='yellow',fg='black',font=('Algerian',14),width=10,command=cleardata)#,command=cleardata
                    clear_bt.place(x=550,y=460)
                    checkd_bt=Button(cs5,text='Check',bg='red',fg='black',command=check__user)#,command=searchidd
                    checkd_bt.place(x=900,y=140)
            
                    
                    
                bs1=Button(cs3,text="FIND",fg="black",bg="yellow",font=('Algerian',15),width=10,command=finduser)  #,command=showfind
                bs1.place(x=20,y=100)
                bs3=Button(cs3,text="DELETE",fg="black",bg="yellow",font=('Algerian',15),width=10,command=delete_user)   #,command=showdelete
                bs3.place(x=20,y=250)
                bs4=Button(cs3,text="UPDATE",fg="black",bg="yellow",font=('Algerian',15),width=10,command=userupdate)    #command=showupdate
                bs4.place(x=20,y=400)
                
                
                tpl_useradmin.mainloop()
            
            userinfo_bt=Button(tpl_adminselectdata,text="USER INFO",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=useradmin)
            userinfo_bt.place(x=200,y=350)
            admininfo_bt=Button(tpl_adminselectdata,text="ADMIN INFO",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=showadmin)
            admininfo_bt.place(x=500,y=350)
            
            #Function for admin to set questions and answers
            def showquestionsdata():
                   
                tpl_showque=Toplevel(tpl_adminselectdata)
                tpl_showque.geometry("1600x1600")
                tpl_showque.title("QUESTIONS PORTAL")
                minimize()
                # function for insert tha new question and answer
                def showsave():
                    r=[]
                    def savedata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                       
                        
                        b=question_entry.get()
                        c=option1_entry.get()
                        d=option2_entry.get()
                        e=option3_entry.get()
                        f=option4_entry.get()
                        g=correctans_entry.get()
                        table=table_var.get()
                        if len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(g)==0:
                            messagebox.showerror('status','check all values..')
                        else:
                            sql=f"insert into {table} (question,option1,option2,option3,option4,answer) values('%s','%s','%s','%s','%s','%s')"%(b,c,d,e,f,g)
                            cur.execute(sql)
                            db.commit()
                            messagebox.showinfo('Status','Data Saved...')
                            question_entry.delete(0,100)
                            option1_entry.delete(0,100)
                            option2_entry.delete(0,100)
                            option3_entry.delete(0,100)
                            option4_entry.delete(0,100)
                            correctans_entry.delete(0,100)
                            db.close()              
   
                    
                    def cleardata():
                       
                            
                            question_entry.delete(0,100)
                            option1_entry.delete(0,100)
                            option2_entry.delete(0,100)
                            option3_entry.delete(0,100)
                            option4_entry.delete(0,100)
                            correctans_entry.delete(0,100)
                         
                   
                   
                    c5=Canvas(tpl_showque,width=1600,height=790,bg="#b4eef5")
                    c5.place(x=150,y=100)
                    table_var=StringVar()
                   
                    subjectid_label=Label(tpl_showque,text="Select SUBJECT:",bg="skyblue",font=('Eras Bold ITC',15))
                    subjectid_label.place(x=500,y=160)
                    subjectid_cbox=ttk.Combobox(tpl_showque,textvariable=table_var,values=['java','mysql','python'],font=("Arial", 20),width=30)
                    subjectid_cbox.set("java")
                    subjectid_cbox.place(x=720,y=160)
                   
                    question_label=Label(tpl_showque,text="Enter Question:",bg="#b4eef5",font=('Eras Bold ITC',15))
                    question_label.place(x=500,y=265)
                    question_entry=Entry(tpl_showque,width=50)
                    question_entry.place(x=720,y=270)
                   
                    option1_label=Label(tpl_showque,text='Enter OPTION 1:',bg="#b4eef5",font=('Eras Bold ITC',15))
                    option1_label.place(x=500,y=315)
                    option1_entry=Entry(tpl_showque,width=50)
                    option1_entry.place(x=720,y=320)
                   
                    option2_label=Label(tpl_showque,text='Enter OPTION 2:',bg="#b4eef5",font=('Eras Bold ITC',15))
                    option2_label.place(x=500,y=365)
                    option2_entry=Entry(tpl_showque,width=50)
                    option2_entry.place(x=720,y=370)
                   
                    option3_label=Label(tpl_showque,text='Enter OPTION 3:',bg="#b4eef5",font=('Eras Bold ITC',15))
                    option3_label.place(x=500,y=415)
                    option3_entry=Entry(tpl_showque,width=50)
                    option3_entry.place(x=720,y=420)
                   
                    option4_label=Label(tpl_showque,text='Enter OPTION 4:',bg="#b4eef5",font=('Eras Bold ITC',15))
                    option4_label.place(x=500,y=465)
                    option4_entry=Entry(tpl_showque,width=50)
                    option4_entry.place(x=720,y=470)
                   
                    correctans_label=Label(tpl_showque,text="Enter CORRECT ANSWER",bg="skyblue",font=('Eras Bold ITC',13))
                    correctans_label.place(x=500,y=515)
                    correctans_entry=Entry(tpl_showque,width=50)
                    correctans_entry.place(x=720,y=520)
   
                    savebt=Button(tpl_showque,text="SAVE",width=10,bg="Yellow",command=savedata) #
                    savebt.place(x=500,y=600)
   
                    clearbt=Button(tpl_showque,text='CLEAR',width=10,bg="yellow",command=cleardata)  #
                    clearbt.place(x=600,y=600)
                # function for find the question and answer
                def showfind():
                        r=[]
                        def finddata():
                            db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                            cur=db.cursor()
                            a=questionno_cbox.get()
                            table=table_var.get()
                            sql=f"Select question,option1,option2,option3,option4,answer from {table} where question_id='%s'"%(a)
                            cur.execute(sql)
                            data=cur.fetchone()
                           
                            if data==None:
                                 subjectid_cbox.delete(0,100)
                                
                                 question_entry.delete(0,100)
                                 option1_entry.delete(0,100)
                                 option2_entry.delete(0,100)
                                 option3_entry.delete(0,100)
                                 option4_entry.delete(0,100)
                                 correctans_entry.delete(0,100)                                
                                 messagebox.showerror('Status','Not found')
                                
                            else:
                                
                                question_entry.delete(0,100)
                                option1_entry.delete(0,100)
                                option2_entry.delete(0,100)
                                option3_entry.delete(0,100)
                                option4_entry.delete(0,100)
                                correctans_entry.delete(0,100)
                               
                                question_entry.insert(0, data[0])
                                option1_entry.insert(0, data[1])
                                option2_entry.insert(0, data[2])
                                option3_entry.insert(0, data[3])
                                option4_entry.insert(0, data[4])
                                
                                correctans_entry.insert(0, data[5])
                                db.close()
                        def filldata():
                            table=table_var.get()
                            a=subjectid_cbox.get()
                            db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                            cur=db.cursor()
                            sql = "SELECT question_id FROM %s"%(a)




                            cur.execute(sql)
                            data=cur.fetchall()
                            for res in data:
                                  r.append(res[0])
                                  
                            db.close()                                
                        def cleardata():
                             
                             question_entry.delete(0,100)
                             option1_entry.delete(0,100)
                             option2_entry.delete(0,100)
                             option3_entry.delete(0,100)
                             option4_entry.delete(0,100)
                             correctans_entry.delete(0,100)                                
                        c5=Canvas(tpl_showque,width=1600,height=790,bg="#b4eef5")
                        c5.place(x=150,y=100)
                        table_var=StringVar()
                        subjectid_label=Label(tpl_showque,text="Select SUBJECT:",bg="skyblue",font=('Eras Bold ITC',15))
                        subjectid_label.place(x=500,y=160)
                        subjectid_cbox=ttk.Combobox(tpl_showque,textvariable=table_var,values=['java','mysql','python'],width=30)
                        subjectid_cbox.set("java")
                        subjectid_cbox.place(x=720,y=160)
                        questionno_label=Label(tpl_showque,text='Select QUESTION NO: ',bg="skyblue",font=('Eras Bold ITC',15))
                        questionno_label.place(x=500,y=215)
                        filldata()
                        questionno_cbox=ttk.Combobox(tpl_showque,width=30)
                        questionno_cbox['values']=r
                        questionno_cbox.set(1)
                        questionno_cbox.place(x=740,y=220)
                       
                        question_label=Label(tpl_showque,text="Enter Question:",bg="#b4eef5",font=('Eras Bold ITC',15))
                        question_label.place(x=500,y=265)
                        question_entry=Entry(tpl_showque,width=100)
                        question_entry.place(x=720,y=270)
                       
                        option1_label=Label(tpl_showque,text='Enter OPTION 1:',bg="#b4eef5",font=('Eras Bold ITC',15))
                        option1_label.place(x=500,y=315)
                        option1_entry=Entry(tpl_showque,width=50)
                        option1_entry.place(x=720,y=320)
                       
                        option2_label=Label(tpl_showque,text='Enter OPTION 2:',bg="#b4eef5",font=('Eras Bold ITC',15))
                        option2_label.place(x=500,y=365)
                        option2_entry=Entry(tpl_showque,width=50)
                        option2_entry.place(x=720,y=370)
                       
                        option3_label=Label(tpl_showque,text='Enter OPTION 3:',bg="#b4eef5",font=('Eras Bold ITC',15))
                        option3_label.place(x=500,y=415)
                        option3_entry=Entry(tpl_showque,width=50)
                        option3_entry.place(x=720,y=420)
                       
                        option4_label=Label(tpl_showque,text='Enter OPTION 4:',bg="#b4eef5",font=('Eras Bold ITC',15))
                        option4_label.place(x=500,y=465)
                        option4_entry=Entry(tpl_showque,width=50)
                        option4_entry.place(x=720,y=470)
                       
                        correctans_label=Label(tpl_showque,text="Enter CORRECT ANSWER",bg="skyblue",font=('Eras Bold ITC',13))
                        correctans_label.place(x=500,y=515)
                        correctans_entry=Entry(tpl_showque,width=50)
                        correctans_entry.place(x=720,y=520)                            
                        findbt=Button(tpl_showque,text="FIND",width=10,bg="Yellow",command=finddata) #,command=savedata
                        findbt.place(x=500,y=650)
       
                        clearbt=Button(tpl_showque,text='CLEAR',width=10,bg="yellow",command=cleardata)  #,command=cleardata
                        clearbt.place(x=600,y=650)              
                # function for delete the question
                def showdelete():
                       
                            r=[]
                            def deletedata():
                                        db=pymysql.connect(host="localhost",user="root",password="root",database="quiz_portal")
                                        cur=db.cursor()
                                        a=questionno_cbox.get()
                                        b=question_entry.get()
                                        c=option1_entry.get()
                                        d=option2_entry.get()
                                        e=option3_entry.get()
                                        f=option4_entry.get()
                                        g=correctans_entry.get()
                                        table=table_var
                                        if len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(g)==0:
                                            messagebox.showerror('status','CHECK DETAILS..')
                                            # minimize_window()
                                        else:
                                           
                                            db=pymysql.connect(host="localhost",user="root",password="root",database="quiz_portal")
                                            cur=db.cursor()
                                            a=questionno_cbox.get()
                                            table=table_var.get()
                                            sql=f"delete from {table} where question_id='%s'"%(a)
                                            cur.execute(sql)
                                            db.commit()
                                            question_entry.delete(0,100)
                                            option1_entry.delete(0,100)
                                            option2_entry.delete(0,100)
                                            option3_entry.delete(0,100)
                                            option4_entry.delete(0,100)
                                            correctans_entry.delete(0,100)
                                           
                                            messagebox.showinfo('Status','DELETED....')
                                           
                            def filldata():
                                        table=table_var.get()
                                        a=subjectid_cbox.get()
                                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                                        cur=db.cursor()
                                        sql = f"SELECT question_id FROM {a}"

           
           
           
           
                                        cur.execute(sql)
                                        data=cur.fetchall()
                                        for res in data:
                                              r.append(res[0])
                                        db.close()

                            def checkdata():
                                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                                        cur=db.cursor()
                                        a=questionno_cbox.get()
                                        table=table_var.get()
                                        sql=f"Select question,option1,option2,option3,option4,answer from {table} where question_id='%s'"%(a)
                                        cur.execute(sql)
                                        data=cur.fetchone()
                                       
                                        if data==None:
                                             # subjectid_cbox.delete(0,100)
                                             # questionno_cbox.delete(0,100)
                                             question_entry.delete(0,100)
                                             option1_entry.delete(0,100)
                                             option2_entry.delete(0,100)
                                             option3_entry.delete(0,100)
                                             option4_entry.delete(0,100)
                                             correctans_entry.delete(0,100)                                
                                             messagebox.showerror('Status','Not found')
                                            # minimize_window()
                                        else:
                                            # questionno_cbox.delete(0,100)
                                            question_entry.delete(0,100)
                                            option1_entry.delete(0,100)
                                            option2_entry.delete(0,100)
                                            option3_entry.delete(0,100)
                                            option4_entry.delete(0,100)
                                            correctans_entry.delete(0,100)
                                           
                                            question_entry.insert(0, data[0])
                                            option1_entry.insert(0, data[1])
                                            option2_entry.insert(0, data[2])
                                            option3_entry.insert(0, data[3])
                                            option4_entry.insert(0, data[4])
                                            # option1_entry.insert(0, data[5])
                                            correctans_entry.insert(0, data[5])
                                            db.close()
                            def cleardata():
                                        # questionno_cbox.delete(0,100)
                                        question_entry.delete(0,100)
                                        option1_entry.delete(0,100)
                                        option2_entry.delete(0,100)
                                        option3_entry.delete(0,100)
                                        option4_entry.delete(0,100)
                                        correctans_entry.delete(0,100)    

               

                           
                            c5=Canvas(tpl_showque,width=1600,height=790,bg="#b4eef5")
                            c5.place(x=150,y=100)
                            table_var=StringVar()
                            subjectid_label=Label(tpl_showque,text="Select SUBJECT ID:",bg="skyblue",font=('Eras Bold ITC',15))
                            subjectid_label.place(x=500,y=160)
                            subjectid_cbox=ttk.Combobox(tpl_showque,textvariable=table_var,values=['java','mysql','python'],width=30)
                            subjectid_cbox.set("java")
                            subjectid_cbox.place(x=720,y=160)
                           
                            questionno_label=Label(tpl_showque,text='Select QUESTION NO: ',bg="skyblue",font=('Eras Bold ITC',15))
                            questionno_label.place(x=500,y=215)
                            filldata()
                           
                            questionno_cbox=ttk.Combobox(tpl_showque,width=30)
                            questionno_cbox['values']=r
                            questionno_cbox.set(1)
                            questionno_cbox.place(x=740,y=220)
                           
                            question_label=Label(tpl_showque,text="Enter Question:",bg="#b4eef5",font=('Eras Bold ITC',15))
                            question_label.place(x=500,y=265)
                            question_entry=Entry(tpl_showque,width=100)
                            question_entry.place(x=720,y=270)
                           
                            option1_label=Label(tpl_showque,text='Enter OPTION 1:',bg="#b4eef5",font=('Eras Bold ITC',15))
                            option1_label.place(x=500,y=315)
                            option1_entry=Entry(tpl_showque,width=50)
                            option1_entry.place(x=720,y=320)
                           
                            option2_label=Label(tpl_showque,text='Enter OPTION 2:',bg="#b4eef5",font=('Eras Bold ITC',15))
                            option2_label.place(x=500,y=365)
                            option2_entry=Entry(tpl_showque,width=50)
                            option2_entry.place(x=720,y=370)
                           
                            option3_label=Label(tpl_showque,text='Enter OPTION 3:',bg="#b4eef5",font=('Eras Bold ITC',15))
                            option3_label.place(x=500,y=415)
                            option3_entry=Entry(tpl_showque,width=50)
                            option3_entry.place(x=720,y=420)
                           
                            option4_label=Label(tpl_showque,text='Enter OPTION 4:',bg="#b4eef5",font=('Eras Bold ITC',15))
                            option4_label.place(x=500,y=465)
                            option4_entry=Entry(tpl_showque,width=50)
                            option4_entry.place(x=720,y=470)
                           
                            correctans_label=Label(tpl_showque,text="Enter CORRECT ANSWER",bg="skyblue",font=('Eras Bold ITC',13))
                            correctans_label.place(x=500,y=515)
                            correctans_entry=Entry(tpl_showque,width=50)
                            correctans_entry.place(x=720,y=520)                            
                            findbt=Button(tpl_showque,text="DELETE",width=10,bg="Yellow",command=deletedata) #,command=deletedata
                            findbt.place(x=500,y=600)
           
                            clearbt=Button(tpl_showque,text='CLEAR',width=10,bg="yellow",command=cleardata)  #
                            clearbt.place(x=600,y=600)                        
                            search_button=Button(tpl_showque,text='CHECK DETAILS',bg='yellow',fg='black',font=('Algerian',9),command=checkdata)
                            search_button.place(x=1000,y=160)
                # function for changes and update the question
                def showupdate():
                            r=[]
                            def updatedata():
                                 db=pymysql.connect(host="localhost",user="root",password="root",database="quiz_portal")
                                 cur=db.cursor()
                                 a=questionno_cbox.get()
                                 
                                 b=question_entry.get()
                                 c=option1_entry.get()
                                 d=option2_entry.get()
                                 e=option3_entry.get()
                                 f=option4_entry.get()
                                 g=correctans_entry.get()
                                 table=table_var.get()
                                 if len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(g)==0:
                                     messagebox.showerror('status','check all values..')
                                     # minimize_window()
                                 elif not all((a, b, c,d,e,f,g)):
                                     messagebox.showerror('status', 'Fill remaining values')
                                     # minimize_window()
                                 else:
                                     sql = f"UPDATE {table} SET question='{b}', option1='{c}', option2='{d}', option3='{e}', option4='{f}', answer='{g}' WHERE question_id='{a}'"
    
                                     cur.execute(sql)
                                     messagebox.showinfo('Status','Update successfully...')
                                     # minimize_window()
                                     db.commit()
                             
                                     question_entry.delete(0,100)
                                     option1_entry.delete(0,100)
                                     option2_entry.delete(0,100)
                                     option3_entry.delete(0,100)
                                     option4_entry.delete(0,100)
                                     correctans_entry.delete(0,100)
                                 db.close()
                            
                            def filldata():
                                    table=table_var.get()
                                    a=subjectid_cbox.get()
                                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                                    cur=db.cursor()
                                    sql = f"SELECT question_id FROM {a}"

                                    cur.execute(sql)
                                    data=cur.fetchall()
                                    for res in data:
                                          r.append(res[0])
                                    db.close()
                            
                            def checkdata():
                                db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                                cur=db.cursor()
                                a=questionno_cbox.get()
                                table=table_var.get()
                                sql=f"Select question,option1,option2,option3,option4,answer from {table} where question_id='%s'"%(a)
                                cur.execute(sql)
                                data=cur.fetchone()
                               
                                if data==None:
                                     subjectid_cbox.delete(0,100)
                                     
                                     question_entry.delete(0,100)
                                     option1_entry.delete(0,100)
                                     option2_entry.delete(0,100)
                                     option3_entry.delete(0,100)
                                     option4_entry.delete(0,100)
                                     correctans_entry.delete(0,100)                                
                                     messagebox.showerror('Status','Not found')
                                    # minimize_window()
                                else:
                                   
                                    question_entry.delete(0,100)
                                    option1_entry.delete(0,100)
                                    option2_entry.delete(0,100)
                                    option3_entry.delete(0,100)
                                    option4_entry.delete(0,100)
                                    correctans_entry.delete(0,100)
                                   
                                    question_entry.insert(0, data[0])
                                    option1_entry.insert(0, data[1])
                                    option2_entry.insert(0, data[2])
                                    option3_entry.insert(0, data[3])
                                    option4_entry.insert(0, data[4])
                                    
                                    correctans_entry.insert(0, data[5])
                                    db.close()
                            def clear_ques():
                                 question_entry.delete(0,100)
                                 option1_entry.delete(0,100)
                                 option2_entry.delete(0,100)
                                 option3_entry.delete(0,100)
                                 option4_entry.delete(0,100)
                                 correctans_entry.delete(0,100)
                            c5=Canvas(tpl_showque,width=1600,height=790,bg="#b4eef5")
                            c5.place(x=150,y=100)
                            table_var=StringVar()
                            subjectid_label=Label(tpl_showque,text="Select SUBJECT ID:",bg="skyblue",font=('Eras Bold ITC',15))
                            subjectid_label.place(x=500,y=160)
                            subjectid_cbox=ttk.Combobox(tpl_showque,textvariable=table_var,values=['java','mysql','python'],width=30)
                            subjectid_cbox.set("java")
                            subjectid_cbox.place(x=720,y=160)
                           
                            questionno_label=Label(tpl_showque,text='Select QUESTION NO: ',bg="skyblue",font=('Eras Bold ITC',15))
                            questionno_label.place(x=500,y=215)
                            filldata()
                            questionno_cbox=ttk.Combobox(tpl_showque,width=30)
                            questionno_cbox['values']=r
                            questionno_cbox.set(1)
                            questionno_cbox.place(x=740,y=220)
                           
                            question_label=Label(tpl_showque,text="Enter Question:",bg="#b4eef5",font=('Eras Bold ITC',15))
                            question_label.place(x=500,y=265)
                            question_entry=Entry(tpl_showque,width=100)
                            question_entry.place(x=720,y=270)
                           
                            option1_label=Label(tpl_showque,text='Enter OPTION 1:',bg="#b4eef5",font=('Eras Bold ITC',15))
                            option1_label.place(x=500,y=315)
                            option1_entry=Entry(tpl_showque,width=50)
                            option1_entry.place(x=720,y=320)
                           
                            option2_label=Label(tpl_showque,text='Enter OPTION 2:',bg="#b4eef5",font=('Eras Bold ITC',15))
                            option2_label.place(x=500,y=365)
                            option2_entry=Entry(tpl_showque,width=50)
                            option2_entry.place(x=720,y=370)
                           
                            option3_label=Label(tpl_showque,text='Enter OPTION 3:',bg="#b4eef5",font=('Eras Bold ITC',15))
                            option3_label.place(x=500,y=415)
                            option3_entry=Entry(tpl_showque,width=50)
                            option3_entry.place(x=720,y=420)
                           
                            option4_label=Label(tpl_showque,text='Enter OPTION 4:',bg="#b4eef5",font=('Eras Bold ITC',15))
                            option4_label.place(x=500,y=465)
                            option4_entry=Entry(tpl_showque,width=50)
                            option4_entry.place(x=720,y=470)
                           
                            correctans_label=Label(tpl_showque,text="Enter CORRECT ANSWER",bg="skyblue",font=('Eras Bold ITC',13))
                            correctans_label.place(x=500,y=515)
                            correctans_entry=Entry(tpl_showque,width=50)
                            correctans_entry.place(x=720,y=520)                            
                            findbt=Button(tpl_showque,text="UPDATE",width=10,bg="Yellow",command=updatedata) #,command=deletedata
                            findbt.place(x=500,y=600)
           
                            clearbt=Button(tpl_showque,text='CLEAR',width=10,bg="yellow",command=clear_ques)  #,command=cleardata
                            clearbt.place(x=600,y=600)                        
                            search_button=Button(tpl_showque,text='CHECK DETAILS',bg='yellow',fg='black',font=('Algerian',9),command=checkdata)
                            search_button.place(x=1000,y=160)
                           
                adminlogin_label=Label(tpl_showque,text="QUESTIONS",bg="#5e65a1",fg="white",width=100,height=2,font=('comic sans ms',25))
                adminlogin_label.pack()          
                c3=Canvas(tpl_showque,width=150,height=800,bg="#5e65a1")
                c3.place(x=0,y=100)
                b1=Button(c3,text="FIND",fg="black",bg="yellow",font=('Algerian',15),width=10,command=showfind)  #,command=showfind
                b1.place(x=20,y=100)
                b2=Button(c3,text="INSERT",fg="black",bg="yellow",font=('Algerian',15),width=10,command=showsave)#,command=showsave
                b2.place(x=20,y=200)
                b3=Button(c3,text="DELETE",fg="black",bg="yellow",font=('Algerian',15),width=10,command=showdelete)   #,command=showdelete
                b3.place(x=20,y=300)
                b4=Button(c3,text="UPDATE",fg="black",bg="yellow",font=('Algerian',15),width=10,command=showupdate)    #,command=showupdate
                b4.place(x=20,y=400)
                tpl_showque.mainloop()
           
            # result section
            def resultdata():
                   
                tpl_result=Toplevel(tpl_adminselectdata)
                tpl_result.geometry("1600x1600")
                tpl_result.title("RESULT'S PORTAL")
                
                result_label=Label(tpl_result,text="RESULTS",bg="#5e65a1",fg="white",width=100,height=2,font=('comic sans ms',25))
                result_label.pack()
                # function for find the result
                def findresult():
                    
                    r=[]
                    def findresultdata():
                            db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                            cur=db.cursor()
                            a=userid_cbox.get()
                            table=subject_cbox.get()
                           
                            sql=f"Select total_score  from {table} where userid='%s'"%(a)
                            cur.execute(sql)
                            data=cur.fetchone()
                            if data==None:
                              subject_cbox.delete(0,100)
                              
                              userid_cbox.delete(0,100)
                              totalscore_entry.delete(0,100)
                                                             
                              messagebox.showerror('Status','Not found')
                            # minimize_window()
                            else:
                       
                                totalscore_entry.delete(0,100)
                               
                                totalscore_entry.insert(0, data[0])
                                
                                db.close()
                            
                    def filldata():
                          
                            a=subject_cbox.get()
                            db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                            cur=db.cursor()
                            sql = f"SELECT userid FROM {a}"
                            cur.execute(sql)
                            data=cur.fetchall()
                            for res in data:
                                  r.append(res[0])
                            db.close()
                    
                    def clearresultdata():
                         subject_cbox.delete(0,100)
                              
                         userid_cbox.delete(0,100)
                         totalscore_entry.delete(0,100)
                         

                    
                    resultfind_label=Label(c7,text='    Find Result   ',width=20,font=('Edwardian Script ITC',25),fg="white",bg='#5e65a1')
                    resultfind_label.place(x=420,y=20)
                    
                    subject_label=Label(c7,text="Select SUBJECT:",bg="#b4eef5",font=('Eras Bold ITC',15))
                    subject_label.place(x=400,y=120)
                    subject_cbox=ttk.Combobox(c7,values=['java_result','mysql_result','python_result'],width=30)
                    subject_cbox.set("python_result")
                    subject_cbox.place(x=600,y=125)
                    
                    userid_label=Label(c7,text='User Id: ',bg="#b4eef5",font=('Eras Bold ITC',15))
                    userid_label.place(x=400,y=150)
                    filldata()
                    userid_cbox=ttk.Combobox(c7,width=30)
                    userid_cbox['values']=r
                    userid_cbox.set(0)
                    userid_cbox.place(x=600,y=155)
                    
                    totalscore_label=Label(c7,text="Total Score:",bg='#b4eef5',font=("areial",15,"bold"))
                    totalscore_label.place(x=400,y=180)
                    totalscore_entry=Entry(c7,width=30)
                    totalscore_entry.place(x=600,y=185)
                    
                    findbt=Button(c7,text="FIND",width=10,bg="Yellow",font=('Algerian',12),command=findresultdata) 
                    findbt.place(x=500,y=250)
   
                    clearbt=Button(c7,text='CLEAR',width=10,bg="yellow",font=('Algerian',12),command=clearresultdata) 
                    clearbt.place(x=650,y=250)
                    
                c7=Canvas(tpl_result,width=1600,height=800,bg="#b4eef5")
                c7.place(x=150,y=100)
        
                c6=Canvas(tpl_result,width=150,height=800,bg="#5e65a1")
                c6.place(x=0,y=100)
                b1=Button(c6,text="FIND",fg="black",bg="yellow",font=('Algerian',15),width=10,command=findresult)  
                b1.place(x=20,y=100)
                # function for create graph
                def check_graph():
                    tpl_graph=Toplevel(tpl_result)
                    tpl_graph.geometry("1600x1600")
                    tpl_graph.title("Score Graph")
                    
                    
                    
                    def graphpy():
                        tpl_graphpy=Toplevel(tpl_result)
                        tpl_graphpy.geometry("1600x1600")
                        tpl_graphpy.title("PYTHON Graph")
                        tpl_graphpy.config(bg="#5e65a1")
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        
                        b=[]
                        c=[]
                        sql="select * from python_result"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            b.append(res[0])
                            c.append(res[1])
                        fig = plt.figure(figsize=(6,4), dpi=100)
                        fig.add_subplot(111).bar(b,c,color=['r','g','b','y'])
                        plt.close()
                        canvas = FigureCanvasTkAgg(fig, master=tpl_graphpy)
                        fig.patch.set_facecolor('skyblue')
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                        tpl_graphpy.mainloop()
                        
                    def graphj():
                        tpl_graphj=Toplevel(tpl_result)
                        tpl_graphj.geometry("1600x1600")
                        tpl_graphj.title("JAVA Graph")
                        tpl_graphj.config(bg="#5e65a1")
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        
                        b=[]
                        c=[]
                        sql="select * from java_result"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            b.append(res[0])
                            c.append(res[1])
                        fig = plt.figure(figsize=(6,4), dpi=100)
                        fig.patch.set_facecolor('skyblue')
                        fig.add_subplot(111).bar(b,c,color=['r','g','b','y'])
                        plt.close()
                        canvas = FigureCanvasTkAgg(fig, master=tpl_graphj)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                        tpl_graphj.mainloop()
                        
                    def graphm():
                        tpl_graphm=Toplevel(tpl_result)
                        tpl_graphm.geometry("1600x1600")
                        tpl_graphm.title("MySQL Graph")
                        tpl_graphm.config(bg="#5e65a1")
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        
                        b=[]
                        c=[]
                        sql="select * from mysql_result"
                        cur.execute(sql)
                        data=cur.fetchall()
                        for res in data:
                            b.append(res[0])
                            c.append(res[1])
                        fig = plt.figure(figsize=(6,4), dpi=100)
                        fig.patch.set_facecolor('skyblue')
                        fig.add_subplot(111).bar(b,c,color=['r','g','b','y'])
                        plt.close()
                        canvas = FigureCanvasTkAgg(fig, master=tpl_graphm)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                        tpl_graphm.mainloop()
                    
                    
                    c7graph=Canvas(tpl_graph,width=1600,height=800,bg="#b4eef5")
                    c7graph.place(x=0,y=0)
                    cnvgraph=Canvas(c7graph,height=100,width=1700,bg='#5e65a1')
                    cnvgraph.place(x=0,y=0)
                    welcome_label=Label(cnvgraph,text="RESULT GRAPHS",font=("comic sans ms",35),bg='#5e65a1',fg="white")
                    welcome_label.place(x=600,y=5)
                    
                    btp=Button(tpl_graph,text="Python Graph",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=graphpy)
                    btp.place(x=300,y=300)
                    btj=Button(tpl_graph,text="Java Graph",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=graphj)
                    btj.place(x=700,y=300)
                    btm=Button(tpl_graph,text="MySQL Graph",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=graphm)
                    btm.place(x=1100,y=300)
                    tpl_graph.mainloop()
                b2=Button(c6,text="CHECK GRAPH",fg="black",bg="yellow",font=('Bold',10),width=15,height=2,command=check_graph)  
                b2.place(x=20,y=200)
                
                
                tpl_result.mainloop()
 
            queans_bt=Button(tpl_adminselectdata,text="QUE/ANS",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=showquestionsdata)
            queans_bt.place(x=800,y=350)
            results_bt=Button(tpl_adminselectdata,text="RESULTS",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=resultdata)
            results_bt.place(x=1100,y=350)
            
            
            
            
            
            tpl_adminselectdata.mainloop()
        else:
            messagebox.showerror("STATUS","Wrong Credentials...")
           
        
    def backbtadlogin():
        tpl_adminlogin.destroy()
    # foction for on click show password    
    def password_visibility1():
        if password_entry1['show'] == '':
            password_entry1['show'] = '*'
        else:
            password_entry1['show'] = ''
    
 
    c1=Canvas(tpl_adminlogin,width=1600,height=800,bg="#b4eef5")
    c1.place(x=0,y=0)

    adminlogin_label=Label(tpl_adminlogin,text="Admin Login",bg="#5e65a1",fg="white",width=300,height=2,font=('comic sans ms',30))
    adminlogin_label.pack()

    adminname_label=Label(tpl_adminlogin,text="Admin ID",bg='#b4eef5',font=("areial",15,"bold"))
    adminname_label.place(x=500,y=220)
    adminname_entry1=Entry(tpl_adminlogin,width=40)
    adminname_entry1.place(x=700,y=223)

    password_label=Label(tpl_adminlogin,text="Password",bg='#b4eef5',font=("areial",15,"bold"))
    password_label.place(x=500,y=270)
    password_entry1=Entry(tpl_adminlogin,width=40,show="*")
    password_entry1.place(x=700,y=273)
    show_password_btn = tk.Checkbutton(tpl_adminlogin, text="Show Password",bg='#b4eef5',font=("areial",10,"bold"))
    show_password_btn.config(command=password_visibility1)
    show_password_btn.place(x=695, y=310)

    login_bt=Button(tpl_adminlogin,text="Login",width=15,font=3,bg="yellow",fg="black",command=adminselectdata)
    login_bt.place(x=500,y=350)

    back_bt=Button(tpl_adminlogin,text="Back",width=15,font=3,bg="yellow",fg="black",command=backbtadlogin)
    back_bt.place(x=750,y=350)
    tpl_adminlogin.mainloop()

            
    
c1=Canvas(t,height=60,width=1700,bg='#5e65a1')
c1.place(x=0,y=0)
welcome_label=Label(c1,text="WELCOME TO QUIZ PORTAL",font=("comic sans ms",28),bg='#5e65a1',fg="white")
welcome_label.place(x=500,y=3)

admin_button=Button(c1,text='Admin Login',bg='yellow',width=15,command=adminlogin)
admin_button.place(x=1200,y=20)


# signup tkinter
def usersignup():
    
    tpl_usersignup=Toplevel(t)
    tpl_usersignup.geometry("1700x1700")
    tpl_usersignup.title("User Sign up details")
    minimize()
    
    
    # function for create strong password
    def is_valid_password(password):
    # Check if the password meets the minimum length requirement
        if len(password) < 8:
            return False
        
        # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
        if not re.search(r'[A-Z]', password) or \
           not re.search(r'[a-z]', password) or \
           not re.search(r'\d', password):
            return False
        
        # Check if the password contains at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        
        # else:
        return True
    # function for check valid mail 
    def is_valid_mail(mail):
        if not re.search(r"[@,.com]",mail):
            return False
        return True
    def generate_otp(mobile_number):
    # Check if the mobile number is valid
        if not re.match(r"^[6-9]\d{9}$", mobile_number):
            raise ValueError("Invalid mobile number")
    
    # Generate the OTP
        otp = random.randint(1000, 9999)
        return otp
    def verify_otp(mobile_number):
        while True:
        # Get the mobile number and generate OTP
                # mobile_number = g
                try:
                    generated_otp = generate_otp(mobile_number)
                    print("Your OTP is:", generated_otp)
                except ValueError as e:
                    messagebox.showerror("Status", str(e))
                    return
        
                # Get the OTP from the user
                user_otp = simpledialog.askstring(title="Enter OTP", prompt="Please enter the OTP received on your mobile number:")
        
                # Check if the OTP is correct
                if user_otp == str(generated_otp):
                    break
                else:
                    choice = messagebox.askquestion("OTP Incorrect", "The OTP you entered is incorrect. Do you want to try again?")
                    if choice == "no":
                        return


    def usersavedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
            cur=db.cursor()
            a=userid_entry.get()
            b=userpassword_entry.get()
            c=username_entry.get()
            d=useradress_entry.get()
            e=usercity_entry.get()
            f=useremail_entry.get()
            g=userphon_entry.get()
            h=usergovid_cbox.get()
            j=usergovidno_entry.get()
            
            

    
            if not is_valid_mail(f):
                messagebox.showerror("Status","Invalid Email Address Please Check Email ID")
                useremail_entry.delete(0,100)
                return
            
            if len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0 or len(g)==0 or len(h)==0 or len(j)==0:
                messagebox.showerror('status','check details..')
            else:
                if not is_valid_password(b):
                    messagebox.showerror('status', 'Please choose a password that contains at least 8 characters including uppercase and lowercase letters, digits, and special characters.')
                    userpassword_entry.delete(0,100)
                    return
                verify_otp(g)
               

                sql="select * from userinfo where userid ='%s'"%a
                cur.execute(sql)
                result = cur.fetchone()
            if  result is not None:
                messagebox.showerror("status","User ID already exists")
                username_entry.delete(0,100)
                useremail_entry.delete(0,100)
                userphon_entry.delete(0,100)
                usercity_entry.delete(0,100)
                userid_entry.delete(0,100)
                userpassword_entry.delete(0,100)
                usergovid_cbox.delete(0,100)
                usergovidno_entry.delete(0,100)
                useradress_entry.delete(0,100)
            else:
                mobile_number = userphon_entry.get()
                try:
                    generated_otp = generate_otp(mobile_number)
                    print("Your OTP is:", generated_otp)
                except ValueError as e:
                    messagebox.showerror("Status", str(e))
                    return
                sql="insert into userinfo values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g,h,j)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Status','Data Saved...')
                username_entry.delete(0,100)
                useremail_entry.delete(0,100)
                userphon_entry.delete(0,100)
                usercity_entry.delete(0,100)
                userid_entry.delete(0,100)
                userpassword_entry.delete(0,100)
                usergovid_cbox.delete(0,100)
                usergovidno_entry.delete(0,100)
                useradress_entry.delete(0,100)
                db.close()
                sendingmail(f, a, b)
                messagebox.showinfo("Status","Mail Send ")
                
            
                # sendingmail(f,a,b)
                
    
    
    def backtologin():
        tpl_usersignup.destroy()
        
    def userclear():
        username_entry.delete(0,100)
        useremail_entry.delete(0,100)
        userphon_entry.delete(0,100)
        usercity_entry.delete(0,100)
        userid_entry.delete(0,100)
        userpassword_entry.delete(0,100)
        usergovid_cbox.delete(0,100)
        usergovidno_entry.delete(0,100)
        useradress_entry.delete(0,100)
    def usersearchid():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=userid_entry.get()
                        sql="select count(*) from userinfo where user_id='%s'"%(a)
                        cur=db.cursor()
                        cur.execute(sql)
                        data=cur.fetchone()
                        x=data[0]
                        if x==0:
                            lblstatususer.config(text='OK GO AHEAD',bg='blue',fg='white')
                        else:
                            lblstatususer.config(text='ALREADY PRESENT',bg='red',fg='white')    

    
    c1=Canvas(tpl_usersignup,width=1600,height=800,bg="#b4eef5")
    c1.place(x=0,y=0)
    
    usersignup_label=Label(tpl_usersignup,text="User Sign Up",bg="#5e65a1",fg="white",width=300,height=2,font=('comic sans ms',30))
    usersignup_label.pack()
    
    btnsearchuser=Button(tpl_usersignup,text='Search',bg="blue",fg="white",command=usersearchid)    
    btnsearchuser.place(x=1000,y=220)
    lblstatususer=Label(tpl_usersignup,text='status',fg='yellow',bg='red')
    lblstatususer.place(x=1100,y=220)
    
    username_label=Label(tpl_usersignup,text="Name",bg='#b4eef5',font=("areial",15,"bold"))
    username_label.place(x=500,y=220)
    username_entry=Entry(tpl_usersignup,width=40)
    username_entry.place(x=700,y=223)

    useremail_label=Label(tpl_usersignup,text="Email",bg='#b4eef5',font=("areial",15,"bold"))
    useremail_label.place(x=500,y=265)
    useremail_entry=Entry(tpl_usersignup,width=40)
    useremail_entry.place(x=700,y=268)
    
    userphon_label=Label(tpl_usersignup,text="Phone NO.",bg='#b4eef5',font=("areial",15,"bold"))
    userphon_label.place(x=500,y=310)
    userphon_entry=Entry(tpl_usersignup,width=40)
    userphon_entry.place(x=700,y=313)
    
    useradress_label=Label(tpl_usersignup,text="Address",bg='#b4eef5',font=("areial",15,"bold"))
    useradress_label.place(x=500,y=355)
    useradress_entry=Entry(tpl_usersignup,width=40)
    useradress_entry.place(x=700,y=358)
    
    usercity_label=Label(tpl_usersignup,text="City",bg='#b4eef5',font=("areial",15,"bold"))
    usercity_label.place(x=500,y=400)
    usercity_entry=Entry(tpl_usersignup,width=40)
    usercity_entry.place(x=700,y=403)
    
    usergovid_label=Label(tpl_usersignup,text="Gov Id",bg='#b4eef5',font=("areial",15,"bold"))
    usergovid_label.place(x=500,y=445)
    
    usergovid_cbox=ttk.Combobox(tpl_usersignup,width=40)
    govid=('Adharcard',"Voter ID",'Driving Licence')
    usergovid_cbox['values']=govid
    usergovid_cbox.place(x=700,y=445)
    
    usergovidno_label=Label(tpl_usersignup,text="Gov Id No",bg='#b4eef5',font=("areial",15,"bold"))
    usergovidno_label.place(x=500,y=490)
    usergovidno_entry=Entry(tpl_usersignup,width=40)
    usergovidno_entry.place(x=700,y=493)
    
    userid_label=Label(tpl_usersignup,text="Create User Id",bg='#b4eef5',font=("areial",15,"bold"))
    userid_label.place(x=500,y=535)
    userid_entry=Entry(tpl_usersignup,width=40)
    userid_entry.place(x=700,y=538)
    
    userpassword_label=Label(tpl_usersignup,text="Create password",bg='#b4eef5',font=("areial",15,"bold"))
    userpassword_label.place(x=500,y=580)
    userpassword_entry=Entry(tpl_usersignup,width=40)
    userpassword_entry.place(x=700,y=583)
    
    usersignup_bt=Button(tpl_usersignup,text="Save",width=15,font=3,bg="yellow",fg="black",command=usersavedata)
    usersignup_bt.place(x=500,y=630)

    userback_bt=Button(tpl_usersignup,text="Back",width=15,font=3,bg="yellow",fg="black",command=backtologin)
    userback_bt.place(x=750,y=630)
    
    userclear_bt=Button(tpl_usersignup,text="Clear",width=15,font=3,bg="yellow",fg="black",command=userclear)
    userclear_bt.place(x=1000,y=630)
    
    
    tpl_usersignup.mainloop()

    


# user login
def check_login():
    username=username_entry.get()
    password1=password_entryun.get()
    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
    cur=db.cursor()
    sql = "SELECT userid, upassword ,email FROM userinfo WHERE userid = '%s'" % (username)
    cur.execute(sql)
    result=cur.fetchone()
    
        
    db.close()
    

    
        
    if result is not None and username == result[0] and password1 == result[1]:
        
        tpl_userportal=Toplevel(t)
        tpl_userportal.geometry("1700x1700")
        tpl_userportal.title("User Sign up details")
        
        
        c1=Canvas(tpl_userportal,width=1600,height=800,bg="#b4eef5")
        c1.place(x=0,y=0)
        
        cs1=Canvas(tpl_userportal,height=90,width=1700,bg='#5e65a1')
        cs1.place(x=0,y=0)
        
        userportal_label=Label(tpl_userportal,text="User portal",bg="#5e65a1",fg="white",width=300,height=2,font=('comic sans ms',30))
        userportal_label.pack()
        def quizbt():
            tpl_quizportal=Toplevel(t)
            tpl_quizportal.geometry("1700x1700")
            tpl_quizportal.title("User Sign up details")
            
            c1=Canvas(tpl_quizportal,width=1600,height=800,bg="#b4eef5")
            c1.place(x=0,y=0)
        
            cs1=Canvas(tpl_quizportal,height=90,width=1700,bg='#5e65a1')
            cs1.place(x=0,y=0)
            
            subjectportal_label=Label(tpl_quizportal,text="Choose Subject",bg="#5e65a1",fg="white",width=300,height=2,font=('comic sans ms',30))
            subjectportal_label.pack()
            # function for python quiz and show the question and option            
            def python():
                tpl_python=Toplevel(t)
                tpl_python.geometry("1700x1700")
                tpl_python.config(bg="skyblue")
                tpl_python.title("Quiz Portal")
                minimize()
                question=[]
                answer=[]
                option1=[]
                option2=[]
                option3=[]
                option4=[]
                optans=''
                ans1,ans2,ans3,ans4='','','',''
                cans=''
                
                global i
                i=0
                global score
                score=0
                def loaddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    sql="select question,answer,option1,option2,option3,option4 from  python"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        question.append(res[0])
                        answer.append(res[1])
                        option1.append(res[2])
                        option2.append(res[3])
                        option3.append(res[4])
                        option4.append(res[5])
                        
                def filldata():
                    a.config(text=question[i])
                    b.config(text=answer[i])
           
                def nextdata():
                    global i
                    i=i+1
                    if i < len(question):
                        if not x.get():
                            messagebox.showerror("Error", "Please select an option.")
                            i = i - 1
                            return
                        
                        x.set(0)
                        
                        a.config(text=question[i])
                        b.config(text=answer[i])
                        filloptions()

                        
                    else:
                        
                        
                        a.config(text="**** END OF QUIZ******")
                        b.config(text='')
                        r1.destroy()
                        r2.destroy()
                        r3.destroy()
                        r4.destroy()
                        bt.destroy()
                        # bt1.destroy()
                        checkresult.destroy()
               
                        if score == len(question):
                            
            
                            message = f"Congratulations! You got all the answers correct \n Your Total Score is {score} out of {len(question)}"
                            result_message1 = Label(tpl_python, text=message, font=("Aerial", 20), bg="skyblue", fg="white")
                            result_message1.place(x=300, y=300)
                            closebt=Button(tpl_python,text="Save data",width=10,height=2,bg="yellow",command=insertresultp)
                            closebt.place(x=800,y=500)
                        else:
                            message = f"You got {score} out of {len(question)} questions correct. Keep it up!"
                            result_message = Label(tpl_python, text=message, font=("Aerial", 20), bg="skyblue", fg="white")
                            result_message.place(x=300, y=300)
                            closebt=Button(tpl_python,text="Save data",width=10,height=2,bg="yellow",command=insertresultp)
                            closebt.place(x=800,y=500)

                        
                        
                    
                def filloptions():
                    
                   
                    r1.config(text=option1[i])
                    r2.config(text=option2[i])
                    r3.config(text=option3[i])
                    r4.config(text=option4[i])
                    
                    
                    ans1=r1['text']
                    ans2=r2['text']
                    ans3=r3['text']
                    ans4=r4['text']
                    
                
                def choose1():
                    global optans
                    optans=r1['text']
                    checkanswer()
                def choose2():
                    global optans
                    optans=r2['text']
                    checkanswer()
                def choose3():
                    global optans
                    optans=r3['text']
                    checkanswer()
                def choose4():
                    global optans
                    optans=r4['text']
                    checkanswer()
                def checkanswer():
                    
                    w=b['text']
                    global optans
                    global score
                    if w==optans:

                        
                        score=score+1


                
                    else:
                       
                        score=score
                
                def putans():
                    ww=int(x.get())
                    if ww==1:
                        ansjava.append()
                
                
                def resultpython():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    user = username_entry.get()
                    sql = f"SELECT COUNT(*) FROM python_result WHERE userid = '{user}'"
                    cur.execute(sql)
                    result = cur.fetchone()
                    if result[0] > 0:
                        messagebox.showinfo('Status', 'You have already attempted the quiz.')
                        tpl_python.destroy()
                        # return True
                    
                        
                        
                    db.close()    
                # function for submint all the answer then show the score
                def insertresultp():
                        totalscore = score
                        # loaddata()
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        user = username_entry.get()
                        # email=usermail_entry.get()
                        
                       
                        sql=f"insert into python_result (userid,total_score) values('%s','%d')"%(user,totalscore)
                        cur.execute(sql)
                        db.commit()
                        messagebox.showinfo('Status','Data Saved...')
                        # sendingmailresult(email,score)
                        tpl_python.destroy()

                        db.close()
                    

                def closeall():
                    t.destroy()
                
                    
                    
                resultpython()    
                loaddata()
                    
                a=Label(tpl_python,font=("Times new Roman",25),bg="#5e65a1",fg="white")
                a.place(x=250,y=150)
                rsc=Label(tpl_python,width=20,height=2)
                rsc.place(x=1200,y=20)
                
                checkresult=Label(tpl_python,width=10,font=("areial",20),bg="skyblue")
                
                checkresult.place(x=1200,y=85)
                x=IntVar()
                
                c1=Canvas(tpl_python,height=60,width=1700,bg='#5e65a1')
                c1.place(x=0,y=0)
                welcome_label=Label(c1,text="WELCOME TO QUIZ PORTAL",font=("comic sans ms",28),bg='#5e65a1',fg="white")
                welcome_label.place(x=500,y=3)
               
                r1=Radiobutton(tpl_python,font=("Areial",15),bg="skyblue",variable=x,value=1,command=choose1)
                r1.place(x=250,y=250)
                r2=Radiobutton(tpl_python,font=("Areial",15),bg="skyblue",variable=x,value=2,command=choose2)
                r2.place(x=250,y=300)
                r3=Radiobutton(tpl_python,font=("Areial",15),bg="skyblue",variable=x,value=3,command=choose3)
                r3.place(x=250,y=350)
                r4=Radiobutton(tpl_python,font=("Areial",15),bg="skyblue",variable=x,value=4,command=choose4)
                r4.place(x=250,y=400)
                b=Label(tpl_python,bg="skyblue")
                b.place(x=1300,y=750)
                filloptions()
                
                filldata()
                
                bt=Button(tpl_python,text="Next",width=10,height=2,bg="yellow",command=nextdata)
                bt.place(x=300,y=500)

                
                
                tpl_python.mainloop()
                
            
            python_bt=Button(tpl_quizportal,text="PYTHON",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=python)
            python_bt.place(x=350,y=300)
            
            # function for java quiz and show the question and option
            def javaq():
                tpl_java=Toplevel(t)
                tpl_java.geometry("1700x1700")
                tpl_java.config(bg="skyblue")
                tpl_java.title("Quiz Portal")
                
                minimize()
                question=[]
                answer=[]
                option1=[]
                option2=[]
                option3=[]
                option4=[]
                optans=''
                ans1,ans2,ans3,ans4='','','',''
                cans=''
                
                global i
                i=0
                global score
                score=0
                
                def loaddata():
      
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    sql="select question,answer,option1,option2,option3,option4 from  java"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        question.append(res[0])
                        answer.append(res[1])
                        option1.append(res[2])
                        option2.append(res[3])
                        option3.append(res[4])
                        option4.append(res[5])
                        
                def filldata():
                    a.config(text=question[i])
                    b.config(text=answer[i])
                    
                def nextdata():
                    global i
                    i=i+1
                    if i < len(question):
                        if not x.get():
                            messagebox.showerror("Error", "Please select an option.")
                            i = i - 1
                            return
                        
                        x.set(0)
                        # filldata()
                        a.config(text=question[i])
                        b.config(text=answer[i])
                        filloptions()
                       
                    
                        
                    else:
                        
                        
                        a.config(text="**** END OF QUIZ******")
                        b.config(text='')
                        r1.destroy()
                        r2.destroy()
                        r3.destroy()
                        r4.destroy()
                        bt.destroy()
                        
                        checkresult.destroy()
                        
                        if score == len(question):
            
                                message = f"Congratulations! You got all the answers correct \n Your Total Score is {score} out of {len(question)}"
                                result_message1 = Label(tpl_java, text=message, font=("Aerial", 20), bg="skyblue", fg="white")
                                result_message1.place(x=300, y=300)
                                closebt=Button(tpl_java,text="Save data",width=10,height=2,bg="yellow",command=insertresultj)
                                closebt.place(x=800,y=500)
                                
                        else:
                                message = f"You got {score} out of {len(question)} questions correct. Keep it up!"
                                result_message = Label(tpl_java, text=message, font=("Aerial", 20), bg="purple", fg="white")
                                result_message.place(x=300, y=300)
                                
                                closebt=Button(tpl_java,text="Save data",width=10,height=2,bg="yellow",command=insertresultj)
                                closebt.place(x=800,y=500)      
     
                        
                        
                    
                def filloptions():
                
                   
                    r1.config(text=option1[i])
                    r2.config(text=option2[i])
                    r3.config(text=option3[i])
                    r4.config(text=option4[i])
                    
                    
                    ans1=r1['text']
                    ans2=r2['text']
                    ans3=r3['text']
                    ans4=r4['text']
                    
                
                def choose1():
                    global optans
                    optans=r1['text']
                    checkanswer()
                def choose2():
                    global optans
                    optans=r2['text']
                    checkanswer()
                def choose3():
                    global optans
                    optans=r3['text']
                    checkanswer()
                def choose4():
                    global optans
                    optans=r4['text']
                    checkanswer()
                def checkanswer():
                    
                    w=b['text']
                    global optans
                    if w==optans:
                        
                        global score
                        
                        score=score+1
                
                    else:
                        
                        score=score
                
                def putans():
                    ww=int(x.get())
                    if ww==1:
                        ansjava.append()
                        
                        
                def resultjava():

                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    user = username_entry.get()
                    sql = f"SELECT COUNT(*) FROM java_result WHERE userid = '{user}'"
                    cur.execute(sql)
                    result = cur.fetchone()
                    if result[0] > 0:
                        messagebox.showinfo('Status', 'You have already attempted the quiz.')
                        tpl_java.destroy()
                        
   
                def insertresultj():
                    totalscore = score
                    # loaddata()
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    user = username_entry.get()
                   
                  
        
                
                  
                    sql=f"insert into java_result (userid,total_score) values('%s','%d')"%(user,totalscore)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Status','Data Saved...')
                    tpl_java.destroy()
                    
                                
                
                def closeall():
                    tpl_java.destroy()
                    
                resultjava()
                loaddata()

                    
                a=Label(tpl_java,font=("Times new Roman",25),bg="#5e65a1",fg="white")
                a.place(x=250,y=150)
                rsc=Label(tpl_java,width=20,height=2)
                rsc.place(x=1200,y=20)
                   
                checkresult=Label(tpl_java,width=10,font=("areial",20),bg="skyblue")
                   
                checkresult.place(x=1200,y=85)
                x=IntVar()
                 
                c1=Canvas(tpl_java,height=60,width=1700,bg='#5e65a1')
                c1.place(x=0,y=0)
                welcome_label=Label(c1,text="WELCOME TO QUIZ PORTAL",font=("comic sans ms",28),bg='#5e65a1',fg="white")
                welcome_label.place(x=500,y=3)
                
                r1=Radiobutton(tpl_java,font=("Areial",15),bg="skyblue",variable=x,value=1,command=choose1)
                r1.place(x=250,y=250)
                r2=Radiobutton(tpl_java,font=("Areial",15),bg="skyblue",variable=x,value=2,command=choose2)
                r2.place(x=250,y=300)
                r3=Radiobutton(tpl_java,font=("Areial",15),bg="skyblue",variable=x,value=3,command=choose3)
                r3.place(x=250,y=350)
                r4=Radiobutton(tpl_java,font=("Areial",15),bg="skyblue",variable=x,value=4,command=choose4)
                r4.place(x=250,y=400)
                b=Label(tpl_java,bg="skyblue")
                b.place(x=1300,y=750)
                filloptions()
                
                filldata()
                resultjava()
                bt=Button(tpl_java,text="Next",width=10,height=2,bg="yellow",command=nextdata)
                bt.place(x=300,y=500)
                 
                
                
                tpl_java.mainloop()
                


            
            java_bt=Button(tpl_quizportal,text="JAVA",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=javaq)
            java_bt.place(x=650,y=300)
            
            # function for mysql quiz and show the question and option            
            def mysql():
                tpl_mysql=Toplevel(t)
                tpl_mysql.geometry("1700x1700")
                tpl_mysql.config(bg="skyblue")
                tpl_mysql.title("Quiz Portal")
                minimize()
                question=[]
                answer=[]
                option1=[]
                option2=[]
                option3=[]
                option4=[]
                optans=''
                ans1,ans2,ans3,ans4='','','',''
                cans=''
                
                global i
                i=0
                global score
                score=0
                def loaddata():
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    sql="select question,answer,option1,option2,option3,option4 from  mysql"
                    cur.execute(sql)
                    data=cur.fetchall()
                    for res in data:
                        question.append(res[0])
                        answer.append(res[1])
                        option1.append(res[2])
                        option2.append(res[3])
                        option3.append(res[4])
                        option4.append(res[5])
                        
                def filldata():
                    a.config(text=question[i])
                    b.config(text=answer[i])
             
                def nextdata():
                    global i
                    i=i+1
                    if i < len(question):
                        if not x.get():
                            messagebox.showerror("Error", "Please select an option.")
                            i = i - 1
                            return
                        
                        x.set(0)
                        # filldata()
                        a.config(text=question[i])
                        b.config(text=answer[i])
                        filloptions()
                       
                       
                        
                    else:
                        
                        
                        a.config(text="**** END OF QUIZ******")
                        b.config(text='')
                        r1.destroy()
                        r2.destroy()
                        r3.destroy()
                        r4.destroy()
                        bt.destroy()
                        # bt1.destroy()
                        checkresult.destroy()
                        # score_lbl.destroy()
                        if score == len(question):
            
                                message = f"Congratulations! You got all the answers correct \n Your Total Score is {score} out of {len(question)}"
                                result_message1 = Label(tpl_mysql, text=message, font=("Aerial", 20), bg="skyblue", fg="white")
                                result_message1.place(x=300, y=300)
                                closebt=Button(tpl_mysql,text="Save data",width=10,height=2,bg="yellow",command=insertresultm)
                                closebt.place(x=800,y=500)
                        else:
                                message = f"You got {score} out of {len(question)} questions correct. Keep it up!"
                                result_message = Label(tpl_mysql, text=message, font=("Aerial", 20), bg="skyblue", fg="white")
                                result_message.place(x=300, y=300)
                                closebt=Button(tpl_mysql,text="Save data",width=10,height=2,bg="yellow",command=insertresultm)
                                closebt.place(x=800,y=500)
       
                        
                        
                    
                def filloptions():
                
                   
                    r1.config(text=option1[i])
                    r2.config(text=option2[i])
                    r3.config(text=option3[i])
                    r4.config(text=option4[i])
                   
                    
                    ans1=r1['text']
                    ans2=r2['text']
                    ans3=r3['text']
                    ans4=r4['text']
                    
                
                def choose1():
                    global optans
                    optans=r1['text']
                    checkanswer()
                def choose2():
                    global optans
                    optans=r2['text']
                    checkanswer()
                def choose3():
                    global optans
                    optans=r3['text']
                    checkanswer()
                def choose4():
                    global optans
                    optans=r4['text']
                    checkanswer()
                def checkanswer():
                    
                    w=b['text']
                    global optans
                    if w==optans:
                       
                        global score
                        
                        score=score+1
                
                    else:
                        # messagebox.showinfo("Status","Wrong answer")
                        score=score
                
                def putans():
                    ww=int(x.get())
                    if ww==1:
                        ansjava.append()
                
                
                def resultmysql():
                     db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                     cur=db.cursor()
                     user = username_entry.get()
                     sql = f"SELECT COUNT(*) FROM mysql_result WHERE userid = '{user}'"
                     cur.execute(sql)
                     result = cur.fetchone()
                     if result[0] > 0:
                        messagebox.showinfo('Status', 'You have already attempted the quiz.')
                        tpl_mysql.destroy()
                        
                def insertresultm():
                    totalscore = score
                    # loaddata()
                    db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                    cur=db.cursor()
                    user = username_entry.get()
                     
                       
                    sql=f"insert into mysql_result (userid,total_score) values('%s','%d')"%(user,totalscore)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Status','Data Saved...')
                    tpl_mysql.destroy()
                    
                        
                
                def closeall():
                    t.destroy()
                    
                resultmysql()   
                loaddata()
                    
                a=Label(tpl_mysql,font=("Times new Roman",25),bg="#5e65a1",fg="white")
                a.place(x=250,y=150)
                rsc=Label(tpl_mysql,width=20,height=2)
                rsc.place(x=1200,y=20)
                
                checkresult=Label(tpl_mysql,width=10,font=("areial",20),bg="skyblue")
                
                checkresult.place(x=1200,y=85)
                x=IntVar()
                
                c1=Canvas(tpl_mysql,height=60,width=1700,bg='#5e65a1')
                c1.place(x=0,y=0)
                welcome_label=Label(c1,text="WELCOME TO QUIZ PORTAL",font=("comic sans ms",28),bg='#5e65a1',fg="white")
                welcome_label.place(x=500,y=3)
     
                r1=Radiobutton(tpl_mysql,font=("Areial",15),bg="skyblue",variable=x,value=1,command=choose1)
                r1.place(x=250,y=250)
                r2=Radiobutton(tpl_mysql,font=("Areial",15),bg="skyblue",variable=x,value=2,command=choose2)
                r2.place(x=250,y=300)
                r3=Radiobutton(tpl_mysql,font=("Areial",15),bg="skyblue",variable=x,value=3,command=choose3)
                r3.place(x=250,y=350)
                r4=Radiobutton(tpl_mysql,font=("Areial",15),bg="skyblue",variable=x,value=4,command=choose4)
                r4.place(x=250,y=400)
                b=Label(tpl_mysql,bg="skyblue")
                b.place(x=1300,y=750)
                filloptions()
                
                filldata()
                bt=Button(tpl_mysql,text="Next",width=10,height=2,bg="yellow",command=nextdata)
                bt.place(x=300,y=500)
                tpl_mysql.mainloop()
            
            
            
            mysql_bt=Button(tpl_quizportal,text="MySQl",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=mysql)
            mysql_bt.place(x=950,y=300)
        
        
            tpl_quizportal.mainloop()
            
            
        userquiz_bt=Button(c1,text="QUIZ",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=quizbt)
        userquiz_bt.place(x=450,y=300)
        # If the user wants to see the result again, this function has been created for this.
        def showresult():
            tpl_showresult=Toplevel(tpl_userportal)
            tpl_showresult.geometry("1700x1700")
            tpl_showresult.title("Show Result")
            minimize()
            
           
            def finddata():
                        db=pymysql.connect(host='localhost',user='root',password='root',database='quiz_portal')
                        cur=db.cursor()
                        a=username_entry.get()
                       
                        table=subject_cbox.get()
                        sql=f"Select total_score from {table} where userid='%s'"%(a)
                        cur.execute(sql)
                        data=cur.fetchone()
                       
                        if data==None:
                             subject_cbox.delete(0,100)
                            
                                                             
                             messagebox.showerror('Status','Not found')
                            
                        else:
                           
                            
                            message = f"Your Total Score is {data[0]} out of 10"
                            result_message1 = Label(c1, text=message, font=("Aerial", 20),width=50 ,bg="purple", fg="white")
                            result_message1.place(x=300, y=400)
                            db.close()
                                         
            def cleardata():
                         # questionno_cbox.delete(0,100)
                         tpl_showresult.destroy()
                         # score_entry.delete(0,100)
            
            c1=Canvas(tpl_showresult,width=1600,height=800,bg="#b4eef5")
            c1.place(x=0,y=0)
        
            cs1=Canvas(tpl_showresult,height=90,width=1700,bg='#5e65a1')
            cs1.place(x=0,y=0)
            
            result_label=Label(tpl_showresult,text="RESULT",bg="#5e65a1",fg="white",width=300,height=2,font=('comic sans ms',30))
            result_label.pack()
            
           
            
            subject_label=Label(c1,text="Select Subject:",bg="#b4eef5",font=('Eras Bold ITC',25))
            subject_label.place(x=300,y=220)
            subject_cbox=ttk.Combobox(c1,values=['java_result','mysql_result','python_result'],font=("Arial", 20),width=20)
            subject_cbox.set("python_result")
            subject_cbox.place(x=600,y=225)
            
            
            
            
            findbt=Button(c1,text="CHECK",width=15,height=2,bg="Yellow",command=finddata) #,command=savedata
            findbt.place(x=1000,y=225)
       
            clearbt=Button(c1,text='CLOSE',width=15,height=2,bg="yellow",command=cleardata)  #,command=cleardata
            clearbt.place(x=1150,y=225)
        
            tpl_showresult.mainloop
        
        userresult_bt=Button(c1,text="RESULT",bg="Yellow",fg="black",width=15,height=2,font='Bold',command=showresult)
        userresult_bt.place(x=750,y=300)
    
        # minimize()
        tpl_userportal.mainloop()
    else:
        messagebox.showerror('Error', 'Invalid username or password')
    
        
    
# show the password on click  

def password_visibility():
    if password_entryun['show'] == '':
        password_entryun['show'] = '*'
    else:
        password_entryun['show'] = ''

    
c2=Canvas(t,height=530,width=650,bg="#a7b4dd")
c2.place(x=450,y=150)
username_label=Label(c2,text="Username",bg='#a7b4dd',font=("areial",15,"bold"))
username_label.place(x=50,y=150)
username_entry=Entry(c2,width=50)
username_entry.place(x=170,y=155)

password_label=Label(c2,text="Password",bg='#a7b4dd',font=("areial",15,"bold"))
password_label.place(x=50,y=230)
password_entryun=Entry(c2,width=50,show='*')
password_entryun.place(x=170,y=235)
tk.BooleanVar()
show_password_btn = tk.Checkbutton(c2, text="Show Password",bg='#a7b4dd',font=("areial",12,"bold"))
show_password_btn.config(command=password_visibility)
show_password_btn.place(x=167, y=280)

signin_bt=Button(c2,text="Sign in",font=("BOLD",15),bg="yellow",width=10,command=check_login)
signin_bt.place(x=170,y=350)
signup_bt=Button(c2,text="Sign up",font=("BOLD",15),bg="yellow",width=10,command=usersignup)
signup_bt.place(x=350,y=350)






t.mainloop()