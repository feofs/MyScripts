import sys
word=sys.stdin.readline().rstrip()
filename=sys.stdin.readline().rstrip()
with open(filename,'r') as fh:
    line=1
    while True:
        current=fh.readline()
        if not current:
            break
        if word in current:
            print('Finded at file {0} line {1} word {2}'.format(filename,line,word))
        line+=1