from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter
from PIL import Image, ImageTk


# Login Window Class
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        

        BackgroundImg = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\MINIPROJECT SE 3RD SEM\Images\download (1).jpeg")
        BackgroundImg = BackgroundImg.resize((1550, 800))
        self.photoimage = ImageTk.PhotoImage(BackgroundImg)
        bg_img = Label(self.root, image=self.photoimage)
        bg_img.place(x=0, y=0, width=1550, height=800)

        #Label Title
        lbl=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("Times new roman",50,"bold"),padx=2,pady=5)
        lbl.pack(side=TOP,fill=X)

        # FRAME
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=350, height=450)

        # ICON IMAGE
        image1 = Image.open(r"C:\Users\Umer Khan\OneDrive\Desktop\MINIPROJECT SE 3RD SEM\Images\LoginIconAppl.png")
        image1 = image1.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(image1)

        lbl_image1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lbl_image1.place(x=740, y=175, width=100, height=100)

        # ADMIN LOGIN LABEL
        get_str = Label(frame, text="Admin Login", font=("Times new roman", 20, "bold"), bg="black", fg="white")
        get_str.place(x=100, y=110)

        # USERNAME LABEL
        username_lbl = Label(frame, text="Username:", font=("Times new roman", 14, "bold"), bg="black", fg="white")
        username_lbl.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("Times new roman", 14, "bold"))
        self.txtuser.place(x=40, y=185, width=270)

        # PASSWORD LABEL
        password_lbl = Label(frame, text="Password:", font=("Times new roman", 14, "bold"), bg="black", fg="white")
        password_lbl.place(x=70, y=220)

        self.txtpass = ttk.Entry(frame, font=("Times new roman", 14, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

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

        # LOGIN BUTTON
        login_btn = Button(frame, text="Login", command=self.login, font=("Times new roman", 14, "bold"),
                           bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        login_btn.place(x=110, y=300, width=120, height=35)

        #REGISTER BUTTON
        #register_btn=Button(frame,text="Register",font=("Times new roman",11,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        #register_btn.place(x=10,y=350,width=100)

        #FORGOT PASSWORD
        #pass_btn=Button(frame,text="Forgot Password",font=("Times new roman",11,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        #pass_btn.place(x=10,y=370,width=155)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required!")
        elif self.txtuser.get() == "Admin04" and self.txtpass.get() == "admin@123":
            messagebox.showinfo("Success", "Login Successful")
            self.open_library_management()  # Open the library management system
        else:
            messagebox.showerror("Error", "Incorrect Username or Password")

    def open_library_management(self):
        self.root.destroy()  # Close the login window
        new_root = Tk()
        LibraryManagementSystem(new_root)  # Pass the new root to LibraryManagementSystem
        new_root.mainloop()


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #VARIABLES
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.fname_var=StringVar()
        self.lname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrow_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latefine_var=StringVar()
        self.overdue_var=StringVar()
        self.finalprice_var=StringVar()


        #Label Title
        lbl_title=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("Times new roman",50,"bold"),padx=2,pady=5)
        lbl_title.pack(side=TOP,fill=X)

        #Creating Frame
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        #Creating Label Frame 
        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERS INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=860,height=360)

        #Label Member Type and ComboBox
        lbl_member=Label(DataFrameLeft,text="Member Type:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_member.grid(row=0,column=0,sticky=W)

        com_Member=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("Times new roman",12,"bold"),width=32,state="readonly")
        com_Member["value"]=("Student")
        com_Member.grid(row=0,column=1,sticky=W)

        #Label PRN Number and TextFill
        lbl_prn=Label(DataFrameLeft,text="PRN Number:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_prn.grid(row=1,column=0,sticky=W)

        txt_prn=Entry(DataFrameLeft,textvariable=self.prn_var,font=("Times new roman",12,"bold"),width=35)
        txt_prn.grid(row=1,column=1,sticky=W)

        #Label ID Number and TextFill
        lbl_id=Label(DataFrameLeft,text="ID Number:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_id.grid(row=2,column=0,sticky=W)

        txt_id=Entry(DataFrameLeft,textvariable=self.id_var,font=("Times new roman",12,"bold"),width=35)
        txt_id.grid(row=2,column=1,sticky=W)

        #Label First Name and TextFill
        lbl_fname=Label(DataFrameLeft,text="First Name:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_fname.grid(row=3,column=0,sticky=W)

        txt_fname=Entry(DataFrameLeft,textvariable=self.fname_var,font=("Times new roman",12,"bold"),width=35)
        txt_fname.grid(row=3,column=1,sticky=W)

        #Label Last Name and TextFill
        lbl_lname=Label(DataFrameLeft,text="Last Name:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_lname.grid(row=4,column=0,sticky=W)

        txt_lname=Entry(DataFrameLeft,textvariable=self.lname_var,font=("Times new roman",12,"bold"),width=35)
        txt_lname.grid(row=4,column=1,sticky=W)

        #Label Address 1 and TextFill
        lbl_add1=Label(DataFrameLeft,text="Address 1:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_add1.grid(row=5,column=0,sticky=W)

        txt_add1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("Times new roman",12,"bold"),width=35)
        txt_add1.grid(row=5,column=1,sticky=W)

        #Label Address 2 and TextFill
        lbl_add2=Label(DataFrameLeft,text="Address 2:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_add2.grid(row=6,column=0,sticky=W)

        txt_add2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("Times new roman",12,"bold"),width=35)
        txt_add2.grid(row=6,column=1,sticky=W)

        #Label Mobile Number and TextFill
        lbl_mobile=Label(DataFrameLeft,text="Mobile Number:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_mobile.grid(row=7,column=0,sticky=W)

        txt_mobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("Times new roman",12,"bold"),width=35)
        txt_mobile.grid(row=7,column=1,sticky=W)

        #Label Postcode and TextFill
        lbl_postcode=Label(DataFrameLeft,text="Post Code:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_postcode.grid(row=8,column=0,sticky=W)

        txt_postcode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("Times new roman",12,"bold"),width=35)
        txt_postcode.grid(row=8,column=1,sticky=W)
        
        #Label Book ID and TextFill
        lbl_bookid=Label(DataFrameLeft,text="Book ID:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_bookid.grid(row=0,column=2,sticky=W)

        txt_bookid=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("Times new roman",12,"bold"),width=35)
        txt_bookid.grid(row=0,column=3,sticky=W)

        #Label Book Title and TextFill
        lbl_booktitle=Label(DataFrameLeft,text="Book Title:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_booktitle.grid(row=1,column=2,sticky=W)

        txt_booktitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("Times new roman",12,"bold"),width=35)
        txt_booktitle.grid(row=1,column=3,sticky=W)

        #Label Author Name and TextFill
        lbl_authorname=Label(DataFrameLeft,text="Author Name:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_authorname.grid(row=2,column=2,sticky=W)

        txt_authorname=Entry(DataFrameLeft,textvariable=self.author_var,font=("Times new roman",12,"bold"),width=35)
        txt_authorname.grid(row=2,column=3,sticky=W)

        #Label Borrow Date and TextFill
        lbl_dtborrow=Label(DataFrameLeft,text="Borrowed Date:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_dtborrow.grid(row=3,column=2,sticky=W)

        txt_dtborrow=Entry(DataFrameLeft,textvariable=self.dateborrow_var,font=("Times new roman",12,"bold"),width=35)
        txt_dtborrow.grid(row=3,column=3,sticky=W)

        #Label Due Date and TextFill
        lbl_dtdue=Label(DataFrameLeft,text="Due Date:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_dtdue.grid(row=4,column=2,sticky=W)

        txt_dtdue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("Times new roman",12,"bold"),width=35)
        txt_dtdue.grid(row=4,column=3,sticky=W)

        #Label Days On Book and TextFill
        lbl_daybook=Label(DataFrameLeft,text="Days On Books:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_daybook.grid(row=5,column=2,sticky=W)

        txt_daybook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("Times new roman",12,"bold"),width=35)
        txt_daybook.grid(row=5,column=3,sticky=W)

        #Label Late Return Fine and TextFill
        lbl_late=Label(DataFrameLeft,text="Late Return Fine:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_late.grid(row=6,column=2,sticky=W)

        txt_late=Entry(DataFrameLeft,textvariable=self.latefine_var,font=("Times new roman",12,"bold"),width=35)
        txt_late.grid(row=6,column=3,sticky=W)

        #Label  Date Over Due and TextFill
        lbl_dtoverdue=Label(DataFrameLeft,text="Date Over Due:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_dtoverdue.grid(row=7,column=2,sticky=W)

        txt_dtoverdue=Entry(DataFrameLeft,textvariable=self.overdue_var,font=("Times new roman",12,"bold"),width=35)
        txt_dtoverdue.grid(row=7,column=3,sticky=W)

        #Label Actual Price and TextFill
        lbl_actualprice=Label(DataFrameLeft,text="Actual Price:",font=("Times new roman",12,"bold"),padx=2,pady=6,bg="powder blue",fg="black")
        lbl_actualprice.grid(row=8,column=2,sticky=W)

        txt_actualprice=Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("Times new roman",12,"bold"),width=35)
        txt_actualprice.grid(row=8,column=3,sticky=W)


        #Creating Label Frame Right
        DataFrameRight=LabelFrame(frame,text="BOOK DETAILS",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Times new roman",12,"bold"))
        DataFrameRight.place(x=870,y=5,width=610,height=360)

        #Textbox
        self.txt_box=Text(DataFrameRight,font=("Times new roman",12,"bold"),width=40,height=16,padx=2,pady=6)
        self.txt_box.grid(row=0,column=2)


        #List Scroll Bar
        listScrollBar=Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0,column=1,sticky="ns")

        #Listbox
        listbook=["Head First Book","Learn Python The Hard Way","Analysis Of Algorithms","Database Management System","Microprocessor","Object Oriented Programming","Data Structure","Computer Graphics"
                 ,"Engineering Mathematics III","Engineering Mathematics IV","Operating System","Advanced Algorithms","JavaScript","Programming in C","Fundamentals of AI",
                 "Deep Learning","BlcokChain Technology"]
        
        def SelectBook(event=""):
            value = str(List_box.get(List_box.curselection()))  # Get selected book title
    
            # Connect to the MySQL database (SQL Workbench)
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="13@Umerkhan",
            database="library_management"
            )
            cursor = conn.cursor()

            # Fetch book details based on the selected title
            query = "SELECT bookid, title, author, price FROM books WHERE title = %s"
            cursor.execute(query, (value,))
            book = cursor.fetchone()

            # Check if a book was found
            if book:
                bookid, title, author, price = book
        
                # Set the values in the respective variables
                self.bookid_var.set(bookid)
                self.booktitle_var.set(title)
                self.author_var.set(author)

                d1 = datetime.date.today()        
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrow_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.finalprice_var.set(price)

            # Close the database connection
            cursor.close()
            conn.close()

        # List_box configuration remains the same
        List_box = Listbox(DataFrameRight, font=("Times new roman", 12, "bold"), width=25, height=16)
        List_box.bind("<<ListboxSelect>>", SelectBook)
        List_box.grid(row=0, column=0, padx=4)
        listScrollBar.config(command=List_box.yview)

        # Insert book titles into List_box (ensure 'listbook' is a list of book titles from the SQL table)
        for item in listbook:
            List_box.insert(END, item)


        #Creating Button Frame
        frame_button=Frame(self.root,bd=12,relief=RIDGE,padx=2,bg="powder blue")
        frame_button.place(x=0,y=530,width=1530,height=60)

        #ADD Button
        btn_add=Button(frame_button,text="Add Data",command=self.add_data,font=("Times new roman",12,"bold"),width=27,bg="Blue",fg="white")
        btn_add.grid(row=0,column=0)

        #Show Button
        btn_show=Button(frame_button,text="Show Data",command=self.show_data,font=("Times new roman",12,"bold"),width=27,bg="Blue",fg="white")
        btn_show.grid(row=0,column=1)

        #Update Button
        btn_update=Button(frame_button,text="Update",command=self.update_data,font=("Times new roman",12,"bold"),width=27,bg="Blue",fg="white")
        btn_update.grid(row=0,column=2)

        #Delete Button
        btn_delete=Button(frame_button,text="Delete",command=self.delete_data,font=("Times new roman",12,"bold"),width=27,bg="Blue",fg="white")
        btn_delete.grid(row=0,column=3)

        #Reset Button
        btn_reset=Button(frame_button,text="Reset",command=self.reset_data,font=("Times new roman",12,"bold"),width=26,bg="Blue",fg="white")
        btn_reset.grid(row=0,column=4)

        #Exit Button
        btn_add=Button(frame_button,text="Exit",command=self.exit,font=("Times new roman",12,"bold"),width=26,bg="Blue",fg="white")
        btn_add.grid(row=0,column=5)


        #Creating Information Frame
        frame_info=Frame(self.root,bd=12,relief=RIDGE,padx=2,bg="powder blue")
        frame_info.place(x=0,y=590,width=1530,height=190)

        #Data Table
        table_frame=Frame(frame_info,bd=6,relief=RIDGE,bg="powder blue")
        table_frame.place(x=0,y=2,width=1500,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(table_frame,columns=("Member Type","PRN Number","ID No","First Name","Last Name","Address 1","Address 2",
                                                             "PostCode","Mobile No","Book ID","Book Title","Author Name","Date of Borrow","Due Date",
                                                             "Days","Fine","Over Due","Price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)

        self.library_table.heading("Member Type",text="Member Type")
        self.library_table.heading("PRN Number",text="PRN Number")
        self.library_table.heading("ID No",text="ID No")
        self.library_table.heading("First Name",text="First Name")
        self.library_table.heading("Last Name",text="Last Name")
        self.library_table.heading("Address 1",text="Address 1")
        self.library_table.heading("Address 2",text="Address 2")
        self.library_table.heading("PostCode",text="PostCode")
        self.library_table.heading("Mobile No",text="Mobile No")
        self.library_table.heading("Book ID",text="Book ID")
        self.library_table.heading("Book Title",text="Book Title")
        self.library_table.heading("Author Name",text="Author Name")
        self.library_table.heading("Date of Borrow",text="Date of Borrow")
        self.library_table.heading("Due Date",text="Due Date")
        self.library_table.heading("Days",text="Days")
        self.library_table.heading("Fine",text="Fine")
        self.library_table.heading("Over Due",text="Over Due")
        self.library_table.heading("Price",text="Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("Member Type",width=100)
        self.library_table.column("PRN Number",width=100)
        self.library_table.column("ID No",width=100)
        self.library_table.column("First Name",width=100)
        self.library_table.column("Last Name",width=100)
        self.library_table.column("Address 1",width=100)
        self.library_table.column("Address 2",width=100)
        self.library_table.column("PostCode",width=100)
        self.library_table.column("Mobile No",width=100)
        self.library_table.column("Book ID",width=100)
        self.library_table.column("Book Title",width=100)
        self.library_table.column("Author Name",width=100)
        self.library_table.column("Date of Borrow",width=100)
        self.library_table.column("Due Date",width=100)
        self.library_table.column("Days",width=100)
        self.library_table.column("Fine",width=100)
        self.library_table.column("Over Due",width=100)
        self.library_table.column("Price",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    #ADD BUTTON FUNCTION
    def add_data(self):
        if (self.member_var.get() == "" or
        self.prn_var.get() == "" or
        self.id_var.get() == "" or
        self.fname_var.get() == "" or
        self.lname_var.get() == "" or
        self.address1_var.get() == "" or
        self.address2_var.get() == "" or
        self.postcode_var.get() == "" or
        self.mobile_var.get() == "" or
        self.bookid_var.get() == "" or
        self.booktitle_var.get() == "" or
        self.author_var.get() == "" or
        self.dateborrow_var.get() == "" or
        self.datedue_var.get() == "" or
        self.daysonbook_var.get() == "" or
        self.latefine_var.get() == "" or
        self.overdue_var.get() == "" or
        self.finalprice_var.get() == ""):
        
            # Show error message if any field is empty
            messagebox.showerror("Error", "All fields must be filled out!")
        else:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="13@Umerkhan",
            database="library_management"
            )

            my_cursor=conn.cursor()
            my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(),
                           self.prn_var.get(),
                           self.id_var.get(),
                           self.fname_var.get(),
                           self.lname_var.get(),
                           self.address1_var.get(),
                           self.address2_var.get(),
                           self.postcode_var.get(),
                           self.mobile_var.get(),
                           self.bookid_var.get(),
                           self.booktitle_var.get(),
                           self.author_var.get(),
                           self.dateborrow_var.get(),
                           self.datedue_var.get(),
                           self.daysonbook_var.get(),
                           self.latefine_var.get(),
                           self.overdue_var.get(),
                           self.finalprice_var.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
        
            messagebox.showinfo("Success","Member Has Been Added Successfully")

    #UPDATE BUTTON FUNCTION
    def update_data(self):
        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="13@Umerkhan",
        database="library_management"
        )

        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member_Type=%s, ID_No=%s, First_name=%s, Last_name=%s, Address1=%s, Address2=%s, Postcode=%s, Mobile_No=%s, Book_ID=%s, Book_Title=%s, Author_Name=%s, Borrow_Date=%s, Due_Date=%s, Days=%s, Fine=%s, Over_Due=%s, Price=%s where PRN_No=%s",
                           (self.member_var.get(),
                           self.id_var.get(),
                           self.fname_var.get(),
                           self.lname_var.get(),
                           self.address1_var.get(),
                           self.address2_var.get(),
                           self.postcode_var.get(),
                           self.mobile_var.get(),
                           self.bookid_var.get(),
                           self.booktitle_var.get(),
                           self.author_var.get(),
                           self.dateborrow_var.get(),
                           self.datedue_var.get(),
                           self.daysonbook_var.get(),
                           self.latefine_var.get(),
                           self.overdue_var.get(),
                           self.finalprice_var.get(),
                           self.prn_var.get()))

        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()    

        messagebox.showinfo("Success","Details has been Updated")


    #SHOW DETAILS IN TABLE
    def fetch_data(self):
        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="13@Umerkhan",
        database="library_management"
        )
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)<=19:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close

    #SHOW FUNCTION
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.fname_var.set(row[3]),
        self.lname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrow_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latefine_var.set(row[15]),
        self.overdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def show_data(self):
        self.txt_box.insert(END,"Member Type\t\t"+self.member_var.get() + "\n")
        self.txt_box.insert(END,"PRN Number\t\t"+self.prn_var.get() + "\n")
        self.txt_box.insert(END,"IC No\t\t"+self.id_var.get() + "\n")
        self.txt_box.insert(END,"First Name\t\t"+self.fname_var.get() + "\n")
        self.txt_box.insert(END,"Last Name\t\t"+self.lname_var.get() + "\n")
        self.txt_box.insert(END,"Address 1\t\t"+self.address1_var.get() + "\n")
        self.txt_box.insert(END,"Adress 2\t\t"+self.address2_var.get() + "\n")
        self.txt_box.insert(END,"Postcode\t\t"+self.postcode_var.get() + "\n")
        self.txt_box.insert(END,"Mobile No\t\t"+self.mobile_var.get() + "\n")
        self.txt_box.insert(END,"Book ID\t\t"+self.bookid_var.get() + "\n")
        self.txt_box.insert(END,"Book Title\t\t"+self.booktitle_var.get() + "\n")
        self.txt_box.insert(END,"Author\t\t"+self.author_var.get() + "\n")
        self.txt_box.insert(END,"Borrow Date\t\t"+self.dateborrow_var.get() + "\n")
        self.txt_box.insert(END,"Due Date\t\t"+self.datedue_var.get() + "\n")
        self.txt_box.insert(END,"Days on Book\t\t"+self.daysonbook_var.get() + "\n")
        self.txt_box.insert(END,"Fine\t\t"+self.latefine_var.get() + "\n")
        self.txt_box.insert(END,"Over Due\t\t"+self.overdue_var.get() + "\n")
        self.txt_box.insert(END,"Price\t\t"+self.finalprice_var.get() + "\n")

    #DELETE BUTTON FUNCTION
    def delete_data(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "First Select the Member!!")
        else:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="13@Umerkhan",
            database="library_management"
            )
            my_cursor = conn.cursor()
        
            # Pass the parameter as a tuple
            my_cursor.execute("DELETE FROM library WHERE PRN_No = %s", (self.prn_var.get(),))

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            messagebox.showinfo("Success", "Details have been deleted!")

    #RESET BUTTON FUNCTION
    def reset_data(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.fname_var.set(""),
        self.lname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrow_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latefine_var.set(""),
        self.overdue_var.set(""),
        self.finalprice_var.set("")
        self.txt_box.delete("1.0",END)

    #EXIT BUTTON FUNCTION
    def exit(self):
        exit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit??")
        if exit>0:
            self.root.destroy()
            return



if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)  # Start with the Login Window
    root.mainloop()
