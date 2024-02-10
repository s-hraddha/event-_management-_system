from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # for adding image in gui
from PIL import ImageDraw
from tkinter import messagebox
from weddingDetail import view_wed_Window
import mysql.connector
import random

class wedding_win:
    def __init__(self,root,Wed_Window):
        self.Wed_Window = Wed_Window 
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1550x800+0+0")

        #--------------textvariable-------------
        self.var_cust_ref = StringVar()
        self.var_Bride_Name = StringVar() 
        self.var_Groom_Name = StringVar() 
        self.var_Date= StringVar() 
        self.var_Wedding_Type= StringVar() 
        self.var_Wedding_Rituals = StringVar() 
        self.var_Wedding_Theme = StringVar() 
        self.var_Wedding_Photoshoot= StringVar() 
        self.var_Dinner = StringVar() 
        self.var_Special_Request = StringVar()  
        
        label_title = Label(self.root, text="Weddings", font=("times new roman", 30, "bold"), fg="black",bg='#ecbee6',relief=RIDGE)
        label_title.place(x=0, y=0, width=1550, height=93)

         #-----------logo---------------
        logo_image1 = Image.open(r"D:\Hotel management system\images\logo1.png")
        logo_image1 = logo_image1.resize((130,130),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image2= ImageTk.PhotoImage(logo_image1) 
        #show image in gui
        label_logo1=Label(self.root, image=self.image2,bd=1,relief=RIDGE)
        label_logo1.place(x=0,y=0,width=190, height=93)
        
        #-----------------background image-------------------
        background_image1 = Image.open(r"D:\Hotel management system\images\wedbg.jpg")
        background_image1 = background_image1.resize((1550,800),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image1= ImageTk.PhotoImage(background_image1) 
        # # #show image in gui
        label_bg1=Label(self.root, image=self.image1,bd=4,relief=RIDGE)
        label_bg1.place(x=0,y=91,width=1550, height=709)
        
        #---------------label frame------------------------------
        wedding_frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Add Details",padx= 1,font=("times new roman", 20, "bold")) #The LabelFrame widget is used to draw a border around its child widgets
        wedding_frame.place(x=370,y=100,width=970,height=690)

        #---------------cust ref------------------------------
        label_cust_ref = Label(wedding_frame, text="Customer Ref", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_cust_ref.grid(row=0,column=0,sticky=W)

        entry_cust_ref = ttk.Entry(wedding_frame,textvariable=self.var_cust_ref,width=30,font=("times new roman", 15))
        entry_cust_ref.grid(row=0, column=1)

        #---------------bride name----------------------
        label_b_name = Label(wedding_frame, text="Bride Name", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_b_name.grid(row=1,column=0,sticky=W)

        entry_b_name = ttk.Entry(wedding_frame,textvariable=self.var_Bride_Name,width=30,font=("times new roman", 15))
        entry_b_name.grid(row=1, column=1)
        
        #---------------groom name----------------------
        label_g_name = Label(wedding_frame, text="Groom Name", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_g_name.grid(row=2,column=0,sticky=W)

        entry_g_name = ttk.Entry(wedding_frame,textvariable=self.var_Groom_Name,width=30,font=("times new roman", 15))
        entry_g_name.grid(row=2, column=1)

        #---------------wedding date----------------------
        label_date = Label(wedding_frame, text="Wedding Date", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_date.grid(row=3,column=0,sticky=W)

        entry_date = ttk.Entry(wedding_frame,textvariable=self.var_Date,width=30,font=("times new roman", 15))
        entry_date.grid(row=3, column=1)
        
        #---------------wedding type---------------------------
        label_wedding = Label(wedding_frame, text="Which type of wedding do you want?", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_wedding.grid(row=4,column=0,sticky=W)

        wedding_combobox = ttk.Combobox(wedding_frame,width=28, textvariable=self.var_Wedding_Type,font=("times new roman", 15, "bold"), state="readonly")
        wedding_combobox["value"] = ["Traditonal Wedding", "Destination Wedding","Elopment Wedding","Vintage Style Wedding", "DIY wedding","Beach Wedding"]
        wedding_combobox.grid(row=4, column=1, sticky=W)

        #---------------wedding rituals---------------------------
        label_rituals = Label(wedding_frame, text="Do you want us to handle all rituals of wedding?", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_rituals.grid(row=5,column=0,sticky=W)

        rituals_combobox = ttk.Combobox(wedding_frame,width=28,textvariable=self.var_Wedding_Rituals, font=("times new roman", 15, "bold"), state="readonly")
        rituals_combobox["value"]= ["Yes", "No"]
        rituals_combobox.grid(row=5, column=1, sticky=W)

        #---------------wedding theme---------------------------
        label_theme = Label(wedding_frame, text="Do you want any theme for the wedding? If yes mention it.", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_theme.grid(row=6,column=0,sticky=W)

        entry_theme = ttk.Entry(wedding_frame,width=30,textvariable=self.var_Wedding_Theme,font=("times new roman", 15))
        entry_theme.grid(row=6, column=1)
       
        #---------------wedding photoshoot---------------------------
        label_preph = Label(wedding_frame, text="Do you want pre-wedding photoshoot?", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_preph.grid(row=7,column=0,sticky=W)

        preph_combobox = ttk.Combobox(wedding_frame,width=28,textvariable=self.var_Wedding_Photoshoot, font=("times new roman", 15, "bold"), state="readonly")
        preph_combobox["value"] = ["Yes", "No"]
        preph_combobox.grid(row=7, column=1, sticky=W)

        #---------------dinner---------------------------
        label_dinner = Label(wedding_frame, text="How do you want to serve Dinner?", font=("times new roman", 15, "bold"),padx = 5, pady=10)
        label_dinner.grid(row=8,column=0,sticky=W)

        dinner_combobox = ttk.Combobox(wedding_frame,width=28,textvariable=self.var_Dinner, font=("times new roman", 15, "bold"), state="readonly")
        dinner_combobox["value"] = ["Plated", "Buffed","Family Style"]
        dinner_combobox.grid(row=8, column=1, sticky=W)
        
        #---------------special request---------------------------
        label_req = Label(wedding_frame, text="Do you want to make any special request? If yes, mention it.", font=("times new roman", 15, "bold"), padx=5, pady=10)
        label_req.grid(row=9, column=0, sticky=W)

        # Create a Combobox to choose "Yes" or "No"
        request_combobox = ttk.Combobox(wedding_frame, width=28, textvariable=self.var_Special_Request,font=("times new roman", 15, "bold"), state="readonly")
        request_combobox["values"] = ["Yes", "No"]
        request_combobox.grid(row=9, column=1, sticky=W)

        # Set a callback function to handle combobox selection
        request_combobox.bind("<<ComboboxSelected>>", self.handle_request_combobox)

        self.entry_req_frame = Frame(wedding_frame)

        #------------------buttons---------
        btn_frame = Frame(wedding_frame, relief=RIDGE)
        btn_frame.place(x=0,y=500,width=900,height=190)

        #-----------button1-----------------
        btn_add = Button(btn_frame, text="Add",command=self.add_data,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btn_add.grid(row=0,column=0,padx=30,pady=30)

        btnset = Button(btn_frame, text="Reset",command=self.reset_data,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnset.grid(row=0,column=1,padx=30,pady=30)

        btnview = Button(btn_frame, text="viewall",command=self.weddingdetail,width=12,font=("times new roman",15),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
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
        if self.var_Wedding_Type.get()=="" or self.var_Date.get()=="":
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

                # Use the same reference ID for the wedding
                wedding_ref = self.var_cust_ref.get()

                # Insert wedding details into the database
                conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00",
                                            database="eventmanagementsystem")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO wedding VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (wedding_ref, self.var_Bride_Name.get(), self.var_Groom_Name.get(),
                                self.var_Date.get(), self.var_Wedding_Type.get(),
                                self.var_Wedding_Rituals.get(), self.var_Wedding_Theme.get(),
                                self.var_Wedding_Photoshoot.get(), self.var_Dinner.get(),
                                self.var_Special_Request.get()))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Wedding details have been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    #----------delete----------------
    def delete_data(self):
        confirm_message = messagebox.askyesno("Event Management System","Do you want to Delete the data ?", parent=self.root)
        if confirm_message>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="#coDing00",database="eventmanagementsystem")
            my_cursor= conn.cursor()
            del_query= "delete from wedding where Wed_ID=%s"
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
        self.var_Bride_Name.set("") 
        self.var_Groom_Name.set("") 
        self.var_Date.set("") 
        self.var_Wedding_Type.set("")  
        self.var_Wedding_Rituals.set("")  
        self.var_Wedding_Theme.set("")  
        self.var_Wedding_Photoshoot.set("")  
        self.var_Dinner.set("")  
        self.var_Special_Request.set("")   

        # random_ref = random.randint(1000,9999)
        # self.var_ref.set(str(random_ref)) 

    def weddingdetail(self):
        self.new_Window = Toplevel(self.root)
        self.app = view_wed_Window(self.new_Window)
        self.app.wedding_window = self

if __name__ == "__main__":
    root=Tk()
    view_wed_obj = view_wed_Window(root)
    obj =wedding_win(root,view_wed_obj)
    view_wed_obj.wedding_window = obj
    root.mainloop()        
