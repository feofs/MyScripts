#Файл генератор барахла для создания двух файлов по 100 тыс строк для процессов
import sys
import string
import random

st=string.ascii_letters
new=''
for i in range(30):
    new+=random.choice(st)
with open('./threads_data/parent.data','w') as fh:
    for line in range(65000):
        if line == 50000:
            fh.write('Test\n')
            continue
        new = ''
        for i in range(30):
            new += random.choice(st)
        new+='\n'
        fh.write(new)
with open('./threads_data/child.data','w') as fh:
    for line in range(65000):
        if line == 40000:
            fh.write('Test_child\n')
            continue
        new = ''
        for i in range(30):
            new += random.choice(st)
        new+='\n'
        fh.write(new)