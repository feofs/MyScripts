import cats,dogs,sys,keyword,math,re,pickle,os
num_array=range(1,10)
print('The second element of array is :',num_array[1])
quarter=['January','February','March']
a,b,c=quarter
print('Rasnakovka massiva :',a,b,c)
print('The first month is',quarter[0])
print('The first letter of Masrh quarter[2][0] is:',quarter[2][0])
cords=([0,1,2,3],[3,4,6])
print('The top left element is :',cords[0][0])
print('The third element of second massive is:',cords[1][2])

basket=['Apple','Mango','Orange','Mushroms']
alcogol=['Wiskey','Vodka']

elem='Money'
#print('The keys of basket :\n')
#print(basket.keys())

print ('The type of basket is :',type(basket))
basket.append(elem)
print ('The basket after append is :',basket)
elem2='Henesy'
basket.insert(1,elem2)
print ('The basket after insert henesy before 2 element :',basket)
deleted_elem=basket.pop(1)

print('We delete Henesy from the array and here it :',deleted_elem)

print ('The index of Mushroms is :',basket.index('Mushroms'))
print ('The length of array is :',len(basket))

#Удалим 3-й єлемент массива
del basket[2]
print('Basket asfter 3 element deleted :',basket)
basket.append('Fruits')
#Удалим последний єлемент из массива и сразу вернем его
print('The last deleted element :',basket.pop())

#Кортеж - єто неизменияемій список пишется в () а множество в {}
#Раснакова кортежa
corteg=('Red','Green','Blue')
a,b,c=corteg
print('Rasnakovka cortega :',a,b,c)

#Mnogestvo
phonetic_set={'Alpha','Bravo','Charlie'}


copy_of_set=phonetic_set.copy()
print('Nachalnoe sostoyanie mnogestva :',phonetic_set)
print ('The copy of set is :',copy_of_set)

elem='Tundra'
phonetic_set.add(elem)
print('Set after add one element :',phonetic_set)

phonetic_set.discard(1)
print('Set after del 2 element :',phonetic_set)

phonetic_set.pop()
print('Set after random delete element :',phonetic_set)

phonetic_set2={'Velo','Moto','Bravo','Charlie'}

#intersection - вернет єлементі принадлежащие обоим множествам
elems=phonetic_set.intersection(phonetic_set2)
print ('Elements in both sets :',elems)

#difference- вернет єлементі из множества1, которіх нет в множестве2
elems=phonetic_set.difference(phonetic_set2)
print ('Elements in first sets :',elems)


print('-----------------Associativny massiv_---------------')
dict={'name':'Bob','ref':'Python','sys':'Win'}
print('The type is :',type(dict))
print('Dict',dict)
print('Reference :',dict['ref'])

#Ассоциативній массив называется словарь, у них  с
print('Vivedem vse kluchi :\n')
print(dict.keys())

del dict['name']
print ('The dictionary afte name deleted :',dict)

#А так можно добавлять ключ и значение
dict['user']='Tom'
print('The dictioanry after add user',dict)


print('The user in dict :','user' in dict)
num=7
if num>5 :
    print('The number more then five')
elif num<5 :
    print('The number less then five')
else:
    print ('The number is five')

def myfunc(var1):
    sum=5**var1
    print('The sum is :',sum)
    return sum
res=myfunc(2)
print ('The function result is :',res)

print('--------------Cycles--------------')
i=1
while i<4:
    print('Outer loop iteration',i)
    i+=1
    j=1
    while j<4:
        print('Inner loop iteration',j)
        j+=1
chars=['A','B','C']
fruit=('Apple','Banana','Cherry')
dict={'name':'Mike','ref':'Python','sys':'Win'}

#for item in chars : так выводятся просто значения элементов списка
for item in chars :
    print(item,end='')

print('\n Enumerated')
#for item in enumerate(chars): а так для вівода єелементов и их индексов
for item in enumerate(chars):
    print(item)

