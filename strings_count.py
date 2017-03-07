#Прогрмма подсчета всех строк в файле
import os,sys

print(os.path.dirname(__file__))
i=0

for filename in os.listdir(os.path.dirname(__file__)):
    if filename.endswith('.py'):
        with open(filename,'r') as fh:
            while True:
                try:
                    line=fh.readline()
                    i+=1
                    if not line:
                        break
                except UnicodeDecodeError:
                    continue

print('Lines in all files is ',i)
