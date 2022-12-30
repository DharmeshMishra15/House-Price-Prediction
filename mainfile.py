from tkinter import *
from tkinter import messagebox


def pred():
    top.destroy()
    import mainfile2
    mainfile2.run1()


def run():
    top.destroy()
    import Loginform
    Loginform.run1()

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

def pref():
    bud=clicked1.get()
    if(bud=="40L-60L"):
        messagebox.showinfo("Top Localites", "Vasai\nVirar\nKharghar\nNaigaon\nNallasopara")
    elif(bud=="60L-80L"):
        messagebox.showinfo("Top Localites", "Mira Road\nDahisar\nDombivali\nKalyan\nPanvel")
    elif (bud == "80L-1CR"):
        messagebox.showinfo("Top Localites", "Mira Road\nBorivali\nBhayandar\nDahisar")
    elif (bud == "1CR-1.5CR"):
        messagebox.showinfo("Top Localites", "Borivali\nKandivali\nMalad\nGoregaon\nJogeshwari")
    elif (bud == "1.5CR-3CR"):
        messagebox.showinfo("Top Localites", "Andheri\nBandra\nKurla\nMatunga\nBandra Kurla Complex")
    elif (bud == "3CR-5CR"):
        messagebox.showinfo("Top Localites", "Dadar\nLower Parel\nMahalakshmi\nMahim\Grant Road")
    elif (bud == "5CR-10CR"):
        messagebox.showinfo("Top Localites", "Churchgate\nMarine Lines\nColaba\n\nMalabar Hills\nPali Hills")





def run2():
    global top
    global canvas
    global fps
    global clicked1
    top=Tk()
    top.geometry("800x800")
    top.title("Price Predictor")
    bg2 = PhotoImage(file="realestate.png")
    f = Frame(height=800,width=800,bg="#56BBF1",cursor="arrow")

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

    lx=Label(f,image=bg2)
    lx.place(x=0,y=0)

    l1 = Label(f,text="Enter your Budget:",font=("times","16","bold"),bg="light grey")
    l1.place(x=100,y=150)

    l2 = Label(f,text="Enter Your Desired Area:",font=("times","16","bold"),bg="light grey")
    l2.place(x=100,y=250)

    l3 = Label(f,text="Preferred Ammenities:",font=("times","16","bold"),bg="light grey")
    l3.place(x=100,y=450)

    l4 = Label(f,text="Property Type:",font=("times","16","bold"),bg="light grey")
    l4.place(x=100,y=350)

  #  t1 = Entry(f,font=("times","16"),bg="light pink")
   # t1.place(x=350,y=150)

    clicked1 = StringVar()
    clicked1.set("Budget")

    drop = OptionMenu(f, clicked1,"40L-60L", "60L-80L", "80L-1CR","1CR-1.5CR","1.5CR-3CR","3CR-5CR","5CR-10CR")
    drop.place(x=350, y=150)
    clicked = StringVar()
    clicked.set("1 BHK")

    drop = OptionMenu(f,clicked,"1 BHK","2 BHK","3 BHK","4 BHK")
    drop.place(x=350,y=350)


    t3 = Entry(f,font=("times","16"),bg="light pink")
    t3.place(x=350,y=250)

    c1=Checkbutton(f,text="Gym",font=("times","16","bold"),bg="light grey")
    c1.place(x=550,y=450)
    c2=Checkbutton(f,text="Swimming Pool",font=("times","16","bold"),bg="light grey")
    c2.place(x=350,y=500)
    c3=Checkbutton(f,text="Garden",font=("times","16","bold"),bg="light grey")
    c3.place(x=350,y=450)
    c4=Checkbutton(f,text="Parking",font=("times","16","bold"),bg="light grey")
    c4.place(x=550,y=500)

    b1 = Button(f,relief=SOLID,text="Submit",cursor="hand1",command=pref,font=("times","20","bold"),bg="#6BCB77")
    b1.place(x=200,y=575,width=100,height=30)

    b2 = Button(f,text="Back",relief=SOLID,cursor="hand1",command=run,font=("times","20","bold"),bg="#6BCB77")
    b2.place(x=350,y=575,width=100,height=30)


    b3= Button(f,text="Click for Predictor",relief=SOLID,cursor="hand1",command=pred,font=("times","20","bold"),bg="#6BCB77")
    b3.place(x=500,y=575,width=230,height=30)

    f.pack()
    top.mainloop()

if __name__ == '__main__':
    run2()
