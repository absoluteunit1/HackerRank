def stones2(n, a, b):
    return sorted({x*a + (n-1-x)*b for x in range(n)})

#  You know that you have some number of 'a's less than n and some number of 'b's less than n. 
# The minimum number on the last stone would then be (n-1) * a (or b if b is less than a) and the maximum number is (n-1) * b. 
# These can be rewritten as: min = ((n-1)* a) + (0 * b) and vice versa. 
# Now all you have to do is solve like so, next iteration = ((n-1-1)*a) + (1 *b) and so on. 