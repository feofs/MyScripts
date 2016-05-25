import pickle,os
#print(dir(__builtins__))
#Модуль builtins содержит объект file который в свою очередь содержит функции для работы с файлами включая такие методы как open(),read(),write(),close()
#Для того чтобы объект типа файл появился его сначала надо открыть функцией open

if os.path.isfile('update.txt'):
    os.remove('update.txt')
    print('File removed')
#print ('File is deleted :',os.path.de
    fp=open('update.txt','w+')

    print('Curent position in file:',fp.tell())
    string='This string i put in file'
    length=len(string)
    print('The language of string is :',length)
    fp.write(string)
    print('Now after write position in file:',fp.tell())
    fp.seek(length+2)
    print('Now after SEEK position in file:',fp.tell())
    string2='V I Lenin'
    fp.write(string2)
    fp.seek(0)
    print('----------File text---------------')
    text=fp.read()
    print(text)
    fp.close()

if os.path.isfile('pickle.dat'):
    os.remove('pickle.dat')
#Вот как можно сериализировать и сохранять несколько объектов в файле, в Питоне это называется консервация и разконсервация
data1=['Tulip','Flowers']
data2=['Orange','Ananas']
fp=open('pickle.dat','wb')
pickle.dump(data1,fp)
pos1=fp.tell()
print('Postition after insert data1 :',pos1)
pickle.dump(data2,fp)
pos2=fp.tell()
print('Postition after insert data2 :',pos2)
fp.close()

#Т.е все таки есть какая-то конечная метка
fp=open('pickle.dat','rb')
print(pickle.load(fp))
print(pickle.load(fp))


