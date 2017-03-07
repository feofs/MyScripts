#Все рекурсивные функции поддерживают два случая, базовый и рекрсивный
#базовый используется для прекращения рекурсии
#Есть ограничение на максимальную вложенность рекурсии получить можно sys.getrecursionlimit и установить sys.setrecursionlimit
#Классический пример - факториал, остановить рекурсию, когда x станет меньше или равным 1, а так продолжать умножать на то что вернет функция
def factorial(x):
    if x<=1:
        return 1
    return x*factorial(x-1)

print(__name__)

def local_func():
    print(__name__)

local_func()

before = ["Nonmetals",
          "    Hydrogen",
          "    Carbon",
          "    Nitrogen",
          "    Oxygen",
          "Inner Transitionals",
          "    Lanthanides",
          "        Cerium",
          "        Europium",
          "    Actinides",
          "        Uranium",
          "        Curium",
          "        Plutonium",
          "Alkali Metals",
          "    Lithium",
          "    Sodium",
          "    Potassium"]

def indented_list_sort(indented_list, indent="    "):
    #Для начала создаем три константы, которые будут выступать в роли индексов
    KEY, ITEM, CHILDREN = range(3)

    def add_entry(level, key, item, children):
        #children - єто массив entries, чтобы до
        #На самом верхнем уровне, когда добавляется корневой элемент рекурсия не возникает, добавляется как элемент кортеж из 3-х элементов
        #ключа, элемента и пустого списка, если список пустой, значит список не содержит дочерних элементов, т.е он вложен в кого-то, это и есть базовый случай
        #Например дошли до InnerTransitionals, тут передасться level=0, innertranslation и списокм entries - дочерних записей
        #т.к для InnerTransitionals уровень равен 0, то он добавляется в тот же список entires c ключом, элементом и пустым списком
        if level == 0:
            children.append((key, item, []))
        else:
            print('------------------Children Start------------')
            print(children)
            print('--------------------Children END---')
            print('----Start elem--->>>',children[-1][2],'<<<<-----------End elem[-------')
            add_entry(level - 1, key, item, children[-1][CHILDREN])

    def update_indented_list(entry):
        indented_list.append(entry[ITEM])
        for subentry in sorted(entry[CHILDREN]):
            update_indented_list(subentry)

    entries = []
    #Алгоритм состоит из 3-х этапов, 1-й - это листаем наш массив и выяснем какие там есть уровни
    for item in indented_list:
        level = 0
        i = 0
        #Что делает этот алгоритм он значит берет и перебирает сначала 4 пробела, если удалось, то жто 1-й уровень, левел увеличивается на 1, к след позиции где искать прибавляем длину отсупа и снова
        #если еще раз увиеличился то это уже втрой уровень, проделывая такую итерации итарцию мы можем узнать какой элемент на каком уровне расположен относительно корня, т.е 0 элемента
        while item.startswith(indent, i):
            i += len(indent)
            level += 1
        #ключом у нас будет имя элемента где все буквы маленькие
        key = item.strip().lower()
        #Теперь вызываем функцию которая запхнет наш элемент с ключом в новый массив
        add_entry(level, key, item, entries)
    #Очистим наш исходный массив и будем пихать в него элементы функцией update_intendet_list, возвращая их по одному из сформированного массива entries
    indented_list = []
    for entry in sorted(entries):
        update_indented_list(entry)
    return indented_list
indented_list_sort(before)