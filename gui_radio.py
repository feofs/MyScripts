from tkinter import *
import tkinter.messagebox as box

window=Tk()
window.title('Tets radio')
window.geometry('600x600')

def info():
    box.showinfo('Test message','Test message')

btn=Button(window,text='Test',command=info)

btn.pack()
window.mainloop()