# n = number of prisoners
# m = number of sweets
# s the chair number to start passing out treats

def save_the_prisoner(n, m, s):
    return (s-1 + m-1)%n + 1

# Explanation One

# The S-1 translates the prisoner id to an equivalent index (since % effectively deals with indexes like 0..N-1). 
# The M-1 handles the fact that the first prisoner to get a sweet is not counted when giving away sweets. 
# Example, if you are giving away 1 sweet and you start at prisoner 37, it is 37 = (37 + 1 - 1) that should be warned. 
# If you are giving away 2 sweets it is 38 = (37 + 2 - 1) that should be warned. 
# And so on. The % N handles the wrapping around based on the index of the prisoners. 
# And the + 1 brings us back to dealing with prisoner ID's instead of indicies.

# Explanation 2

# We start off at some random prisoner S and try to distribute M candies. So we could just do S + M to see which prisoner we end up at. 
# However, we may have more candies than prisoners, so we loop back around to the first prisoner by doing the % N where N is number of prisoners.
# Each +1 and -1 that you see in the equation is to fix the off-by-one problems that exist since prisoners are counted from 1 to N while modular arithmetic is counted from 0.