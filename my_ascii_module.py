import string
import functools
text='basjkdjfjhdjjkdsfj'

#Для доктестов можно сделать так is_ascii_punctuation.__doc__ = """\ но мы сразу запхнем эту строку документирования в функцию
def is_ascii(text):
    """
    >>> is_ascii("Universal suffrage")
    True
    >>> is_ascii("Cinema vérité")
    False
    """
    new=list(map(lambda char: ord(char),text))
    #Можно просто сранить длину двух массивов т.е сначала мы преобразовали в цифры текст, и если фильтр не удалил никаких символов то все ок все символі влезли
    new2 = list(filter(lambda char: True if char<127 else False, new))
    if len(new)==len(new2):
        return True
    else:
        return False


def is_punctuation(text):
    """Doctest
    >>> is_punctuation('.,?!')
    True
    >>> is_punctuation('dfdf')
    False
    """
    new=list(map(lambda char: True if char in string.punctuation else False,text))
    return True if all(new) else False

def is_printable(text):
    """Doctest
    >>> is_printable('dfdfdf')
    True
    >>> is_punctuation('@!?*\\t\\x05\\n')
    False
    """
    new = list(map(lambda char: True if char in string.printable else False, text))

    return True if all(new) else False


print('All symbols are ASCII text ' ,is_ascii(text))
print('All symblos is puntuation ',is_punctuation(text))
text2=',.!?'
print('All symblos is puntuation ',is_punctuation(text2))
print('All symblos is printable ',is_printable(text))

if __name__ == "__main__":
    import doctest
    doctest.testmod()