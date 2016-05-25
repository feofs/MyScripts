nil=0
num=0
max=1
cap='A'
low='a'
print('Equality:\t',nil,'==',num, nil==num)
print('Equality:\t',cap,'==',low, cap==low)

print('Ineqiality:\t',nil,'!=',max, nil!=max)

print('Greater:\t',max,'<',num, max>num)
print('Leather:\t',max,'<',num, max<num)

print('More or equal:\t',nil,'<=',num, max<=num)
print('Leather or equal:\t',cap,'>=',low, cap>=low)

a=10
b=5
print('Trenarnaya operaciya')
print('A bolshe B')if(a>b)else print('A menshe B')

print('A zdes esli ostatok t.e modul ot delenya na 2 = 0 to chislo chetnoe')
c=17
print('Chislo nechetnoe')if(c%2!=0)else('Chislo chetnoe')

a=1
b=2

print('Variable is:\t','One' if (a==1) else 'NotOne' )
print('Variable is:\t','Evan' if (a%2==0) else 'Odd' )
a=1
b=2

print ('Proverim na max peremenny')
maxs=a if (a>b) else b

print('Maximum is:\t',maxs)
