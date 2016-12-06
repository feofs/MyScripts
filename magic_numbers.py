#Прога пытается динамически импортировать (загрузить) все модули, имя которых
#содержит слово magic. Такие модули как ожидается содержат единственную общедоступную функцию
#get_files_type()
import sys
import os
def main():
    #попробуем подгрузить все модули с magic
    modules=load_modules()
    #создадим массив, куда будем помещать наши найденные функции
    get_file_type_functions=[]

    for module in modules:
        #Листаем модули и пытаемся с помощью ф-ии get_function получить функцию
        #get_file_type, если такая есть то занеесм в ловарь
        get_file_type=get_function(module,'get_file-type')
        if get_file_type is not None:
            get_file_type_functions.append(get_file_type)

    for file in get_files(sys.arv[1:]):
        fh=None
        try:
            fh=open(file)
            magic=fh.read(1000)
            for get_file_type in get_file_type_functions:
                #Применяем поочередно функции из списка, какая-то да что-то вернет т.е
                #за одну итрацию к одному файлу будет примененно 2 функции
                filetype = get_file_type(magic,os.path.splitext(file)[1])
                if filetype is not None:
                    #Если функция что-то вернула то распечатаем, доплнив точками до 20 сиволов, вырвнивнавине вправао
                    print('{0:.<20}{1}'.format(filetype,file))
                    break
                else:
                    print('{0:.<20}{1}'.format('Unknown', file))
        except EnvironmentError as err:
            print(err)
        finally:
            if fh is not None:
                fh.close()

#Будет три реализации load_modules
def load_modules():
    modules=[]
    #__file__ - встровенная переменная, полный путь к файлу Python а уже оттуда  извлечем путь к папке
    #и потом листаем файлы в ней, если это текущий каталог то вернет пустую строку а соответсвенно os.path.dirname вызвоет исключение, то для этого нужно передать еще через ок точку
    for name in os.listdir(os.path.dirname(__file__) or '.'):
        print(name)
        #Листая файлы проверяем заканчивется ли имя на расширение  питиноа и есть ли в имени слова magic
        if name.endswith(".py") and "magic" in name.lower():
            filename=name
            #Разбивает до расширение и возвращает кортеж, в первом элементе - имя файла во втором расширение
            #а вот втором расширение
            name=os.path.splitext(name)
            #isidentifier - проверяет является ли имя допустимым идентификатором, т.е допустимым имененм переменной, и если это имя не входит в системные модули
            #если все хорошо, то следующий код попытается импортировать его
            if name.isidentifier() and name not in sys.modules:
                fh=None
                try:
                    fh=open(filename,'r',encoding='utf8')
                    #Читаем код содержащийся в файле, в переменную, которую потом выполним в exec, а словарь куда будут помещенны все функции и аргии, будет
                    code=fh.read()
                    #В общем строка хитрожопая, например в переменную int можно записать целое число так x=5 x=int(5) или же сначала получить типа какой-то переменной записать его в переменную а потом в эту переменную запхнуть нашу
                    #int_type=type(1) а затем x=int_type(5) Но можно в одной строке сразу снять тип и присвоить его переменной module=type(sys)(name) т.е переменной name мы присваиваем такой же тип что и у модуля и ее присваиваем modlue
                    module=type(sys)(name) #т.е module - ссылка на модуль
                    #теперь импортируем его путем присваивание в словарь системніх модулей, но он пока пустой, он заполниться функциями и пременными после exec
                    #он добавляется пустой, чтобы предотвратить непреднамеренное повторное его импортирование
                    sys.modules[name]=module
                    #Выполняем код модуля а его функции помещаем в словарь, т.е как бы в контекст по научному
                    exec(code, module.__dict__)
                    #В коннце модуль добавляется в словарь, который мы будем использовать для получения типов файлов
                    modules.append(module)
                except (EnvironmentError, SyntaxError) as err:
                    sys.modules.pop(name, None)
                    print(err)
                finally:
                    if fh is not None:
                        fh.close()
    return modules

def load_modules2():
    modules=[]
    #__file__ - встровенная переменная, полный путь к файлу Python а уже оттуда  извлечем путь к папке
    #и потом листаем файлы в ней, если это текущий каталог то вернет пустую строку а соответсвенно os.path.dirname вызвоет исключение, то для этого нужно передать еще через ок точку
    for name in os.listdir(os.path.dirname(__file__) or '.'):
        print(name)
        #Листая файлы проверяем заканчивется ли имя на расширение  питиноа и есть ли в имени слова magic
        if name.endswith(".py") and "magic" in name.lower():
            filename=name
            #Разбивает до расширение и возвращает кортеж, в первом элементе - имя файла во втором расширение
            #а вот втором расширение
            name=os.path.splitext(name)
            #isidentifier - проверяет является ли имя допустимым идентификатором, т.е допустимым имененм переменной, и если это имя не входит в системные модули
            #если все хорошо, то следующий код попытается импортировать его
            if name.isidentifier() and name not in sys.modules:
                #Здесь мы тупо просто пытаемся импортировать т.е выполнить консткурцию import magic...
                try:
                    exec("import " + name)
                    #и потом заносим его в список модулей
                    modules.append(sys.modules[name])
                except SyntaxError as err:
                    print(err)


    return modules

