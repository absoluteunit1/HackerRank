def add(p1, p2):
    return sum((i or j) for i, j in zip(p1, p2))

a = [1,2,3,4]
b = [1,2,3,4]

print(add(a, b))


# What does (i or j) mean and what does zip() do. 

