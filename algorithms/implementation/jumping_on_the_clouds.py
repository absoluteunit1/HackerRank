
# My solution 
def jumpingOnClouds(c):
    last_cloud      = len(c) - 1                # last cloud is length of c - 1 (0-based indexing)
    jumps           = 0                         
    current_cloud   = 0
    while current_cloud != last_cloud:
        if current_cloud == last_cloud - 1:     # account for the fact that if we are on the second last cloud, we cannot index c[current_cloud + 2] as we will get an index error
            current_cloud += 1
            jumps += 1
        else:                                   # if we are not on the second last cloud, follow this code to check if we will do a 2-index jump or 1-index jump
            if c[current_cloud + 2] == 0:
                jumps += 1
                current_cloud += 2
            else:
                jumps += 1
                current_cloud += 1
    return jumps
# Also my solution 
# Recursive approach

def jumpingOnClouds2(c):
    if len(c) == 1:                                 # base case 1: if len of the list is 1, then we are on the last cloud
        return 0
    if len(c) == 2:                                 # base case 2: if the len of the list is 2, then we are on the second last item and that only requires one more jump to the last cloud
        return 1
    elif c[2] == 0:                                 # if the thirdelement of our list is 0, than we can jump two clouds in one jump (move by two indices instead of 2)
        return 1 + jumpingOnClouds2(c[2:])
    return 1 + jumpingOnClouds2(c[1:])              # if the third element is not 0, than 