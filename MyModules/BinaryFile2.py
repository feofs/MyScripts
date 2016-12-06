#Вот еще один профессиональный момент
#при обычном чтении файл читается в память полностью с текущими объемами это норма, но вот хорошо бы было читать в память порциями
#как то делает SQL или DBM это легко реализовать используя типа ключ-значение для произвольного доступа к данным на диске
'''
BinaryRecordFile.BinaryRecordFile.
Экземпляры этого класса являются универсальным представлением
двоичных файлов, доступных для чтения и записи, состоящих из по
следовательности записей фиксированной длины.
Т.е как бы состоящий из кусков строк определнной длины к которым можно обратиться
Он напоминает список т.к обеспечивает добавление и удаление записей по заданной позиции
Когда запись удаляется она просто метиться как удаленная но остается, тогда нет необходимости перемещать и сдвигать другие записи
что значит что все первоначальные индексы остаются допустимыми, а также можно легко восстановить
также это будет решаться за счет методов уплотнения которые удалят помеченные на удаление а остальные пресанут
Пример
Сontact=Struct.struct('<15si') - создается структура для переовда данных в бинарник (обратный порядок, сначала идет строка длиной 15 символов,
затем 32 битовое целое
contacts=BinaryRecordFile(filename,Contact.Size) - создается экземляр класса куда передаем имя файла и размер записи, соотвествующий размеру структуры
если есть, его содержимое останется на месте, если нет то запишеться новый
#Впакуем в структуру и передадим на запись в файл в ячейку 4 и 5
contacts[4] = Contact.pack("Abe Baker".encode("utf8"), 762)
contacts[5] = Contact.pack("Cindy Dove".encode("utf8"), 987)
типа файд воспринимаем как список
они перезапишут прежнее а если у файла менее 6-ти записей то будут созданны две новые  каждая из которых заполненна байтами 0x00
Поскольку строка «Cindy Dove» содержит менее 15 символов UTF8,
при упаковывании в конец ее будут добавлены байты 0x00. Поэтому
при извлечении записи contact_data будет содержать кортеж из двух
элементов (b'Cindy Dove\x00\x00\x00\x00\x00', 987). Чтобы получить
имя, необходимо декодировать последовательность байтов в кодиров
ке UTF8 для получения строки Юникода и потом удалить завершаю
щие байты 0x00.
Каждая запись начинается с байта
_DELETED = b"\x01"
_OKAY = b"\x02"
т.е значит состояние записи и того полчим 1 байт состояния + 15 байт строки + 4 байта числа = 20 байтам
'''
import os
import struct
class BinaryRecordFile:
    _DELETED=b"\x01"
    _OK=b"\x02"
    #Т.к это не ограниченный по размеру объект то пользователь сам должен установить желаемый размер записи т.е одного элемента
    def __init__(self,filename,record_size,auto_flush=True):
        #При передаче данных увеличим реальный размер на 1 т.к нужно записать еще 1 байт инфы о записи ОК или удаленна
        self.__record_size=record_size+1
        print(self.__record_size)
        mode="w+b" if not os.path.exists(filename) else "r+b"
        self.__fh=open(filename,mode)
        print(self.__fh.mode)

        self.auto_flush=auto_flush
    #Устновим некоторые свойства только для чтения
    @property
    def record_size(self):
        return self.__record_size-1
    @property
    def name(self):
        return self.__fh.name

    def flush(self):
        return self.auto_flush

    def close(self):
        self.__fh.close()

