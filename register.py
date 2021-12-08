from tkinter import*
from tkinter import ttk,messagebox
from tkinter import font
import mysql.connector
class Register:
    
    def __init__(self,root):
        self.root=root
        self.root.title("APPLICATION FORM")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="sky blue")
        #bg img
        # bg=PhotoImage(file="E:\\python\\gui\\project\\pro 18\\bg1.png")
        # my_label=Label(self.root,image=bg)
        # my_label.place(x=0, y=0, relwidth=1, relheight=1)
        #self.bg=ImageTk.PhotoImage(image= "bg1.jpg")
        #bg=Label(self.root,image=self.bg).place(x=250,y=0,realwidth=1,realheight=1)
        #left img
        #self.left=PhotoImage(file="2.jpg")
        #left=Label(self.root,image=self.left).place(x=80,y=100,relwidth=400,realheight=500)
        # frame
        Frame1=Frame(self.root,bg="white")
        Frame1.place(x=400,y=100,width=800,height=550)
        # Heading
        title=Label(Frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=50,y=30)
        #First name
        f_name=Label(Frame1,text="First Name",font=("times new roman",12,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        #Last name
        f_name=Label(Frame1,text="Last Name",font=("times new roman",12,"bold"),bg="white",fg="gray").place(x=470,y=100)
        self.txt_lname=Entry(Frame1,font=("times new roman",12),bg="silver")
        self.txt_lname.place(x=470,y=130,width=250)
        #contact number
        contact=Label(Frame1,text="Contact No",font=("times new roman",12,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(Frame1,font=("times new roman",12),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        #email
        Email=Label(Frame1,text="Email id",font=("times new roman",12,"bold"),bg="white",fg="gray").place(x=470,y=170)
        self.txt_email=Entry(Frame1,font=("times new roman",12),bg="lightgray")
        self.txt_email.place(x=470,y=200,width=250)
        #gender
        Gender=Label(Frame1,text="Gender",font=("times new roman",12,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_gen=ttk.Combobox(Frame1,font=("times new roman",12),state='Readonly',justify=CENTER)
        self.cmb_gen['values']=("Male","Female","trans gender")
        self.cmb_gen.place(x=50,y=270,width=250)
        #branch
        Branch=Label(Frame1,text="Branch",font=("times new roman",12,"bold"),bg="white",fg="gray").place(x=470,y=240)
        self.txt_branch=Entry(Frame1,font=("times new roman",12),bg="lightgray")
        self.txt_branch.place(x=470,y=270,width=250)
        #org
        self.ch1=IntVar()
        self.ch2=IntVar()
        self.ch3=IntVar()
        self.ch4=IntVar()
        self.ch5=IntVar()
        self.ch6=IntVar()
        self.ch7=IntVar()
        self.ch8=IntVar()
        self.ch9=IntVar()
        self.ch10=IntVar()
        
        chk=Checkbutton(Frame1,variable=self.ch1,text="(1). Cyber security organization").place(x=50,y=300)
        chk=Checkbutton(Frame1,variable=self.ch2,text="(2). Community service organizations").place(x=50,y=330)
        chk=Checkbutton(Frame1,variable=self.ch3,text="(3). Media and publication organizations").place(x=50,y=360)
        chk=Checkbutton(Frame1,variable=self.ch4,text="(4). Political or multicultural organizations").place(x=50,y=390)
        chk=Checkbutton(Frame1,variable=self.ch5,text="(5). Recreation and sports organizations").place(x=50,y=420)
        chk=Checkbutton(Frame1,variable=self.ch6,text="(6). Student government organizations").place(x=480,y=300)
        chk=Checkbutton(Frame1,variable=self.ch7,text="(7). Religious and spiritual organizations").place(x=480,y=330)
        chk=Checkbutton(Frame1,variable=self.ch8,text="(8). Nano technology organization").place(x=480,y=360)
        chk=Checkbutton(Frame1,variable=self.ch9,text="(9). Leadership development").place(x=480,y=390)
        chk=Checkbutton(Frame1,variable=self.ch10,text="(10). Inovation and Developement organization").place(x=480,y=420)
        btn_submit=Button(root,fg="black",text="Submit",width=14,height=1,bg="peach puff",font=("comicsansms",20),command=self.register_data).place(x=700,y=580)
    def register_data(self):
        print("Organizations:")
        if(self.ch1.get()==1):
            print("Cyber security organization")
        if(self.ch2.get()==1):
            print("Community service organizations")
        if(self.ch3.get()==1):
            print("Media and publication organizations")
        if(self.ch4.get()==1):
            print("Political or multicultural organizations")
        if(self.ch5.get()==1):
            print("Recreation and sports organizations")
        if(self.ch6.get()==1):
            print("Student government organizations")
        if(self.ch7.get()==1):
            print("Religious and spiritual organizations")
        if(self.ch8.get()==1):
            print("Nano technology organization")
        if(self.ch9.get()==1):
            print("Leadership development")
        if(self.ch10.get()==1):
            print("Inovation and Developement organization")
        if print(self.txt_fname,self.txt_lname,self.txt_contact,self.txt_email,self.cmb_gen,self.txt_branch):
        # if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_gen.get()=="" or self.txt_branch.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            messagebox.showinfo("succes","Register Successful",parent=self.root)
            # try:
            #     con=mysql.connector(host="localhost",user="root",password="sagar@143",database="sagar")
            #     cur=con.cursor()
            #     cur.execute("select * from students where email=%s",self.txt_email.get())
            #     row=cur.fetchone()
            #     print(row)
            #     cur.execute("insert into sagar(f_name,l_name,contact,email,gender,branch) value(%s%s%s%s%s%s)",
            #                     (self.txt_fname.get(),
            #                     self.txt_lname.get(),
            #                     self.txt_contact.get(),
            #                     self.txt_email.get(),
            #                     self.cmb_gen.get(),
            #                     self.txt_branch.get()
            #                     ))
            #     con.commit()
            #     con.close()
            #     messagebox.showinfo("succes","Register Successful",parent=self.root)
            # except Exception as es:
            #     messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
root=Tk()
obj=Register(root)
root.mainloop()
