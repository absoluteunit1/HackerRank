
# My solution. Passes 60% of test cases; times out on the other 40%

def strangeCounter2(t):
    n = 3 
    reset_count = 0
    for i in range(1, t+1):
        if i == t:
            return n
        n -= 1
        if n == 0:
            reset_count += 1
            n = 3*2**reset_count

# Solution that passes all test cases
# Explanation:
# - The counter begins at 3. Each time it would tick down to zero, it instead “loops” up to double its previous maximum value, represented by "rem *= 2".
# - "t = t-rem" represents the counter ticking down before reinitializing. 
# By subtracting the counter’s current maximum value directly from the remaining timer, 
# we can skip looping the counter ticking "t" times, instead only following the number of times the counter itself loops back up from 0 within the bounds of t.
# - Once the remaining timer is less than the maximum counter, you’re in the final “loop” of the counter. 
# The output is the value remaining on the counter once the timer runs out

def strangeCounter(t):
    n = 3
    while t > n:
        t = t - n
        n *= 2
    return n-t+1