from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        BackgroundImg =Image.open(r"Images/login_bg.jpeg")
        BackgroundImg = BackgroundImg.resize((1550,800))
        self.photoimage = ImageTk.PhotoImage(BackgroundImg)

        bg_img = Label(self.root,image=self.photoimage)
        bg_img.place(x=0,y=0,width=1550,height=800)

        #FRAME
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=350,height=450)

        #ICON IMAGE
        image1=Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\MINIPROJECT SE 3RD SEM\Images\LoginIconAppl.png")
        image1=image1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(image1)

        lbl_image1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lbl_image1.place(x=740,y=175,width=100,height=100)

        #ADMIN LOGIN LABEL
        get_str=Label(frame,text="Admin Login",font=("Times new roman",20,"bold"),bg="black",fg="white")
        get_str.place(x=100,y=110)

        #USERNAME LABEL
        username_lbl=Label(frame,text="Username:",font=("Times new roman",14,"bold"),bg="black",fg="white")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("Times new roman",14,"bold"))
        self.txtuser.place(x=40,y=185,width=270)

        #PASSWORD LABEL
        password_lbl=Label(frame,text="Password:",font=("Times new roman",14,"bold"),bg="black",fg="white")
        password_lbl.place(x=70,y=220)

        self.txtpass=ttk.Entry(frame,font=("Times new roman",14,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #ICON IMAGES
        image2=Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\MINIPROJECT SE 3RD SEM\Images\LoginIconAppl.png")
        image2=image2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(image2)
        lbl_image2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbl_image2.place(x=650,y=323,width=25,height=25)


        image3=Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\MINIPROJECT SE 3RD SEM\Images\lock-512.png")
        image3=image3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(image3)
        lbl_image3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbl_image3.place(x=650,y=390,width=25,height=25)

        #LOGIN BUTTON
        login_btn=Button(frame,text="Login",command=self.login,font=("Times new roman",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=110,y=300,width=120,height=35)

        #REGISTER BUTTON
        register_btn=Button(frame,text="New User Register",font=("Times new roman",11,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        register_btn.place(x=10,y=350,width=170)

        #FORGOT PASSWORD
        pass_btn=Button(frame,text="Forgot Password",font=("Times new roman",11,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        pass_btn.place(x=10,y=370,width=155)

    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fills Required!!")
        elif self.txtuser.get()=="Admin04" and self.txtpass.get()=="admin@123":
            messagebox.showinfo("Success","Login Successful")
        else:
            messagebox.showerror("Error","Incorrect Username and Password")



if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()

        