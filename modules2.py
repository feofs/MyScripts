import sys,keyword
print(keyword.kwlist)
print('Python version :',sys.version)
print('Iterpretator location',sys.executable)

print ('Module searhable paths')
for dir in sys.path:
	print (dir)

print ('Keywords of Python')
for word in keyword.kwlist:
	print (word)