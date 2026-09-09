from tkinter import *
window=Tk()
window.title("A project")
window.geometry("400x380")

e=Label(window,text="Hellooooo!!!",fg="white",bg="midnightblue",width=50)
e.grid(row=0,column=0,columnspan=2,padx=20,pady=10)

a=Label(window,text="Name:",fg="black",bg="white")
a.grid(row=1,column=0,columnspan=2)

b=Entry(window,fg="blue",bg="pink")
b.grid(row=1,column=1,columnspan=2)

c=Label(window,text="Age:",fg="black",bg="white")
c.grid(row=2,column=0,columnspan=2)

d=Entry(window,fg="blue",bg="pink")
d.grid(row=2,column=1,columnspan=2)


frame=Frame(window,relief=GROOVE,borderwidth=5)
frame.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

l=Label(frame,text="Stuff:")
l.pack()

t=Text(frame,width=40,height=4,fg="blue",bg="pink")
t.pack()

bu=Button(window,text="show my card",bg="pink",relief=RAISED)
bu.grid(row=4,column=0,columnspan=2,padx=10,pady=5)

window.mainloop()