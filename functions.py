global_var=1
def myvars():
	print('The Global var is :',global_var)
	local_var=2
	print('The Local var is :',local_var)

myvars()
#print('The var in function', local_var)

def myfunc(name,surname,age,sys='Linux'):
	print('Your name is :',name)
	print('Your surname is :',surname)
	print('Your age is :',age)
	print('The system is :', sys)
	return name+surname
indname=str(input('Vvedite svoe imya :'))
indsurname=str(input('Vvedite svoy familiy :'))
indage=int(input('Vvedite svoy vozrast :'))

myfunc(indname,indsurname,indage)

print ('#####################Teper peredadim v ukazanim poradke###############################')

data=myfunc(surname=indsurname,age=24,name=indname)
print ('Funkciya vernula rezultat :',data)

num=int(input('Please input a number here :'))
def square(num):
	if num>5:
		return 'Znachenie bolshe 5'
	elif num<5:
		return 'Znachenie menshe 5'
	else:
		return 'Znachenie ravno 5'
result=square(num)
print ('The result is :', result)


print ('#####################Teper peredadim v ukazanim poradke###############################')

def function_1(x): return x**2
def function_2(x): return x**3
def function_3(x): return x**4

print ('########Ssilki na imena funkciy mogno pomeshat v massiv tak callbaks=[function_1,function_2]#######')
callbacks=[function_1,function_2,function_3]

print ('\nThe result of callbacks functions')

for func in callbacks.item():
	print ('Result', func(3))

