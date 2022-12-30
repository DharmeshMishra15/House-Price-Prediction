from tkinter import *
from tkinter import messagebox

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

def disp():
    import sqlite_prac as sq
    username=t1.get()
    password=sq.authenticate(username)
    messagebox.showinfo("Your Password", "Your password is "+password)

def run():
    top.destroy()
    import Loginform
    Loginform.run1()

def run1():
    global top
    global t1
    global canvas
    global fps
    top=Tk()
    top.geometry("1000x1000")
    top.title("Password Reset")

    f= Frame(top,height=1000,width=1000,bg="#56BBF1",cursor="arrow")

    bg = PhotoImage(file="realestate.png")
    lx = Label(f,image=bg)
    lx.place(x=0, y=0)

    #p1 = PhotoImage(file="he.png")
   # lt=Label(f,text="Housing Price Prediction",bg="#ECECEC",anchor=CENTER,font=("Times","28","bold"))
    #lt.place(x=260,y=0,width=500,height=40)
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


    l1 = Label(f,text="Username",bg="#ECECEC",font=("times","24","italic"))
    l1.place(x=240,y=150)

    t1 = Entry(f,font=("times","24","bold"))
    t1.place(x=400,y=150)

    l2 = Label(f,text="Security Question",bg="#ECECEC",font=("times","24","italic"))
    l2.place(x=240,y=215)

    t2 = Entry(f,text="Your Answer",font=("times","24","bold"))
    t2.place(x=500,y=215)

    clicked = StringVar()
    clicked.set("Questions")

    drop = OptionMenu(f,clicked,"Your Nickname")
    drop.place(x=500,y=260)

    b1 = Button(f,text="Submit",font=("times","24","bold"),cursor="hand1",bg="#6BCB77",command=disp,activeforeground="#398AB9",activebackground="#D1D1D1",foreground="white")
    b1.place(x=300,y=350,width=150,height=50)

    b2 = Button(f,text="Back",font=("times","24","bold"),cursor="hand1",command=run,bg="#6BCB77",activeforeground="#398AB9",activebackground="#D1D1D1",foreground="white")
    b2.place(x=500,y=350,width=150,height=50)

    f.pack()
    top.mainloop()

if __name__ == '__main__':
    run1()