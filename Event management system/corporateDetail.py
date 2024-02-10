from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # for adding image in gui
from PIL import ImageDraw
from tkinter import messagebox
import mysql.connector


class view_corporate_Window:
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

        btnsearch = Button(self.root, text="Search",command=self.search_data,width=12,font=("times new roman",13),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnsearch.grid(row=0,column=3,padx=4,pady=5)

        btnshow = Button(self.root, text="showAll",width=12,command=self.fetch_data,font=("times new roman",13),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        btnshow.grid(row=0,column=4,padx=4,pady=5)

        #--------------show data table--------------------

        view_table = Frame(self.root,bd=2,relief=RIDGE)
        view_table.place(x=0,y=45,width=898, height=553)

        scroll_x =ttk.Scrollbar(view_table,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(view_table,orient=VERTICAL)

        self.corporate_detail_table = ttk.Treeview(view_table,columns=("Cust_Ref","Name","Company_Name","Email","Job_Title","Address",
                                                                  "Website","Company_size","Event_Type","Date","Special Request"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.corporate_detail_table.xview)
        scroll_y.config(command=self.corporate_detail_table.yview)
        
        self.corporate_detail_table.heading("Cust_Ref",text="Cust_Ref")
        self.corporate_detail_table.heading("Name",text="Name")
        self.corporate_detail_table.heading("Company_Name",text="Company_Name")
        self.corporate_detail_table.heading("Email",text="Email")
        self.corporate_detail_table.heading("Job_Title",text="Job_Title")
        self.corporate_detail_table.heading("Address",text="Address")
        self.corporate_detail_table.heading("Website",text="Website")
        self.corporate_detail_table.heading("Company_size",text="Company_size")
        self.corporate_detail_table.heading("Event_Type",text="Event_Type")
        self.corporate_detail_table.heading("Date",text="Date")
        self.corporate_detail_table.heading("Special Request",text="Special Request")
        
        self.corporate_detail_table["show"]="headings"
        self.corporate_detail_table.column("Cust_Ref",width=100)
        self.corporate_detail_table.column("Name",width=100)
        self.corporate_detail_table.column("Company_Name",width=100)
        self.corporate_detail_table.column("Email",width=100)
        self.corporate_detail_table.column("Job_Title",width=100)
        self.corporate_detail_table.column("Address",width=100)
        self.corporate_detail_table.column("Website",width=100)
        self.corporate_detail_table.column("Company_size",width=100)
        self.corporate_detail_table.column("Event_Type",width=100)
        self.corporate_detail_table.column("Date",width=100)
        self.corporate_detail_table.column("Special Request",width=100)
        self.corporate_detail_table.pack(fill=BOTH,expand=1)
        self.corporate_detail_table.bind("<ButtonRelease-1>",self.get_info)
        self.fetch_data()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="#coDing00",database="eventmanagementsystem")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from corporate")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.corporate_detail_table.delete(*self.corporate_detail_table.get_children())
            for i in data:
                self.corporate_detail_table.insert("",END, values=i)
            conn.commit()
        conn.close() 


    def get_info(self, event=""):
        info_row=self.corporate_detail_table.focus() 
        row_data=self.corporate_detail_table.item(info_row)
        row=row_data["values"]  

            #update the entry widgets in cutomerwindow
        if len(row) >0:
                # self.corporate_window.var_cust_ref.set(row[0])
            self.corporate_window.var_cust_ref.set(row[1]) 
            self.corporate_window.var_var_Name.set(row[2]) 
            self.corporate_window.var_company_Name.set(row[3]) 
            self.corporate_window.var_Email.set(row[4])  
            self.corporate_window.var_job_title.set(row[5])  
            self.corporate_window.var_address.set(row[6])  
            self.corporate_window.var_website.set(row[7])  
            self.corporate_window.var_size.set(row[8])  
            self.corporate_window.var_Event_type.set(row[9])  
            self.corporate_window.var_Date.set(row[10])  
            self.corporate_window.var_Special_Request.set(row[11])     
    
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00", database="eventmanagementsystem")
        my_cursor = conn.cursor()
    
        if self.search_by.get() and self.txt_search.get():
            query = f"select * from corporate where {self.search_by.get()} LIKE '%{self.txt_search.get()}%'"
            my_cursor.execute(query)
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.corporate_detail_table.delete(*self.corporate_detail_table.get_children())
                for i in rows:
                    self.corporate_detail_table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No matching records found.")
        else:
            messagebox.showwarning("Warning", "Please provide search criteria.")
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = view_corporate_Window(root)
    root.mainloop()         