#Теперь напишем основной метод, который позволяет записать в файл при обращении по индексу
    def __setitem__(self, index, record):
        assert isinstance(record,(bytes,bytearray)), 'Recrord must be ninary data'
        assert len(record)==self.record_size,'Length of data must be {0} '.format(self.__record_size)
        #Т.к мы задали индекс куда вставить передвинем курсор в файле на заданное кол-во позиций по длине
        self.__fh.seek(index*self.__record_size)
        #Пофиг есть там запись или нет, если есть то перезапишем но перед этим еще и вписав и метку
        self.__fh.write(self.__class__._OK)
        self.__fh.write(record)
        if (self.auto_flush):
            self.__fh.flush()
    #__getitem -то же самое но возвращает запись в бинарном виде по переданному индексу
    def __seek_to_index(self,index):
        #Для начално насильно вытолкнем данные  из буферов на диск

        if self.auto_flush:
            self.__fh.flush()
        # Тут то мы можем же задать неправильный индекс, который больше по размеру
        # поэтому по хитрому там же можно указав os.SEEK_END, и сместив на 0 байт с конца мы узнаем длину файла
        # и вставив проверку не позволим указывать неккоректные индексы
        self.__fh.seek(0,os.SEEK_END)
        end=self.__fh.tell()
        offset=index*self.__record_size
        if offset>=end:
            raise IndexError('no record at position {0}'.format(index))
        self.__fh.seek(0)
        self.__fh.seek(offset)

    def __getitem__(self, index):
        #Т.к операцию перемещения указателя по индексу нужно будет повторять часто  то вынесем в отдельную функцию
        self.__seek_to_index(index)
        #Получим для начала состояние чтобы первый байт был равен ОК
        state=self.__fh.read(1)
        if state!=self.__class__._OK:
            return None
        #Не забываем что прочитав 1 байт мы сдвинули указатель на байт, поэтому можно сразу читать данные без сдвига на этот байт
        return self.__fh.read(self.record_size)

    def __delitem__(self, index):
        #Тут для начала вызовем функцию seek_to_item, которая проверит не выходит ли за границы файла индекс если да то вызовет ошибку, а потом проверим первый бит на ОК
        #и если он ОК записать туда Делетед
        self.__seek_to_index(index)
        state=self.__fh.read(1)
        if state!=self.__class__._OK:
            return
        #Т.к мы прочитали 1 байт состояни то нужно передвинуть назад, и записать Делетед
        self.__fh.seek(-1, os.SEEK_CUR)
        self.__fh.write(self.__class__._DELETED)
        if self.auto_flush:
            self.__fh.flush()

    #Та же функция только помечает как ОК, если до этого был помечен на удаление
    def undelete(self,index):
        self.__seek_to_index(index)
        state = self.__fh.read(1)
        if state != self.__class__._DELETED:
            return
        # Т.к мы прочитали 1 байт состояни то нужно передвинуть назад, и записать Делетед
        self.__fh.seek(-1, os.SEEK_CUR)
        self.__fh.write(self.__class__._OK)
        if self.auto_flush:
            self.__fh.flush()
    def __len__(self):
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0,os.SEEK_END)
        end=self.__fh.tell()
        return end//self.__record_size

#Для удаления удаленных записей можно использовать два способа, первый - присвоение индексов удаленным записям более большим значениями индексов, и усечь его с конца, если в нем были пустые строки

#второй скопировать все нормальные значения в новый файл и назначить индексы по порядку опишем оба из них
    def inplace_compact(self):
        index=0
        length=len(self)
        #Просматриваем в цикле по индексам наши записи
        while index<length:
            self.__seek_to_index(index)
            status=self.__fh.read(1)
            if status!=self.__class__._OK:
                #Если верхнее условие нашло помеченный на удаление то будем искать следующий с состоянием ОК, чтобы переместить его на данное место от следующего элемента до конца файла, меняя их местами
                #а так тут то не в индексах дело, индексы то не пишуться в данные вместе с записью в файл, т.е пустая запись или помеченная на удаление замещается не пустой, в конце все не пустые записи должны остаться в конце файла
                for next in range(index+1,length):
                    self.__seek_to_index(next)
                    state=self.__fh.read(1)
                    if state==self.__class__._OK:
                        self[index]=self[next]
                        #удаляем дубликат
                        del self[next]
                #Вставим для цикла еlse, т.к если цикл закончился, то значит
                else:
                    break
            index+=1
            #Ну по идее тут даже после этого цикла не должно было остаться пустых записей, если мы и так их позаменяли
        #Теперь нужно просмотреть записи начиная с 0 и если запись равно ОК то удлим все вплоть до нее, т.к все записи
        self.__seek_to_index(0)
        state=self.__fh.read(1)
        if state!=self.__class__._OK:
            self.__fh.truncate(0)
        else:
            #Если же первая запись оказалась все таки нормальной, то введем переменную limit,которая принимает индкес первой не пустой записи
            #а как она это делает - листаем файл, начиная от первой с конца записи в указанном цикле, сдвигая индекс на 1, что делает за нас функция
            #затем читаем 1-й байт и если он не ОК то передаем его в лимит и транкаем файл по этому лимиту умноженному на размер записи, если записей не найденно бреканем
            limit=None
            for index in range(len(self),-1,0,1):
                self.__seek_to_index(index)
                state=self.__fh.read(1)
                if state!=self.__class__._OK:
                    limit=index
                else:
                    break
            if limit is not None:
                self.__fh.truncate(limit*self.__record_size)
        self.__fh.flush()

    def compact(self,backup=True):
        comapct_file=self.__fh.name+'.$$$'
        backup_file=self.__fh.name+'.bak'
        self.__fh.flush()
        self.__fh.seek(0)
        fh=open(comapct_file,'wb')
        while True:
            data=self.__fh.read(self.__record_size)
            if not data:
                break
            #Здесь хитрость, которую нужно запомнить, т.к и _OK и data - являются объектами типа bytes, но если мы извлекаем только по индексу например data[0] - то мы получим обїект типа int
            #а если по срезу то объект типа bytes, который и пожно сравнить с объектом типа bytes _OK
            if data[:1]==self.__class__._OK:
                fh.write(data)
        #Закрываем файл открытый и для записи и для чтения
        fh.close()
        self.__fh.close()
        os.rename(self.__fh.name,backup_file)
        os.rename(comapct_file,self.__fh.name)
        if not backup:
            os.remove(backup_file)
        self.__fh=open(self.__fh.name,'rb')

