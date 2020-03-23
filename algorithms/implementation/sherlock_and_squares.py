import math

# amazing solution 
# Explanation:

# See if the square root of starting number is say 5.6 and ending number is lets say 8.1 then in between you have 5.7 ,5.8, 5.9, 6, 6.1 and so on till 8.1. 
# But we know that square root of only perfect square will be an integer, so the number of integers between 8.1 and 5.6 will tell us exactly how many perfect squares are there between corresponding numbers. 

# Explanation 2:

# For our case, look at the graph of y = x2. For each point y of the graph, there is an x, square of which will give the graph value (y). This x can be found with inverse function, sqrt(x).

# For the interval [a,b] for y, all x which give the y point in [a,b] lay in the [sqrt(a), sqrt(b)] interval. This follows from the definitions of function and inverse function.

# So, to count all whole y from [a,b], we need just to count all whole x from [ceil(sqrt(a)), floor(sqrt(b))]. (ceil(x) gives closest high integer for x, floor(x) gives closest lower integer for x - see Topics tab). 
# For interval [m, n] (m,n are whole, including endpoints m, n), the number of integers in it is (n - m) + 1. This gives us the solution.

# We can generalise this: all whole numbers of f(x) in [a,b] can be counted as:
# floor(f-1(b)) - ceil(f-1(a)) + 1

# Now Sherlok can easily found the number of cubes in [a,b], number of degrees of 2 in [a,b], etc, provided he has proper inverse function :).

def squares(a,b):
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1