print('-----------------Zipped----------------')
#zip для обхода сразу нескольких списков
for item in zip(dict,fruit):
    print(item)

for key,value in dict.items():
    print (key,'=>',value)

square=lambda x:x**2
print(square(5))

funcs=(lambda x:x**2,lambda x:x**3,lambda x:x**4)
i=0

for func in funcs:
    print (func(5))

#В отличие от обічной функции у лямбда функций нет имен, их омжно візвать только присвоим какой нибудь
#переменной или загнав в массив, чтобы хоть через какое-то имя можно было к ней обратиться
def function1(num) : return num**2
def function2(num) : return num**3
def function3(num) : return num**4

callbacks=[function1,function2,function3]
#теперь их можно листать в массиве
print ('\nNamde functions')
for func in callbacks:
    print('Result :',func(2))

#А теперь создадим lambda c передачей двух переменных и сохраним их в массиве
test=lambda num,arg: num*arg
print('Test lambda',test(2,3))

print('Lambda funcs with two arguments saved in array')
lambdas=[lambda num,arg: num+arg,lambda num,arg: num*arg,lambda num,arg: num**arg]
print('len of lambdas :',len(lambdas))
i=0
while i<len(lambdas):
    func=lambdas[i]
    print ('Lambda ',i,' from array :',func(2,i))
    i+=1

#Результат работы continue
title='Python in easy steps'

#Цикл как видим в основном применяется с in, т.е типа ПХП-ного while list(key,value)
for char in title :
    if char=='y':
       print('*',end='')
       continue
    print(char,end='')

#Лучше сделать так на цифрах
print('-------------------------------------')
i=1
while i<10 :
    #if i==5:
        #continue
    print(i,'\n')
    i+=1
#Генераторы Python - в отличие от return, которая передает значение переменной возвращенной return
#т.е при следующем вызове будут выполняться снова одни и те же инструкции от начала до конца.
#Но есть функиция yield которая возвращает обїект а не просто какую строку или цифру
#т.е пременной присваивается какая-то точка внутри фнукции, затем с помощью функции next
#можно выполнять следующие шаги продемонстрируем это на примере от 1 до 10
print('-------------YIELD----------------')
def increment():
    i=1
    i=2
    i=3
    yield i
    i=4
    i=5
    i=6
    i=7
    yield i
    i=8
    i=9
    i=10
    yield i
#Теперь присваиваем эту функцию переменной
inc=increment()

print(next(inc))
#Затем с помощью функции next переводим выполнение на след инструкцию,
#т.е сначала выведется 3, заетм состояние запонится, при следующем вызове функции с помощью
#next выполниться блок кода в функции следующий за i=3 yiled i т.е
#i=4
#i=5
#i=6
#i=7
print(next(inc))
#затем состояние 7-ки запонится и после следующего вызова next выполниться блок кода
#в функции вплоть до 10-ки т.е следующего yield
print(next(inc))

#TRY EXCEPT - очень простое правило, те инстркуции, или блоку кода, который может ошибку помещаем
#в try, а инструкции и операторі по обработке візванніх ошибок в except
#в finally можно поместить инструкции после того как все ошибки будут обработанны
#Pythin имеет много строенных исключений таких как NameError - если не найденно имя, ValueError
#если значенте помещенное в переменную не соответсвует ожиданию
#IndexError - если не найден єлемент
title='Python in easy steps'
array={'name':'Ivan','sys':'Windows'}
chisla=range(1,3)
name=''
if name=='':
    print('Go to pervious page and type all fields')
#можно сделать exit но можно передать єто except    exit()
#также сразу там же он и обработает если число больше 32
day=32
try :
    print('===>',title)
    print(title1)

#Здесь проверим сразу переменную на пустоту
#raise - можно генерировать свои сообщения об ошибке
except NameError as msg:
    print('No such variables with that names')
    #а вот тут в принципе можно внести в лог или в базу оригинальную ошибку вместо ее вывода
    print('Оригинальная ошибка :',msg)


