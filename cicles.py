i=1
while i<=3:
	print('Outer Loop iteration:',i)
	i+=1
	j=1
	while j<=3:
		print('Inner Loop iteration',j)
		j+=1
print ('###########Yslovniy oprator if##############')
var1=int(input('Vvedi peremennuy :'))
if var1>5 and var1<10 :
	print ('Var1 bolshe 5 no menshe 10')
elif var1>10 and var1<15 :
	print ('Var1 bolhe10 no menshe 15')
elif var1==5 :
	print ('Var1 ravno 5')
else :
	print ('Tut voobshe huy pimi chto')

print ('##############Obhod elementov v massive##############')
chars=['A','B','C']
fruit={'Apple','Banana','Chery'}
dict={'name':'Nick','ref':'Python','sys':'Win'}

print('Prosto vivvod vseh elementov spiska\n', end='')
for element in chars :
	print (element, end=' ')

print ('\nVivod vseh kluchey i ih znacheniy\n')
for kurwa in enumerate(chars):
	print (kurwa, end=' ')

print ('\nVivod vseh elementov spiska i kortega\n')
for ded in zip(chars,fruit) :
	print (ded, end=' ')

print ('\nVivod kluchey i svyazannih znacheniy\n')
for key, value in dict.items() :
	print (key,'=',value)

for i in range(1,4):
	for j in range(1,4):
		if i==1 and j==1:
			print('Continues inner loop i=1 j=1')
			continue
		print('Running i=',i,'j=',j)
		if i==2 and j==2:
			print('Cycle breaking now')
		break


