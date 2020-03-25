def karprekarNumbers(p, q):
    listOfNums = []
    for i in range(p, q + 1):
        number  = str(i**2)
        l       = len(number)
        if l > 1:
            if int(number[:l//2]) +int(number[l//2:]) == i:
                listOfNums.append(i)
        elif i == 1:
            listOfNums.append(i)
    if len(listOfNums) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(map(str, listOfNums)))

