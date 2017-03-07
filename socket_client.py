import socket
import string
import struct
import pickle

#Тут мы вводим просто какую то строку
#Для начала создадим соеднинение с сервером и потом будем посылать ему данные запакованные в биты, для начала длину данных а потом сами данные, а сервер будет принимать

conn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #необходимо передавать ей кортеж из адреса и порта
params=('127.0.0.1',9000)
conn.connect(params)
while True:
    try:
        data=str(input('Please input string to send to server : '))
    except TypeError as err:
        print('Error during convert data to string ',err)
        exit()
    data = pickle.dumps(data, pickle.HIGHEST_PROTOCOL)
    StructSize=struct.Struct('!I')
    conn.sendall(StructSize.pack(len(data)))
    conn.sendall(data)
    #Ожидаем получение размера идущих за ними данными
    size_data = conn.recv(StructSize.size)
    #Распаковываем и получаем длину
    size = StructSize.unpack(size_data)[0]
    #Затем пытаемся считать и распаковать данные т.к они запакованны пиклем
    result_data=conn.recv(size)
    result_data=pickle.loads(result_data)

    print('The result returned from server : ',result_data)
    #conn.close()





