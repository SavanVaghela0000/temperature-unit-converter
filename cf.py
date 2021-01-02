from tkinter import *
import tkinter.messagebox as ss
savan = Tk()
savan.title("temperature unit converter")
savan.geometry("500x700")
savan.configure(background="lightgrey")
i = u'\N{DEGREE SIGN}'
l1= Label(text=f"Enter The Value of {i}C :") 
l10= Label(text=f"Enter The Value of {i}F :") 
abc = IntVar()
e1=Entry(textvariable="abc", justify = "left" , font = "verdana 12" , relief = FLAT)
def cnvt() :
    c=e1.get()
    b=int(c)*1.8
    z = b+32
    z = str(z)
    i = u'\N{DEGREE SIGN}' 
    ss.showinfo("" ,f"{e1.get()} {i}C = {z} {i}F" )
    # l = Label(text=f"{e1.get()} C = {z} F").pack()
def cnvt1() :
    c=e1.get()
    b=int(c)-32
    f = b*5/9
    f = str(f)
    i = u'\N{DEGREE SIGN}' 
    ss.showinfo("" ,f"{e1.get()} {i}F = {f} {i}C" )
    # l = Label(text=f"{e1.get()} F = {f} C").pack()
b3 = Button(text="convert" , command= cnvt ,activebackground = "white" , font = "verdana" , bg = "grey" , fg = "white" , relief = "flat" )
b4 = Button(text="convert" , command= cnvt1 ,activebackground = "white" , font = "verdana" , bg = "grey" , fg = "white" , relief = "flat" )
def kav() :
    l1.place(x = 60 , y = 100)
    e1.place(x = 260 , y = 100 , height = 31 , width = 100)
    b3.place(x = 370 , y = 100 , height= 31.4)
def kav1() :
    l10.place(x = 60 , y = 100)
    e1.place(x = 260 , y = 100 , height = 31 , width = 100)
    b4.place(x = 370 , y = 100 , height= 31.4)
b1 = Button(text=f"{i}C to {i}F" ,command = kav  ,activebackground = "white" , font = "verdana" , bg = "grey" , fg = "white" , relief = "flat").place(x=220 , y=500)
b2 = Button(text=f"{i}F to {i}C" ,command = kav1  ,activebackground = "white" , font = "verdana" , bg = "grey" , fg = "white" , relief = "flat").place(x=220 , y=600)
savan.resizable(0,0)
savan.mainloop()