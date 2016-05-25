import math
print ('Sinus 60 degrees', math.sin(60))
print ('Rounded UP 9.5 :',math.ceil(9.5))
print ('Rounded Down 9.5 :',math.floor(9.5))

#print('Spizok iz 6 unikalnih chisle ot 1 do 49')
#nums=random.sample(range(1,49),6)
#print('Your luky numbers',nums)

from datetime import *
today=datetime.today()
print ('The type of today is:', type(today))
print ('The datetime is :',today)
print ('The hour of today is :',today.hour)

print(type(today))

print('------------------Clasees-------------------')
class Man:
	__name='Ivan'
	__age=19
	def set_name(self,n):
		self.__name=n
		return self
obj=Man()
name=obj.set_name('John')
print ('The type of name is :',type(name))
print ('The value of name is:',name)

class A:
	def __init__(self,n):
		self.n=n
	def __str__(self):
		return '[{}]'.format(self.n)

a=A(5)
print ('The a is :',a)

print('------------------Clasees-------------------')
#getattr получает определнный атрибут из класса
print (getattr(today,'hour'))
array=['year','month','day','hour','minute','second','microsecond']

for attr in array :
	print(attr,'ravno ',getattr(today,attr))

#но можно записывать и через точку так
print ('The time :',today.hour,':',today.minute)

day=today.strftime('%A')
month=today.strftime('%B')
full=today.strftime('%Y%M%d %H:%S')
print ('Full',full,'Day ', day,' month',month)

def uslovie ():
	n=int(input('Vvedi:'))
	if n==1 :
		n=1
		return n
n=uslovie()

if n==1:
	from time import *


print ('Now timer started')
start_timer=time()
struct=localtime(start_timer)

i=10
while i>-1:
	print(i)
	i-=1
	sleep(1)
end_timer=time()
dif=localtime(round(end_timer-start_timer))

print('Program executed time :', strftime('%S',dif))
