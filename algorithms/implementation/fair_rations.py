
# My solution! 

def fairRations(B):
    if all(i%2 == 0 for i in B): # if all the numbers are even, then return 0 as zero loaves of bread are needed for all numbers to be even
        return 0 
    elif len([i for i in B if i%2 == 1])%2 == 1: # if the number of odd numbers in the array is odd, then it is impossible to make all the numbers even because each time you add 2 loaves and so one odd number will always be leftover (Odd:n = 2k+1)
        return "NO"
    loaves = 0
    for i in range(len(B)):
        if B[i]%2 == 1:
                B[i] += 1
                B[i+1] += 1
                loaves += 2
    return loaves

