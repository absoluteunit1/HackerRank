# My solution. Works but does not execute in time for all arrases. O(N**3) 

def beautifulTriplets(d, arr):
    triplets = 0
    for i in range(len(arr) - 2):
        for j in range(i, len(arr) - 1):
            for k in range(j, len(arr)):
                if arr[j] - arr[i] == d and arr[k] - arr[j] == d:
                    triplets += 1
    return triplets

# Lighter solution from discussions

def beautifulTriplets2(d, arr):
    triplets = 0
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr: # Genius! 
            triplets +=1
    return triplets
