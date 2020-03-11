nums1 = list(map(int, input().split()))  # why do we convert to int?

n = nums1[0]
m = nums1[1]

arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# My solution:

happiness = 0
for i in arr:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1
print(happiness)

# Other solutions:

nums1 = list(map(int, input().split()))  # why do we convert to int?

n = nums1[0]
m = nums1[1]

sc_ar = list(map(int,input().split()))

A = set(map(int,input().split()))
B = set(map(int, input().split()))
print(sum([(i in A) - (i in B) for i in sc_ar])) # "i in A" returns 1 if i is present in set A and 0 if its not


