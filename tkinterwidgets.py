from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window=Tk()
window.title("Tkinter Widgets")
window.geometry("400x380")

a=Label(window, text="Hellooooo!!!",fg="white",bg="black")
a.pack()
pic=Image.open("picture1.jpg")
pic=pic.resize((200,150))
pic=ImageTk.PhotoImage(pic)
p=Label(window, image=pic)
p.pack()

def show_message():
    messagebox.showinfo("WOW!!!")
b=Button(window,text="CLICK ME!!!",fg="black",bg="cyan",command=show_message)
b.pack()

def show_detail():
    top=Toplevel()
    top.title("Details")
    top.geometry("200x190")
    c=Label(top,text="Subject:A white owl")
    c.pack()
    d=Label(top,text="Background: A garden full of flowers")
    d.pack()
    top.mainloop()
b1=Button(window,text="Show details of the pic",fg="cyan",bg="black",command=show_detail)
b1.pack()

window.mainloop()