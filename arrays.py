print('Poluchi rezultat kurwa :',sum)
array=[0,1,2,3,4]
print('The first third of array is', array[2])
quarter=['January','February','March']
print('The first month is',quarter[0])
print('The first letter of Masrh is:',quarter[2][0])
cords=([0,1,2,3],[3,4,6])
print('The top left element is :',cords[0][0])
print('The third element of second massive is:',cords[1][2])

basket=['Apple','Bananas','Oranges']
pocket=['Bread','Wiskey','Oil']
element='Sugar'

print('Original array is :',basket)

basket.append(element)
print ('The array after adding element to end :', basket)

print ('The index of element oranges is :',basket.index('Oranges'))

basket.pop(1)
print('The array after removing element number 2 one element to end :', basket)

new='Babuin'
basket.insert(2,new)
print('Array after insert new element before third element :',basket)

element2='Sugar'
basket.append(element2)
print ('Array with to identical elements :',basket)

print('How much identical elemnts in array :',basket.count('Sugar'))

basket.extend(pocket)
print('Now the buscet with pocket',basket)

print ('The indexes of sugar is :',basket.index('Sugar'))

print ('The counts of sugar is :',basket.count('Sugar'))
print ('The length of all the array is :',len(basket))

basket.sort()
print ('The basket after sort :',basket)

tuples=('Red','Green','Blue','Red','Brown')
a,b,c,d,e=tuples

print ('The color of c is :',c)

zoo=('Kengoroo','Leopard','Mouse')
print('The set is :',zoo,'The length of set is :',len(zoo))
print ('The type of zoo :',type(zoo))

bag={'Red','Green','Blue'}
print ('The set is :',bag,'The length of set is :',len(bag))

bag.add('Yellow')
print ('The SET after added new element in the end :',bag)

#bag.update('Purble','Black')
#print ('The bag after add twoe elements :',bag)

print ('The Green in the bag set :', 'Green' in bag)
print ('The Orange in the bag set :', 'Orange' in bag)

box={'Green','Red','Suka','Blua'}
team=bag.intersection(box)
print ('Elements in both sets is :',team)

dict={'name':'Bob','ref':'Python','sys':'Win'}

print ('Dictionary :',dict)
print ('Reference is :',dict['ref'])
print ('The keys in dict :',dict.keys())
del dict['name']
dict['user']='Tom'
print('After modify thi dictionary is :',dict)

print('The are name in key :','name' in dict)

print ('The are user in keys :','user' in dict)

print ('Find the value of key like Python', 'python' in dict)

a=input('Vvedite chislo :')
a=int(a)
if a<5:
	print ('A menshe 5')
elif a>5:
	print ('A bolshe 5')
else:
	print ('Number is 5')

b=int(input('Vvedite chislo'))
if b>7 and b<9:
	print ('Chislo ravno 8')
if b==1 or b==3:
	print ('Chislo 1 ili 3')


i=1
while i<=3:
	print ('Outer chicle is:', i)
	i+=1
		j=1
		while j<=3:
		print ('Inner cicle is',j)
		j+=1

