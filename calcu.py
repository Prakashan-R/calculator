from tkinter import *
window=Tk()
window.title('Calculator')
window.geometry('350x350')
e=Entry(window, width=42, borderwidth=5)
e.place(x=0, y=0)



b=Button(window, text='7', width=5)
b.place(x=10, y=50)


window.mainloop()