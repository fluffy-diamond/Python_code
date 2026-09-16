from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window=Tk()
window.title("Calculator for money")
window.geometry("400x380")

abc=Label(window, text="Hellooooo!!!",fg="white",bg="black")
abc.pack()
pic=Image.open("app_img.jpg")
pic=pic.resize((200,150))
pic=ImageTk.PhotoImage(pic)
p=Label(window, image=pic)
p.pack()


def topwin():
    top=Toplevel()
    top.title("The calculator")
    top.geometry("400x380")

    a= Label(top,text="Write the money you have:")
    a.grid(row=0,column=0,columnspan=2,padx=20,pady=10)
    b=Entry(top)
    b.grid(row=0,column=1,columnspan=2,padx=20,pady=10)


    c=Label(top,text="------------------------------------------------------")
    c.grid(row=1,column=0,columnspan=2,padx=20,pady=10)


    d=Label(top,text="No. of 500 notes:")
    d.grid(row=2,column=0,columnspan=2,padx=20,pady=10)
    e=Entry(top)
    e.grid(row=2,column=1,columnspan=2,padx=20,pady=10)

    f=Label(top,text="No. of 100 notes:")
    f.grid(row=3,column=0,columnspan=2,padx=20,pady=10)
    g=Entry(top)
    g.grid(row=3,column=1,columnspan=2,padx=20,pady=10)

    h=Label(top,text="No. of 50 notes:")
    h.grid(row=4,column=0,columnspan=2,padx=20,pady=10)
    i=Entry(top)
    i.grid(row=4,column=1,columnspan=2,padx=20,pady=10)

    def clc():
        try:
            global amount
            amount=int(b.get())
            a1=amount//500
            amount %= 500
            a2=amount//100
            amount %= 100
            a3=amount//50
            amount %= 50

            e.delete(0,END)
            g.delete(0,END)
            i.delete(0,END)

            e.insert(END,str(a1))
            g.insert(END,str(a2))
            i.insert(END,str(a3))
        except ValueError:
            messagebox.showerror('Enter a normal value please')
            
    j=Button(top,text="Click me to calculate!!!",command=clc)
    j.grid(row=5,column=0,columnspan=2,padx=20,pady=10)

    top.mainloop()

bu=Button(window,text="Click me!",command=topwin)
bu.pack()
window.mainloop()