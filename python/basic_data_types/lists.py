# Method 1

N = int(input())
ls = []
for i in range(N):
    s = list(input().split(" "))
    command = s[0]
    arguments = s[1:]
    if command != "print":
        command += f"({','.join(arguments)})"
        eval("ls."+command)
    else:
        print(ls)

# Method 2

# Notes: using eval() is bad practice so another method is to use getattr()
# 1. Dangerous and insecure
# 2. Makes debugging difficult
# 3. Slow

N = int(input())
ls = []
for i in range(N):
    line = input().strip()
    if line == "print":
        print(ls)
        continue
    parts = list(line.split(" "))
    getattr(ls, parts[0])(*(map(int, parts[1:])))

# Method 3
# Using a dictionary and lambdas

n = int(input())
operations = [input().strip() for _ in range(n)]

list_ = []

commands = {
    'insert': lambda idx, ele: list_.insert(int(idx), int(ele)),
    'print': lambda: print(list_),
    'remove': lambda ele: list_.remove(int(ele)),
    'append': lambda ele: list_.append(int(ele)),
    'sort': lambda: list_.sort(),
    'pop': lambda: list_.pop(),
    'reverse': lambda: list_.reverse(),
}

for operation in operations:
    name, args = [i.strip() for i in (operation + ' ').split(' ', maxsplit=1)]
    command = commands.get(name)
    command(*args.split())