try :
    print(title2)
except NameError as msg1:
    print('No such variables with that names')
#а вот тут в принципе можно внести в лог или в базу оригинальную ошибку вместо ее вывода
    print('Оригинальная ошибка :',msg1)

try :
    print (array['surname'])
    print(chisla[5])
except KeyError as msg1:
    print('IndexError',msg1)

#try:
#    if name == '':
#        raise ValueError('The name is empty')

#except ValueError as msg:
#    print('Слудющие поля не верны', msg)
#try:
#    if day > 31:
#        raise ValueError('The day greater then 31')
#except ValueError as msg:
#    print('Слудющие поля не верны', msg)



#finally:
 #   print('Go back and try')

#Assert - позволяет проверять выражение на true или false и если проверка не пройдена т.е выражение равно FALSE то выдает ошибку assertion error и выражение которое мы задали
#assert выражение, описательное сообщение
# Например поставим условие, чтобы элемент был целым числом и проверим, если возвращает FALSE т.е строка естествеено не целое то выводится наша ошибка и выполнение программы прекращается
str='Bla bla bla'
#Вот еще одно отличие от PHP там есть втроенные функции is_float($var), is_double($var) а тут так var is float
#Можно применить его в try и тогда выполнение программы продолжиться
try:
    assert type(str) is int, 'Argument must be integer'
except AssertionError as msg:
    print('The assertion error with Except')
print('Hello world')

#Можно также написать функцию по отображению элементов массива и в ней вставить перед отображением проерку чтобы параметр переданный в функцию в качестве индекса был целым числом, иначе прекращать выполнение программы

print('-----------------Assertions------------------------')
chars=['Alfa','Betta','Gamma']
def display(elem):
    assert type(elem) is int,'Argument not integer.Program aborted'
    number=elem
    print('List element ',number,'=',chars[number])

elem=1
#elem=int(elem)
display(elem)
#elem=elem/2
#display(elem)

#Tak mogno imprortirovat togda vizivaem funkciy tak modul.funkciya
#Так как таблица символов не добавляется к текущему модулю то добавляя путем import ничего страшного не будет
# если у функции будут одинаковые имена т.к обращаемся через точку

cats.speak()
cats.link()
cats.sleep('Vodka')
#Также можно обращаться не только к функциям модуля но и к переменным также через точку
print('-------->',cats.variable)
dogs.speak()
dogs.link()


#А вот так уже импортируется в таблицу символов текущей программы
#Если мы импортируем какие-то отдельные функции или все через конструкцию from module import
#то мы можем обращаться непосредственно к функции без точки, но если импортируем по порядку один модульЮ потом другой
#то соотвественно функции будут использоваться из последнего имортированого модуля
from cats import speak
from dogs import *
print('-----------------')
speak()
link('Basya')
sleep()

#Системные модели и системные запросы позволяет получить списо системных переменных и системных функций из модулей
#keyword - содержит список всеъ ключевых слов языка Python типа return, yield, continue, while и т.д
#sys - содержит список всех системных функций типа print, len, float,count

print('Python version :',sys.version)
print('Python path :',sys.executable)
print('The type of sys.version is:',type(sys.version))
print('The type of sys.path is:',type(sys.path))
#Как видим тип атрибута sys.path список, т.е массив, значик его обычным for elem in array можно пролистать
print('The library paths :\n')
array=sys.path
for elem in array:
    print(elem)

#Вверху для лучшего понимания а вообще листать можно так
print('------------Module dirs------------')
for dir in sys.path:
    print(dir)
print('------------Kwlist------------')
print('The type of keyword.kwlist is :',type(keyword.kwlist))
for word in keyword.kwlist:
    print(word)

integer=math.ceil(1.72)
print('Integer',integer)

