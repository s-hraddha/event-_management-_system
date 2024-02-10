from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk # for adding image in gui
from PIL import ImageDraw
from tkinter import messagebox
import webbrowser


class about_win:
    def __init__(self,root):
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1550x800+0+0")

        label_title = Label(self.root, text="About Us", font=("times new roman", 30, "bold"), fg="black",bg='#ecbee6',relief=RIDGE)
        label_title.place(x=0, y=0, width=1550, height=93)

         #-----------logo---------------
        logo_image1 = Image.open(r"D:\Hotel management system\images\logo1.png")
        logo_image1 = logo_image1.resize((130,130),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image2= ImageTk.PhotoImage(logo_image1) 
        #show image in gui
        label_logo1=Label(self.root, image=self.image2,bd=1,relief=RIDGE)
        label_logo1.place(x=0,y=0,width=190, height=93)

        #--------background image-------
        background_image1 = Image.open(r"D:\Hotel management system\images\bg3.jpg")
        background_image1 = background_image1.resize((1500,700),Image.ANTIALIAS) #resize the image ANTIALIAS is a high-quality resampling filter that produces smooth results.
        self.image1= ImageTk.PhotoImage(background_image1) 
        # # #show image in gui
        # label_bg1=Label(self.root, image=self.image1,bd=4,relief=RIDGE)
        # label_bg1.place(x=230,y=91,width=1313, height=709)
        about_text ='''Welcome to Tulip Event Management, where we blossom creativity into 
                    extraordinary experiences! With a passion for precision and a 
                    flair for the fabulous, we are your dedicated partners in 
                    crafting seamless and unforgettable events.\n
                    At Tulip, we understand that each event is a unique bloom, 
                    deserving of its own distinct charm. Drawing from years of 
                    expertise, we specialize in curating events that range 
                    from corporate gatherings and private celebrations to 
                    weddings that bloom with romance.\n
                    THANKYOU!!!'''
        
        
        text_label = Label(root, text=about_text,compound="center", image=self.image1,font=("times new roman",20,"bold"),fg="#4A235A")
        text_label.place(x=0, y=91)
        
        contact_frame = Frame(self.root,relief=RIDGE,bg="#FAD8D8")
        contact_frame.place(x=1240,y=91,width=300, height=799)
        
        contact_text='''Tulip event management \n 1206 W. 38th\n Street Suite 1104 \n Greater Noida, \nDelhi 230575\n\n\ntulipevent009@gmail.com\n\n\n0512-657436'''
    
        contact_label = Label(contact_frame,compound="center",text=contact_text,font=("times new roman",20),bg="#FAD8D8")
        contact_label.place(x=0,y=20)

        
   


if __name__ == "__main__":
    root=Tk()
    obj = about_win(root)
    root.mainloop()         