def load_modules3():
    modules=[]
    #__file__ - встровенная переменная, полный путь к файлу Python а уже оттуда  извлечем путь к папке
    #и потом листаем файлы в ней, если это текущий каталог то вернет пустую строку а соответсвенно os.path.dirname вызвоет исключение, то для этого нужно передать еще через ок точку
    for name in os.listdir(os.path.dirname(__file__) or '.'):
        print(name)
        #Листая файлы проверяем заканчивется ли имя на расширение  питиноа и есть ли в имени слова magic
        if name.endswith(".py") and "magic" in name.lower():
            filename=name
            #Разбивает до расширение и возвращает кортеж, в первом элементе - имя файла во втором расширение
            #а вот втором расширение
            name=os.path.splitext(name)
            #isidentifier - проверяет является ли имя допустимым идентификатором, т.е допустимым имененм переменной, и если это имя не входит в системные модули
            #если все хорошо, то следующий код попытается импортировать его
            if name.isidentifier() and name not in sys.modules:
                #Здесь мы тупо просто пытаемся аналогично конструкции import module_name, но тут в все в том что функция __import__(name) - возвращает объект типа модуль
                #в то время как import ничего не возвращает
                try:
                    module = __import__(name)
                    modules.append(module)
                except (ImportError,SyntaxError) as err:
                    print(err)




    return modules

def get_function(module, function_name):
    #Смотрим наш словарь кэшей созданный ниже, тут алгоритм таков, что если она уже там есть то не выполнять ее присваивание а просто вернуть
    #ключ жто кортеж из модуля и имени функции, а значение - сама функция, get - установить значение None для этих ключей если ее нет
    #т.е сначала словарь будет пуст, а потом если мы уже раз нашли, и видим что такое имя попалось снова то зачем нам опять искать в нем, слишком затратно на сотни файлов, будем брать из кэша
    function = get_function.cache.get((module, function_name), None)
    #Такая методика кеширования называется запоминанием, т.к программный код остается неизменным для любой
    if function is None:
        try:
            #Получем аттрибут из модуля, и проверяем есть ли в его уже аттрибутах, т.к полученный аттрибут функции тоже объект
            #и если в нем есть __call__ то это сто пудов функция, тогда можно занести ее в словарь
            function = getattr(module, function_name)
            if not hasattr(function, "__call__"):
                raise AttributeError()
            get_function.cache[module, function_name] = function
        except AttributeError:
            function = None
    return function

get_function.cache = {}
#Полезные функции
'''
__import__(name) - мипортирует модуль по имени и возвращает объект типа модуль
compile(source, file, mode) - компилирует и возвращает объект с программным кодом, может записать в файл mode - значит, какую функцию использовать
delattr(obj,name) - удаляет из обїекта аттрибут с именем name
dir(obj) - перечисляет все аттрибуты и методы объекта
eval(source,globals,locals) - возвращает резалт вычисления единственного выражениея source, если определнеы globals и locals -то они будут тспользованны ка кглобальный и локльный контексты соотвественно
getattr(obj, name, value) - возвращет значение свойства если есть, или val, если в объекте отсутсвует указанный аттрибут
hasattr(obj,name) - вернет TRUE - если аттрибут с таким именем есть в объекте
globals() и locals() - словари текущего глобального и локального контекство
vars(obj) - вернет контекст объекта obj или локальный контекст если obj не определен

'''

#В общем есть еще такой прикол как онтексты видимости или имполнения кода в exec, например по разному будет выполняться скомпилированный код если суммируем то будет все нормб а если удаляем то все равно не удалим
#кароч пример
my_code_object=compile('''
x=x+2
''','<string>','exec') #Значит скомпилировать указанный код в строку
def exec_code_and_return_x(code_object,x):
    x=x
    print(locals())
    exec (code_object,locals())
    return x


my_code_object2=compile('''
del x
''','<string>','exec')

z=exec_code_and_return_x(my_code_object,1)
print(z)

z=exec_code_and_return_x(my_code_object2,1)
print(z)

#Кароч оно нихрена сверху не выполняется
#Теперь создадим два словаря и выполним в обоих exec и посмотрим где сохраняться объекты
#Кстати регулируя __builtins__ словарь мы можем регулировать, какие аттрибуты и методы будут доступны в exec из глобального словаря
code_globals={}
code_locals={}
code_object=compile('''
x=1
''','<string>','exec')

exec (code_object) in code_globals,code_locals
print(code_locals)

print('---------Some tests with local and global---------------')
animal='angry'

def test_locals():
    a=10
    b=20
    c=30
    global animal
    animal='wombat'
    print(locals())
    print(globals())
    #А вот так мы изменяем глобальную переменную


    print('The global war is : ',animal)

test_locals()
print(' No in function global animal is : ',animal)

animal='fruitbar'
def change_and_print_global():
    global animal
    animal='wombat'
    print('inside function change_and_print_global :',animal)
print('Animal before doing function :',animal)
change_and_print_global()
print('Animal after doing function :',animal)


print ('------------Scopes tests------------')
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        #Nonlocal - отшлет переменную с ее значение в родительскую функцию
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    #Тут будет видно test_spam а не local spam - т.к do_local присвоит только в своей области видимости local
    print("After local assignment:", spam)
    #А вот nonlocal в функции do_nonlocal - присвоит уже родительской функции
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    #А вот global присвоит глобальной, но в print будет видно nonlocal т.к интерпретатор сначала ищет переменную в локальной области
    # потом выше по ступеньке в родительской функции, и так как там он еще нашел то в global не пойдет, а вот что ниже пойдет т.к global будет для нее родителем
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

#Как видим локальный словарь содержит только переменные в функции, а глобальный - глобальные
#main()