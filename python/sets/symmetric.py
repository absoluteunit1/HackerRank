_, n = int(input()), set(map(int, input().split()))
_, m = int(input()), set(map(int, input().split()))
print(len(n.symmetric_difference(m)))