#Повторение про учус и контексты, говороят что елси просто выполнить exec т оне будут доступны модули, и наши переменные но эт оне так
import math
code='''
def area_of_sphere(r):
    return 4*match.pi*r**2
a=10

'''
exec_dict={}
#Так как мы собираемся поместить результаты работа кода в другой словарь то нам также нужно добавить и в этот словарь єлемент с ключом match
#и значение модуля match, чтобы он стал доступен функции
exec_dict['match']=math
exec(code,exec_dict)

#Обратитья к результам кода, т.е переменніе, модули и
print(exec_dict['a'])
func=exec_dict['area_of_sphere']
print(func(8))
#result=
#print(exec_dict)


#Теперь нужно чтобы был доступен реальный код и результаты программы

c=10
code='''
result=c+10
name='Ivan'
z=215
'''
#Так то мы можем получить результаты но вот, просто если создаем код, не обращаясь к внешним переменным переменная с не будет доступно внутри exec
exec(code)
print(name)
print(result)

d=20
code='''
res=d+20
s=215
'''
exec(code) #Такой прием обеспечит и доступ ко всему глобальному словарю и помещению в этот же словарь результатов

print('The d+20 ',res)

#print(globals())
#Но есть и другой способо, типа словарю присвоить весь глобальный конткест, его копию а потом к нему также как и выше обращаться
context=globals().copy()
code='''
def some_func(x):
    return x+10
'''

exec(code,context)
func=context['some_func']
print('The result of func in context ', func(37))
