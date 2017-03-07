#Дефаултдикт отличается от обычного словаря тем что каждый раз при добавлении будет вызвана ключевая функция
import collections
def append(x):
    return x+10

dict=collections.defaultdict(append)
dict['one']=10
dict['two']=20
print('The dixt two must be 30 ',dict['two'])

#Сверху не работает, но если мы зададим например list то тогда можно помещать в один элемент целый список, например создадим с одним элементом one, а потом к нему будем аппендить все что попадется
dc=collections.defaultdict(list)
for i in range(5):
    dc['one'].append(i)
print(dc)

arr=[1,2,3]
arr[0]=12