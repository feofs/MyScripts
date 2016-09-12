#Нужно ввести квадратное уровнение ax2+bx+c=0  пользователю нужно ввести а,б и с а х найдем по уравнению, т.к све оно должно быть равно 0
import cmath
import math
import sys
import re

#напишем функцию которая будет получать и проверять данные от пользователя
def get_float(msg,allow_zero):
    x=None
    #типа бесконенчный цикл сначала присваиваем ничего х, потом пока он равен этому просим польз-ля ввести  сначал присваиваем затем проверяем чтобы
    #не вывалилась ошибка и число не біло нулем
    #жто можно сделать также с помощью регулярки
    while x is None:
        try:
            x=float(input(msg))
            #Машинный эпсилон это число например 0.000000000000000000000000000000000000000000000000121  и т.д т.е с каким-то количеством знаков после зпаятой, после которого уже воспринимется как ноль

            if not allow_zero and abs(x)<sys.float_info.epsilon:
                print('zerro not allowed')
                x=None
        except ValueError:
            print('Input must be float')
            continue
    return x


def get_float2(msg,allow_zero):
    x=None
    #типа бесконенчный цикл сначала присваиваем ничего х, потом пока он равен этому просим польз-ля ввести  сначал присваиваем затем проверяем чтобы
    #не вывалилась ошибка и число не біло нулем
    #жто можно сделать также с помощью регулярки
    expr=re.compile(r'^[0-9]+.[0-9]+')
    while x is None:


        try:
            x=input(msg)
            if expr.search(x):
                x=float(x)
            else:
                print('Try input valid float')

            #Машинный эпсилон это число например 0.000000000000000000000000000000000000000000000000121  и т.д т.е с каким-то количеством знаков после зпаятой, после которого уже воспринимется как ноль

            if not allow_zero and abs(x)<sys.float_info.epsilon:
                print('zerro not allowed')
                x=None
        except ValueError:
            print('Input must be float')
            continue
    return x


print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a=get_float('enter a :',False)
b=get_float('enter b :',True)
c=get_float('enter b :',True)


#Теперь по формуле найдем наши х сначала они безтиповые сначала найдем то что под корнем затем в зависиомти от того больше оно
x1=None
x2=None
discriminant=(b**2)-(4*a*c)
if discriminant==0:
    x1=-(b/(2*a))
elif discriminant>0:
    root = math.sqrt(discriminant)
else: # discriminant < 0
    root = cmath.sqrt(discriminant)
    x1 = (b+root)/(2*a)
    x2 = (b+root)/(2*a)

#теперь выведм то что мы получили и то что вводил пользователь
equation=("{0}x + {1}x + {2} = 0 \N{RIGHTWARDS ARROW} x={3}").format(a,b,c,x1)
#если также ечть и х2 то дополним строку это просто также к добавляемому куску строки приставим формат
if x2 is not None:
    equation+=' x = {0}'.format(x2)
print(equation)


