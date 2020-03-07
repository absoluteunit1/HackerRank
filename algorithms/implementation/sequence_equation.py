# 2 3 1 
# x = 1 == p(3) == p(p(2)), y = 2
def permutationEquation(p):
    newList = []
    dict1 = { x + 1: p[x] for x in range(0, len(p)) }
    for x in range(1, len(p) + 1):
        for key in dict1:
            if dict1[dict1[key]] == x:
                newList.append(key)
    return newList
