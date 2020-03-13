import collections
# My solution

def cutTheSticks(arr):
    result = [len(arr)]
    while( len(arr) != 0 ):
        shortestStick = min(arr)
        arr = [i for i in arr if i != shortestStick]
        arr = [stick - shortestStick for stick in arr]
        if len(arr != 0):
            result.append(len(arr))
    return result

# Another solution

def cutTheStick2(arr):
    result = []
    a = sorted(arr)
    c = collections.Counter(a)
    count = [c[k] for k in sorted(c)]
    for i in range(len(count)):
        result.append(sum(count[i:])) # Why does this work??????
    return result
