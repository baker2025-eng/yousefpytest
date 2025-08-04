from customtkinter import *
from tkinter import *
from PIL import Image
from tkinter import messagebox
import sqlite3
import dashboard




class LoginClass:
  
  
   def __init__(self,root):
        self.root=root
        self.root.geometry('1100x600+100+50')
        self.root.title('شاشة تسجيل الدخول ')
        self.root.config(bg='#f6f5f5')
        self.root.resizable(False,False)
    


    #--------------------------------------
        
    

#-----------------------------frame
        login_frame=CTkFrame(root,width=1080,height=550,fg_color='#f6f5f5')
        sinup_frame=CTkFrame(root,width=1080,height=550,fg_color='white')

        for frame in (login_frame,sinup_frame):
            frame.place(x=10,y=20)

        def show_frame(frame):
            frame.tkraise()
        show_frame(login_frame)

        #-------------------------------logo image
        img=CTkImage(Image.open('photo/login1.png'),size=(490,400))
        img_lbl=CTkLabel(login_frame,image=img,fg_color='#f6f5f5',text='')
        img_lbl.place(x=10,y=70)

        #--------------------------------frame and botton
        usr_admin=StringVar()
        pass_admin=StringVar()
        global na;
        na=usr_admin.get()

        def open_dash(na):
            win=Toplevel()
            dashboard.DashboardClass(win)
            lab=Label(win,text=f"مرحباً بك \n  {na}",bg="#DA7297",fg='white',font=('calibri',16,'bold'),justify=CENTER)
            lab.place(x=50,y=80)
            root.withdraw()
            win.deiconify()

        def check_open():
            global na
           
            con=sqlite3.connect('school.db')
            cr=con.cursor()
            if usr_admin.get()=="" or pass_admin.get()=="":
                messagebox.showerror("تحذير","الرجاء ملى جميع الحقول ")
            else:
                cr.execute("select * from Admin where username_admin=? and password_admin=?",(
                    usr_admin.get(),
                    pass_admin.get(),
                ))
                data=cr.fetchall()
                if data:
                    na=usr_admin.get()
                    messagebox.showinfo("نجاح"," اهلا بك في برنامج ادارة المدرسة\n\nCLICK 'ok' to continu..")   
                    open_dash(na)
                   
                    
                else:
                    messagebox.showerror("error","اسم مستخدم او كلمة مرور غير صحيحة")
       
        

        

        frame=CTkFrame(login_frame,width=520,height=500,fg_color='#f6f5f5',bg_color='#f6f5f5',border_width=2,corner_radius=30,
                        border_color='#DA7297')
        frame.place(x=520,y=20)

        uptext_lbl=CTkLabel(frame,text='تسجيل الدخول',corner_radius=10,fg_color='#DA7297',width=200,height=30,
                              text_color='white',font=('arial',20,'bold'))
        
        uptext_lbl.place(x=160,y=50)
        uptext_lb2=CTkLabel(frame,text='سجل للاستمرار.....!!',corner_radius=10,fg_color='#f6f5f5',width=200,height=25,
                              text_color='#DA7297',font=('arial',20,'bold'))
                              
        uptext_lb2.place(x=30,y=110)

        uptext_lb3=CTkLabel(frame,text='هل انت عضو ام لا ؟',corner_radius=10,fg_color='#f6f5f5',width=200,height=25,
                              text_color='#DA7297',font=('arial',16,'bold'))
        uptext_lb3.place(x=15,y=140)
        #--------------------------------label + entry
        lb_user=CTkLabel(frame,text=' : اسم المستخدم ',width=150,height=25,text_color='gray',font=('arial',18))
        lb_user.place(x=340,y=180)
        user_en=CTkEntry(frame,width=300,height=35,font=('corier',20),border_width=1,border_color='#DA7297',justify='center',textvariable=usr_admin)
        user_en.place(x=200,y=215)

        lb_pass=CTkLabel(frame,text=' : كلمة المرور ',width=150,height=25,text_color='gray',font=('arial',18))
        lb_pass.place(x=340,y=250)
        user_pass=CTkEntry(frame,width=300,height=35,font=('corier',20),border_width=1,border_color='#DA7297',justify='center',textvariable=pass_admin,show="*")
        user_pass.place(x=200,y=280)

        forgeet_btn=CTkButton(frame,text='نسيت كلمة المرور',width=150,height=20,fg_color='transparent',text_color='#DA7297',font=('arial',16,'bold'),hover_color='#f6f5f5',command=lambda:forget())
        forgeet_btn.place(x=220,y=340)

        signup_btn=CTkButton(frame,text='إنشاء حساب جديد',width=150,height=20,fg_color='transparent',text_color='gray',font=('arial',16,'bold'),hover_color='#f6f5f5',command=lambda:show_frame(sinup_frame))
        signup_btn.place(x=170,y=140)

        signin_btn=CTkButton(frame,text='تسجيل الدخول ',width=150,height=20,fg_color='#DA7297',text_color='white',bg_color='#f6f5f5',font=('arial',16,'bold'),border_width=2,hover_color='#DA7297',border_color='#DA7297',
                               corner_radius=20,command=check_open)
        signin_btn.place(x=155,y=400)
        #--------------------------------forget password page
        
        
        

        

            #-------------------------------------label and entry
        def forget():
            win_forget=Toplevel()
            win_forget.geometry('400x400+680+150')
            win_forget.title("forget password")
            win_forget.config(bg='#f6f5f5')
            win_forget.resizable(False,False)
            lbl1=CTkLabel(win_forget,text='تغيير كلمة السر الخاصة بك ',width=200,height=25,text_color='#DA7297',font=('calibri',18,'bold'))
            lbl1.place(x=100,y=50)

            lb_user_forget=CTkLabel(win_forget,text=' : اسم المستخدم ',width=150,height=25,text_color='gray',font=('arial',18))
            lb_user_forget.place(x=220,y=100)
            user_en_forget=CTkEntry(win_forget,width=200,height=35,font=('corier',14),border_width=2,border_color='#DA7297',justify='center',corner_radius=20)
            user_en_forget.place(x=150,y=140)

            lb_pass_forget=CTkLabel(win_forget,text=' : كلمة المرور الجديدة  ',width=150,height=25,text_color='gray',font=('arial',18))
            lb_pass_forget.place(x=220,y=180)
            pass_en_forget=CTkEntry(win_forget,width=200,height=35,font=('corier',14),border_width=2,border_color='#DA7297',justify='center',corner_radius=20)
            pass_en_forget.place(x=150,y=220)

            rest_pass=CTkButton(win_forget,text='إعادة ضبط كلمة المرور',width=150,height=20,fg_color='#DA7297',text_color='white',bg_color='#f6f5f5',font=('arial',16,'bold'),border_width=2,hover_color='#DA7297',border_color='#DA7297',
                               corner_radius=20)
            rest_pass.place(x=180,y=300)
            #------------------------signup page
            #-----------------------------------------المتغيرات من اجل قواعد البيانات 
        name=StringVar()
        user_name=StringVar()
        password=StringVar()
        confirm_password=StringVar()
      
        

        def clear():
            name.set("")
            user_name.set("")
            password.set("")
            confirm_password.set("")

        def record_count():
            con=sqlite3.connect('school.db')
            cr=con.cursor()
            cr.execute("""
                        WITH RECURSIVE cte AS(
                       SELECT ROW_NUMBER() OVER(ORDER BY ID) AS new_id,ID FROM Account)
                       UPDATE Account SET ID=(SELECT new_id FROM cte WHERE cte.ID=Account.ID)
                        """)
        #------------------------------functiom
        def sign_up():
            if name.get()=="" or user_name.get()=="" or password.get()=="" or confirm_password.get()=="":
                messagebox.showerror("خطأ","الرجاء كتابة كامل الحقول بالبيانات ")
                return
            elif password.get() != confirm_password.get():
                messagebox.showerror("خطأ ","لايوجد تطابق في كلمات السر الرجاء التأكد من الادخال ")
            else:
                try:
                    con=sqlite3.connect('school.db')
                    cr=con.cursor()
                    cr.execute("insert into Account(name,username,password)values(?,?,?)",
                               (name.get(),user_name.get(),password.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("نجاح العملية","تم إضافة مستخدم جديد بنجاح")
                    clear()
                    record_count()
                except Exception as ex:
                    messagebox.showerror("خطأ ","حدث خطأ في الاتصال بقاعدة البيانات حاول لاحقاً")



     # ----------------------------------------------------------

        mg1=CTkImage(Image.open('photo/login1.png'),size=(490,400))
        lb=CTkLabel(sinup_frame,image=mg1,text='ggggg')
        lb.place(x=10,y=70)

        frame1=CTkFrame(sinup_frame,width=520,height=500,fg_color='#f6f5f5',bg_color='#f6f5f5',border_width=2,corner_radius=30,
                    border_color='#DA7297')
        frame1.place(x=520,y=20)

        uptext_lbl1=CTkLabel(frame1,text='تسجيل عضو جديد',corner_radius=10,fg_color='#DA7297',width=200,height=20,
                              text_color='white',font=('arial',20,'bold'))
        uptext_lbl1.place(x=200,y=20)

        lb_newuser=CTkLabel(frame1,text=' : الاسم الثلاثي  ',width=150,height=25,text_color='gray',font=('arial',18))
        lb_newuser.place(x=350,y=70)
        newuser_en=CTkEntry(frame1,width=200,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center',textvariable=name)
        newuser_en.place(x=300,y=100)

        lb_nickuser=CTkLabel(frame1,text=' : اسم المستخدم   ',width=150,height=25,text_color='gray',font=('arial',18))
        lb_nickuser.place(x=350,y=140)
        nickser_en=CTkEntry(frame1,width=200,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center',textvariable=user_name)
        nickser_en.place(x=300,y=170)

        lb_pass=CTkLabel(frame1,text=' : كلمة المرور   ',width=150,height=25,text_color='gray',font=('arial',18))
        lb_pass.place(x=350,y=200)
        pass_en=CTkEntry(frame1,width=200,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center',textvariable=password)
        pass_en.place(x=300,y=230)

        confirm_pass=CTkLabel(frame1,text=' :  تأكيد كلمة المرور   ',width=150,height=25,text_color='gray',font=('arial',18))
        confirm_pass.place(x=350,y=270)
        confirmpass_en=CTkEntry(frame1,width=200,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center',textvariable=confirm_password)
        confirmpass_en.place(x=300,y=300)

        signing_btn=CTkButton(frame1,text='لدي حساب بالفعل',width=150,height=20,fg_color='transparent',text_color='gray',font=('arial',16,'bold'),hover_color='#f6f5f5',command=lambda:show_frame(login_frame))
        signing_btn.place(x=100,y=70)

        signin1_btn=CTkButton(frame1,text='إنشاء مستخدم ',width=150,height=20,fg_color='#DA7297',text_color='white',bg_color='#f6f5f5',font=('arial',16,'bold'),border_width=2,hover_color='#DA7297',border_color='#DA7297',
                               corner_radius=20,command=sign_up)
        signin1_btn.place(x=155,y=400)

#-------------------------------------checking hogin
         

        



        
        


           
















if __name__=="__main__":
    root=Tk()
    LoginClass(root)
    root.mainloop()
