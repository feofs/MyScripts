#Regularnie virageniya takie ge po tipy PHP
import re,dogs

#print ('--------------DOC----------------')
#docs=re.__doc__
#print (docs)
#print ('--------------DOC----------------')
pattern=re.compile('^1{2}7$')


print ('The type of pattern is:',type(pattern))

def get_number():
	#number=input('Enter number 117  :')
	number=str(117)
	is_valid=pattern.match(number)
	if is_valid :
		print ('The number is valid')
	else :
		print ('The number is invalid')
get_number()

#Operacii so strokami
str1='Hello'
str2='world'
result=str1+str2
print ('Sliyanie strok :', result)
name='Ivan'*3
print ('Name 3 raza :',name)

print ('Between 0 and 7 symbols',result[0:7])
print ('Four simbols from end and 2 from begin',result[2:-4])

basket=['Apple','Orange','Fruits','Basnas']
pocket=['Money','Hrivnas']
elem='Sys'

basket.append(elem)
print ('Basket after append :',basket)
basket.extend(pocket)
print ('Basket after insert other array:',basket)
print ('The type of basket is :',type(basket))
basket.pop(1)
print ('Basket after delete first element :',basket)

arr=result[2:-4]
for elem in arr:
	print (elem)

print ('Stroka s simvolom r\n')

print('H' in 'Hello')

if 'H' in 'Hello':
	print ('H est v Hello')

def display(s):
	'''Display inputed message'''
	print (s)

