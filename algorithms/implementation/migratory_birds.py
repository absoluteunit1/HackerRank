# One solution (doesn't pass all the test cases)
import collections

def migratory_birds(arr):
    ar = sorted(arr)
    my_dict = {i:ar.count(i) for i in ar}
    return max(my_dict, key=my_dict.get)
    
# Another solution (doesn't work for one test case!)

def migratory_birds2(arr):
    c = collections.Counter(arr)
    return (c.most_common(1)[0][0])



# BEST SOLUTION 

# Solution from discussions (works for all test cases)

# Uses the index of a list for the bird type

def migratory_birds3(arr):
    count = [0]*6                   # each type of bird is 1-5 so we create a list with index from 0-5
    for t in arr:   
        count[t] += 1               # as we iterate through the list, add the count of the type of bird at its index 
        print(count)
    return count.index(max(count))  # finds the maximum value of the birds, and returns the index of that max value. The count.index(max(count)) returns the index of  first occurence of the max value in the list

migratory_birds3(list(map(int, "2 4 3 2 3 1 2 1 3 3".rstrip().split())))