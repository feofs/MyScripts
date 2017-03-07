#Вот еще прикольно то что можно писать определенные классы а в их методы определять  для работы с SQL, например напишем класс где __пуе
import MySQLdb
class Test:
    a=10
    def __getattr__(self, item):
        print('Вы пытаетесь вызвать __getattr__')
    def __getattribute__(self, item):

        return  'Bla bla',object.__getattribute__(self,item)

#Тут значит __getattribute__ работает только для существующих переменных значит его и нужно использовать
#а __getattr__ работает для всех, то есть проверим что пользователь хочет сделать и либо вернем либо вставим в базу и вернем
o=Test()
print(o.a)
o.b
o.c

class AbstarctMySQL:
    def __init__(self,host,user,password,basename):
        self.db = MySQLdb.connect(host=host, user=user, passwd=password, db=basename)
        #self.__dict__['test']=1
        #self.cursor=self.db.cursor()
    def __getattribute__(self, name):
        self.name=name
        self.cursor=self.db.cursor()
        self.cursor.execute('select url from urls where name=%s',(self.name,))
        self.url=self.cursor.fetchone()[0]
        self.db.commit()
        if not self.url or self.url is None:
            return None
             #self.cursor.execute('INSERT INTO urls (name) values(%s)',(self.name,))
        else:
            return self.url

    def __setattr__(self, item, value):
        #Только в словарь, инче вызывая self.name = мы снова вызываем метод __setattr__
        print('Zaebala recursiaya',item,value)
        db=MySQLdb.connect(host='localhost', user='root', passwd='minimals', db='test')
        cursor=db.cursor()
        cursor.execute('INSERT INTO urls (name,url) values (%s,%s)',(item,value))
        db.commit()


absmysql=AbstarctMySQL('localhost','root','minimals','test')
print(absmysql.vodka)
#absmysql.vodka='http://vodka.com'

#А вот тут еще напишем менеджер контеста для теста

