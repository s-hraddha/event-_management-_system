from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # for adding image in gui
from PIL import ImageDraw
from tkinter import messagebox
from corporateDetail import view_corporate_Window
import mysql.connector

class Corporate_win:
    def __init__(self,root,corp_Window):
        self.corp_Window = corp_Window
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1550x800+0+0")

        #--------------textvariable-------------
        self.var_cust_ref = StringVar()
        self.var_Name = StringVar() 
        self.var_Company_Name= StringVar() 
        self.var_Email= StringVar() 
        self.var_job_title= StringVar() 
        self.var_address = StringVar() 
        self.var_website = StringVar() 
        self.var_size= StringVar() 
        self.var_Event_Type = StringVar() 
        self.var_Date = StringVar() 
        self.var_Special_Request = StringVar() 

        label_title = Label(self.root, text="Corporate Events", font=("times new roman", 30, "bold"), fg="black",bg='#ecbee6',relief=RIDGE)
        label_title.place(x=0, y=0, width=1550, height=93)

         #-----------logo---------------
        logo_image1 = Image.open(r"D:\Hotel management system\images\logo1.png")
        logo_image1 = logo_image1.resize((130,130),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image2= ImageTk.PhotoImage(logo_image1) 
        #show image in gui
        label_logo1=Label(self.root, image=self.image2,bd=1,relief=RIDGE)
        label_logo1.place(x=0,y=0,width=190, height=93)
        
        #-----------------background image-------------------
        background_image1 = Image.open(r"D:\Hotel management system\images\corp.jpg")
        background_image1 = background_image1.resize((1550,800),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image1= ImageTk.PhotoImage(background_image1) 
        # # #show image in gui
        label_bg1=Label(self.root, image=self.image1,bd=4,relief=RIDGE)
        label_bg1.place(x=0,y=91,width=1550, height=709)
        
        #---------------label frame------------------------------
        corporate_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Add Details",padx= 1,font=("times new roman", 20, "bold")) #The LabelFrame widget is used to draw a border around its child widgets
        corporate_frame.place(x=370,y=100,width=970,height=690)
        
        #---------------cust ref------------------------------
        label_cust_ref = Label(corporate_frame, text="Customer Ref", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_ref.grid(row=0,column=0,sticky=W)

        entry_cust_ref = ttk.Entry(corporate_frame,textvariable=self.var_cust_ref,width=30,font=("times new roman", 15))
        entry_cust_ref.grid(row=0, column=1)

        #---------------name----------------------
        label_name = Label(corporate_frame, text="Name", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_name.grid(row=1,column=0,sticky=W)

        entry_name = ttk.Entry(corporate_frame,textvariable=self.var_Name,width=30,font=("times new roman", 15))
        entry_name.grid(row=1, column=1)

        #---------company name----------------------
        label_cName= Label(corporate_frame, text="Company Name", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cName.grid(row=2,column=0,sticky=W)

        entry_cName = ttk.Entry(corporate_frame,textvariable=self.var_Company_Name,width=30,font=("times new roman", 15))
        entry_cName.grid(row=2, column=1)
        
         #---------email name----------------------
        label_bEmail= Label(corporate_frame, text="Buisness Email", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_bEmail.grid(row=3,column=0,sticky=W)

        entry_bEmail = ttk.Entry(corporate_frame,textvariable=self.var_Email,width=30,font=("times new roman", 15))
        entry_bEmail.grid(row=3, column=1)


        #---------job title----------------------
        label_job= Label(corporate_frame, text="Job Title", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_job.grid(row=4,column=0,sticky=W)

        entry_job = ttk.Entry(corporate_frame,textvariable=self.var_job_title,width=30,font=("times new roman", 15))
        entry_job.grid(row=4, column=1)

        #---------address----------------------
        label_add= Label(corporate_frame, text="Address", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_add.grid(row=5,column=0,sticky=W)

        entry_add = ttk.Entry(corporate_frame,width=30,textvariable=self.var_address,font=("times new roman", 15))
        entry_add.grid(row=5, column=1)

        #------website------------------------
        label_web = Label(corporate_frame, text="Website", font=("times new roman", 15, "bold"), padx=5, pady=10)
        label_web.grid(row=6, column=0, sticky=W)

        self.entry_web = ttk.Entry(corporate_frame, width=30, textvariable=self.var_website,font=("times new roman", 15))
        self.entry_web.grid(row=6, column=1)
        
        #------------size--------------------------- 
        label_size = Label(corporate_frame, text="Company Size", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_size.grid(row=7,column=0,sticky=W)

        size_combobox = ttk.Combobox(corporate_frame,width=28, textvariable=self.var_size,font=("times new roman", 15, "bold"), state="readonly")
        size_combobox["value"] = ["1-100", "100-500","500-1000","1000-5000", "5000 +"]
        size_combobox.grid(row=7, column=1, sticky=W)

        #------------event types--------------------------- 
        label_size = Label(corporate_frame, text="What type of event you want to organize?", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_size.grid(row=8,column=0,sticky=W)

        size_combobox = ttk.Combobox(corporate_frame,width=28,textvariable=self.var_Event_Type, font=("times new roman", 15, "bold"), state="readonly")
        size_combobox["value"] = ["Conference,Seminar,Meetings", "Dealers Meet","Gala Night","Award Night", "Hr-Admin Program"]
        size_combobox.grid(row=8, column=1, sticky=W)

        #--------------event date-----------------
        label_eDate= Label(corporate_frame, text="Event Date", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_eDate.grid(row=9,column=0,sticky=W)

        entry_eDate = ttk.Entry(corporate_frame,textvariable=self.var_Date,width=30,font=("times new roman", 15))
        entry_eDate.grid(row=9, column=1)

        #---------------special request---------------------------
        label_req = Label(corporate_frame, text="Do you want to make any special request? If yes, mention it.", font=("times new roman", 15, "bold"), padx=5, pady=10)
        label_req.grid(row=10, column=0, sticky=W)

        # Create a Combobox to choose "Yes" or "No"
        request_combobox = ttk.Combobox(corporate_frame, textvariable=self.var_Special_Request,width=28, font=("times new roman", 15, "bold"), state="readonly")
        request_combobox["values"] = ["Yes", "No"]
        request_combobox.grid(row=10, column=1, sticky=W)

        # Set a callback function to handle combobox selection
        request_combobox.bind("<<ComboboxSelected>>", self.handle_request_combobox)

        self.entry_req_frame = Frame(corporate_frame)

        
        #------------------buttons---------
        btn_frame = Frame(corporate_frame, relief=RIDGE)
        btn_frame.place(x=0,y=540,width=950,height=140)

        #-----------button1-----------------
        btn_add = Button(btn_frame, text="Add",width=12,command=self.add_data,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btn_add.grid(row=0,column=0,padx=30,pady=30)

        btnset = Button(btn_frame, text="Reset",command=self.reset_data,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnset.grid(row=0,column=1,padx=30,pady=30)

        btnview = Button(btn_frame, text="viewall",command=self.corporatedetail,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnview.grid(row=0,column=2,padx=30,pady=30)

        btndel = Button(btn_frame, text="Delete",command=self.delete_data,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btndel.grid(row=0,column=3,padx=30,pady=30)
 
    
    def handle_request_combobox(self, event):
        selected_value = event.widget.get()

        if selected_value == "Yes":
            # If "Yes" is selected, create and display the Entry widget
            self.entry_req = ttk.Entry(self.entry_req_frame, width=30, font=("times new roman", 15))
            self.entry_req.grid(row=0, column=0)
            self.entry_req_frame.grid(row=11, column=0, columnspan=2, sticky=W)
        else:
            # If "No" is selected, hide the Entry widget
            self.entry_req_frame.grid_forget()

    #-----------add data---------------
    def add_data(self):
        if self.var_Company_Name.get()=="" or self.var_Event_Type.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Fetch customer details using customer reference ID
                conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00",
                                            database="eventmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM customer WHERE refrence_id=%s", (self.var_cust_ref.get(),))
                customer_data = my_cursor.fetchone()
                conn.close()

                # Check if customer with the provided reference ID exists
                if not customer_data:
                    messagebox.showerror("Error", "Customer with the given reference ID does not exist", parent=self.root)
                    return

                # Use the customer reference ID for the corporate event
                corporate_ref = self.var_cust_ref.get()

                # Insert corporate event details into the database
                conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00",
                                            database="eventmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO corporate VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (corporate_ref, self.var_Name.get(), self.var_Company_Name.get(),
                                    self.var_Email.get(), self.var_job_title.get(),
                                    self.var_address.get(), self.var_website.get(),
                                    self.var_size.get(), self.var_Event_Type.get(),
                                    self.var_Date.get(), self.var_Special_Request.get()))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Corporate Event details have been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    
    #----------delete----------------
    def delete_data(self):
        confirm_message = messagebox.askyesno("Event Management System","Do you want to Delete the data ?", parent=self.root)
        if confirm_message>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="#coDing00",database="eventmanagementsystem")
            my_cursor= conn.cursor()
            del_query= "delete from corporate where corporate_Id=%s"
            value=(self.var_cust_ref.get(),)
            my_cursor.execute(del_query,value)
        else:
            if not confirm_message:
                return
        conn.commit()
        conn.close()                      
    
    #-----------reset function-----------
    def reset_data(self):
        # self.var_ref.set(""),
        self.var_cust_ref.set("")
        self.var_Name.set("")
        self.var_Company_Name.set("")
        self.var_Email.set("")
        self.var_job_title.set("")
        self.var_address.set("")
        self.var_website.set("")
        self.var_size.set("")
        self.var_Event_Type.set("") 
        self.var_Date.set("")
        self.var_Special_Request.set("")


    def corporatedetail(self):
        self.new_Window = Toplevel(self.root)
        self.app = view_corporate_Window(self.new_Window)
        self.app.corporate_window = self    

if __name__ == "__main__":
    root=Tk()
    view_corp_obj= view_corporate_Window(root)
    obj = Corporate_win(root,view_corp_obj)
    view_corp_obj.corporate_window = obj
    root.mainloop()         