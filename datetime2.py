import math
from datetime import *

number=9.76
ceil=math.ceil(number)
print ('Celoe chislo',ceil)
print (type(ceil))

class Person:
	name='Ivan'
	age=23
	def set_age(self,n):
		self.age=n
		return self
	def set_name(self,n):
		self.name=n
obj=Person()
ages=obj.set_age(50)
name=ages.set_name('Skotina')
print ('The type of is :', type(ages))
print ('The name is :', ages.name)
#print ('The type is :',type(ages),'vozrast=',ages)


#for dir in sys
print ('________________________________________')
#С помощью функции dir можно вывести все атрибуты и методы класса
#print (dir(datetime))
print ('________________________________________')
#Вот так можно задать любую дату и время присваивая классу дату и время.типа как строке присваиваем время и можно к ним обращаться через точку dt.year, dt.hour и т.д
dt=datetime(2007,12,6,16,29,43,79043)
print('The datetme year is :',dt.year,dt.month,dt.hour,':',dt.minute)


#А есть в этом класе и набор методов которые присваивают оатрибутам объекта datetime сегодняшние месяц, год, и т.д
print ('-----------------------------------------')

today=datetime.today()

print('Segodnyahnyaya data i vremya :',today)

print('Test test test :',today.strftime("%d.%m.%Y %I:%M %p"))


todaytime=datetime.now()
print ('Segodnyashnee vremya :',todaytime)
arr=['hour','minute']



#print('Popitalsya dobavit k imeni peremennoy :',todaytime.arr[0]) так нельзя а вот с помощью getattr можно, что удобно в цикле
print ('Vzyal imya s pomoshy getattr :',getattr(today,'year'))
print ('The hor of is :',todaytime.hour)

arr=['year','month','day','hour','minute','second']
for attr in arr :
	print(attr,'is :',getattr(today,attr))
#По идее today должен біть обьектом и т.к єто оббект то в нем есть функция strftime которая форматирует время в строку

strdate=today.strftime("%Y%B%d% %A %H:%M:%S")
#print('Sformatirovannya data :', strdate)
print('Test test test :',today.strftime("%d.%m.%Y %I:%M %p"))