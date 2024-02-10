from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # for adding image in gui
from PIL import ImageDraw
from tkinter import messagebox
from socialDetail import view_social_Window
import mysql.connector

class social_win:
    def __init__(self,root,social_Window):
        self.social_Window= social_Window
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1550x800+0+0")

        #----------text variable----------
        self.var_Cust_Ref = StringVar()
        self.var_Name = StringVar() 
        self.var_Phone_No= StringVar() 
        self.var_Size= StringVar() 
        self.var_Event_type = StringVar() 
        self.var_Event_Date = StringVar() 
        self.var_Dinner = StringVar() 
        self.var_Special_Request = StringVar()

        label_title = Label(self.root, text="Social Events", font=("times new roman", 30, "bold"), fg="black",bg='#ecbee6',relief=RIDGE)
        label_title.place(x=0, y=0, width=1550, height=93)

         #-----------logo---------------
        logo_image1 = Image.open(r"D:\Hotel management system\images\logo1.png")
        logo_image1 = logo_image1.resize((130,130),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image2= ImageTk.PhotoImage(logo_image1) 
        #show image in gui
        label_logo1=Label(self.root, image=self.image2,bd=1,relief=RIDGE)
        label_logo1.place(x=0,y=0,width=190, height=93)
        
        #-----------------background image-------------------
        background_image1 = Image.open(r"D:\Hotel management system\images\fund.jpg")
        background_image1 = background_image1.resize((1550,800),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image1= ImageTk.PhotoImage(background_image1) 
        # # #show image in gui
        label_bg1=Label(self.root, image=self.image1,bd=4,relief=RIDGE)
        label_bg1.place(x=0,y=91,width=1550, height=709)
        
        #---------------label frame------------------------------
        social_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Add Details",padx= 1,font=("times new roman", 20, "bold")) #The LabelFrame widget is used to draw a border around its child widgets
        social_frame.place(x=370,y=100,width=970,height=690)

        #---------------cust ref------------------------------
        label_cust_ref = Label(social_frame, text="Customer Ref", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_ref.grid(row=0,column=0,sticky=W)

        entry_cust_ref = ttk.Entry(social_frame,textvariable=self.var_Cust_Ref,width=30,font=("times new roman", 15))
        entry_cust_ref.grid(row=0, column=1)
        
        #---------------name----------------------
        label_name = Label(social_frame, text="Name", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_name.grid(row=1,column=0,sticky=W)

        entry_name = ttk.Entry(social_frame,textvariable=self.var_Name,width=30,font=("times new roman", 15))
        entry_name.grid(row=1, column=1)
        
        #----------------Phone Number----------------------
        label_num = Label(social_frame, text="Phone Number", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_num.grid(row=2,column=0,sticky=W)

        entry_num = ttk.Entry(social_frame,width=30,textvariable=self.var_Phone_No,font=("times new roman", 15))
        entry_num.grid(row=2, column=1)
        #------------size--------------------------- 
        label_size = Label(social_frame, text="Max Count of Person in Events?", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_size.grid(row=3,column=0,sticky=W)

        size_combobox = ttk.Combobox(social_frame,width=28,textvariable=self.var_Size ,font=("times new roman", 15, "bold"), state="readonly")
        size_combobox["value"] = ["1-100", "100-500","500-1000","1000-5000", "5000 +"]
        size_combobox.grid(row=3, column=1, sticky=W)

        #------------event types--------------------------- 
        label_size = Label(social_frame, text="What type of event you want to organize?", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_size.grid(row=4,column=0,sticky=W)

        size_combobox = ttk.Combobox(social_frame,width=28, textvariable=self.var_Event_type,font=("times new roman", 15, "bold"), state="readonly")
        size_combobox["value"] = ["Birthdays", "Bridal & Baby Showers","Family Reunions","Holiday Parties", "Seasonal Events", "Anniversery Parties"]
        size_combobox.grid(row=4, column=1, sticky=W)

        #--------------event date-----------------
        label_eDate= Label(social_frame, text="Event Date", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_eDate.grid(row=5,column=0,sticky=W)

        entry_eDate = ttk.Entry(social_frame,width=30,textvariable=self.var_Event_Date,font=("times new roman", 15))
        entry_eDate.grid(row=5, column=1)

        #---------------dinner---------------------------
        label_dinner = Label(social_frame, text="How do you want to serve Dinner?", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_dinner.grid(row=6,column=0,sticky=W)

        dinner_combobox = ttk.Combobox(social_frame,width=28, textvariable=self.var_Dinner,font=("times new roman", 15, "bold"), state="readonly")
        dinner_combobox["value"] = ["Plated", "Buffed","Family Style"]
        dinner_combobox.grid(row=6, column=1, sticky=W)

        #---------------special request---------------------------
        label_req = Label(social_frame, text="Do you want to make any special request? If yes, mention it.", font=("times new roman", 15, "bold"), padx=5, pady=10)
        label_req.grid(row=7, column=0, sticky=W)

        # Create a Combobox to choose "Yes" or "No"
        request_combobox = ttk.Combobox(social_frame, width=28,textvariable=self.var_Special_Request, font=("times new roman", 15, "bold"), state="readonly")
        request_combobox["values"] = ["Yes", "No"]
        request_combobox.grid(row=7, column=1, sticky=W)

        # Set a callback function to handle combobox selection
        request_combobox.bind("<<ComboboxSelected>>", self.handle_request_combobox)

        self.entry_req_frame = Frame(social_frame)

        
        #------------------buttons---------
        btn_frame = Frame(social_frame, relief=RIDGE)
        btn_frame.place(x=0,y=450,width=950,height=140)

        #-----------button1-----------------
        btn_add = Button(btn_frame, text="Add",command=self.add_data,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btn_add.grid(row=0,column=0,padx=30,pady=30)

        btnset = Button(btn_frame, text="Reset",width=12,command=self.reset_data,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnset.grid(row=0,column=1,padx=30,pady=30)

        btnview = Button(btn_frame, text="viewall",width=12,command=self.socialdetail,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnview.grid(row=0,column=2,padx=30,pady=30)

        btndel = Button(btn_frame, text="Delete",width=12,command=self.delete_data,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
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
        if self.var_Event_Date.get()=="" or self.var_Event_type.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Fetch customer details using customer reference ID
                conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00",
                                            database="eventmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM customer WHERE refrence_id=%s", (self.var_Cust_Ref.get(),))
                customer_data = my_cursor.fetchone()
                conn.close()

                # Check if customer with the provided reference ID exists
                if not customer_data:
                    messagebox.showerror("Error", "Customer with the given reference ID does not exist", parent=self.root)
                    return

                # Use the customer reference ID for the corporate event
                corporate_ref = self.var_Cust_Ref.get()

                # Insert corporate event details into the database
                conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00",
                                            database="eventmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO corporate VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (corporate_ref, self.var_Name.get(), self.var_Name.get(),
                                    self.var_Phone_No.get(), self.var_Size.get(),
                                    self.var_Event_type.get(), self.var_Event_Date.get(), 
                                    self.var_Dinner.get(), self.var_Special_Request.get()))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Sociall Event details have been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    
    #----------delete----------------
    def delete_data(self):
        confirm_message = messagebox.askyesno("Event Management System","Do you want to Delete the data ?", parent=self.root)
        if confirm_message>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="#coDing00",database="eventmanagementsystem")
            my_cursor= conn.cursor()
            del_query= "delete from social where Social_Id=%s"
            value=(self.var_Cust_Ref.get(),)
            my_cursor.execute(del_query,value)
        else:
            if not confirm_message:
                return
        conn.commit()
        conn.close()                      
    
    #-----------reset function-----------
    def reset_data(self):
        # self.var_ref.set(""),
        self.var_Cust_Ref.set("")
        self.var_Name.set("")
        self.var_Phone_No.set("") 
        self.var_Size.set("")
        self.var_Event_type.set("")
        self.var_Event_Date.set("")
        self.var_Dinner.set("")
        self.var_Special_Request.set("")

    def socialdetail(self):
        self.new_Window = Toplevel(self.root)
        self.app = view_social_Window(self.new_Window)
        self.app.corporate_window = self     
        

if __name__ == "__main__":
    root=Tk()
    view_social_obj = view_social_Window(root)
    obj = social_win(root,view_social_obj)
    view_social_obj.social_window = obj
    root.mainloop()         