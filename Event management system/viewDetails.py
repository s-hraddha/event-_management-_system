from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # for adding image in gui
from PIL import ImageDraw
from tkinter import messagebox
import mysql.connector


class viewAllWindow:
    def __init__(self,root):
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("900x600+280+140") 

        searchby=Label(self.root,font=("times new roman", 17, "bold"),text="Search:",bg="#FAD8D8",fg="black")
        searchby.grid(row=0,column=0,sticky=W,padx=5)
        
        self.search_by=StringVar()
        search_combobox = ttk.Combobox(self.root,width=20,textvariable=self.search_by, state="readonly")
        search_combobox["values"] = ["refrence_id","cust_name"]
        search_combobox.grid(row=0, column=1, sticky=W,ipady=4)

        self.txt_search = StringVar() 
        txtSearch=ttk.Entry(self.root,textvariable=self.txt_search,font=("times new roman", 17, "bold"),width=15)
        txtSearch.grid(row=0,column=2,padx=2, pady=5)

        btnsearch = Button(self.root,command=self.search_data, text="Search",width=12,font=("times new roman",13),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnsearch.grid(row=0,column=3,padx=4,pady=5)

        btnshow = Button(self.root,command=self.fetch_data, text="showAll",width=12,font=("times new roman",13),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnshow.grid(row=0,column=4,padx=4,pady=5)

        #--------------show data table--------------------

        view_table = Frame(self.root,bd=2,relief=RIDGE)
        view_table.place(x=0,y=45,width=898, height=553)

        scroll_x =ttk.Scrollbar(view_table,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(view_table,orient=VERTICAL)

        self.view_detail_table = ttk.Treeview(view_table,columns=("ref","name","gender","phone","email","address",
                                                                  "pincode","idproof","idnumber"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.view_detail_table.xview)
        scroll_y.config(command=self.view_detail_table.yview)
        
        self.view_detail_table.heading("ref",text="Refrence No")
        self.view_detail_table.heading("name",text="Name")
        self.view_detail_table.heading("gender",text="Gender")
        self.view_detail_table.heading("phone",text="Phone No")
        self.view_detail_table.heading("email",text="Email")
        self.view_detail_table.heading("address",text="Address")
        self.view_detail_table.heading("pincode",text="Pincode")
        self.view_detail_table.heading("idproof",text="ID-Proof")
        self.view_detail_table.heading("idnumber",text="ID-Number")
        
        self.view_detail_table["show"]="headings"
        self.view_detail_table.column("ref",width=100)
        self.view_detail_table.column("name",width=100)
        self.view_detail_table.column("gender",width=100)
        self.view_detail_table.column("phone",width=100)
        self.view_detail_table.column("email",width=100)
        self.view_detail_table.column("address",width=100)
        self.view_detail_table.column("pincode",width=100)
        self.view_detail_table.column("idproof",width=100)
        self.view_detail_table.column("idnumber",width=100)

        self.view_detail_table.pack(fill=BOTH,expand=1)
        self.view_detail_table.bind("<ButtonRelease-1>",self.get_info) #This method is used to associate an event with a callback function.
                                                                       #<buttonRelease-1> specifically refers to the release of the left mouse button.
        self.fetch_data() 

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="#coDing00",database="eventmanagementsystem")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from customer")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.view_detail_table.delete(*self.view_detail_table.get_children())
            for i in data:
                self.view_detail_table.insert("",END, values=i)
            conn.commit()
        conn.close()  
        
 
    #------------get data on table----------------
    def get_info(self, event=""):
        info_row=self.view_detail_table.focus() 
        row_data=self.view_detail_table.item(info_row)
        row=row_data["values"]  

        #update the entry widgets in cutomerwindow
        if len(row) >0:
            self.customer_window.var_ref.set(row[0])
            self.customer_window.var_custName.set(row[1])
            self.customer_window.var_gender.set(row[2])
            self.customer_window.var_phn.set(row[3])
            self.customer_window.var_email.set(row[4])
            self.customer_window.var_address.set(row[5])
            self.customer_window.var_pincode.set(row[6])
            self.customer_window.var_idproof.set(row[7])
            self.customer_window.var_idNum.set(row[8]) 

    # def search_data(self):
    #     conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00", database="eventmanagementsystem")
    #     my_cursor = conn.cursor()
        
    #     my_cursor.execute("select * from customer where "+str(self.search_by.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
    #     rows=my_cursor.fetchall()
    #     if len(rows)!=0:
    #         self.view_detail_table.delete(*self.view_detail_table.get_children())
    #         for i in rows:
    #             self.view_detail_table.insert("",END, values=i)
    #         conn.commit()
    #     conn.close()     

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00", database="eventmanagementsystem")
        my_cursor = conn.cursor()
    
        if self.search_by.get() and self.txt_search.get():
            query = f"select * from customer where {self.search_by.get()} LIKE '%{self.txt_search.get()}%'"
            my_cursor.execute(query)
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.view_detail_table.delete(*self.view_detail_table.get_children())
                for i in rows:
                    self.view_detail_table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No matching records found.")
        else:
            messagebox.showwarning("Warning", "Please provide search criteria.")
        conn.close()

   
        
        

if __name__ == "__main__":
    root = Tk()
    obj = viewAllWindow(root)
    root.mainloop()         