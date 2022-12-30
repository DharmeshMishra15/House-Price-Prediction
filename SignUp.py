import gettext
from glob import glob
from tkinter import *
from tkinter import messagebox


def shift():
   x1, y1, x2, y2 = canvas.bbox("marquee")
   if (x2 < 0 or y1 < 0):  # reset the coordinates
      x1 = canvas.winfo_width()
      y1 = canvas.winfo_height() // 2
      canvas.coords("marquee", x1, y1)
   else:
      canvas.move("marquee", -2, 0)
   canvas.after(1000 // fps, shift)


def dest():
   top1.destroy()
   import Loginform


def sel():
   selection = "You selected the option " + str(var.get())

def back():
   top1.destroy()
   import Loginform
   Loginform.run1()
   

# def calling():
#    Loginform.run1()

def submit():
   global topx
   import sqlite_prac
   username =ex.get()
   Name = e1.get()
   City = e2.get()
   Phone =e3.get()
   val = var.get()
   Answer=e7.get()
   Password=e8.get()
   if(val==1):
      sqlite_prac.send(username,Name,City,Phone,"Male",Answer,Password)
   elif(val==1):
      sqlite_prac.send(username, Name, City, Phone, "Female", Answer, Password)
   messagebox.askokcancel("Redirect", "SignUp Successful")







def run():   
   global top1
   global var
   global ex
   global e1
   global e2
   global e3
   global e4
   global e5
   global e7
   global e8
   global str
   global canvas
   global fps


   top1 = Tk()
      
   top1.title("SignUp Form")
   top1.geometry("1000x1000")
   # top.wm_iconbitmap('home.ico')
   var = IntVar()
   bg = PhotoImage(file="realestate.png")
   f1 = Frame(top1, height=1920, width=1280, cursor="arrow")

   canvas = Canvas(top1, bg='black')
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


   lx = Label(f1, image=bg)
   lx.place(x=0, y=0)


   lx = Label(f1, text="Username", bg="light grey", foreground="Black", font=("Times", "20", "bold italic"))
   lx.place(x=400, y=50)

   ex = Entry(f1, font=("Times", "12", "bold italic"),bg="light pink")
   ex.place(x=600, y=55, width=200, height=30)


   l1 = Label(f1, text="Name",bg="light grey", foreground="Black", font=("Times", "20", "bold italic"))
   l1.place(x=400, y=130)

   e1 = Entry(f1, font=("Times", "12", "bold italic"),bg="light pink")
   e1.place(x=600, y=135, width=200, height=30)

   l2 = Label(f1, text="City",bg="light grey", foreground="Black", font=("Times", "20", "bold italic"))
   l2.place(x=400, y=210)

   e2 = Entry(f1, font=("Times", "12", "bold italic"),bg="light pink")
   e2.place(x=600, y=215, width=200, height=30)

   l3 = Label(f1, text="Phone Number", bg="light grey", foreground="Black", font=("Times", "20", "bold italic"))
   l3.place(x=400, y=290)

   e3 = Entry(f1, font=("Times", "12", "bold italic"),bg="light pink")
   e3.place(x=600, y=295, width=200, height=30)

   l4 = Label(f1, text="Gender",bg="light grey", foreground="Black", font=("Times", "20", "bold italic"))
   l4.place(x=400, y=370)

   str1 = StringVar()

   e4 = Radiobutton(f1, font=("Times", "20", "bold italic"), variable=var, text="Male", value=1, command=sel)
   e4.place(x=540, y=375, width=200, height=30)

   e5 = Radiobutton(f1, font=("Times", "20", "bold italic"),variable=var, text="Female", value=2,command=sel)
   e5.place(x=720, y=375, width=200, height=30)

   l5 = Label(f1,text="Security Question",font=("Times", "20", "bold italic"),bg="light grey")
   l5.place(x=400, y=460)

   clicked = StringVar()
   clicked.set("Questions")

   drop=OptionMenu(f1,clicked,"Your Nickname")
   drop.place(x=650,y=465)

   l7 = Label(f1, text="Your Answer",bg="light grey", foreground="Black", font=("Times", "20", "bold italic"))
   l7.place(x=400, y=540)

   e7 = Entry(f1,bg="light pink", font=("Times", "20", "bold italic"))
   e7.place(x=600, y=545, width=200, height=30)

   l8 = Label(f1, text="Password", bg="light grey", foreground="Black", font=("Times", "20", "bold italic"))
   l8.place(x=400, y=620)

   e8 = Entry(f1,show="*", bg="light pink",font=("Times", "20", "bold italic"))
   e8.place(x=600, y=625, width=200, height=30)

   b1 = Button(f1,cursor="hand1", anchor="nw", text="Submit", bg="lavender", relief=SOLID,activeforeground="#398AB9", activebackground="#D1D1D1",foreground="black", font=("Times", "20", "bold italic"),command=submit)
   b1.place(x=400, y=700, width=130, height=40)

   b2 = Button(f1, anchor="nw",cursor="hand1", relief=SOLID,text="Back", bg="lavender", activeforeground="#398AB9",activebackground="#D1D1D1", foreground="black", font=("Times", "20", "bold italic"),command=back)
   b2.place(x=580, y=700, width=130, height=40)

   f1.pack()
   top1.mainloop()


# import Loginform




if __name__=='__main__':
   run()