#Модуль math содержит кучу математических функций
cos=math.cos(60)
sin=math.sin(60)
tan=math.tan(60)
floor=math.floor(9.5)
print('Cos 60 degrees:',cos)
print('Tan 60 degrees:',sin)
print('Sin 60 degrees:',tan)
print('Floor of 9.5 :',floor)

num=16

print('Vozvedem 16 v 3 stepen:',math.pow(num,3))
print('Poluchim coren iz 16',math.sqrt(num))

#Модуль random содержит функции для работы с рандомами всякими, например генератор 6-ти случаных чисел от 1 до 49
#nums=random.sample(range(1,49),6)
#print('Your lycky num is :',nums)

#Есть проблема в округлении после 3 шо знака например значение немного меньше 0,735 округлено до 0,73 а например больше 1,435 округленно до 1.44
#для решения импортируется модуль decimal и метод вdecimal
item=0.7
rate=1.05

from datetime import *
today=datetime.today()

print('The type of today is:',type(today))
print('Today is :',today)

data=today.strftime('%Y %B %A %H:%M:%S')
print('Today is:',data)

print('The day is:',getattr(today,'day'))

data=datetime(2017,12,28,14,45,32,232)
print('Get year,month from class by getattr :',getattr(data,'year'),getattr(data,'month'))

#Можно также непостредственно обращаться к атрибутам через точку
print('The year is',data.year)

#класс аналог datetime, где метод возвращает сам экземпляр класса, + еще миеет стровое представление
class A:
    __name='xxxx'
    #это типа класс в строковом представлении, когда мы вызовем функцию today, и этот объект имеет строковое представление то в print он выведет blablabla
    def __str__(self):
        return self.__name
    def today(self,n):
        self.__name=n
        return self

object=A()
test=object.today('sometext')
print('The type of text must be class<A> :',type(test))
print('The today of class A is blabla :',test)

#time удобно для всяких замеров начала и конца операции содержится в модуле time функция time, в модуле, но не в объекте смотри скрипт date_times

#Регулярные выражения
#Смысл тот же что и в ПХП - поиск и замена подстрок, а функции содержаться в модуле re и описанны ниже
#Для начала следует скомпилировать нашу регулярку для поиска в объект
string='Windows the power OS'
expr=re.compile('^Wind.{1,} ')
print('The type of expression is :',type(expr))

#for method in dir(expr) :
#    if callable(getattr(expr,method)):
 #       print(method)
    #print (method if callable(getattr(expr,method)) else 'No calable')

#метод match позволяет проверить найденно ли соотвесвие строки регулярному выражению, если не найденно выражение возращает None, если найденно то объект совпадений
#содержащий методы start и end, т.е начала и конца совпадений а также метод group который возвратит всю строку соотвествия
#тут уже бля создастся новый объект с методами start, end и group указанными выше
sovpadenie=expr.match(string)
if sovpadenie:
    print('Совпадение найденно :',sovpadenie.group())
else:
    print('Не найденно совпадений')

#Теперь напишем функцию проеврки введенного еmail
#1)Для начала составим регулярку и скомпилируем ее в объект
#2) Потом из этого объекта вызовем функцию match куда передадим email
#3) Функция macth вернет none если совпадений не найденно лиюо объект где будет метод group - который вывдете это совпадение
expr=re.compile('^[-0-9a-z_\.]+@[-0-9a-z_^\.]+\.[a-z]{2,6}$')
def get_address():
    #email=input('Please input your email :')
    email='ivc@mail.ru'
    is_valid=expr.match(email)
    if is_valid:
        print('Your email is valid :',is_valid.group())
    else:
        print('Not valid email address')
get_address()

#Трудности могут быть когда один объект создает другой с разными методами

