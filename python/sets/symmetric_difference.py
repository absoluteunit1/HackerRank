M = int(input())
setM = set(map(int, input().split()))
N = int(input())
setN = set(map(int, input().split()))

a = setM.difference(setN)
b =setN.difference(setM)

a.update(b)
for i in sorted(a):
    print(i)
