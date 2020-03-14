import numpy
# Using recursion

def extraLongFactorials(n):
    return 1 if n == 1 else n*extraLongFactorials(n-1)

# Using list comprehension and for loop

def extraLongFactorials2(n):
    a = [n-i for i in range(n)]
    result = 1
    for i in a:
        result *= i
    return result

# Using numpy.prod()

def extraLongFactorials3(n):
    return numpy.prod([n-i for i in range(n)])

# Simple for loop approach 

def extraLongFactorials4(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


print(extraLongFactorials(5))
print(extraLongFactorials2(5))
print(extraLongFactorials3(5))
print(extraLongFactorials4(5))

