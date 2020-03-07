def reverseArray(a):
    return a[::-1]

def reverseArray1(a):
    a.reverse()
    return a

def reverseArray2(a):
    reversedArr = []
    for i in range(len(a) -1, -1,-1):
        reversedArr.append(a[i])
    return reversedArr

