# e = energy (int)
# k = jump size (int)\
# c = array of clouds (list)
# n = numbers of clouds
# takes one unit of energy to make a jump
# next cloud index = c[(i + k) % n]
# if c[i] == 1 then e -= 2
# game ends when lands on cloud [0]

# Task: Determine final e after the game ends!

def jumping_on_clouds(c, k):
    n = len(c)
    e = 99
    if c[0] == 1:
        e -= 2
    nextCloud = (0 + k)%n
    while nextCloud != 0:
        if c[nextCloud] == 1:
            e -= 2
        e -= 1
        nextCloud = (nextCloud + k)%n
    return e


