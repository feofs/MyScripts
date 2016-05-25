print('Hello world')
a=10
b=7
c=a+b
print ('The a=',a,'b=',b,'and type of sum is',type(c))
a=b=c=8
print(a,b,c)
a,b,c=1,2,3
print(a,b,c)
#user=str(input('Input ypur name please :'))
#print ('Your name is :',user)
#lang=str(input('Your favourite programming lsnguage:'))
#print(lang, 'Is','Fun',sep='*',end='\n')

#Это синтаксическая ошибка т.к нет запятой  вконце
#print('The Python is easy)

#А это ошибка выполнения т.к нет переменной title1
#title='Python'
#print(title1)

#А это логическая ошибка т.к умножение будет выполняться в первую очередь
num=3
print(num*8+4)
print(num*(8+4))

#Целочисленное деление тут должно быть 5
print(22//4)
#Взятие по модулю, остаток от деления а тут 3
print(11%4)

#Возведение в степень
print(4**3)

#Логические выражения
nil=0
num=0
max=1
low='a'
cap='A'

print('Equality nil==num : ',nil==num)
print('Equality max==nil : ',max==nil)
print('Equality cap==low : ',cap==low)

print('Greater max>nil :', max>=nil)
print('Leather max<nil :', max<=nil)

print('More or equal num>=nil :', num>=nil)
print('Less or equal num<=nil :', num<=nil)


#Логические операторы
#AND возвращает TRUE если оба оператора TRUE или оба FALSE
#OR возращает если хотя бы один TRUE
#NOT унарные опертор применяется с одним операндом например NOT a где a было FALSУ вернет TRUE
a=True
b=False
print('AND logic')
print ('TRUE AND TRUE :', a and a)
print ('TRUE AND FALSE :', a and b)
print ('FALSE AND FALSE :', b and b)

print('OR logic')
print ('TRUE AND TRUE :', a or a)
print ('TRUE AND FALSE :', a or b)
print ('FALSE AND FALSE :', b or b)

print('NOT logic')
print('NOT TRUE :', not a)
print('NOT FALSE :', not b)


#Тренарная операция
print('-------------------------------Trenarnaya operaciya--------------------------------')
a=1
b=2
print ('The variable is :','One' if(a==1) else 'Not One' )
result='TAK' if(b==1) else 'B ne ravno 1'

print (result)

print('-------------------------------Massivy--------------------------------')
array=range(1,10)
month=['March','April','May']

print('The third element of range is :',array[2])
print('The third month is :',month[2])

print('The first letter of May is:',month[2][0])
cords=([0,1,2,3],[3,4,6])
print('The top left element is :',cords[0][0])
print('The third element of second massive is:',cords[1][2])

basket=['Eggs','Mushrums','Bread','Vodka']
pocket=['Money','Cigaretes']

elem='Arbuz'

basket.append(elem)
print ('Basket after append :',basket)

basket.extend(pocket)
print ('Basket after extend :',basket)

