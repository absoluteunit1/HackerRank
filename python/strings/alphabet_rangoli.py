import string

def print_rangoli(size):
    ls = []
    letters = string.ascii_lowercase
    for i in range(size):
        rangoli = "-".join(letters[i:size])
        print(rangoli)
        ls.append( (rangoli[::-1] + rangoli[1:]).center(4*size-3, "-") )
        print(ls)
    print('\n'.join( ls[:0:-1] + ls))
