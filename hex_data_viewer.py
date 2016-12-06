import sys
import os
import optparse
if len(sys.argv)==1 or sys.argv[1] in ('-h','--help'):
    print ('''Используйте следующие опции : \n
               -h, --help      Вывести это справочное сообщение
               -b BLOCKSIZE, --blocksize=BLOCKSIZE
                               Размер блока (8...80) [по умолчанию 16]
               -d, --decimal   Блоки десятичных чисел
                               По умолчанию шестнадцатиричные
               -e ENCODING, --encoding=ENCODING
                               Кодировка (ASCII...UTF-32) [по умолчанию UTF8]
           ''')

#Теперь еще установим опции, какого они должны быть формата и в какую переменую заноситься
parser = optparse.OptionParser(conflict_handler="resolve")
#parser.set_defaults(blocksize=16, decimal=None, encoding='UTF-8')
parser.add_option("-b", "--blocksize", dest="blocksize", type=int,default=16,help='Размер блока (8...80) [по умолчанию : %default]')
parser.add_option("-d", "--decimal", dest="decimal",type=None,default=False,help='Блоки десятичных чисел. По умолчанию шестнадцатиричные [по умолчанию %default]')
parser.add_option("-e", "--encoding", dest="encoding", type=str,default='UTF-8',help='Кодировка (ASCII...UTF-32) [по умолчанию UTF8]')
#help=("the maximum number of characters that can be "
#"output to string fields [default: %default]"))
#parser.add_option("f", "format", dest="format",
#help=("the format used for outputting numbers "
#"[default: %default]"))
#parser.set_defaults(maxwidth=100, format=".0f")
parser.parse_args()
parser.print_help()