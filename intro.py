from tkinter import*
root=Tk()
root.geometry("2000x2000")


def sagarcode():
    import register
def openNewWindow():

    newWindow=Toplevel(root)
    newWindow.title("INTRODUCTION")
    newWindow.geometry("2000x2000")
    Label(newWindow,bg="green",fg="white",width=2000,text="INTRODUCTION \n\n STUDENT  ASSOCIATION  :  ASSOCIATION  OF  THE  STUDENT , BY  THE  STUDENT , FOR THE STUDENT.\nThe Division of Student Welfare has always been filled with exciting, dynamic opportunities and to help push\n the students beyond their comfort levels and unlock their potential.Our university gates are always graced by \n eminent and enigmatic personalities.Student Organization Cell comes under the Aegis of Division of Student\n  Welfare,Lovely Professional University, Punjab with more than 200 organisations are working for the beneficiary \n of Students under more than 18 Categories.Here, students get the opportunity to start their own  organizations \n to bring together students  who share the same interests and ideologies. Student Organizations majorly work for \n the  Holistic  growth of Students  as they  learn to  innovate and initiate .\n Makes students well aware of the current trends: Joining  and working in a student organization not only require \n commitment but one also needs to be aware of the current market trends to organize events, which will turn out to be a hit.\n Improves Interpersonal Skills:  It’s like a long-term soft skills class experience when you are an active member \n  of a student organization. It demands a student to communicate things well either to the new hires or to clients. \n There is when you learn how to express yourself and how to communicate well. \n Increases network marketing: When you work for a student organization of any category, you take the oath  \n to work for the community and it’s when you come across people you haven’t met before. Just imagine: you’re going \n  to a firm for a sponsorship request for an event and that firm coming for in campus placement – it’s \n definitely going to work for you. \n Teaches teamwork: Working in a student organization means that all the team members are involved in \n the process. You’ll learn how to work with a team, making you realize how teamwork can positively affect our life. \n \n * Students can join any association which they like by clicking on the apply button from the previous page.* ",font=("comicsansms",20)).pack()
     
    
root.title('application form')
bg=PhotoImage(file="E:\\python\\gui\\project\\pro 18\\1.png")
my_label=Label(root,image=bg)
my_label.place(x=20, y=80, relwidth=1, relheight=1)

f1=Frame(root,bg='yellow')
f2=Frame(root,borderwidth=2,relief=SUNKEN)
l=Label(f1,text="STUDENT ASSOCIATION",bg='sky blue',height=1,width=2000, fg="BLACK",font=("comicsansms",40),relief=GROOVE)
b=Button(root,fg="WHITE",text="CLICK FOR APPLY",width=50,height=1,bg="DARKBLUE",font=("comicsansms",20),command=sagarcode)

b1=Button(f2,fg="purple",text="Introduction about organization",width=50,height=1,bg="chocolate",font=("comicsansms",20),command= openNewWindow)

f1.pack()
f2.pack(side=LEFT,anchor="nw")
l.pack()
b.pack()
b1.pack()
root.mainloop()