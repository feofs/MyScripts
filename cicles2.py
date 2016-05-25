i=1
while i<=3:
	print('Outer Loop iteration:',i)
	i+=1
	j=1
	while j<=3:
		print('Inner Loop iteration',j)
		j+=1

chars=['A','B','C']
i=1
for element in chars :
	print ('The item ',i,' in array ', element)
	i+=1
tulip=('Apple','Orange','Seems','Vodka')
print ('The second element in array :', tulip[1])
print ('The counts elements in array :', len(tulip))

i=0
while i<len(tulip) :
	if i==0 :
		elem='First'
	elif i==1 :
		elem='Second'
	elif i==2 :
		elem='Third'
	else :
		elem='Fourth'
	print ('The element number', elem,' is : ', tulip[i])
	i+=1

#Funkciya range generiruet posledovatalnost

print(range(1,10))
#print ('Generated range of numbers is :', numbers)
fruits={'Apple','Banana','Cherry','Vodochka'}
dict={'name':'Ivan','surname':'Sukov','sys':'Linux'}

print ('The keys in array\n')

for key in enumerate(dict) :
	print ('The key is :', key)

#zip ispolzuetsya dlya vivoda elementov v cicle iz 2 i bolee massivov kolichestvo elementov dolgno bit ravnoe inache vivedet menshee

for elem in zip(dict,fruits):
	print ('The element of zipped 2 arrays is :', elem)

#array.items() vivedet srazy kluchi i znacheniya
for key,value in dict.items():
	print ('The key : ',key,'----',value)

#break eto vihod iz cicla obichno delaetsya po usloviy v zavivsmosti ot togo kuda vstavim budet
#prerivatsya libo vnutreniy ili vneshniy cicl
for i in range(1,4):
	for j in range(1,4):
		print ('Running i=',i,' j=',j)
		if i==2 and j==1:
			print ('Breaks inner loop at i=2 j=1')
			break

#esli hotim propustit iteraciy to vstavlyaem continue
print ('################################################################')
for i in range(1,4):
	for j in range(1,4):
		print ('Running i=',i,' j=',j)
		if i==1 and j==1:
			print ('Continue inner loop at i=1 j=3')
			continue
		if i==2 and j==1:
			print ('Breaks inner loop at i=2 j=1')
			break



