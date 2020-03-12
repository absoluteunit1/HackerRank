# Using counter() from collections

import collections
K = int(input())
a = collections.Counter(list(map(int, input().split())))
capsRoom = 0
for roomNumber, count  in a.items():
    if count == 1:
        capsRoom = roomNumber
print(capsRoom)

# Using sets

K = int(input())
rooms = input().split()

rooms.sort()
print(set(rooms[0::2]))
print(set(rooms[1::2]))
capt_room = (set(rooms[0::2]) ^ set(rooms[1::2])) # symmetric difference: numbers that are not common to both sets (unique to one set)
print(capt_room.pop())
