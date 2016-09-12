from tkinter import *
import tkinter.messagebox as box

#Изображения можно выводить на виджетах Label, Button, Text, Canvas
#констркутор Photoimage() создаст обїект из изображения со всеми методами, хороший метод subsample(x=2,y=2) для уменьшения изображения на укзанное кол-во раз по ширине и высоте
#после того как изображение созданно его можно добавлять в label b Button опцией image для указания объекта - изображения также конструктор Text имеет метод image_create('1.0,'image.jpeg')
#где 1.0 - строка и буква в строке куда вставлять а image - путь
#также и Canvas имеет create_image х,у - куда вставлять, и само изображение
window=Tk()
window.title('Tets radio')
window.geometry('600x600')

img=PhotoImage(file='img.png')
img=img.subsample(x=3,y=3)
can=Canvas(window,width=600,height=600,bg='cyan')
can.create_image((0,0),image=img)
can.place(x=0,y=0)
window.mainloop()