A = set(map(int, input().split()))
tests = 0
n = int(input())
for testCase in range(n):
    if A.issuperset(set(map(int, input().split()))) == True:
        tests += 1
print(True if tests == n else False)


    