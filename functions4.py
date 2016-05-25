from cats import speak,sleep
from dogs import speak,sleep

speak()
sleep()
import sys, keyword
print ('The type of SYS is :',type (sys))
print ('#############The main keywords of Python############')
#for i in dir(sys): print i

print ('The version of Python is :',sys.version)
print ('The executable of Python is :',sys.executable)

print ('#############The main keywords of Python############')
print ('\n\n\n')
pass
print ('The type of keywords is :',type (keyword.kwlist))
for word in keyword.kwlist:
	print (word)

import math, random
num=9
res=math.sqrt(num)
ugol=60
res=math.sin(ugol)

array=['Apple','Orange','Babuin','Negr']
print (array.sort)

newarr=random.sample(array)

for eleme in newarr :
	print(elem)
