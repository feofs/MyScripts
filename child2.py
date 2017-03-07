import os
import sys
import subprocess

#Тут нам нужно просто из стандартного потока принять данные
data=sys.stdin.readline().rstrip()
data=data.split(',')
word=data[0]
filename=data[1]

with open(filename,'r') as fh:
    line = 1
    while True:
        current = fh.readline()
        if not current:
            break
        if word in current:
            #print('Finded at file {0} line {1} word {2}'.format(filename, line, word))
            st='Finded at file {0} line {1} word {2}'.format(filename, line, word)
            sys.stdout.write(st+'\n')

        line += 1
