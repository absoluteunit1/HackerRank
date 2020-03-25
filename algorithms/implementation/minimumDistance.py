# My solution

def minimumDistance(a):
    distances = []
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                distances.append(abs(j-i))
    return -1 if distances == [] else min(distances)

# Another solution O(n) 
# Uses dictionary to store the index of each element as a value and the element as the key and then at each iteration compares the min_difference with the current elements recorder index. (if they are the same)
def minimumDistance2(a):
    d={}
    n = len(a)
    # Initialize minimum difference variable as one more than the maximum value(n-1) we can achieve
    min_diff = n

    # Going through each element in the array
    for i in range(n):

    # Try/Except statement to find record of the last known index for the element in the dictionary(for index difference calc), if unable to find the record then create the record
        try:

    # min_diff equals minimum value between (the element index i and the last known location of the same element) and (min_diff)
            min_diff = min(i-d[a[i]],min_diff) 

    # Change the last known position of the element
            d[a[i]]=i

    # Now if min_diff has value 1 then the code doesnt need to go further as its the minimum possible value for the answer
            if min_diff == 1:
                return 1
        
        except:
            d[a[i]]=i

    # If min_diff is the same as initialized value meaning no element in input array is repeating then print -1 else the minimum difference value
    if min_diff == n:  
        return -1
    return min_diff