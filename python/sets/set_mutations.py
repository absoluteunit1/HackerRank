# One method

n = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    instruction = list( input().split() )
    command = instruction[0]
    getattr(A, command)(set(map(int, input().split())))
print(sum(A))

