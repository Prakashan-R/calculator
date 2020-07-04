from tkinter import *
window=Tk()
window.title('Calculator')
window.geometry('350x350')
e=Entry(window, width=42, borderwidth=5)
e.place(x=0, y=0)



b=Button(window, text='7', width=5)
b.place(x=10, y=50)

b=Button(window, text='8', width=5)
b.place(x=80, y=50)

b=Button(window, text='9', width=5)
b.place(x=150, y=50)

b=Button(window, text='/', width=5)
b.place(x=220, y=50)

b=Button(window, text='4', width=5)
b.place(x=10, y=100)

b=Button(window, text='5', width=5)
b.place(x=80, y=100)

b=Button(window, text='6', width=5)
b.place(x=150, y=100)

b=Button(window, text='*', width=5)
b.place(x=220, y=100)

b=Button(window, text='1', width=5)
b.place(x=10, y=150)

b=Button(window, text='2', width=5)
b.place(x=80, y=150)

b=Button(window, text='3', width=5)
b.place(x=150, y=150)

b=Button(window, text='-', width=5)
b.place(x=220, y=150)

b=Button(window, text='.', width=5)
b.place(x=10, y=200)

b=Button(window, text='0', width=5)
b.place(x=80, y=200)

b=Button(window, text='=', width=5)
b.place(x=150, y=200)

b=Button(window, text='+', width=5)
b.place(x=220, y=200)

b=Button(window, text='Clear', width=5)
b.place(x=120, y=250)

window.mainloop()