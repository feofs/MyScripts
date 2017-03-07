#напишем простую программку, которая ляжет в основу будущего примера,
#здесь напишем прогу сервера, который прослушивает определнный порт, ему будут отсылаться данные запакованные модулем strcut где первые 4 байта длина следующих за ним данных
#сервер распакует их и запишет в файл и отправит ответ
import socket
import string
import struct
import pickle

def main():
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_PORT=9000
    TCP_ADDRESS=''
    #Запускаем наш сервер, который будет слушать порт и получать данные
    server.bind((TCP_ADDRESS,TCP_PORT))
    #Теперь мы можем начать прослушивать порт, сдулаем это в бесконечном цмкле
    # опять таки создадим структурированные данные чтобы для начала получить длину данных а затем сами данные, распаковать и записать в файд
    StructSize=struct.Struct('!I')
    print(StructSize.size)

    server.listen(10)
        #Теперь мы можем начать принимать данные по сеодинению, она вернет conn - это двусторонии сокет по которому мы можем получать данные recv и отправлять данные клиенту
        #в address[0][1] - будет соотвественно и адресс и порт удаленного клиента
    conn,address=server.accept()
    while True:
            data_size=conn.recv(StructSize.size)
            #try:
            data_size=StructSize.unpack(data_size)[0]
            #except struct.error:
            #    continue
            print(data_size)
            #Тип возвращаемых данных bytes запакованные pickle теперь нам нужно их распаковать и записать в файл и вывдем сообщение
            data=conn.recv(data_size)

            data=pickle.loads(data)
            print(data)
            if not data:
                break
            print('Data received from {0} {1}'.format(address,data))
            try:
                with open('server_data.txt','w+') as fh:
                    fh.write(data)
            except (EnvironmentError,FileExistsError) as err:
                print('During saving to file was error ',err)
                continue
            message='Data saved to file'
            message=pickle.dumps(message,pickle.HIGHEST_PROTOCOL)
            conn.sendall(StructSize.pack(len(message)))
            conn.sendall(message)

            #conn.close()
main()









