#Математические фугкции также предоставляют расширенную работу с числами, match - синусы, косинусы, тангенсы, арктангесы и др, корни, степени
#а cmatch - это библиотека для рабоыт с комплексными числами
#также есть модуль numbers - с абстрактными классами, т.е теми классами, которые невозмно применять сами но можно наследоавть, удобно проверять с его помощью принадлежит ли число какому то числовому типу
import math
import numbers

x=45
print('Cosinus :',math.cos(x))
print('Sinus :',math.sin(x))
print('Tangens :',math.tan(x))
print('Arctangens :',math.atan(x))

#isinstance - проверяет является ли объект экземпляром какого-то класса, например проверим на целое и флоат, походу нимберс неявно импортируется при создании проги
print(isinstance(x,numbers.Number))

#Модуль datetime используется для реализации работы с датой и временем, хотя он простой, и не учитывает что в сутках не ровно 24 часа, а в году не ровно 365 дней и т.д
#для этого есть более подходящие модули mxDatetime timeutil
import calendar,datetime,time
#Перменная moon_datetime_a - хранит дату и время посадки корябля на луну
moon_datetime_a=datetime.datetime(1969,7,20,20,17,44)
#а это просто преобразует в кортеж с именами вида tm_year, tm_mon, tm_hour
list_time=moon_datetime_a.utctimetuple()
#а moon_time - целое число, скорее отрицательное хранит кол-во секунд от начала эпохи UNIX до даты посадки
moon_seconds=calendar.timegm(moon_datetime_a.utctimetuple())
print('Prosto objext date.time :',moon_datetime_a)
print('Secund ot 1969 7 20 :',moon_seconds)
print('Spisok vremeni ot secund:',list_time)

#Создает структурированный формат времени из  секунд от начала эпохи
moon_datetime_b=datetime.datetime.utcfromtimestamp(abs(moon_seconds))
print('UTC from seconds',moon_datetime_b)

print('ISO format from moon_datetime_a :',moon_datetime_a.isoformat())
print('ISO format from moon_datetime_b :',moon_datetime_b.isoformat())

#А вот так можно преобразовываоть в строку для встваки в БД
time_to_db1=time.strftime('%Y-%m-%dT%H:%M:%S',time.gmtime(abs(moon_seconds)))
print('Time to database 1 : ',time_to_db1)
#time_to_db2=datetime.datetime.strftime('%Y-%m-%dT%H:%M:%S',moon_datetime_a)
time_to_db2=moon_datetime_a.strftime('%Y-%m-%dT%H:%M:%S')
print('Time to database 2 : ',time_to_db2)

#Модуль bisect - содержит функции поиска в отсортированных последовательностях, а модуль hepq - содержит функции для преобразования последовательности в кучу, т.е такую последовательность где первый элемент наименьший
#а collections - такие как словари со значением по умолчанию - defaultdict, и namedtuple а также классі для создания поль-их словарей UserList и UserDict
#а также элемент dequeue - обеспечивает быстрое добавление и удаление на обоих концах последовательности, а списки только в конец
#а модуль arrray хранит класс arrray - из него можно создавать массиві он отличется от списка тем что в нем можно хранить не несколько разніх списков, а только определенные - например числа или строки определяется при создании
#weakref - создание сдабых ссылок на объект отличаются от обычных тем что если одна но она слабая, то объект готов к утилизации

#Куча - это двоичное дерево, где первый элемент мин иил максимальный, каждое поддерево в куче является тоже кучей
import heapq
heap=[]
heapq.heappush(heap,(5,0))
heapq.heappush(heap,(2,'work'))
heapq.heappush(heap,(4,'study'))
heapq.heappush(heap,(1,'sleep'))
print(heap)

ls=[22,3,4,7,8,10,2,4]
#hepfy - преобразовывает список в кучу
heap=heapq._heapify_max(ls)
print(heap)
#А merge возвращает итератор из нескольких списков позволяющиц пройтись по всем спискам
for x in heapq.merge([1,3,5,6,9],[12,0,1,-2,34,6]):
    print(x,end=' ')