#Теперь напишем класс BykeStock - который использует, класс BinaryRecordFile, ключи - идентификаторы велосипедов а значения - их индексы в файле
'''
Пример использования, например откроем файл и загрзим его в объект, а затем посчитаем общую стоимость всех влеосипедов, потом увелиичм кол-во велосипедов марки Гекко на 2
а затем найдем велосипеды начинающиеся с B4U и увеличим на 1
bicycles=BikeStock(filename)
value=0.0
for bike in bicycles:
    value+=bike.value
bicycles.increase_stock("Gekko",2)
for bike in bicycles:
    if bike.identity.startswitch('B4U')
     if not bicycles.increase_stock(bike.identity,1):
     print('stock movement failed for {0}'.format(bike.identity))

'''
#По ходу если мы даже если через __init__ устанвливаем значения то мы все равно обращаемся к свойсву этой переменной то есть на самом то деле как описанно в свойствах, мы устанавливаем не name а __name
class Bike:
    def __init__(self,identity,name,quantity,price):
        assert len(identity)>3, ("invalid bike identity '{0}'".format(identity))
        self.__identity=identity
        self.name=name
        self.quantity=quantity
        self.price=price

    #Опишем некоторые свойсвва, через которые будем обращаться к переменным
    @property
    def identity(self):
    #"The bike's identity"
        return self.__identity

    @property
    def name(self):
        #"The bike's name"
        return self.__name

    @name.setter
    def name(self, name):
        assert len(name), "bike name must not be empty"
        self.__name = name

    @property
    def quantity(self):
        #"How many of this bike are in stock"
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        assert 0 <= quantity, "quantity must not be negative"
        self.__quantity = quantity
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        assert type(price)in (int,float), 'price must be int or float'
        assert 0.0 <= price, "price must not be negative"
        self.__price = price

    @property
    def value(self):
        #Вернет общую стоимость т.е кол-во умноженное на цену
        return self.quantity * self.price

#здесь мы создали структурный объект, сначал идет строка длиной 8 симовлов, пот строка 30 символов, потом мы можем передоать имя файла и длину этого объекта
#в объект BinaryRecord т.е тем самым создадим типа объект он будет знать длину записи от которой и будут отталкиваться все другие методы, как-то запись, и считывание по индексу
#Формат 8 символов на ИД, 30 символов на имя потом - єто 16 битовое целое на колво и 32 битовій флоат на цену
_BIKE_STRUCT = struct.Struct("<8s30sid")

#А вот ниже приведены 2 функции модуля, 1-я хитрожопо распаковывет список от 0до4-х  в переменные, чтобы обращаться потом по переменным а не индексам по формату нашей записи
#
def _bike_from_record(record):
        ID, NAME, QUANTITY, PRICE = range(4)
        #тут когда с помошью какого либо метода мы получили бинарный кусок файла в переменную record, мы берем, распаковывем ее и затем по id вынимаем нужные нам части по id
        #и потом сразу распаковыем их в наш объект, в итоге функция вернет уже инициализированный объект
        parts = list(_BIKE_STRUCT.unpack(record))
        #Т.к ID и имя могут быть меньше заданной двоичной длины то в конце будут присутсвовать нули просто обрежем их
        parts[ID] = parts[ID].decode("utf8").rstrip("\x00")
        parts[NAME] = parts[NAME].decode("utf8").rstrip("\x00")
        return Bike(*parts)


def _record_from_bike(bike):
    # а тут мы наоброт пакуем данные и возращаем байтовые, которые поместим потом в файл
    #а тут просто возврати двоичные данные из полей объекта
    return _BIKE_STRUCT.pack(bike.identity.encode("utf8"),
            bike.name.encode("utf8"),bike.quantity, bike.price)

