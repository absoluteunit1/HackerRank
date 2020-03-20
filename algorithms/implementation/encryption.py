# remove the spaces from the string
# rows x columns >= L

import math

# Solution One
# Using a 2D array
# Only works for 4/13 test cases. Couldn't make it work for all the test cases' iterating through the string might be an easier approach


def encryption(s):

    noSpaces = "".join(s.split())
    L = len(noSpaces)
    
    row = math.floor(math.sqrt(L))
    col = math.ceil(math.sqrt(L))

    if L > col*row:
        row = math.ceil(math.sqrt(L))
    
    encrypted = []

    for row in range(row):

        if len(noSpaces) >= col:
            encrypted.append([noSpaces[i] for i in range(col)])

        elif len(noSpaces) < col:
            encrypted.append([noSpaces[i] for i in range(len(noSpaces))])
        noSpaces = noSpaces[(row or 1)*col:]
    
    print(encrypted)

    cipher = ""
    lastRowLen = len(encrypted[-1])
    count = 0

    for number in range(col):
        for row in encrypted:
            if len(row) == col:
                cipher += row[number]
            elif count < lastRowLen:
                cipher += row[count]
                count += 1
        cipher += " "

    return cipher

# Solution Two
# Iterating through the string. Only 3 lines of code needed
def encryption2(s):
    
    # remove the spaces and join the characters by replacing the whitespace with an empty string
    noSpaces = s.replace(" ", "")

    # calculate the ceiling value of the square root of the length of the string. Row calculation is not nocessary. 
    c = math.ceil(math.sqrt(len(noSpaces)))
    
    # Step 1. Create a list using list comprehension "noSpace[i::c]" gives a string of every c character starting from i. Ex: a = "HelloWorld!", a[0::3] gives "Hlod". 
    # Step 2. Join each list element with a space by using join function. 
    return " ".join([noSpaces[i::c] for i in range(c)])

