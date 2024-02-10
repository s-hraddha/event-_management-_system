from tkinter import *
from PIL import Image, ImageTk # for adding image in gui
from PIL import ImageDraw
from customer import CustomerWindow
from wedding import wedding_win
from corporate import Corporate_win
from social import social_win
from about import about_win

class EventManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1550x800+0+0")  #0+0 means the starting of thw window
         
        #---------tilte--------------------
        label_title = Label(self.root, text="EVENT MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), fg="black",bg='#ecbee6',relief=RIDGE)
        label_title.place(x=0, y=0, width=1550, height=93)


        #-----------logo---------------
        logo_image1 = Image.open(r"D:\Hotel management system\images\logo1.png") #r is used to convert the backslash
        logo_image1 = logo_image1.resize((130,130),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image2= ImageTk.PhotoImage(logo_image1) 
        #show image in gui
        label_logo1=Label(self.root, image=self.image2,bd=1,relief=RIDGE)
        label_logo1.place(x=0,y=0,width=190, height=93)

        #----------main frame------------
        main_frame = Frame(self.root,bd=1, relief=RIDGE)
        main_frame.place(x=0,y=95,width=1550,height=700)

        #  # -------------NAVBAR LIST-------------------
        navbar_label = Label(main_frame,text="MENU",font=("times new roman",25),bg="#ecbee6",fg="black",bd=2,relief=RIDGE)
        navbar_label.place(x=0,y=0,width=230)


         #--------------btn frame-----------
        btn_frame = Frame(self.root, bd=2, relief=RIDGE,bg="#ecbee6")
        btn_frame.place(x=0,y=140,width=230,height=334)

        # #-----------button1-----------------
        
        button1 = Button(btn_frame, text="About Us",command=self.about_detail,width=12,font=("times new roman",25),bg="#FAD8D8",fg="black",bd=2,relief=RIDGE)
        button1.grid(row=0,column=0,pady=1)

        button2 = Button(btn_frame, text="Customer",command=self.cust_detail,width=12,font=("times new roman",25),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        button2.grid(row=1,column=0,pady=1)

        button3 = Button(btn_frame, text="Weddings",command=self.wed_detail,width=12,font=("times new roman",25),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        button3.grid(row=2,column=0,pady=1)

        button4 = Button(btn_frame, text="Corporate Events",command=self.corporate_detail,width=12,font=("times new roman",25),bg="#FAD8D8",fg="black",bd=1,relief=RIDGE)
        button4.grid(row=3,column=0,pady=1)

        button5 = Button(btn_frame, text="Social Events",command=self.social_detail,width=12,font=("times new roman",25),bg="#FAD8D8",fg="black",bd=2,relief=RIDGE)
        button5.grid(row=4,column=0,pady=1)

        #--------background image-------
        background_image1 = Image.open(r"D:\Hotel management system\images\bg1.jpg")
        background_image1 = background_image1.resize((1305,700),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image1= ImageTk.PhotoImage(background_image1) 
        # # #show image in gui
        # label_bg1=Label(self.root, image=self.image1,bd=4,relief=RIDGE)
        # label_bg1.place(x=230,y=91,width=1313, height=709)
        text_label = Label(root, text='WELCOME \n TO \n TULIP EVENT MANAGEMENT', image=self.image1, compound="center",font=("times new roman",40,"bold"),fg="#4A235A")
        text_label.place(x=230, y=93)

        #---------------side image---------------
        side_image1 = Image.open(r"D:\Hotel management system\images\social.jpg")
        side_image1 = side_image1.resize((350,350),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image3= ImageTk.PhotoImage(side_image1) 
        # # #show image in gui
        label_side1=Label(main_frame, image=self.image3,bd=4,relief=RIDGE)
        label_side1.place(x=0,y=310,width=230, height=426)
    
    def about_detail(self):
        self.new_Window = Toplevel(self.root)  #toplevel object which will be treated as a new window
        self.app = about_win(self.new_Window)

    def cust_detail(self):
        self.new_Window1 = Toplevel(self.root)  #toplevel object which will be treated as a new window
        self.app1 = CustomerWindow(self.new_Window1, self)

    def wed_detail(self):
        self.new_Window2 = Toplevel(self.root)
        self.app2 = wedding_win(self.new_Window2,self)   

    def corporate_detail(self):
        self.new_Window3 = Toplevel(self.root)
        self.app3 = Corporate_win(self.new_Window3,self) 

    def social_detail(self):
        self.new_Window4 = Toplevel(self.root)
        self.app4 = social_win(self.new_Window4,self)    
     

if __name__ == "__main__":
    root=Tk()
    obj = EventManagementSystem(root)
    root.mainloop()        


 