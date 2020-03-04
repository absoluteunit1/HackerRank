from collections import Counter

# counter is a cotainer that stores elements as dictionary keys and their counts as dictionary values

# elements are counted from an iterable or initialized from another mapping

# counter objects have a dictionary interface except that they return a zero count for missing items instead of raising key error

# Ex:
# c = Counter(['eggs', 'ham])
# c['bacon'] will return 0 instead of key error as a normal dictionary would


from collections import Counter
x = int(input())
sizes = list(map(int,input().split()))
n = int(input())
sizes = Counter(sizes)
pr = 0
for i in range(n):
    sz,pz = map(int,input().split())
    if(sizes[sz]):
        sizes[sz] -= 1
        pr += pz
print(pr)



