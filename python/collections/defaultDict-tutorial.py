from collections import defaultdict
import sys

# The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want. 

d = defaultdict(list)
lst = list(map(int, input().split()))

n = lst[0]
m = lst[1]

for i in range(n):
    d[sys.stdin.readline().strip()].append(i+1)

for i in range(m):
    l = d[sys.stdin.readline().strip()]
    if l: print(*l)
    else: print(-1)
    