#Работа со строками
#Простые операции
#+ строка1+строка2 - конатенация строк
#строка*2 - повторение строки указанное количество раз
#'Hello'[0] - выбор символа по указаному индексу выведет Н, или указанному диапазону индексов [0:4] - выведет символы от 1-го о 4-го
#'H' in 'Hello' - вернет истину если такая буква пристсвует или подстрка
#not in - вернет истинну если такая подстрока не присутсвует
#r\n - подваление экранирующей последовательности - выведет \n
#
#'''текст'''  строка документации для описания, модуля, функции, или класса

def display(s):
    '''This is function description'''
    print(s)
print(display.__doc__)

string1='Hello'
string2='kitty'
output=string1+string2
print(output)
print('Hello'*3)

string='World'
output=string[0:3]
print(output)

if 'H' in 'Hello':
    print('This true H in Hello')
else:
    print('No such symbol in Hello')
if 'W' not in 'Hello':
    print('This is true W not in Hello')
else:
    print('Nu ego nah')
print(r'c:\program files')

#A zdes prosto vivedet TRUe
print('H' in 'Hello')

#dir(cats) можно использовать для вывода всех функций в модуле либо объекте
#obj=dir(__builtins__)
#print('Type :',type(obj))

#Объект str, который встроен в модуль __builtins__ также в него встроена функция print()
#result='{} and Ella {}'.str.format('Burger','Fries')
#print('Type of string of format :',type(result))

#Фигурными скобками обозначаем что куда вставлять
snuck='{} and {}'.format('Burger','Frees')
print(snuck)
# можно еще в них указать порядок
snuck='{1} and {0}'.format('Burger','Frees')
print(snuck)

#Но можно еще использовать %s, кароч formated - это функция а не хер знает что, а знак % типа заменяет выражение formated
snuck='%s and %s' % ('Milk','Cookies')
print(snuck)
#snuck='{1} and {0}' % ('Milk','Cookies')
print(snuck)

str='python in easy steps'
print('----------------------------------------------------------')
print('The type of string is :',type(str))
#Кароч получается т.к Python уж слишком сильно завязан на классах то и строка єто класс и когда мы присваиваем какое-то сртроковое значение пременной то создается класс со всеми аттрибуами и методаи
#до которых можно достучаться через название переменной даже не переменные а все даже функции являются экземплярами классов
print ('String capitalized :',str.capitalize())
print ('String upper :',str.upper())
print ('String titled :',str.title())
print ('String centered :',str.center(60,'*'))

#Чтобы лучше понять Python здесь надо понимать что все является объектами, т.е создавая число оно уже является объектом, создаем строку например * - оно уже объект, тюе  кнему
#уже можно применять функции класса іекштп
print('-----------Types of strings and int----------')
print('The type of 7 is :',type(7))
print('The type of 12.12 is :',type(12.12))
print('The type of * is :',type('*'))
print('-----------------------------')
array=['Apple','Orange','Milk']
new_str="*".join(array)
print('String from array :',new_str)
print ('String join:',str.join('**'))
print ('String rjust :',str.rjust(50,'c'))
print ('Python replaced by PHP',str.replace('python','PHP'))

email='ivc@betonmash.com'
#Например пользоваетль ввел такое в форме а нам надо заменить на др. и пишем
newemail=email.replace('ivc','market')
print(newemail)

#print(dir(__builtins__))
#Модуль builtins содержит объект file который в свою очередь содержит функции для работы с файлами включая такие методы как open(),read(),write(),close()
#Для того чтобы объект типа файл появился его сначала надо открыть функцией open

print ('File is deleted :',os.path.defpath('update.txt'))
fp=open('update.txt','w+')

print('Curent position in file:',fp.tell())
string='This string i put in file'
length=len(string)
print('The language of string is :',length)
fp.write(string)
print('Now after write position in file:',fp.tell())
fp.seek(length+2)
print('Now after SEEK position in file:',fp.tell())
string2='V I Lenin'
fp.write(string2)
print('----------File text---------------')
print(fp.read())
fp.close()














