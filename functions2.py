print ('########Ssilki na imena funkciy mogno pomeshat v massiv tak callbaks=[function_1,function_2]#######')
def function_1(x): return x**2
def function_2(x): return x**3
def function_3(x): return x**4

callbacks=[function_1,function_2,function_3]

print ('\nThe result of callbacks functions')

for func in callbacks:
	print ('Result', func(3))

print ('######Lambda functions here#######')

lambdafunc=[lambda x:x**2,lambda x:x**3,lambda x:x**4]
for func in lambdafunc:
	print ('\n Result of lambda func', func(4))

bool1=True
if bool1 :
	print ('Python is easy')
else:
	pass
print ('######Generator function#######')
def increment():
	i=1
	while True:
		yield i
		i+=1
inc=increment()
print (next(inc))
print (next(inc))
print (next(inc))



def fibonacci_generator():
	a=b=1
	r=1
	while True:
		yield r
		r=a+b
		a=b
		b=r
func=fibonacci_generator()

for i in func:
	if i>100:
		break
	else:
		print ('Generated',i)



title='Text Text Text'
try :
	print(titlye)
except NameError as msg:
	print (msg)

day=32
try:
	if day>31:
		raise ValueError('Invalid day number')
		pass
		pass
except ValueError as msg:
	print('The program found An :',msg)
finally:
	print('There are good day isnt it')


print ('##############################')
a=5
b=10
print ('Peremenaya A',a)
print ('Peremenaya B',b)
print ('------------------------------')
a,b=b,a+b

print ('Peremenaya A',a)
print ('Peremenaya B',b)

print ('######################################')

def incrementor():
	i=1
	while True:
		yield i
		i+=1

inc=incrementor()
a=next(inc)
print ('Znachenie ravno',a)

a=next(inc)
print ('Znachenie ravno',a)

a=next(inc)
print ('Znachenie ravno',a)

print ('##############Here the TRY-EXEC FUNCTIONS###############')

title='Python in easy steps'
#try:
#	print('Here must be error',tritle)

#except NameError as msg:
#	msg1='Putin were here '
#	msg1=msg1+msg
#	print (msg1)


#Zdes sravnivaem uslovie esli den bolshe 31 to s pomoshy raise opredelim svoe soobshenie ob oshibke
day=32
try:
	if day>31:
		raise ValueError('Invalid day number')

except ValueError as msg:
	print ('The Program Error is :',msg)
finally:
	print('Beatiful day today isnt it')



###Funkciya nige prosto vivodit element poziciy kotorogo mi peredali v funkciy tipe print chars[elem]
#print ('###Funkciya nige prosto vivodit element poziciy kotorogo mi peredali v funkciy tipe print chars[elem]################')

chars=['Alpha','Beta','Gama','Epsilon']
print ('Elem 4 :',chars[3])
def display (elem):
    assert type(elem) is int, print ('Argument must be integer')
    print('List elem',elem,'=',chars[elem])

num=2
num=int(num)
display(num)

num=1.24

display(num)

