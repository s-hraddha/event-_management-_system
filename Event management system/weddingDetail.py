from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # for adding image in gui
from PIL import ImageDraw
from tkinter import messagebox
import mysql.connector


class view_wed_Window:
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

        self.wedding_detail_table = ttk.Treeview(view_table,columns=("Wed_Ref","Bride_Name","Groom_Name","Date","Wedding_Type","Wedding_Rituals","Wedding_Theme",
                                                                  "Wedding_Photoshoot","Dinner","Special_Request"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.wedding_detail_table.xview)
        scroll_y.config(command=self.wedding_detail_table.yview)
        
        self.wedding_detail_table.heading("Wed_Ref",text="Wed_Ref")
        self.wedding_detail_table.heading("Bride_Name",text="Bride_Name")
        self.wedding_detail_table.heading("Groom_Name",text="Groom_Name")
        self.wedding_detail_table.heading("Date",text="Date")
        self.wedding_detail_table.heading("Wedding_Type",text="Wedding_Type")
        self.wedding_detail_table.heading("Wedding_Rituals",text="Wedding_Rituals")
        self.wedding_detail_table.heading("Wedding_Theme",text="Wedding_Theme")
        self.wedding_detail_table.heading("Wedding_Photoshoot",text="Wedding_Photoshoot")
        self.wedding_detail_table.heading("Dinner",text="Dinner")
        self.wedding_detail_table.heading("Special_Request",text="Special_Request")
        
        self.wedding_detail_table["show"]="headings"
        self.wedding_detail_table.column("Wed_Ref",width=100)
        self.wedding_detail_table.column("Bride_Name",width=100)
        self.wedding_detail_table.column("Groom_Name",width=100)
        self.wedding_detail_table.column("Date",width=100)
        self.wedding_detail_table.column("Wedding_Type",width=100)
        self.wedding_detail_table.column("Wedding_Rituals",width=100)
        self.wedding_detail_table.column("Wedding_Theme",width=100)
        self.wedding_detail_table.column("Wedding_Photoshoot",width=100)
        self.wedding_detail_table.column("Dinner",width=100)
        self.wedding_detail_table.column("Special_Request",width=100)
        self.wedding_detail_table.pack(fill=BOTH,expand=1)
        self.wedding_detail_table.bind("<ButtonRelease-1>",self.get_info) #This method is used to associate an event with a callback function.
                                                                       #<buttonRelease-1> specifically refers to the release of the left mouse button.
        self.fetch_data() 

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="#coDing00",database="eventmanagementsystem")
        my_cursor= conn.cursor()
        my_cursor.execute("select * from wedding")
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.wedding_detail_table.delete(*self.wedding_detail_table.get_children())
            for i in data:
                self.wedding_detail_table.insert("",END, values=i)
            conn.commit()
        conn.close() 


    #------------get data on table----------------
    def get_info(self, event=""):
        info_row=self.wedding_detail_table.focus() 
        row_data=self.wedding_detail_table.item(info_row)
        row=row_data["values"]  

        #update the entry widgets in cutomerwindow
        if len(row) >0:
            self.wedding_window.var_cust_ref.set(row[0])
            self.wedding_window.var_Bride_Name.set(row[1]) 
            self.wedding_window.var_Groom_Name.set(row[2]) 
            self.wedding_window.var_Date.set(row[3]) 
            self.wedding_window.var_Wedding_Type.set(row[4])  
            self.wedding_window.var_Wedding_Rituals.set(row[5])  
            self.wedding_window.var_Wedding_Theme.set(row[6])  
            self.wedding_window.var_Wedding_Photoshoot.set(row[7])  
            self.wedding_window.var_Dinner.set(row[8])  
            self.wedding_window.var_Special_Request.set(row[9])     
    
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="#coDing00", database="eventmanagementsystem")
        my_cursor = conn.cursor()
    
        if self.search_by.get() and self.txt_search.get():
            query = f"select * from wedding where {self.search_by.get()} LIKE '%{self.txt_search.get()}%'"
            my_cursor.execute(query)
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.wedding_detail_table.delete(*self.wedding_detail_table.get_children())
                for i in rows:
                    self.wedding_detail_table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No matching records found.")
        else:
            messagebox.showwarning("Warning", "Please provide search criteria.")
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = view_wed_Window(root)
    root.mainloop()         