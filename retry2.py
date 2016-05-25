chislo1=15
chislo2=12
chislo1=int(chislo1)
chislo2=int(chislo2)
sum=chislo1+chislo2

a=4
a+=a

print ('The sum of chislo1 and chislo2=',sum, end='\n',sep='*')
print ('The a after a+ =',a)

a=b=c=8
print ('The a,b,c now =',a,b,c)
a,b,c=1,2,3
print ('The a,b,c now =',a,b,c)

string='Python in easy steps'
floating=1.34
integer=18

print ('The types of some integers\n')
print ('The type of string is :',type(string))
print ('The type of integer is :',type(integer))
print ('The type of float is :',type(floating))

#lang=input('Your favourite programming language :')
#lang=str(lang)
#number=input('Vvedite lubie chislo :')
#print ('Your language is :', lang)
#print ('The number what you typed is :',number)

array=[0,1,2,3,4,5]
print ('The third element of array :', array[2])

quarter=['January','February','March','April']
print ('The first letter in second month is :', quarter[1][0])

basket=['Apple','Oranges','Bananas']
pocket=['Whiskey','Vodka','Salo']
element='Money'

basket.append(element)
print ('The basket after append Money in the end', basket)

index=basket.index('Oranges')
print ('The index of lement Orange in basket is :',index)

basket.pop(index)

print ('Remove element Oranges from basket',basket)

basket.extend(pocket)
print ('Basket after extend by other array is :', basket)

elem2='Bananas'
basket.append(elem2)

print ('The numbers of elements in basket is:', basket.count('Bananas'))

#Udalaet pervoe vhogdenie naidennogo elementa
basket.remove('Bananas')

print ('The basket after remove first Bananas :', basket)

#Vastvim element pered 3-m
elem3='Tomato'
basket.insert(2,elem3)

print ('Iserted tomato before 4 element in list :', basket)

basket.sort()

print ('The basket sorted by alfa :',basket)

touple=('Red','Green','Blue')
a,b,c=touple
print ('Rspinovka kortega :',a,b,c)

arr={'One','Two','Three'}

print ('Chistoe mnogestvo :',arr)
new='Five'
arr.add(new)
print ('Mnogestvo posle dobavleniya 1 elementa :',arr)
elem1=str('Six')
elem2=str('Seven')

arr.update(elem1,elem2)
print ('Mnogestvo posle dobavleniya 2 elementov :',arr)
new_arr=arr.copy()
print ('The copy of array :',new_arr)

arr1={'One','Two','Three'}
arr2=arr1.copy()
arr2.add('Four')

print ('The difference between arr2 and arr1',arr2.difference(arr1))


dict={'name':'Bob','surname':'Ivanov','sys':'Linux'}
print ('The surname in dictioanry :',dict['surname'])
print ('The sys :',dict['sys'])
print ('The keys in dictionary is', dict.keys())

####Udalenie i dobavlnie elementa v mnogestvo
del dict['name']
dict['user']='Ivan'
print('Now dictory is :',dict)

######Vivedem kluchi sluchainim obrazom
print ('Kluchi v sluchainim poradke :', dict.keys())65

####Poist po associativnomy spisky
print ('Poisk po name v associativnom spiske :', 'user' in dict)

a=10
b=5
print('Trenarnaya operaciya')
print ('A bolse B') if (a>b) else print('A menshe B')








