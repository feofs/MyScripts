import MySQLdb
import py3eg.Console as Console
import sys
import xml.sax.saxutils
DISPLAY_LIMIT=10
def main():
    while True:
        try:

            db = MySQLdb.connect(host='localhost',user='root',passwd='minimals',db='test')

            call = dict(a=add_bookmark, e=edit_bookmark, l=list_bookmarks, d=delete_bookmark, q=quit)
            menu = ("(A)dd DVDs, (E)dit DVDs, (L)ist DVDs, (D)elete DVDs, (Q)uit")
            valid = frozenset('aeldq')
            action=Console.get_menu_choice(menu,valid,'a')
            if action=='q':
                sys.exit(1)
            else:
                call[action](db)
        finally:
            if db is not None:
                db.close()

def add_bookmark(db):
    #Теперь как обычно просим ввести имя и УРЛ
    name = Console.get_string("Name", "name")
    if not name:
        return
    url = Console.get_string("URL", "url")
    if not url:
        return
    url=xml.sax.saxutils.escape(url)
    if not url.startswith('http://'):
        url='http://'+url
    cursor=db.cursor()
    sql='INSERT INTO urls (name,url) values (%s,%s)'
    #print(sql,locals())
    try:
        cursor.execute(sql,(name,url))
        db.commit()
    except MySQLdb.MySQLError as err:
        print('During insert to database was error ',err)
    return None

def edit_bookmark(db):
    id = find_bookmark(db, 'edit')
    if not id or id is None:
        return
    cursor=db.cursor()
    new_name=get_string_from_user('Please input new name :','new_name')
    new_url=get_string_from_user('Please input new url :','new_url')
    query='UPDATE urls SET name=%s,url=%s where id=%s'
    cursor.execute(query,(new_name,new_url,id))
    db.commit()
    return None

def get_string_from_user(msg,name):
    while True:
        value = Console.get_string(msg,name)
        if not value:
            continue
        else:
            break
    return value

def delete_bookmark(db):
    id = find_bookmark(db, 'edit')
    if not id or id is None:
        return
    cursor = db.cursor()
    query='DELETE FROM urls where id=%s'
    cursor.execute(query,(id,))
    db.commit()
    return None

def list_bookmarks(db):
    cursor = db.cursor()
    # составим запрос но пока не применим, а просто для начала ниже посчитаем всолько всего записей в базе и если их больше запрос будем потихоньку наращивать
    sql = ('SELECT * from urls')
    start = None
    count=bookmarks_count(db)
    if count>DISPLAY_LIMIT:
        start=get_string_from_user('Please input more information for name','name')
        sql += ' AND name like %s'
    sql += ' ORDER BY name'
    if start is None:
        cursor.execute(sql)
    else:
        cursor.execute(sql, (start + '%',))

    results = cursor.fetchall()
    print(' {0: ^4} {1: ^40} {2: ^60}'.format('ID', 'NAME', 'URL'))
    print(' {0:_^4} {0:_^40} {0:_^60}'.format(''))
    for id, name, url in results:
        print(' {0: ^4} {1: ^40} {2: ^60}'.format(id, name, url))

def bookmarks_count(db):
    cursor=db.cursor()
    cursor.execute('select count(*) from urls')
    count=cursor.fetchone()[0]
    return count


def find_bookmark(db,msg):
    msg='Please enter URL name what you want to find and '+msg+' or (q) to exit'
    cursor=db.cursor()
    #Теперь нам тут нужно бесконечно просить либо уточнять имя пока не дойдем лимита а потом уже просить выбрать из имеющихся
    while True:
        start = Console.get_string(msg, 'title', None)
        # Хотя вставит
        if start is None or not start:
            continue
        elif start == 'q':
            return None

        query='SELECT * FROM urls where name like %s'
        cursor.execute(query,(start+'%',))
        #Теперь извлечем все строки из запроса fetchcone - получить одну последнюю строку из запроса в виде кортеджа и fetchall - получить все строки в виде кортежа - кортежей
        results=cursor.fetchall()
        if len(results)>DISPLAY_LIMIT:
            print('Try input more informative name')
            continue
        if len(results)==0:
            print('Try input more informative name')
            continue
        print(' {0: ^4} {1: ^40} {2: ^60}'.format('ID','NAME','URL'))
        print(' {0:_^4} {0:_^40} {0:_^60}'.format(''))
        for id,name,url in results:
            print(' {0: ^4} {1: ^40} {2: ^60}'.format(id, name, url))
        choise=Console.get_integer('Please your choise','choise')
        return choise




main()