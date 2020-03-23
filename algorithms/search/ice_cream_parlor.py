# m = money pooled together
# arr = flavour costs (1 based indexing)

# My solution. Passes all test cases
# O(n^2) 
def iceCreamParlor(m, arr):
    ln = len(arr)
    flavours = []
    for i in range(ln - 1):
        for j in range(ln):
            if arr[i] + arr[j] == m and i != j and flavours == []:
                flavours.append(i + 1)
                flavours.append(j + 1)
    return flavours

# Another solution
# Using dictionaries
# O(n)
def iceCreamParlor2(m, arr):
    test = dict()
    for i in range(len(arr)):
        if arr[i] not in test: 
            test[m-arr[i]] = i+1 # dollar match amount is key, 1-based index is value
        else:
            return sorted([i+1, test[arr[i]]])