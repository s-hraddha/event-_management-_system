from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from viewDetails import *
from viewDetails import viewAllWindow
import mysql.connector
import random


class CustomerWindow:
    def __init__(self,root,view_all_window): #This view_all_window attribute is used to establish a connection
        self.view_all_window = view_all_window  # between the two windows, allowing them to interact with each other. 
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1550x800+0+0")

        #-----------text variable----------------
        self.var_ref = StringVar()
        random_ref = random.randint(1000,9999)
        self.var_ref.set(str(random_ref))

        self.var_custName = StringVar()
        self.var_gender = StringVar()
        self.var_phn = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_pincode = StringVar()
        self.var_idproof = StringVar()
        self.var_idNum = StringVar()
        
        #-------------title-------------
        label_title = Label(self.root, text="ADD DETAILS", font=("times new roman", 20, "bold"), fg="black",bg='#ecbee6',relief=RIDGE)
        label_title.place(x=0, y=0, width=1550, height=93)

         #-----------logo---------------
        logo_image1 = Image.open(r"D:\Hotel management system\images\logo1.png")
        logo_image1 = logo_image1.resize((130,130),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image2= ImageTk.PhotoImage(logo_image1) 
        #show image in gui
        label_logo1=Label(self.root, image=self.image2,bd=1,relief=RIDGE)
        label_logo1.place(x=0,y=0,width=190, height=93)
        
        #-----------------background image-------------------
        background_image1 = Image.open(r"D:\Hotel management system\images\bg2.jpg")
        background_image1 = background_image1.resize((1550,800),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image1= ImageTk.PhotoImage(background_image1) 
        # # #show image in gui
        label_bg1=Label(self.root, image=self.image1,bd=4,relief=RIDGE)
        label_bg1.place(x=0,y=91,width=1550, height=709)

        #---------------label frame------------------------------
        label_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Add Details",padx= 1,font=("times new roman", 20, "bold")) #The LabelFrame widget is used to draw a border around its child widgets
        label_frame.place(x=520,y=100,width=600,height=670)

        #---------------cust ref------------------------------
        label_cust_ref = Label(label_frame, text="Customer Ref", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_ref.grid(row=0,column=0,sticky=W)

        entry_cust_ref = ttk.Entry(label_frame,textvariable=self.var_ref,width=30,font=("times new roman", 15))
        entry_cust_ref.grid(row=0, column=1)

        #---------------cust_name----------------------
        label_cust_name = Label(label_frame, text="Customer Name", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_name.grid(row=1,column=0,sticky=W)

        entry_cust_name = ttk.Entry(label_frame,textvariable=self.var_custName,width=30,font=("times new roman", 15))
        entry_cust_name.grid(row=1, column=1)

        #---------------gender---------------------------
        label_cust_gen = Label(label_frame, text="Gender", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_gen.grid(row=2,column=0,sticky=W)

        gender_combobox = ttk.Combobox(label_frame, textvariable=self.var_gender,width=30, state="readonly")
        gender_combobox["value"] = ["Male", "Female", "Other"]
        gender_combobox.grid(row=2, column=1, sticky=W)  #sticky=W: Ensures that the Combobox sticks to the West (left) side of its grid cell.

        #-----------------phone number----------------------
        label_cust_no = Label(label_frame, text="Mobile Number", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_no.grid(row=3,column=0,sticky=W)

        entry_cust_no = ttk.Entry(label_frame,width=30,textvariable=self.var_phn,font=("times new roman", 15))
        entry_cust_no.grid(row=3, column=1)

        #----------------email----------------------------
        label_cust_email = Label(label_frame, text="Email", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_email.grid(row=4,column=0,sticky=W)

        entry_cust_email = ttk.Entry(label_frame,textvariable=self.var_email,width=30,font=("times new roman", 15))
        entry_cust_email.grid(row=4, column=1)

        #----------------address---------------------------
        label_cust_add = Label(label_frame, text="Address", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_add.grid(row=5,column=0,sticky=W)

        entry_cust_add = ttk.Entry(label_frame,textvariable=self.var_address,width=30,font=("times new roman", 15))
        entry_cust_add.grid(row=5, column=1)

        #---------------------pincode-------------------------------
        label_cust_pin = Label(label_frame, text="Pincode", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_pin.grid(row=6,column=0,sticky=W)

        entry_cust_pin = ttk.Entry(label_frame,textvariable=self.var_pincode,width=30,font=("times new roman", 15))
        entry_cust_pin.grid(row=6, column=1)

        #------------------------idproof------------------------------
        label_cust_id = Label(label_frame, text="ID-Proof", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_id.grid(row=7,column=0,sticky=W)
        
        Idproof_combobox = ttk.Combobox(label_frame, textvariable=self.var_idproof,width=30, state="readonly")
        Idproof_combobox["values"] = ["Adhaar Card", "Pan Card", "Driving License"]
        Idproof_combobox.grid(row=7, column=1, sticky=W)

        #--------------------idnumber---------------------------------
        label_cust_ino = Label(label_frame, text="ID Number", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_ino.grid(row=8,column=0,sticky=W)

        entry_cust_ino = ttk.Entry(label_frame,width=30,textvariable=self.var_idNum,font=("times new roman", 15))
        entry_cust_ino.grid(row=8, column=1)

        #------------------buttons---------
        btn_frame = Frame(label_frame, relief=RIDGE)
        btn_frame.place(x=0,y=440,width=592,height=190)

        # #-----------button1-----------------
        btn_add = Button(btn_frame, text="Add",command=self.add_data,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btn_add.grid(row=0,column=0,padx=4)

        btnset = Button(btn_frame, text="Reset",command=self.reset_data,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnset.grid(row=0,column=1,padx=4)

        btnview = Button(btn_frame, text="viewall",command=self.viewdetail,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnview.grid(row=0,column=2,padx=4)

        btndel = Button(btn_frame, text="Delete",command=self.delete_data,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btndel.grid(row=0,column=3,padx=4)


    def add_data(self):
        if self.var_email.get()==""or self.var_idNum.get()=="":
            messagebox.showerror("Error","All Fiels are required",parent= self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="#coDing00",database="eventmanagementsystem")
                my_cursor= conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_ref.get(),
                                                                                self.var_custName.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_phn.get(),
                                                                                self.var_email.get(),
                                                                                self.var_address.get(),
                                                                                self.var_pincode.get(),
                                                                                self.var_idproof.get(),
                                                                                self.var_idNum.get()
                                                                            )) 
                conn.commit()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent= self.root) #parent is used to show on the relevent window
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)           
            
    #---------------delete function---------------
    def delete_data(self):
        confirm_message = messagebox.askyesno("Event Management System","Do you want to Delete the data ?", parent=self.root)
        if confirm_message>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="#coDing00",database="eventmanagementsystem")
            my_cursor= conn.cursor()
            del_query= "delete from customer where refrence_id=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(del_query,value)
        else:
            if not confirm_message:
                return
        conn.commit()
        conn.close() 

#-----------reset function-----------
    def reset_data(self):
        # self.var_ref.set(""),
        self.var_custName.set(""),
        self.var_gender.set(""),
        self.var_phn.set(""),
        self.var_email.set(""),
        self.var_address.set(""),           
        self.var_pincode.set(""),
        self.var_idproof.set(""),
        self.var_idNum.set("") 

        random_ref = random.randint(1000,9999)
        self.var_ref.set(str(random_ref))   
    
    def viewdetail(self):
        self.new_Window = Toplevel(self.root)
        self.app = viewAllWindow(self.new_Window)
        self.app.customer_window = self    
 

if __name__ == "__main__":
    root = Tk()
    view_all_obj = viewAllWindow(root) #The customer_window attribute of view_all_obj is 
    obj = CustomerWindow(root, view_all_obj) #set to obj, establishing the bidirectional connection. 
    view_all_obj.customer_window = obj
    root.mainloop()        