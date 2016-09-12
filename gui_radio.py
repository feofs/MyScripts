from tkinter import *
import tkinter.messagebox as box

window=Tk()
window.title('Tets radio')
window.geometry('600x600')

frame_left=Frame(window,width=200, height=600,background="bisque")
frame_right=Frame(window,width=400,height=600,background="grey")
label_radio=Label(frame_left,text="Input your favourite language")
label_result=Label(frame_right,text="Get result here")

#устанавливаем переменную в котрую типа будем сваливать значения, котрое выбранно
book=StringVar()

#Каждый кружок - это объект радиобаттнона
radio1=Radiobutton(frame_left,text="HTML5",variable=book,value='HTML5 in easy steps')
radio2=Radiobutton(frame_left,text="CSS",variable=book,value='CSS in easy steps')
radio3=Radiobutton(frame_left,text="Java",variable=book,value='Java in easy steps')
radio2.select()

#Виджет Checkbutton - обеспечивает добавление в графическое приложение флажков, который может быть выбр
var1=IntVar()
var2=IntVar()
var3=IntVar()

checkbox1=Checkbutton(frame_left,text='HTML5 in easy steps1',variable=var1,onvalue=1,offvalue=0)
checkbox2=Checkbutton(frame_left,text='CSS in easy steps',variable=var2,onvalue=1,offvalue=0)
checkbox3=Checkbutton(frame_left,text='Java in easy steps',variable=var3,onvalue=1,offvalue=0)

#Здесь важно понимать Checkbutton предусматривает присваоение значение сразу нескольким разным переменным которые мы объявили ранее, а радиобатон только одной переменной
#поэтому функция должна обрабатывать и просмотривать значения наших нескольких переменных






#Т.к при выборе у нас просто устанавливается переменная book то в функции просто выведем ее как метку
def show_radio():
#Очищаем фрем от предудщего нагромождения элементов
    for child in frame_right.winfo_children():
        child.destroy()

    label_cheked=Label(frame_right,text=book.get())
    label_cheked.place(x=200,y=200)
    print(book.get())


def show_checkbox():
    for child in frame_right.winfo_children():
        child.destroy()
    str1='You choise :\n'
    #Проверяем просто какие переменные нажаты т.е равны 1
    if var1.get()==1 : str1+='HTML5 in easy steps\n'
    if var2.get() == 1: str1 += 'CSS in easy steps\n'
    if var3.get() == 1: str1 += 'Java in easy steps\n'
    label_checkbutton=Label(frame_right,text=str1)
    label_checkbutton.place(x=200,y=250)


def func1():
    funcShow('Кнопка1')

def func2():
    funcShow('Кнопка2')

def funcShow(name='Ivan'):
    print(name)
funcShow()

btn_radio=Button(frame_left,text='Test',command=func1,bd=5,width=10)

btn_checkbox=Button(frame_left,text='Checkbox',command=func2,bd=5,width=10)




frame_left.pack(side=LEFT,padx=0)
frame_right.pack(side=RIGHT)
label_radio.place(x=20,y=5)
label_result.place(x=160,y=5)

#radio1.place(x=30,y=50)
#radio2.place(x=30,y=70)
#radio3.place(x=30,y=90)

#checkbox1.place(x=30,y=310)
#checkbox2.place(x=30,y=330)
#checkbox3.place(x=30,y=350)

btn_radio.place(x=60,y=250)
btn_checkbox.place(x=60,y=450)

window.mainloop()