#Класс ByteStock реализует собственные методы манипулирования объектами типа Bike, которые используют методы типа Bike доступные для записи
#В общем что делает єтот класс - он использует BinaryRecord класс, который открывает двоичный файл з записями дибо создает, если такого не существует
# потом листает этот файл, чатсная _bike_from_record распаковывает его и возвращает объет типа Bike, в том классе нихрена нет кроме свойтсв
class BikeStock:
    def __init__(self,filename):
        #Создадим внутренюю переменную для двоичного файла, типа будет как массив, к заисям в файле можно обращаться по индексам
        self.__file=BinaryRecordFile(filename,_BIKE_STRUCT.size)
        #Теперь переменную словарь для помещения туда имя байка - индекс в файле
        self.__index_from_identity={}
        for index in range(len(self.__file)):
            #Листаем по кол-ву индексов точнее записей в файле, которая нам вернула функция len()
            record=self.__file[index]
            #Если запись не пуста передадим ее в функцию, которая распакует запись и вернет уже заполнеый объект типа Bike
            if record is not None:
                bike=_bike_from_record(record)
                #А мы извлечем из этого объекта строковый идентификатор и создадим словарь соот-ий идентификатор - индекс в файле
                self.__index_from_identity[bike.identity]=index

    def append(self,bike):
        #Записи добавляются в конец словаря, поэтому мы должны знать длину self.__file - объекта типа BinaryRecordFile
        index=len(self.__file)
        #Запкуем в спомощью функции _record_from_bike и запишем в файл
        self.__file[index]=_record_from_bike(bike)
        self.__index_from_identity[bike.identity]=index

        #Для удаления записи достаточно просто узнать индекс по имени в словаре, а затем метод класса BinaryRecordFile - пометит эту запись как удаленную
    def __delitem__(self, identity):
        del self.__file[self.__index_from_identity[identity]]
    #Получить запись, вернет объект типа Bike со всеми его свойствами
    def __getitem__(self, identity):
        #Извлекаем запись по идентификатору
        #print(self.__file[self.__index_from_identity[identity]])
        #print(self.__index_from_identity[identity])
        record=self.__file[self.__index_from_identity[identity]]
        return None if record is None else _bike_from_record(record)

    def __change_stock(self,identity,amount):
        #Сначала извлечем индекс по имени а затем извлечем данные по индексу
        index=self.__index_from_identity[identity]
        record=self.__file[index]
        if record is None:
            return False
        #Потом из двоичных данных получим объект, изменим его свотсво с кол-вом, и снова запишем потому же индексу в файл
        bike=_bike_from_record(record)
        bike.quantity+=amount
        self.__file[index]=_record_from_bike(bike)
        return True

    def change_name(self, identity, name):
        # Сначала извлечем индекс по имени а затем извлечем данные по индексу
        index = self.__index_from_identity[identity]
        record = self.__file[index]
        if record is None:
            return False
        # Потом из двоичных данных получим объект, изменим его свотсво с кол-вом, и снова запишем потому же индексу в файл
        bike = _bike_from_record(record)
        bike.name=name
        self.__file[index] = _record_from_bike(bike)
        return True

    def change_price(self, identity, price):
        # Сначала извлечем индекс по имени а затем извлечем данные по индексу
        index = self.__index_from_identity[identity]
        record = self.__file[index]
        if record is None:
            return False
        # Потом из двоичных данных получим объект, изменим его свотсво с кол-вом, и снова запишем потому же индексу в файл
        bike = _bike_from_record(record)
        bike.price = price
        self.__file[index] = _record_from_bike(bike)
        return True

    #Лямбда функция, типа сразу возращает значение, 1- строчная функция, передаем туда три арга, которые засунем в функцию __change_stock, которая сделает все за нас и вернет резалт
    #в итоге полуим две лямбда функии, они будут как бы полноценными методами класса, к которым можно обратиться как к методу и передать арги
    increase_stock=(lambda self,identity,amount: self.__change_stock(identity,amount))
    #Если хотим уменьшить значение то просто передаем с минусом
    decrease_stock = (lambda self, identity, amount: self.__change_stock(identity, -amount))

    #Провернем функцию итерации которая будет возвращать по очереди объекты типа Bike
    def __iter__(self):
        for index in range(len(self.__file)):
            record=self.__file[index]
            if record is not None:
                yield _bike_from_record(record)

#g=lambda x,y:x*y;
#print(g(3,4))







