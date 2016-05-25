global_var='Outer var'
def myfunc():
	print ('The global variable is :', global_var)
	global in_func
	in_func='This global var in func'


myfunc()
print (in_func)

def echo(user):
	print ('The username is :',user)

echo ('Mike')

#predopredelleniye vsegda v konce
def myfunc2(user,sys,browser,surname='Ivanov'):
	print (user,surname,sys,browser)

#tak nelzya kak v Asterisk delat propuskaya argument poseredine, predopredelennie argumenti luche vinosit v konec
#myfunc2('Ivan',,'Linux')

#a vot tak mogno ne po poryadku no ukazivaya imya
myfunc2(browser='Opera',user='Ivanov',sys='Linux')

def mirror (user='Charlie',lang='Java') :
	print ('The user is :',user)
	print ('The lang is :',lang)

mirror()
mirror(user='Masha')
mirror(lang='Python')

def mysum(a,b):
	return a+b
res=mysum(4,5)

print('The sum result is',res)

#Mogno return ispolzovat dlya prerivanya funkcii po usloviy

def mysum(a,b):
	if a>5 :
		return
	return a+b
#a=int(input('Vvedite A chislo :'))
a=10
print ('The sum is :',mysum(a,4))

#num=input('Vvedite chislo :')

#def square(sq):
#	if not sq.isdigit():
#		return 'Value must be integer'
#	return sq*sq

#print ('The square is :', square(num))

#Lambda funkcii eto odnostrochnie funkcii iz kotorix daje mogno sostavit massiv
def function_1(x): return x**2
def function_2(x): return x**3
def function_3(x): return x**4

callbacks=[function_1,function_2,function_3]
for function in callbacks :
	print ('Znachenie funckcii', function(3))

square=lambda x: x**4
print (square(2))

callbacks=[lambda x:x**2,lambda x:x**3,lambda x:x**4]
for function in callbacks :
	print ('Znachenie funckcii', function(3))

title='Python is easy steps'

for char in title:
	print (char, end=' ')

#Continue perehodit k sled iteracii cilca
#a pass naoborot vipolnyaet sled instrukciy
for char in title:
	if char=='y' :
		print ('*',end=' ')
		continue
	print (char,end=' ')
print ('\n')
for char in title:
	if char=='y' :
		print ('*',end=' ')
		pass
	print (char,end=' ')

#Yiled сохраняет состояние и выходит из функии например бесконечный цмкл сначала выведет 1 2 3 и т.д
#next переходит к след после yield т.е после 1 цикл остановиться next его снова запустит прибавиться еще
#odin poluchim 2 i td
def increment():
	i=1
	while True :
		yield i
		i+=1
inc=increment()
print(next(inc))
print(next(inc))
print(next(inc))

title='Python in easy steps'

try:
	print (title1)
except NameError as msg:
	print ('Iskluchenie :', msg)

#raise - это пользовательское описание ошибки
day=31

try:
	if day>31:
		raise ValueError('Invalid day number')
except ValueError as msg:
	print ('Iskluchenie:', msg)
#finnaly - это вывод сообщения после успешной обработки исключения
finally:
	print ('All work')

#assert это что то типа проверочного выражение
#assert условие(TRUE или FALSE) описательное сообщение если FALSE
array=['Apple','Orange','Gus','Vodka']
#assert type(array) is int, 'Argument must be integer'

def display_elem(elem):
	assert type(elem) is int, 'Argiment must be integer'
	print ('The lement of array is :', array[elem])

elem=3
display_elem(elem)

print ('The len of array is :', len(array))

i=0
while i<len(array):
	display_elem(i)
	i+=1



