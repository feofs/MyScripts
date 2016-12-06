import sys
import os
import glob
#Улучшеные приемы программирования, например нам нужно сдеалть обход, в котором мы вызываем какие-то функции в зависмости от переменной
# if action == "a":
#add_dvd(db)
#elif action == "e":
#edit_dvd(db)
#elif action == "l":
#list_dvds(db)
#elif action == "r":
#remove_dvd(db)
#elif action == "i":
#import_(db)
#elif action == "x"
def edit_dvd(var):
    print('Edit : ',var)
def add_dvd(var):
    print('Add : ',var)
def del_dvd(var):
    print('Delete : ',var)

#Но ведь имя например значения а,e,l - можно хранить в словаре как ключи а вместо этого вызывать по этому ключу имя функции, это все можно значительно сократить?
functions=dict(a=add_dvd,e=edit_dvd,d=del_dvd)
#Тперь напишем условие, что если переменная входит в кортеж передать ее как ключ функции и мы то сразу получим синтаксическую констркуцию типа имени гду в скобках сразу можно передать параметр
var='e'
if var in ('a','e','d'):
    functions[var]('Ypu choise Edited')
#Или вот еще хороший пример, передать в функцию расширение и реадер, так как ключами словаря могут быть и кортежи, ссылки это те же объекты а имя переменной ссылка на область памяти, где храниться объект
#а словарю пофиг у него все может быть и ключами и означениями - любые объекты
def import_xml_dom(text):
    print('You choise import xml {0}'.format(text))
def import_text_manual(text):
    print('You choise import manual {0}'.format(text))


call={('.aix','dom'):import_xml_dom,
      ('.ait','manual'):import_text_manual
    }
extension='.ait'
reader='manual'
call[extension,reader]('Manual' if extension=='.ait' else 'DOM')

#А вот хер она все элементы выведет, затнется на первом цикле так как уже будет return, второй образей тот же просто генератор вставлен
def items_in_key_order1(d):
    for key in sorted(d):
        return [key,d[key]]
#Т.к у нас первый образец выше возвращет только одно значение то перезапишем его с yield, тогда будет норм

#А вот эта какого-то хера работает, наверное влияет порядок расположения операторов
def items_in_key_order2(d):
    return ((key,d[key])for key in sorted(d))

def items_in_key_order3(d):
    for key in sorted(d):
        yield (key,d[key])


#Теперь можно вызывать функцию в цикле и выводить поэлементно

dc={'name':'Ivan','surname':'Czikov','addres':'Slavyansk'}
#Чтобы получить сразу все значение нужно передать в функцию list или tuple
print(list(items_in_key_order1(dc)))

print(list(items_in_key_order2(dc)))

print('----------Itema_in_key_orders1------------')
for elem in items_in_key_order1(dc):
    print(elem)
    #print(key,'-->',value)
print('----------Itema_in_key_orders2------------')
for key,value in items_in_key_order2(dc):
    #print(elem)
    print(key,'-->',value)

print('----------Itema_in_key_orders3------------')
for key,value in items_in_key_order3(dc):
    #print(elem)
    print(key,'-->',value)

#Генраторы хороши тем что их можно использовать нужное кол-во раз, например внутри поставить бесконечный цикл, но в условии поставить break, например, когда x будет равноым 1
def quarters(next_quarter=0.0):
    while True:
        yield next_quarter
        next_quarter+=0.25

for x in quarters():
    print(x)
    if x>=1.0:
        break

#Выше функция всякие раз вела отчет от 0 и т.д возвращая поочередно, но что нужно, чтобы генератор начал вопроизводить последовательность с текущего значения
def quarters2(next_quarter=0.0):
    while True:
        received = (yield next_quarter)
        if received is None:
            next_quarter += 0.25
        else:
            next_quarter = received
print(sys.float_info.epsilon)

result=[]
#Здесь создаем переменную хранящую ссылку на функцию генератор
generator=quarters2()

while len(result)<5:
    #Потом в цикле делаем next(ссылка на переменную с ф-ей генератором), которая вернет сначала 0.0 потом 0.25 потом 0.50 и т.д
    x=next(generator)
    #а вот здесь проверяем, типа не раавно ли х 0.5, т.е 0.5-0.5 будет абсолютный 0, т.е меньше абсолютного машинного нуля
    #если это так то перескочим итерацию и генератору передается значение 1.0 т.е получим [0.0, 0.25, 1.0, 1.25, 1.5]
    if abs(x-0.5)<sys.float_info.epsilon:
        #send - значит что это выражение будет приянто функцией генератором в качестве значения выражение yield
        #а сама функция проверяет если ничего не полученно то просто дальше прибавляет 0.25, если полученно то устанавливает значение генератора в полученное выражение
        '''
        received = (yield next_quarter)
        if received is None:
            next_quarter += 0.25
        else:
            next_quarter = received
        '''
        x=generator.send(1.0)
    result.append(x)

print(result)


#также можно задать поведение одной и той же функции в зависимости от какого либо параметра, например от платформы
if sys.platform.startswith("win"):
    #передаем любым образом полученный список файлов в список names
    def get_files(names):
        #Листаем имена файлов в списке файлов
        for name in names:
            #Проверяем действительно ли это файл если да то в генераторе возвращаем его
            if os.path.isfile(name):
                yield name
            #Иначе если все таки ене файл пытаемся обработать функцией iglob
            else:
                #Эта функция возвращает список имен файлов если переданаа конструкция вида *.txt или единственный файл если например передан autoexec.bat
                for file in glob.iglob(name):
                    if not os.path.isfile(file):
                        continue
                    yield file
else:
    def get_files(names):
        return (file for file in names if os.path.isfile(file))




