# My solution

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    command, arg = input().split(" ")
    arg = int(arg)
    if command == "pop":
        s.pop()
    elif command == "remove":
        s.remove(arg)
    elif command == "discard":
        s.discard(arg)

print(sum(s))

# Another solution - using eval() which takes a python string as an arguement and evaluates it as a python expression

n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))

# Another solution

n = int(input())
s = set(map(int, input().split())) 

for i in range(int(input())):

    c, *args = map(str,input().split())

    getattr(s,c) (*(int(x) for x in args))  # explanation at (4th comment) https://www.hackerrank.com/challenges/py-set-discard-remove-pop/forum


print (sum(s))