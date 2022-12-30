from tkinter import *
from tkinter import messagebox
#import SignUp

#def signup_run():
 #   top.destroy()
  #  SignUp.run(

def pred():
    import db_prac
    Location=e1.get()
    BHK=e2.get()
    Area=e4.get()
    Price=db_prac.run1(Location,Area,BHK)
    #l8 = Label(f, text="The predicted price is "+Price, foreground="Black", font=("Times", "18", "bold italic"))
    #l8.place(x=350, y=800, width=200, height=18)
    messagebox.showinfo("Predicted Price", "The predicted price is " + Price)

def back():
    top.destroy()
    import mainfile
    mainfile.run2()


def run1():
    global top
    global e1
    global e2
    global e4
    global f
    top=Tk()
    top.title("Login Form")
    top.geometry("1000x1000")

#top.wm_iconbitmap('home.ico')
    bg = PhotoImage(file="realestate.png")
    f = Frame(top, height=1920, width=1280, cursor="arrow")

    lx = Label(f, image=bg)
    lx.place(x=0, y=0)
#f=Frame(top,height=400,width=750,bg="#56BBF1",cursor="arrow")

    l1=Label(f,text="Welcome to House Pricing predictor",foreground="Black",font=("Times","36","bold italic"))
    l1.place(x=180,y=0,width=750,height=100)

    l2=Label(f,text="Want to predict a new house in Mumbai? try filling the details below:",foreground="Black",font=("Times","14","bold italic"))
    l2.place(x=210,y=120,width=600,height=50)

    l3=Label(f,text="Select the location",foreground="Black",font=("Times","18","bold italic"))
    l3.place(x=180,y=180,width=200,height=18)

    l4=Label(f,text="Enter BHK",foreground="Black",font=("Times","18","bold italic"))
    l4.place(x=535,y=180,width=200,height=18)

    #l5=Label(f,text="Username",foreground="Black",font=("Times","18","bold italic"))
    #l5.place(x=170,y=290,width=200,height=18)

    l6=Label(f,text="Enter total sq.ft",foreground="Black",font=("Times","18","bold italic"))
    l6.place(x=350,y=280,width=200,height=18)

    e1=Entry(f,font=("Times","12","bold italic"))
    e1.place(x=180,y=200,width=270,height=40)

    e2=Entry(f,font=("Times","12","bold italic"))
    e2.place(x=530,y=200,width=270,height=40)

    #e3=Entry(f,font=("Times","12","bold italic"))
    #e3.place(x=170,y=320,width=270,height=40)

    e4=Entry(f,font=("Times","12","bold italic"))
    e4.place(x=350,y=320,width=270,height=40)

#b1=Button(f,text="Login",bg="#5800FF",foreground="white",font=("Times","12","bold italic"))
#b1.place(x=60,y=200,width=70,height=30)

#b2=Button(f,text="Sign Up",bg="#5800FF",foreground="white",font=("Times","12","bold italic"))   #, command=signup_run)
#b2.place(x=150,y=200,width=70,height=30)

    b3=Button(f,text="Predict Price",relief=SOLID,bg="#5800FF",foreground="white",command=pred,font=("Times","24","bold italic"))
    b3.place(x=325,y=380,width=300,height=40)

    b4=Button(f,text="Back",relief=SOLID,command=back,bg="#5800FF",foreground="white",font=("Times","24","bold italic"))
    b4.place(x=325,y=700,width=300,height=40)

    f.pack()
    top.mainloop()

if __name__ == '__main__':
    run1()