from tkinter import *
from tkinter import Frame
from tkinter import messagebox

def signup_run():
    top.destroy()
    import SignUp
    SignUp.run()

def forgot():
    top.destroy()
    import forgot
    forgot.run1()


def mainfile():
    import sqlite_prac
    Username=e1.get()
    Password=e2.get()
    Password1=sqlite_prac.authenticate(Username)
    if(Password==Password1):
        messagebox.showinfo("Login Successfull", "Login Successfull")
        top.destroy()
        import mainfile
        mainfile.run2()
    else:
        messagebox.showinfo("Login Unsuccessfull", "Credentials are incorrect,try again")

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)


def run1():
    global top
    global e1
    global e2
    global canvas
    global fps

    top=Tk()
    top.title("Login Form")
    top.geometry("1024x768")

    bg = PhotoImage(file = "realestate.png")
    f=Frame(top,height=1920,width=1280,cursor="arrow")

    lx=Label(f,image=bg)
    lx.place(x=0,y=0)

    canvas = Canvas(top, bg='black')
    canvas.pack(fill=BOTH, expand=1)
    text_var = "House Pricing Prediction"
    text = canvas.create_text(0, -2000, text=text_var, font=('Times New Roman', 24, 'bold'), fill='white',
                              tags=("marquee",), anchor='w')
    x1, y1, x2, y2 = canvas.bbox("marquee")
    width = x2 - x1
    height = y2 - y1
    canvas['width'] = width
    canvas['height'] = height
    fps = 70  # Change the fps to make the animation faster/slower
    shift()

    l1=Label(f,text="Username",bg="#DFDFDE",anchor="nw",foreground="Black",font=("Times","24","bold italic"))
    l1.place(x=400,y=250)

    e1=Entry(f,background="#D1D1D1",font=("Times","24","bold italic"))
    e1.place(x=600,y=255,width=200,height=30)

    l2=Label(f,anchor="nw",bg="#DFDFDE",text="Password",foreground="Black",font=("Times","24","bold italic"))
    l2.place(x=400,y=355)

    e2=Entry(f,show="*",background="#D1D1D1",font=("Times","24","bold italic"))
    e2.place(x=600,y=360,width=200,height=30)

    b1=Button(f,relief=SOLID,anchor="nw",text=" Login",bg="#6BCB77",activeforeground="#398AB9",activebackground="#D1D1D1",foreground="white",font=("Times","24","bold italic"),command=mainfile)
    b1.place(x=340,y=500,width=100,height=50)

    b2=Button(f,relief=SOLID,cursor="hand1",anchor="nw",text="Sign Up",bg="#6BCB77",activeforeground="#398AB9",activebackground="#D1D1D1",foreground="white",font=("Times","24","bold italic"), command=signup_run)
    b2.place(x=500,y=500,width=120,height=50)

    b3=Button(f,relief=SOLID,cursor="hand1",anchor="nw",text="Forgot Password?",bg="#6BCB77",activeforeground="#398AB9",activebackground="#D1D1D1",foreground="white",font=("Times","24","bold italic"),command=forgot)
    b3.place(x=680,y=500,width=250,height=50)


    f.pack()

    top.mainloop()
if __name__ == '__main__':
    run1()
